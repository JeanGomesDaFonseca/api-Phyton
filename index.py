import csv
import requests

# Lista para armazenar os dados de todos os estabelecimentos
estabelecimentosDados = []

# Iterar sobre as páginas de 1 a 247
for page in range(1, 248):
    print('OI JEAN', page)
    # Construir a URL com o valor atual de 'page'
    url = f'https://user.getinapis.com/restaurant/v1/units?service=&distance=10&price_range=&pagination=1&per_page=20&page={page}'

    # Fazer a requisição GET
    response = requests.get(url)

    # Verificar o status da resposta
    if response.status_code == 200:
        conteudo = response.json()
        estabelecimentos = conteudo['data']

        for estabelecimento in estabelecimentos:
            obj = {
                'name': estabelecimento['name'],
                'website': estabelecimento['website'],
                'telephone': estabelecimento['telephone']
            }

            estabelecimentosDados.append(obj)
    else:
        # A requisição falhou
        print(f'Erro na página {page}:', response.status_code)

# Salvar os dados em um arquivo CSV
nome_arquivo = 'estabelecimentos.csv'

with open(nome_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
    # Definir os nomes das colunas do CSV
    fieldnames = ['name', 'website', 'telephone']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Escrever os nomes das colunas no arquivo CSV
    writer.writeheader()

    # Escrever os dados dos estabelecimentos no arquivo CSV
    for estabelecimento in estabelecimentosDados:
        writer.writerow(estabelecimento)

print(f'Os dados foram salvos no arquivo "{nome_arquivo}" com sucesso.')
