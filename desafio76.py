produto = [["Arroz", 3.50],
     ["Leite", 4.50],
     ["Cuzcus", 2.00],
    ["Farinha", 5.00]]

print("{:<12} {:<15} ".format('Produto', 'Valor'))

for v in produto:
    Produto, Valor = v
    print("{:.<12} R${:<15} ".format(Produto, Valor))
