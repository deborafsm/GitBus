"""
docsstrings <[°•°]>
"""

#imprimir 
print(1+1)
 #imprime 2

#aula 1 funcao print
#argumento nao nomeado
#sep="" -> escolher separador.
#\r \n -> CRLF (WINDOWS)
#\n -> UNIX
#print(12, 34, sep="-", ens="+")
#print(45, 67, sep="#", end="*")

#tipos de dados.
#tipagem dinamica forte = ja sabe o tipo nao precisa colocar int, float... entao ele já sabe.
#str string
""" 
strings = texto que sao colocado entre aspas "" ou aspas simples ''.

"""

print("oi")
print('oi também')
#colocar uma aspas com escape \

#tipos de valores
print(type("oi td bem ?"))
print(type(7))
print(type(7.8))
print(type(10==10))

#conversao de tipo / tycasthing / coerção


print(int('1'), type(int('1')))
print(float('1')+6)
print(bool(' '))


#variaveis -> salvam algo na memória.

nome = 'Débora Freire'
altura= 1.63
cons_alta = altura >= 1.70

print('Nome: ',nome,'alutra: ',altura)
print('Considerada alta ?',cons_alta)
