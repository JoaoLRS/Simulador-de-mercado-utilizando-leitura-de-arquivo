import json

def ler_categorias(caminho='src/categoria.json'):
    with open(caminho, mode='r', encoding='utf-8') as arquivo:
        data = json.load(arquivo)
        return data["categorias"]

def ler_percentuais(caminho='src/categoria.json'):
    with open(caminho, mode='r', encoding='utf-8') as arquivo:
        data = json.load(arquivo)
        return data["percentuais"]