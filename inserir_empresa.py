import csv
from empresa import Empresa

def ler_empresas(caminho_arquivo='src/empresas.csv'):
    lista_empresas = []
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        try:
            next(leitor_csv)  
        except StopIteration:
            return lista_empresas

        for linha in leitor_csv:
            nova_empresa = Empresa(categoria=linha[0], nome=linha[1], produto=linha[2], custo=linha[3], qualidade=linha[4])
            lista_empresas.append(nova_empresa)
            
    return lista_empresas