from numpy.random import randint


def generate_formula(k, n, v):
    '''
    Generate boolean formula in conjunctive normal form.
    :param k: number of literals in clause
    :param n: number of clauses
    :param v: number of variables
    :return: Lists of lists. Each smaller list means the clause.
    Value represents variable index, negative value means a negation of the value.
    '''
    formula = []
    for i in range(n):
        clause = []
        for j in range(k):
            literal = randint(v)
            negative = randint(1)
            if negative:
                literal = -literal
            clause.append(literal)
        formula.append(clause)
    return formula


def solve_sat(formula, m):
    '''
    Randomized SAT implementation.
    :param formula: formula in generate_formula function result format
    :param m: Maximum number of iterations
    :return: boolean valuse - formula satisfiability
    '''
    # %%% START YOUR CODE HERE %%%
    pass
    # %%% END YOUR CODE HERE %%%
