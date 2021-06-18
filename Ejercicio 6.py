produc = {}
for i in range(2):
    prod = input("Digite el producto: ")
    uni = int(input("Digite la cantidad de unidades del producto: "))
    produc[prod] = uni
    keys = list(produc.keys())
    organi = list(produc.values())
print(produc)
print(sorted(organi))