from ingrediente import Ingrediente
from produto import Produto


i1 = Ingrediente("Chocolate", 20, 100, 8)
i2 = Ingrediente("Cacau em pó", 14.5, 300, 22)
i3 = Ingrediente("Prestígio", 30, 500, 34)

b1 = Produto("Bolo de prestígio", [i1, i3], 14)

print (b1.custo_total())
print (b1.lucro_unitario())