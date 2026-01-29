"""
Etapa 1 - Integração com a API de Dados Abertos da ANS

Responsabilidades:
- Identificar os últimos 3 trimestres disponíveis
- Baixar arquivos ZIP de demonstrações contábeis
- Extrair e processar arquivos de despesas
- Normalizar e consolidar os dados em um único CSV

Observação:
Este código foi estruturado de forma modular e documentada,
considerando execução local em Python.
"""

import requests
import zipfile
import os
import pandas as pd

BASE_URL = "https://dadosabertos.ans.gov.br/FTP/PDA/"

def identificar_trimestres():
    """
    Identifica os 3 últimos trimestres disponíveis na API.
    Estratégia:
    - Listar diretórios por ano/trimestre
    - Ordenar do mais recente para o mais antigo
    """
    pass

def baixar_zips(trimestres):
    """
    Para cada trimestre identificado:
    - Localiza arquivos ZIP
    - Realiza download
    - Armazena localmente
    """
    pass

def extrair_e_processar():
    """
    Processa os arquivos baixados:
    - Extrai ZIPs
    - Identifica arquivos relacionados a despesas/sinistros
    - Suporta CSV, TXT e XLSX
    - Normaliza nomes de colunas
    """
    pass

def consolidar_dados():
    """
    Consolida os dados processados em um único arquivo CSV
    com as colunas:
    CNPJ, RazaoSocial, Ano, Trimestre, ValorDespesas
    """
    pass

if __name__ == "__main__":
    trimestres = identificar_trimestres()
    baixar_zips(trimestres)
    extrair_e_processar()
    consolidar_dados()
