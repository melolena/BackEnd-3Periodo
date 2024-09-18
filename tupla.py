dictA = {}
dictB = dict()


# dictA["dia"]  = "terça"
# print(dictA)

# print(len(dictA))

# print(dictA.keys())

indexLista = [0, 1, 2, 3, 4]

lista = [2, 4, -1, 5, 7]

# for i in range(len(lista)):
#     print(lista[i])

# for item in lista:
#     print(item)


# for x in range(10):
#     if x==3:
#         continue
#     if x==5:
#         break
#     print(x)


# print (sorted(lista))

listaNomes= ["José", "Fabiano", "Cleiton"]


# print(sorted(listaNomes))

def fibonacci(x):
    if x == 0 or x == 1:
        return 1
    else:
        return  fibonacci(x - 1) + fibonacci(x - 2)

listaFibonacci = [fibonacci(x) for x in range(10)]

# print(listaFibonacci)

# def fatorial_for(n):
#   resultado = 1
#   for i in range(1, n + 1):
#     resultado *= i
#   return resultado

# print(fatorial_for(6))


# def fatorial_recursao(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * fatorial_recursao(n - 1)

# print(fatorial_recursao(6))



# def fatorialWhile(n):
#     i = 0
#     resposta = 0
#     while i <= n:
#         if (i<=1):
#             resposta = 1
#         resposta *= i

#         i += 1

#     return resposta

# # print(fatorialWhile(5))


# def fatorialFor(n):
#     resp = 0
#     for i in range(n + 1):
#         if(i <= 1):
#             resp = 1
#         else:
#             resp *= i
#     return resp

# print(fatorialFor(5))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# print(numeros[::-1])
soma_total = 0

for i in numeros:
    soma =  i ** i

    soma_total += soma
print(soma_total)


