# qsim — meu simulador quântico

Projeto contínuo do curso. Cada fase adiciona uma peça:

| Fase | Marco |
|---|---|
| 1 | Criar estados e medi-los (Regra de Born) |
| 2 | Aplicar portas a 1 qubit e plotar na Esfera de Bloch |
| 3 | Suportar n qubits (produto tensorial, CNOT) e comparar com o Qiskit |
| 4 | Rodar Deutsch-Jozsa e Grover no próprio simulador |
| 5 | Adicionar ruído com matriz densidade |

Rodar os testes (a partir da raiz do projeto):

```bash
pytest simulador/tests
```
