moneda_argentina=[1,2,5,10,20,50,100,200,500,1000]

cuanto_paga= input("Ingrese con cuanto paga: ")
a_pagar= input("Ingrese monto a pagar: ")

vuelto= int(cuanto_paga) - int(a_pagar)


i= len(moneda_argentina)

if int(a_pagar) == int(cuanto_paga):
    vuelto_moneda=[0]
else:    
    vuelto_moneda=[]
    for moneda in moneda_argentina:
        while vuelto >= moneda_argentina[i-1]:
            vuelto_moneda.append(moneda_argentina[i-1])
            vuelto= int(vuelto)-moneda_argentina[i-1]
        i-=1

print(vuelto_moneda)