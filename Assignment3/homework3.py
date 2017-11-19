import parser_tree as ptree
import copy
import itertools
import time
import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'VAR', 'CONST', 'PRED',
    'COMMA',
    'LEFT_P', 'RIGHT_P',
    'NOT', 'OR',
)

t_NOT = r'\~'
t_OR = r'\|'
t_COMMA = r','
t_LEFT_P = r'\('
t_RIGHT_P = r'\)'


def t_PRED(t):
    r'[A-Z][a-zA-Z]*\('
    return t


def t_CONST(t):
    r'[A-Z_][a-zA-Z0-9_]*'
    return t


def t_VAR(t):
    r'[a-z]'
    return t


lexer = lex.lex()

precedence = (
    ('left', 'OR'),
    ('right', 'NOT'),
)


def p_sentence_not(p):
    "sentence : NOT sentence"
    if p[2].op == '~':
        p[0] = p[2].left
    else:
        p[0] = ptree.NegateOp(p[2])


def p_sentence_op(p):
    "sentence : sentence OR sentence"
    p[0] = ptree.BinOp(p[1], p[2], p[3])


def p_sentence_nested(p):
    "sentence : LEFT_P sentence RIGHT_P"
    p[0] = p[2]


def p_literal(p):
    "literal : PRED term_list RIGHT_P"
    p[0] = ptree.Predicate(p[1][0:-1])
    p[0].children = p[2].children


def p_sentence_literal(p):
    "sentence : literal"
    p[0] = p[1]


def p_term_list(p):
    '''term_list : term
                 | term_list COMMA term'''
    if len(p) == 2:
        p[0] = ptree.List(p[1])
    elif len(p) == 4:
        p[1].children.append(p[3])
        p[0] = p[1]


def p_term_variable(p):
    "term : VAR"
    p[0] = ptree.Variable(p[1])


def p_term_constant(p):
    "term : CONST"
    p[0] = ptree.Constant(p[1])


def populate_parent(root):
    if root.type == "pred":
        return
    right, left = root.right, root.left
    if right:
        right.parent = root
        populate_parent(right)
    if left:
        left.parent = root
        populate_parent(left)


def sentence_parse(line):
    res = ptree.Start(yacc.parse(line))
    populate_parent(res)
    # push_negation_inward(res)
    # distribute_or(res)
    return res


yacc.yacc()

cnt = itertools.count()


class Predicate:
    def copy(self):
        new_args = []
        i = 0
        while i < len(self.args):
            arg = self.args[i]
            if arg.type == 'var':
                new_args.append(copy.copy(arg))
            else:
                new_args.append(arg)
            i = i + 1
        return Predicate(self.name, new_args, None)

    def __init__(self, name, args, prev):
        self.args = args
        self.prev = prev
        self.name = name
        self.next = None
        self.head = None


class Clause:
    def __init__(self):
        self.next = None
        self.num = next(cnt)

    def copy(self, pred=None):
        head = Clause()
        current = head
        cur_origin = self.next
        for i in itertools.count():
            if not cur_origin:
                break
            temp = current
            current = cur_origin.copy()
            if cur_origin is pred:
                pred = current
                current.prev, current.head = temp, head
                temp.next = current
                cur_origin = cur_origin.next
            else:
                current.prev, current.head = temp, head
                temp.next = current
                cur_origin = cur_origin.next
        if not pred:
            return head
        else:
            return head, pred

    def merge(self, rhs):
        current, tail = self, None
        for i in itertools.count():
            if not current:
                break
            tail, current = current, current.next
        tail.next = rhs.next
        if rhs.next:
            rhs.next.prev = tail


def seperate_clauses(root):
    clauses = []
    queue = []

    queue.append(root)
    for i in itertools.count():
        if not queue:
            break
        node = queue.pop()
        if node.op != '&':
            clauses.append(node)
        else:
            queue.append(node.left)
            queue.append(node.right)
    return clauses


def convert_predicate(node, prev):
    if node.type != 'not':
        ret = Predicate(node.name, node.children, prev)
    else:
        pred_node = node.left
        ret = Predicate('-' + pred_node.name, pred_node.children, prev)
    return ret


def convert_clause_list(clause_root):
    queue = []
    head = Clause()
    current = head

    queue.append(clause_root)
    for i in itertools.count():
        if not queue:
            break
        node = queue.pop()
        if node.op != '|':
            temp = current
            current = convert_predicate(node, temp)
            current.head = head
            temp.next = current
        else:
            queue.append(node.left)
            queue.append(node.right)
    return head


def put_sentence(kb, line, s):
    line = line.replace(' ', '')
    start = sentence_parse(line)
    clauses = seperate_clauses(start.left)
    j = 0
    while j < len(clauses):
        clause_t = clauses[j]
        j = j + 1
        clause_list = convert_clause_list(clause_t)
        current = clause_list.next
        for i in itertools.count():
            if not current:
                break
            substitute_constant(current, s)
            if current.name in kb:
                kb[current.name].append(current)
            else:
                kb[current.name] = []
                kb[current.name].append(current)
            current = current.next
    return clause_list


def substitute_constant(pred, const_map):
    assert isinstance(pred, Predicate)

    var_map = {}
    args = pred.args

    i = 0
    while i < len(args):
        if args[i].type == 'var':
            if args[i].value not in var_map:
                var_map[args[i].value] = args[i]
            else:
                args[i] = var_map[args[i].value]
        elif args[i].type == 'const':
            if args[i].value not in const_map:
                const_map[args[i].value] = args[i]
            else:
                args[i] = const_map[args[i].value]
        i += 1


def unify(clause1, clause2, subst):
    if clause1 is clause2:
        return subst
    elif subst is None:
        return None
    elif isinstance(clause1, list):
        if len(clause1) != 1:
            return unify(clause1[1:], clause2[1:], unify(clause1[0], clause2[0], subst))
        else:
            return unify(clause1[0], clause2[0], subst)
    elif clause2.type == 'var':
        return unify_var(clause2, clause1, subst)
    elif clause1.type == 'var':
        return unify_var(clause1, clause2, subst)
    elif clause1.type == 'const':
        if clause1.value != clause2.value:
            return None
        else:
            return subst
    else:
        return None


def unify_var(var, x, s):
    if x in s:
        return unify(var, s[x], s)
    elif var in s:
        return unify(s[var], x, s)
    else:
        s[var] = x
        return s


def standardize_clause(clause, name_gen, map):
    current = clause.next
    for i in itertools.count():
        if not current:
            break
        standardize_pred(current, name_gen, map)
        current = current.next


def standardize_pred(pred, name_gen, map):
    l = pred.args
    i = 0
    while i < len(l):
        if l[i].type == 'var':
            if l[i].value in map:
                l[i] = map[l[i].value]
            else:
                map[l[i].value] = l[i]
                l[i].value = next(name_gen)
        i += 1


def subst(s, clause):
    current = clause.next
    for i in itertools.count():
        if not current:
            break
        args = current.args
        i = 0
        while i < len(args):
            while args[i] in s:
                args[i] = s[args[i]]
            i += 1
        current = current.next


def query_sentence(kb, a):
    if a.name not in kb:
        return False
    i = 0
    while i < len(kb[a.name]):
        pred = kb[a.name][i]
        i += 1
        if unify(a.args, pred.args, {}) is None:
            continue
        else:
            to_resolve, to_unify = pred.head.copy(pred)
            var_name_gen = gen_var()
            clause_resolve(to_resolve, to_unify, a, var_name_gen)
            abort_time = time.time() + 2
            if to_resolve.next == None or resolution(kb, to_resolve, set(), 0, abort_time):
                return True
    return False


def clause_resolve(to_resolve, to_unify, alpha, name_gen):
    standardize_clause(to_resolve, name_gen, {})
    sub = unify(to_unify.args, alpha.args, {})
    to_unify.prev.next = to_unify.next
    if to_unify.next:
        to_unify.next.prev = to_unify.prev
    subst(sub, to_resolve)
    return sub


record_count = itertools.count()


def resolution(kb, clause, met, depth, abort):
    if depth > 500 or time.time() > abort:
        return False
    term = clause.next
    if not term:
        return True
    clause_id = convert_clause(clause)
    if clause_id in met:
        return False
    else:
        met.add(clause_id)
    nt = negate_name(term.name)
    if nt not in kb:
        return False
    is_resolvable = False
    i = 0
    while i < len(kb[nt]):
        pred = kb[nt][i]
        i += 1
        if unify(term.args, pred.args, {}) is None:
            continue
        is_resolvable = True
        to_resolve, to_unify = pred.head.copy(pred)
        new_clause, new_term = clause.copy(term)
        var_name_gen = gen_var()

        standardize_clause(new_clause, var_name_gen, {})
        s = clause_resolve(to_resolve, to_unify, new_term, var_name_gen)

        new_term.prev.next = new_term.next
        if new_term.next:
            new_term.next.prev = new_term.prev

        subst(s, new_clause)
        new_clause.merge(to_resolve)
        factorize(new_clause)
        if resolution(kb, new_clause, met, depth + 1, abort):
            return True
    if not is_resolvable:
        return False


def factorize(clause):
    factor_set = set()
    current = clause.next
    while current:
        pred_id = predicate_to_tuple(current)
        if pred_id not in factor_set:
            factor_set.add(pred_id)
        else:
            current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
        current = current.next


def convert_clause(clause):
    l = []
    current = clause.next

    for i in itertools.count():
        if not current:
            break
        l.append(predicate_to_tuple(current))
        current = current.next
    return tuple(l)


def predicate_to_tuple(pred):
    l = []
    count = 0
    l.append(pred.name)
    j = 0
    while j < len(pred.args):
        arg = pred.args[j]
        if arg.type != 'var':
            l.append(arg)
        else:
            l.append('v')
        j = j + 1
    return tuple(l)


def negate_name(name):
    if name[0] != '-':
        return '-' + name
    else:
        return name[1:]


def gen_var():
    cnt = itertools.count(1)
    var_list = ['p', 'q', 'r', 'x', 'y', 'z']

    while True:
        list = []
        name = ''
        for num in range(next(cnt)):
            num -= 1
            list.append(var_list[num % 6])
            num //= 6
        for item in list:
            name += list.pop()
        yield name


def read_queries(text_file):
    return query_size, queries


if __name__ == '__main__':
    kb = {}
    sub = {}
    output = open('output.txt', 'w')
    with open('input.txt', 'r') as inp:
        queries = []
        query_size = int(inp.readline())
        for i in range(query_size):
            queries.append(inp.readline().strip())
        kb_size = int(inp.readline())
        kb_count = 0
        while kb_count < kb_size:
            st = inp.readline().strip('\n')
            put_sentence(kb, st, sub)
            kb_count += 1

        for query in queries:
            query = query.replace(' ', '')
            start = sentence_parse(query)
            query_pred = convert_predicate(start.left, None)
            substitute_constant(query_pred, sub)

            if query_sentence(kb, query_pred):
                output.write('TRUE\n')
            else:
                output.write('FALSE\n')
    output.close()
