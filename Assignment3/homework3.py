from copy import deepcopy

predicates_g = set()
constants = set()
queries = set() #
stmts = set() #
kkb = {}

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
            predicate = predicate.strip()
            predicates_g.add(predicate)
            ret.append(predicate)
        else:
            predicate = x[:x.index('(')]
            predicate = predicate.strip()
            predicates_g.add(predicate)
            ret.append(predicate)
    print("ret"+str(ret))
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

def process_statements():
    for query in queries:
        #get predicate
        print(query)
        print(get_predicates(query))
        print(get_constants(query))
        for y in stmts



if __name__ == "__main__":
    with open("input.txt", "r") as file:
        n_queries = int(file.readline().strip())
        print(n_queries)

        for x in range(n_queries):
            query = file.readline().strip()
            queries.add(query)
            get_constants(query)
        m_stmts = int(file.readline().strip())

        for x in range(m_stmts):
            stmt = file.readline().strip()
            stmts.add(stmt)
            get_predicates(stmt)
        #for x in predicates_g:
        #    print("p:"+str(x))

        dict_p = {p:{'+':{},'-':{}} for p in predicates_g}

        process_statements()


        #print(constants)
        print(dict_p)
