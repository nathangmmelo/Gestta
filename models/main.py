from ingrediente import Ingrediente
from produto import Produto
from venda import Venda
from caixa import Caixa
from despesa import Despesa

caixa = Caixa()

#- - Ingredientes - -
i1 = Ingrediente("Chocolate", 20, 100, 8)
i2 = Ingrediente("Cacau em pó", 14.5, 300, 22)
i3 = Ingrediente("Prestígio", 30, 500, 34)

#- - Bolos feitos - -
b1 = Produto("Bolo de prestígio", [i1, i3], 14)

#- - Despesas - -
d1 = Despesa("Potes", 12.80, "Embalagem", "21/08/26")

#- - Vendas - -
v1 = Venda(b1, 1, "21/09/26")
v2 = Venda(b1, 3, "21/08/26")

#- - Registro - -
caixa.registrar_venda(v1)
caixa.registrar_despesa(d1)

#- - Print - -
print (b1.custo_total())
print (b1.lucro_unitario())
print (v2.valor_bruto())
print (v2.valor_liquido())
