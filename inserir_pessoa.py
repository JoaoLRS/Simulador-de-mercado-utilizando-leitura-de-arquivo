from pessoa import Pessoa

def inserir_dados_finais(caminho):
    pessoas = []
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        next(arquivo)  
        for linha in arquivo:
            valores = linha.strip().split(',')
            if len(valores) >= 3:
                try:
                    patrimonio = int(valores[1].strip())
                    salario = int(valores[2].strip())
                    pessoas.append(Pessoa(patrimonio, salario))
                except ValueError:
                    print(f"Erro de conversão na linha: {linha.strip()}")
    return pessoas
