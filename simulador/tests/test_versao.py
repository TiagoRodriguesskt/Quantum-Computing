"""Teste inicial: confirma que o pacote qsim pode ser importado."""

import sys
from pathlib import Path

# Permite importar qsim sem instalá-lo como pacote
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import qsim


def test_pacote_importa():
    assert qsim.__version__ == "0.0.1"
