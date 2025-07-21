class Empresa:
  def __init__(self, categoria, nome, produto, custo, qualidade):
      self.categoria = categoria
      self.nome = nome
      self.produto = produto
      self.custo = float(custo)       
      self.qualidade = float(qualidade) 
      self.margem = 0.05
      self.oferta = 0
      self.reposicao = 10
      self.vendas = 0