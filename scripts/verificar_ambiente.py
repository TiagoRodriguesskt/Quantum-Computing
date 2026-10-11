"""Verifica se o ambiente do projeto está pronto para o curso.

Uso (na raiz do projeto):
    uv run python scripts/verificar_ambiente.py

O script faz três tipos de teste:
  1. Ambiente  -> versão do Python e ambiente virtual ativo
  2. Pacotes   -> cada dependência do requirements.txt importa sem erro
  3. Física    -> mini-experimentos que só funcionam se tudo estiver certo
"""

import importlib
import sys

OK, FALHA, AVISO = "✅", "❌", "⚠️ "
falhas = 0


def resultado(passou, mensagem, aviso=False):
    """Imprime uma linha do relatório e conta as falhas."""
    global falhas
    if passou:
        print(f"  {OK} {mensagem}")
    elif aviso:
        print(f"  {AVISO} {mensagem}")
    else:
        print(f"  {FALHA} {mensagem}")
        falhas += 1


# ------------------------------------------------------------------
print("\n[1/3] Ambiente")
# ------------------------------------------------------------------
v = sys.version_info
resultado(v >= (3, 10), f"Python {v.major}.{v.minor}.{v.micro} (mínimo: 3.10)")

em_venv = sys.prefix != sys.base_prefix
resultado(em_venv, f"Ambiente virtual ativo: {sys.prefix}", aviso=True)

# ------------------------------------------------------------------
print("\n[2/3] Pacotes")
# ------------------------------------------------------------------
# nome usado no import -> nome no requirements.txt
pacotes = {
    "numpy": "numpy",
    "scipy": "scipy",
    "matplotlib": "matplotlib",
    "jupyterlab": "jupyterlab",
    "ipykernel": "ipykernel",
    "qiskit": "qiskit",
    "qiskit_aer": "qiskit-aer",
    "qiskit_ibm_runtime": "qiskit-ibm-runtime",
    "pylatexenc": "pylatexenc",
    "pytest": "pytest",
}
for modulo, nome in pacotes.items():
    try:
        m = importlib.import_module(modulo)
        versao = getattr(m, "__version__", "instalado")
        resultado(True, f"{nome:<20} {versao}")
    except Exception as erro:  # noqa: BLE001
        resultado(False, f"{nome:<20} NÃO importou ({type(erro).__name__}: {erro})")

# ------------------------------------------------------------------
print("\n[3/3] Testes de física")
# ------------------------------------------------------------------

# Teste A: NumPy — Hadamard em |0> deve dar 50% / 50%
try:
    import numpy as np

    ket0 = np.array([1, 0], dtype=complex)
    H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    psi = H @ ket0
    probs = np.abs(psi) ** 2
    resultado(np.allclose(probs, [0.5, 0.5]),
              f"NumPy: H|0> -> P(0)={probs[0]:.2f}, P(1)={probs[1]:.2f}")

    # Unitariedade: H†H = I
    resultado(np.allclose(H.conj().T @ H, np.eye(2)), "NumPy: H é unitária (H†H = I)")
except Exception as erro:  # noqa: BLE001
    resultado(False, f"NumPy: erro no teste ({erro})")

# Teste B: Matplotlib — gerar uma figura sem abrir janela
try:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.bar(["0", "1"], [0.5, 0.5])
    plt.close(fig)
    resultado(True, "Matplotlib: figura gerada")
except Exception as erro:  # noqa: BLE001
    resultado(False, f"Matplotlib: erro ({erro})")

# Teste C: Qiskit + Aer — estado de Bell deve dar só '00' e '11'
try:
    from qiskit import QuantumCircuit, transpile
    from qiskit_aer import AerSimulator

    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()

    sim = AerSimulator()
    contagens = sim.run(transpile(qc, sim), shots=1000).result().get_counts()
    so_correlacionados = set(contagens) <= {"00", "11"}
    resultado(so_correlacionados, f"Qiskit Aer: estado de Bell -> {dict(contagens)}")
except Exception as erro:  # noqa: BLE001
    resultado(False, f"Qiskit Aer: erro ({erro})")

# Teste D: desenho de circuito (usa pylatexenc)
try:
    qc.draw("mpl")
    resultado(True, "Qiskit: desenho de circuito com matplotlib")
except Exception as erro:  # noqa: BLE001
    resultado(False, f"Qiskit: desenho falhou ({erro})")

# ------------------------------------------------------------------
print("\n" + "=" * 50)
if falhas == 0:
    print(f"{OK} Ambiente pronto! Pode começar a Aula P1.")
else:
    print(f"{FALHA} {falhas} teste(s) falharam. Copie esta saída e envie para análise.")
print("=" * 50 + "\n")
sys.exit(1 if falhas else 0)
