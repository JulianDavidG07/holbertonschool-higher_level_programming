#!/usr/bin/python3
"""module mathematic numpy
"""


import numpy as np
"""
function multiplication two matrices
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Args
       m_a: matrix A
       m_b: matrix B
    """
    return(np.matmul(m_a, m_b))
