from pessoa import Pessoa

def add_pessoas(pessoas_lista, num_pessoas, patrimonio, salario, variacao=0.0):
    for i in range(num_pessoas):
        pessoas_lista.append(Pessoa(patrimonio + i * variacao, salario + i * variacao))

def inserir_dados_finais(caminho):
    pessoas = [] 
    with open(f"{caminho}", 'r') as arquivo:
        for linha in arquivo:
            valores = linha.strip().split(',')
            if len(valores) == 4:
                add_pessoas(pessoas, int(valores[0]), int(valores[1]), int(valores[2]), int(valores[3]))
    return pessoas