from sympy.physics.quantum.qubit import Qubit
from sympy.physics.quantum.qubit import matrix_to_qubit, qubit_to_matrix
from sympy import init_printing #setting printing options
from sympy.printing.latex import latex, print_latex
from sympy.printing.mathml import mathml
from IPython.display import Latex, Math
import numpy as np

q0 = Qubit(0)
q1 = Qubit(1)

print(q0)
print(q1)

print(q0.nqubits)
print(len(q0))
print(qubit_to_matrix(q0))
print(type(q0))
print(type(qubit_to_matrix(q0)))
type(np.matrix(q0))
print(np.matrix(qubit_to_matrix(q0)))

print(q1)
print(latex(q1))
print(mathml(q1))
print(mathml(qubit_to_matrix(q0)))
init_printing()
display(latex(qubit_to_matrix(q0)))
display(Math(latex(qubit_to_matrix(q0))))
display(Math(latex(qubit_to_matrix(q1))))


A = sp.Matrix([[1, 2], [3, 4]])
B = sp.Matrix([[2, 3], [1, 2]])

# Iloczyn tensorowy
C = sp.tensorproduct(A, B)

# Wydrukowanie obliczeń krok po kroku
print("A =")
sp.pprint(A)
print("\nB =")
sp.pprint(B)
print("\nA ⊗ B =")
sp.latex(C)
