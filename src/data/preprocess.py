import torch


def cnf_to_tensor(cnf, max_vars=20):
    tensor = torch.zeros((len(cnf.clauses), max_vars))

    for i, clause in enumerate(cnf.clauses):
        for lit in clause:
            idx = abs(lit) - 1
            tensor[i][idx] = 1 if lit > 0 else -1

    return tensor
