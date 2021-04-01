stack=[]
cadena = input("ingrese una serie de corchetes:")
error = 0



for caracter in cadena:
    try:
        if caracter == "[":
           stack.append(caracter)
        else:
           stack.pop(-1)
    except:
        error = 1
        break



if (len(stack) == 0) and (error != 1) :
    print("True")
else:
    print("False")