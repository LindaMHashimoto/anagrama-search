import random
import json


palavra = input('Digite a palavra a ser sorteada: ')
lista_letras = list(palavra)
lista_diferentes = list(dict.fromkeys(lista_letras))

tamanho_lista_letras = len(lista_letras)
tamanho_diferentes = len(lista_diferentes)
total1 = 1
total2 = 1

for n in range(tamanho_lista_letras):

	total1 = total1 * (n+1)


count = 0
mylist = []
for i in range(total1):

	palavra_embaralhada = ''.join(random.sample(palavra, len(palavra)))
	mylist.append(palavra_embaralhada)
	mylist = list(dict.fromkeys(mylist))
	mylist2 = mylist.sort()
	count = len(mylist)

print(mylist, 'Quantidade de anagramas: ', count)

#funcao para converter a lista de anagramas em um arquivo json

def convert_to_json(lista):

	nome_arquivo = input('Digite o nome do novo arquivo JSON (coloque .json no final do nome pra nao dar pau): ')
	arquivo = open(nome_arquivo, "w")
	json.dump(lista, arquivo, indent = 4, sort_keys = False)
	arquivo.close()
	print('Arquivo JSON ', nome_arquivo, ' criado com sucesso!')

'''
#funcao para converter url em string
def convert_to_string(palavra):

	str(palavra)
'''
#lista de urls encontradas para os anagramas
lista_urls = []

for item in mylist:

	try:

		from googlesearch import search
	except ImportError:

		print('No module named google found')

	query = item
	print('Palavra buscada: ', query)
	print('')
	for j in search(query, tld = "com", num = 3, stop = 3, pause = 2):


		print ('Resultado encontrado: ', j)
		#convert_to_string(j)
		lista_urls.append(j)
lista_urls.append(count)
print(lista_urls)
#chamada da funçao para transformar lista em arquivo JSON
convert_to_json(lista_urls)