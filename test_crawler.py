import unittest
from Produto import Produto

def test_incluir_produtos():
    teste = Produto('f1000001', 1)
    lista_t = teste.incluir_produtos()
    assert lista_t != None