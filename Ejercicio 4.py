op = 1
vf = 0
key = []
valor = []
while(op == 1):
    pro = input("Por favor digite el nombre del producto: ")
    val = eval(input("Por favor digite el valor del producto: "))
    val+= (val*0.8)
    vf = vf + val
    key.append(pro)
    valor.append(val)
    op = int(input("1. Si \n2. No \n¿Desea digitar otro producto?: "))
print("Productos: ", key)
print("Valor: ", valor)
print("Valor total mas iva: ", vf)