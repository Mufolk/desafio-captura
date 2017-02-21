#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectTimeout, ConnectionError

class Produto(object):
    def __init__ (self, id_site, last_page):
        self.id_site = id_site # há apenas um por url
        self.last_page = last_page # muda a cada tipo de produto
        
    def incluir_produtos(self):
        page = 0  # variável que irá contar as páginas
        export_parcial = [] # lista que irá reter os dados dos produtos
        while (page<=(self.last_page)):
            url = ('http://www.epocacosmeticos.com.br/buscapagina?fq=C%3A%2'
                   '{0}''%2F&PS=20&sl=3d564047-8ff1-4aa8-bacd-f11730c3fce6&cc'
                   '=4&sm=0&PageNumber=''{1}'.format(self.id_site,page))
            site = self.acessar_site(url)
            export_parcial = self.ler_pagina(site, export_parcial)  
            print 'Página ',page,' finalizada'       
            page +=1 #adiciona uma página, movendo o crawler para frente
        return export_parcial
    
    def acessar_site(self, url):
        try:
            site = requests.get(url)
            return site
        except (ConnectTimeout, ConnectionError) as erro:
            print 'Conexão não estabelecida: %s' %(erro)
        
    def ler_pagina (self, site, export_parcial):
        soup = BeautifulSoup(site.content, 'html.parser')
        for a in soup.findAll('a', attrs={'class': 'productImage'}): 
                #adiciona, já formatado, os produtos na lista
            export_parcial.append('Nome: %s, Link: %s' %(a.get('title'), 
                                                         a.get('href')))
        return export_parcial
            
# Observações:
# Os prints servem para dar uma ideia do que está acontecendo com o crawler

# A variável self.id_site é a váriavel que muda na url de cada tipo de
# produto do site.

# A variável self.last_page é um outro dado que muda a cada setor, foi
# utilizado para terminar o loop e devolver a lista com todos os produtos
# formatados para o main.

# Por essas características que o construtor possui esses dois parâmetros.
# Assim, o beautiful soup poderá acessar todas as páginas, vasculhando seu
# conteúdo.