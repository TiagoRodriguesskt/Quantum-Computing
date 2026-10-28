# qsim — meu simulador quântico

Projeto contínuo do curso. O `qsim` é instalado como pacote pelo `uv sync`
(configurado no `pyproject.toml` da raiz), então qualquer script do projeto
pode simplesmente fazer:

```python
import qsim
```

Cada fase adiciona uma peça:

| Fase | Marco |
|---|---|
| 1 | Criar estados e medi-los (Regra de Born) |
| 2 | Aplicar portas a 1 qubit e plotar na Esfera de Bloch |
| 3 | Suportar n qubits (produto tensorial, CNOT) e comparar com o Qiskit |
| 4 | Rodar Deutsch-Jozsa e Grover no próprio simulador |
| 5 | Adicionar ruído com matriz densidade |

## Rodar os testes

A partir da raiz do projeto:

```bash
uv run pytest              # todos os testes
uv run pytest -v           # mostrando o nome de cada teste
```

> Criou um módulo novo em `qsim/`? Não precisa reinstalar nada: o `uv sync`
> instala o pacote em modo editável, e as mudanças valem na hora.
