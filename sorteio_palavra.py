import random

palavra = input('Digite a palavra a ser sorteada: ')
lista_letras = list(palavra)
lista_diferentes = list(dict.fromkeys(lista_letras))

tamanho_lista_letras = len(lista_letras)
tamanho_diferentes = len(lista_diferentes)
total1 = 1
total2 = 1

for n in range(tamanho_lista_letras):

	total1 = total1 * (n+1)

''''
for n in range(tamanho_diferentes):

	total2 = total2 * (n+1)

num_combinacoes = int(total1/total2)
'''
#print(total1, total2, num_combinacoes)

#print(tamanho_lista_letras, tamanho_diferentes)

#palavra_embaralhada = ''.join(random.sample(palavra, len(palavra)))

#print(palavra_embaralhada)
count = 0
mylist = []
for i in range(total1):

	palavra_embaralhada = ''.join(random.sample(palavra, len(palavra)))
	mylist.append(palavra_embaralhada)
	mylist = list(dict.fromkeys(mylist))
	mylist2 = mylist.sort()
	count = len(mylist)

print(mylist, 'Quantidade de anagramas: ', count)


#calcular numero de possibilidades para elementos repetidos para servir como iterator do for
#fazer o google search
palavra_busca = random.choice(mylist)
#print('Palavra buscada: ', palavra_busca)

for item in mylist:

	try:

		from googlesearch import search
	except ImportError:

		print('No module named google found')

	query = item
	print('Palavra buscada: ', query)
	print('')
	for j in search(query, tld = "com", num = 10, stop = 10, pause = 2):


		print (j)