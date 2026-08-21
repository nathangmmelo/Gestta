class Produto:
    def __init__(self, nome, ingredientes, preco_venda):
        self.nome = nome
        self.ingredientes = ingredientes
        self.preco_venda = preco_venda

    def custo_total(self):
        total = 0
        for i in self.ingredientes:
            total += i.custo_na_receita()
        return total

    def lucro_unitario(self):
        return self.preco_venda - self.custo_total()