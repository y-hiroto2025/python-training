import numpy as np

pr = np.array([[-1,3],
               [1,-2]])
a = np.array([[13,-30],
              [5,-12]])
p = np.array([[2,3],
              [1,1]])


def diagonalize(A, P):
    P_reverse = np.linalg.inv(P)

    return np.dot(np.dot(P_reverse, A), P)

print(diagonalize(A=a, P=p))