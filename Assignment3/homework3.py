from copy import deepcopy

predicates_g = set()
constants = set()
queries = set()  #
stmts = set()  #
kb = {}


def get_predicates(sentence):
    parts = []
    ret = []
    if '|' in sentence:
        parts = sentence.split('|')
    else:
        parts.append(sentence)
    for x in parts:
        if '~' in x:
            predicate = x[x.index('~') + 1:x.index('(')]
        else:
            predicate = x[:x.index('(')]
        predicate = predicate.strip()
        predicates_g.add(predicate)
        ret.append(predicate)
    print("predicates:" + str(ret))
    return deepcopy(ret)


def get_constants(query):
    if ',' in query:
        constant = [x.strip() for x in query[query.index('(') + 1:query.index(')')].split(',')]
        for x in constant:
            constants.add(x)
    else:
        constant = query[query.index('(') + 1:query.index(')')]
        constants.add(constant)
    return deepcopy(constant)


def build_kb():
    for y in stmts:
        pred = get_predicates(y)
        for x in pred:
            if y.index(x) == 0:
                kb[x]['+'].add(y)
            elif y[y.index(x) - 1] == '~':
                kb[x]['-'].add(y)
            else:
                kb[x]['+'].add(y)


def get_positivity(query):
    return '+' if query[0] == '~' else '-'

def unify(a, b):
    pass

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        n_queries = int(file.readline().strip())

        for x in range(n_queries):
            query = file.readline().strip()
            queries.add(query)
            get_constants(query)
        m_stmts = int(file.readline().strip())

        for x in range(m_stmts):
            stmt = file.readline().strip()
            stmts.add(stmt)
            get_predicates(stmt)

        kb = {p: {'+': set(), '-': set()} for p in predicates_g}

        build_kb()

        # for q in queries:
        #     pred = get_predicates(q)
        #     for dict_st
        print(stmts)
        print(queries)
        print(predicates_g)
        print(constants)

        for x in kb.items():
            print(x)

        for query in queries:
            query_predicate = get_predicates(query)
            query_constants = get_constants(query)
            query_sign = get_positivity(query)
            for stmt in kb[query_predicate][query_sign]:
                result = unify(query, stmt)