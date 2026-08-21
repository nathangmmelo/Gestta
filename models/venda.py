class Venda:
    def __init__(self, produto, quantidade, data):
        self.produto = produto
        self.quantidade = quantidade
        self.data = data

    def valor_bruto(self):
        return self.produto.preco_venda * self.quantidade

    def valor_liquido(self):
        return self.produto.lucro_unitario() * self.quantidade