import copy

predicates = []


def get_predicates(sentence):
    parts = []
    if '|' in sentence:
        parts = sentence.split('|')
    for x in parts:
        if '~' in x:
            predicates.append(x[x.index('~') + 1:x.index('(')])


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        n_queries = int(file.readline().strip())
        print(n_queries)
        queries = []
        for x in range(n_queries):
            queries.append(file.readline().strip())
        m_stmts = int(file.readline().strip())
        stmts = []
        for x in range(m_stmts):
            stmt = file.readline().strip()
            stmts.append(stmt)
            get_predicates(stmt)
        predicates = set(predicates)
        dict_p = {p:{'+':{},'-':{}} for p in predicates}

        print(dict_p)
