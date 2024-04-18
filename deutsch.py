from quantuminspire.api import QuantumInspireAPI

# Token was saved in a disk
qi = QuantumInspireAPI(authentication=None, project_name='ksi_dokt')
# Documentation:
# https://quantuminspire.readthedocs.io/en/latest/api.html#quantuminspire.api.QuantumInspireAPI

qi.list_backend_types()
qi.get_default_backend_type()
qi.get_backend_types()
qi.get_backend_type_by_id(11)
qi.get_backend_type(11)
qi.list_projects()
qi.get_projects()
qi.list_jobs()
qi.get_jobs()
qi.list_results()
qi.get_result(7994635)
qi.list_assets()
qi.get_asset_from_job(8008757)

qasm = '''
version 1.0
qubits 2

H q[0]
CNOT q[0], q[1]
Measure q[0,1]
'''

backend_type = qi.get_backend_type_by_name('QX single-node simulator')
result = qi.execute_qasm(qasm, backend_type=backend_type, number_of_shots=1024, )

if result.get('histogram', {}):
    print(result['histogram'])
else:
    reason = result.get('raw_text', 'No reason in result structure.')
    print(f'Result structure does not contain proper histogram data. {reason}')
