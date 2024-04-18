from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit_aer import Aer
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

def deutch_jozsa(ftype:str): 
    simulator = Aer.get_backend('statevector_simulator')
    lst_circuit_steps = []
    # Create a new quantum circuit with 2 qubits
    circuit = QuantumCircuit(2, 1)
    # Initialize qubits in |+> and |-> state
    # prep_z q[0:1]
    # This is equivalent to initializing the qubits in the |0> state, which is the default in Qiskit
    circuit.reset([0,1])
    circuit.barrier()
    lst_circuit_steps.append(transpile(circuit, simulator))
    # X q[1]
    # Apply an X gate (NOT gate) on qubit 1
    circuit.x(1)
    circuit.barrier()
    lst_circuit_steps.append(transpile(circuit, simulator))
    # Apply a Hadamard gate on both qubits
    circuit.h([0,1])
    circuit.barrier()
    lst_circuit_steps.append(transpile(circuit, simulator))
    # Identity
    if ftype == 'fc1':
        circuit.id([0, 1])
    elif ftype == 'fc2':
        circuit.x(1)
    elif ftype == 'fb3':
        circuit.cx(0,1)
    elif ftype == 'fb4':
        circuit.cx(0,1)
        circuit.x(1)
    circuit.barrier()
    lst_circuit_steps.append(transpile(circuit, simulator))
    # Hadamard
    circuit.h([0])
    circuit.barrier()
    lst_circuit_steps.append(transpile(circuit, simulator))
    # Measure
    circuit.measure([0], [0])
    lst_circuit_steps.append(transpile(circuit, simulator))
    
    return lst_circuit_steps


def f_draw_steps(ftype:str):
    lst_circuit_steps = deutch_jozsa(ftype)
    plot_circuit = lst_circuit_steps[-1].draw(output='mpl')
    pdf = PdfPages(f'out/{ftype}.pdf')
    pdf.savefig(plot_circuit)
    
    simulator = Aer.get_backend('qasm_simulator')

    job = simulator.run(lst_circuit_steps[-1])
    result = job.result()
    counts = result.get_counts(lst_circuit_steps[-1])
    hist_plot = plot_histogram(counts)
    pdf.savefig(hist_plot)
    
    # all_states = [format(i, '0' + str(lst_circuit_steps[-1].num_qubits) + 'b') for i in range(2**lst_circuit_steps[-1].num_qubits)]
    
    
    for circuit_step in lst_circuit_steps[:-1]:
        state = Statevector.from_instruction(circuit_step)
        
        plot_circuit = circuit_step.draw(output='mpl')
        pdf.savefig(plot_circuit)

        bloch = plot_bloch_multivector(state) 
        pdf.savefig(bloch)
        
        # Execute the circuit on the qasm simulator
        simulator = Aer.get_backend('qasm_simulator')
        circuit_step.measure_all()
        job = simulator.run(circuit_step)
        result = job.result()
        counts = result.get_counts(circuit_step)
        hist_plot = plot_histogram(counts)
        pdf.savefig(hist_plot)
    pdf.close()
    
if __name__ == "__main__":
    f_draw_steps('fc1')
    f_draw_steps('fc2')
    f_draw_steps('fb3')
    f_draw_steps('fb4')
    