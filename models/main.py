from ingrediente import Ingrediente
from produto import Produto
from venda import Venda
from caixa import Caixa

caixa = Caixa()


i1 = Ingrediente("Chocolate", 20, 100, 8)
i2 = Ingrediente("Cacau em pó", 14.5, 300, 22)
i3 = Ingrediente("Prestígio", 30, 500, 34)

b1 = Produto("Bolo de prestígio", [i1, i3], 14)

print (b1.custo_total())


v1 = Venda(b1, 1, "21/09/26")
caixa.registrar_venda(v1)

print (caixa.faturamento_total())
print (caixa.lucro_total())

