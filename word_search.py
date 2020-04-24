try:

	from googlesearch import search
except ImportError:

	print('No module named google found')

query = input('Digite a palavra a ser pesquisada: ')
print('Palavra buscada: ', query)
print('')
for j in search(query, tld = "com", num = 10, stop = 10, pause = 2):

	print (j)