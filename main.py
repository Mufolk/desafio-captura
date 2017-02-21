#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Produto import Produto

print 'Inicializando crawler...'

perfumes = Produto('f1000001', 50)
lista_p = perfumes.incluir_produtos()
print 'Seguindo para próxima categoria de produtos'

maquiagem = Produto('f1000004', 50)
lista_m = maquiagem.incluir_produtos()
print 'Seguindo para próxima categoria de produtos'
 
cabelos = Produto('f1000037', 50)
lista_c = cabelos.incluir_produtos()
print 'Seguindo para próxima categoria de produtos'
 
dermocosmeticos = Produto('f1000130', 39)
lista_d = dermocosmeticos.incluir_produtos()
print 'Seguindo para próxima categoria de produtos'
 
tratamentos = Produto('f1000089', 37)
lista_t = tratamentos.incluir_produtos()
print 'Seguindo para próxima categoria de produtos'
 
corpo_e_banho = Produto('f1000070', 32)
lista_cb = corpo_e_banho.incluir_produtos()
print 'Seguindo para próxima categoria de produtos'
 
unhas = Produto('f1000013', 11)
lista_u = unhas.incluir_produtos()
 
print 'Concatenando as listas'
export = lista_p + lista_m + lista_c + lista_d + lista_t + lista_cb + lista_u


print 'Removendo itens repetidos'
export = list(set(export)) # retira os itens duplicados da lista

print 'Exportando lista de produtos'

try:
    with open('csvfile.csv','ab') as arquivo: 
            for line in export:
                try:
                    arquivo.write(line.encode('utf-8'))#linha formatada em utf-8 
                except (UnicodeEncodeError) as erro:
                    print 'A linha não possui um caractere válido %s' %(erro)
                arquivo.write('\n')           
    arquivo.close()
except ():
    print 'Arquivo csv não pode ser gerado'
 
print 'Finalizando Crawler...'
    
# Como funciona a criação da referência ao objeto produto: 
# (tipo de produto) = Produto (variável que identifica o tipo de produto,
#                              última página com produtos)