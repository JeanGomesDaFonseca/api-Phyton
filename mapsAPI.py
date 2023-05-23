import googlemaps
import csv
import requests

# Configurar a API do Google Maps com sua chave de API
gmaps = googlemaps.Client(key='AIzaSyDQYsgnzTrERfFWoM2pu3kjDQ-JVYCIXl8')

# Lista para armazenar os dados de todos os estabelecimentos
estabelecimentosDados = []

for page in range(1, 247):
    # Construir a URL com o valor atual de 'page'
    url = f'https://user.getinapis.com/restaurant/v1/units?service=&distance=10&price_range=&pagination=1&per_page=20&page={page}'

    # Fazer a requisição GET
    response = requests.get(url)

    # Verificar o status da resposta
    if response.status_code == 200:
        conteudo = response.json()
        estabelecimentos = conteudo['data']

        for estabelecimento in estabelecimentos:
            nome_estabelecimento = estabelecimento['name']

            resultado = gmaps.places(query=nome_estabelecimento)

            if resultado['status'] == 'OK':
                print("OI JEAN", page)
                primeiro_resultado = resultado['results'][0]
                primeiro_resultado['nome'] = nome_estabelecimento

                estabelecimentosDados.append(primeiro_resultado)
    else:
        # A requisição falhou
        print(f'Erro na página {page}:', response.status_code)

if estabelecimentosDados and estabelecimentosDados[0]:
    # Extrair as chaves dos dicionários como nomes das colunas
    fieldnames = list(estabelecimentosDados[0].keys())

# Salvar os dados em um arquivo CSV
nome_arquivo = 'estabelecimentosGoogleAPI.csv'

    # Filtrar os dados do estabelecimento para incluir apenas as chaves presentes em fieldnames
estabelecimentosFiltrados = []
for estabelecimento in estabelecimentosDados:
    estabelecimentoFiltrado = {key: estabelecimento.get(key, '') for key in fieldnames}
    estabelecimentosFiltrados.append(estabelecimentoFiltrado)


with open(nome_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Escrever os nomes das colunas no arquivo CSV
    writer.writeheader()

    # Escrever os dados dos estabelecimentos no arquivo CSV
    writer.writerows(estabelecimentosFiltrados)

print(f'Os dados foram salvos no arquivo "{nome_arquivo}" com sucesso.')
