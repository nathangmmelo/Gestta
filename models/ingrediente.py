class Ingrediente:
    def __init__(self, nome, preco_compra, qtd_comprada, qtd_usada):
        self.nome = nome
        self.preco_compra = preco_compra 
        self.qtd_comprada = qtd_comprada 
        self.qtd_usada = qtd_usada

    def custo_unitario(self):
        return self.preco_compra / self.qtd_comprada

    def custo_na_receita(self):
        return self.custo_unitario() * self.qtd_usada
    
    
