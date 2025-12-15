from qiskit import QuantumCircuit

def build_qaoa_circuit(bqm, var_names, params, p=1):
    n = len(var_names)
    qc = QuantumCircuit(n)

    var_to_idx = {v: i for i, v in enumerate(var_names)}
    gammas = params[:p]
    betas = params[p:2*p]

    qc.h(range(n))

    for layer in range(p):
        gamma = gammas[layer]

        # Quadratic penalty e^{-iγZ⊗Z}
        for (u, v), coeff in bqm.quadratic.items():
            q1 = var_to_idx[u]
            q2 = var_to_idx[v]
            qc.cx(q1, q2)
            qc.rz(-2*gamma*coeff, q2)
            qc.cx(q1, q2)

        # Linear penalty e^{-iγZ}
        for name, coeff in bqm.linear.items():
            q = var_to_idx[name]
            qc.rz(-gamma*coeff, q)

        # Mixer e^{-iβX}
        beta = betas[layer]
        for q in range(n):
            qc.rx(2*beta, q)

    qc.measure_all()
    return qc
