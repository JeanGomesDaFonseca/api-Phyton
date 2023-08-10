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
                 'cuisine_name': estabelecimento['cuisine_name'],
                 'city_name': estabelecimento['city_name'],
                 'city_slug': estabelecimento['city_slug'], 
                 'state_name': estabelecimento['state_name'], 
                 'name': estabelecimento['name'], 
                 'slug': estabelecimento['slug'], 
                 'about': estabelecimento['about'], 
                 'payment_description': estabelecimento['payment_description'], 
                 'opening_hours_description': estabelecimento['opening_hours_description'], 
                 'price_range': estabelecimento['price_range'],
                 'price_range_description': estabelecimento['price_range_description'], 
                 'cover_image': estabelecimento['cover_image'],
                 'profile_image': estabelecimento['profile_image'], 
                 'photos': estabelecimento['photos'], 
                 'website': estabelecimento['website'], 
                 'telephone': estabelecimento['telephone'],
                 'zipcode': estabelecimento['zipcode'], 
                 'address': estabelecimento['address'], 
                 'number': estabelecimento['number'],
                 'complement': estabelecimento['complement'],
                 'neighborhood': estabelecimento['neighborhood'], 
                 'full_address': estabelecimento['full_address'], 
                 'coordinates': estabelecimento['coordinates'], 
                 'reservation': estabelecimento['reservation'],
                'line': estabelecimento['line'],
                'distance': estabelecimento['distance'], 
                'line_count': estabelecimento['line_count'], 
                'menu': estabelecimento['menu'],
                'user_known': estabelecimento['user_known'], 
                'total_user_known': estabelecimento['total_user_known'], 
                'published_at': estabelecimento['published_at'], 
                'amenities': estabelecimento['amenities'], 
                'events': estabelecimento['events']
            }
            print(obj)

            estabelecimentosDados.append(obj)
    else:
        # A requisição falhou
        print(f'Erro na página {page}:', response.status_code)

# Salvar os dados em um arquivo CSV
nome_arquivo = 'estabelecimentosAllData.csv'

with open(nome_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
    # Definir os nomes das colunas do CSV
    fieldnames = ['cuisine_name', 'city_name', 'city_slug',
             'state_name', 'name', 'slug'  ,
             'about','payment_description', 'opening_hours_description',
             'price_range', 'price_range_description', 'cover_image', 'profile_image',
             'photos', 'website', 'telephone', 'zipcode', 'address',
             'number', 'complement', 'neighborhood','full_address','coordinates',
             'reservation', 'line', 'distance', 'line_count', 'menu', 'user_known',
             'total_user_known', 'published_at', 'amenities', 'events'
               ]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Escrever os nomes das colunas no arquivo CSV
    writer.writeheader()

    # Escrever os dados dos estabelecimentos no arquivo CSV
    for estabelecimento in estabelecimentosDados:
        writer.writerow(estabelecimento)

print(f'Os dados foram salvos no arquivo "{nome_arquivo}" com sucesso.')
