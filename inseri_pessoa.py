from pessoa import Pessoa


pessoas = []


def add_pessoas(num_pessoas, patrimonio, salario, variacao=0.0):
    for i in range(num_pessoas):
        pessoas.append(Pessoa(patrimonio + i * variacao, salario + i * variacao))


dados_finais = []

def inserir_dados_finais(caminho):
    with open(f"{caminho}", 'r') as arquivo:
        for linha in arquivo:
            valores = linha.strip().split(',')
            if len(valores) == 4:
                add_pessoas(int(valores[0]),int(valores[1]), int(valores[2]), int(valores[3 ]))