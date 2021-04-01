
diccionario_romano= {
    '0':{'unidad':'',
         'decena':'',
         'centena':'',
         'milenio':''},
    '1':{'unidad':'I',
         'decena':'X',
         'centena':'C',
         'milenio':'M'},
    '2':{'unidad':'II',
         'decena':'XX',
         'centena':'CC',
         'milenio':'MM'},
    '3':{'unidad':'III',
         'decena':'XXX',
         'centena':'CCC',
         'milenio':'MMM'},
    '4':{'unidad':'IV',
         'decena':'XL',
         'centena':'CD',
         'milenio':'MMMM'},
    '5':{'unidad':'V',
         'decena':'L',
         'centena':'D',
         'milenio':'MMMMM'},
    '6':{'unidad':'VI',
         'decena':'LX',
         'centena':'CC',
         'milenio':'MMMMMM'},
    '7':{'unidad':'VVI',
         'decena':'LXX',
         'centena':'DCC',
         'milenio':'MMMMMMM'},
    '8':{'unidad':'VIII',
         'decena':'LXXX',
         'centena':'DCCC',
         'milenio':'MMMMMMMM'},
    '9':{'unidad':'IX',
         'decena':'XC',
         'centena':'CM',
         'milenio':'MMMMMMMMM'}

}



def convertir_numero(num,tipo):
    num_milenio=int(num / 1000)
    num_centena= int((num % 1000) / 100)
    num_decena= int(((num % 1000) % 100) / 10 )
    num_unidad= int((((num % 1000) % 100) % 10 ) / 1)

    if tipo.lower()=='minuscula':
        print((diccionario_romano[str(num_milenio)]['milenio']+diccionario_romano[str(num_centena)]['centena']+diccionario_romano[str(num_decena)]['decena']+diccionario_romano[str(num_unidad)]['unidad']).lower())
    else:
        print(diccionario_romano[str(num_milenio)]['milenio']+diccionario_romano[str(num_centena)]['centena']+diccionario_romano[str(num_decena)]['decena']+diccionario_romano[str(num_unidad)]['unidad'])
    




def menu_seleccion_tipo_letra():
    seleccion_tipo = input('Como desea que se muestre el numero romano (mayuscula o minuscula):')
    if (seleccion_tipo.lower() != 'mayuscula') and (seleccion_tipo.lower() != 'minuscula'):
        print('No ingresó una opcion valida. El numero romano se mostrará en mayuscula por defecto.')
        seleccion_tipo='mayuscula'
    return seleccion_tipo



numero_a_convertir=input("Ingrese le numero que desea convertir a ROMANO : ")
tipo = menu_seleccion_tipo_letra()
while (int(numero_a_convertir) < 0) or (int(numero_a_convertir) >9999):
    print(" ")
    print("El numero ingresado es mayor a lo permitido. Por favor ingrese un numero entre el 1 y el 9999")
    numero_a_convertir=input("Ingrese le numero que desea convertir a ROMANO : ")

convertir_numero(int(numero_a_convertir),tipo)

