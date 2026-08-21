from venda import Venda
from despesa import Despesa

class Caixa:
    def __init__(self):
        self.vendas = []
        self.despesas = []
    
    def registrar_venda(self, venda):
        self.vendas.append(venda)

    def faturamento_total(self):
        total = 0
        for v in self.vendas:
            total += v.valor_bruto()
        return total

    def lucro_total(self):
        total = 0
        for v in self.vendas:
            total += v.valor_liquido()
        return total
    
    def registrar_despesa(self, despesa):
        self.despesas.append(despesa)

