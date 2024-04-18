from quantuminspire.api import QuantumInspireAPI

# Token was saved in a disk
qi = QuantumInspireAPI(authentication=None, project_name='deutsch_wyklad')

f1 = """
.oracle_fc1
# do nothing or 
I q[0:1]
"""

f2 = """
.oracle_fc2
X q[1]
"""

f3 = """
.oracle_fb3
CNOT q[0],q[1]
"""

f4 = """
.oracle_fb4
CNOT q[0],q[1]
X q[1]
"""

qasm_part1 = """
version 1.0
qubits 2

# In the Deutsch–Jozsa algorithm we use an oracle to determine if a binary function f(x) is constant or balanced.
# Constant f(x)=fc1=0 OR f(x)=fc2=1
# Balanced f(x)=fb3=x OR f(x)=fb4=NOT(x)
# The algorithm requires only a single query of f(x).
# By changing the Oracle, the 4 different functions can be tested.

# Initialize qubits in |+> and |-> state
.initialize
prep_z q[0:1]
X q[1]
{H q[0]|H q[1]}
"""

qasm_part3 = """
.measurement
H q[0]
measure q[0]
"""
 
lst_backends = ['QX single-node simulator', 'QX-34-L', 'Spin-2'] 

for backend_name in lst_backends[1:]:
    backend_type = qi.get_backend_type_by_name(backend_name)

    qasm = f"{qasm_part1}{f1}{qasm_part3}"
    result = qi.execute_qasm(qasm, backend_type=backend_type, number_of_shots=1024, identifier=f"f1, {backend_name}")
    print(result)

    qasm = f"{qasm_part1}{f2}{qasm_part3}"
    result = qi.execute_qasm(qasm, backend_type=backend_type, number_of_shots=1024, identifier=f"f2, {backend_name}")
    print(result)

    qasm = f"{qasm_part1}{f3}{qasm_part3}"
    result = qi.execute_qasm(qasm, backend_type=backend_type, number_of_shots=1024, identifier=f"f3, {backend_name}")
    print(result)

    qasm = f"{qasm_part1}{f4}{qasm_part3}"
    result = qi.execute_qasm(qasm, backend_type=backend_type, number_of_shots=1024, identifier=f"f4, {backend_name}")
    print(result)