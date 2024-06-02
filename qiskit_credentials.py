import qiskit
print(qiskit.__version__)
from qiskit_ibm_runtime import QiskitRuntimeService

with open('qiskit_token.txt', 'r') as f:
    qiskit_token = f.read()
    
service = QiskitRuntimeService(channel='ibm_quantum', token = qiskit_token)
QiskitRuntimeService.save_account(channel='ibm_quantum', token= qiskit_token, overwrite=True)
