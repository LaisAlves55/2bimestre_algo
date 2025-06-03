numero = ( 5, 8, 12, 8,7, 8, 3)
#Para ser uma tupla precisa estar entre parenteses!!!
print ("Tupla original:", numero)
#imprimindo para o usuario a tupla original, sem manipulaçoes
print("Tamanho da tupla:", len(numero))
print('Acessando o terceiro elemento - por Indice:', numero[2])
#escolhendo qual elemento da tupla queremos acessar atraves do indice
print("Fazendo um slicing do 2 ao 5", numero[2:5])
# o slicing nao pega o ultimo item definido no recorte
print("Quantas vezes o 8 repete na tupla:", numero.count(8))
print (" Posiçao da primeira ocorrencia do 7:", numero.index(7))
minimo_tupla = min (numero)
print("O menor elemento da tupla:", minimo_tupla)
maximo_tupla = max (numero)
print("O maior elemento da tupla:", maximo_tupla)
soma_tupla = sum (numero)
print("A soma dos elementos da tupla:", soma_tupla)
tupla_ordenada = sorted (numero)
print("A tupla ordenada:", tupla_ordenada)
print("Os numeros em ordem utilizando o sort:", tupla_ordenada)
print(" O numero 4 está na tupla?", 4 in numero)
numero2=(15,20)
tupla_concatenada = numero + numero2
print (" A concatenaçao das tuplas 1 e 2 resulta na nova tupla:", tupla_concatenada)
tupla_duplicada = numero * 2
print("A tupla multiplicada por 2:", tupla_duplicada)
