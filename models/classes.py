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

class Venda:
    def __init__(self, produto, quantidade, data):
        self.produto = produto
        self.quantidade = quantidade
        self.data = data

    def valor_bruto(self):
        return self.produto.preco_venda * self.quantidade
    
    def valor_liquido(self):
        return self.produto.lucro_unitario() * self.quantidade


