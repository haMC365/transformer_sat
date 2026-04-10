from pysat.formula import CNF
import random


def generate_random_cnf(n_vars=10, n_clauses=20):
    cnf = CNF()
    for _ in range(n_clauses):
        clause = [random.randint(1, n_vars) * random.choice([-1, 1]) for _ in range(3)]
        cnf.append(clause)
    return cnf
