# input

cant_minuto=input("dijite la cantidad de minuto: ")
cant_minuto=int(cant_minuto)

# procesing

if cant_minuto <=3:
    print("el valor de la llamada es : 300 pesos")

else:
    valor_llamada= 300+50*(cant_minuto-3)

    # output
    print ("el valor de la llamada es: "+str(valor_llamada))