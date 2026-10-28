"""Teste inicial: confirma que o pacote qsim está instalado e importa.

O qsim é instalado pelo `uv sync` (veja pyproject.toml), por isso o
`import qsim` funciona direto, sem nenhum truque de caminho.

Rodar:  uv run pytest
"""

import qsim


def test_pacote_importa():
    assert qsim.__version__ == "0.0.1"
