def calcular(numeros):
    if numeros.find(',') != -1:
        lista = [float(i) for i in numeros.split(',')]
        print(lista)
        num_of_terms = len(lista)
        sum_of_terms = 0
        for term in lista:
            sum_of_terms  += term
            
        median = sum_of_terms / num_of_terms    
        print ("La mediana es: {}".format(median))
    else:
        lista = [float(i) for i in numeros.split(' ')]
        print(lista)
        num_of_terms = len(lista)
        sum_of_terms = 0
        for term in lista:
            sum_of_terms  += term
            
        median = sum_of_terms / num_of_terms    
        print ("La mediana es: {}".format(median))

if __name__ == "__main__":
    entrada = input("Ingresa la lista de números: ")
    if entrada == '':
        print('No se han ingresado valores, por favor, ingresa una lista de números')
        numeros = input("Ingresa la lista de números: ")
    else:
        numeros=entrada   
    calcular(numeros)

    