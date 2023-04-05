import requests

print('Consulta CEP\n')

cepinput = input('Digite o CEP:\nEx: 00000000\n')

if len(cepinput) != 8:
        print('CEP inválido!')
        exit()

url = f'https://viacep.com.br/ws/{cepinput}/json/'

request = requests.get(url)

address_data = request.json()

if 'erro' not in address_data:
    print('==> CEP ENCONTRADO <==')

    print(f'CEP: {address_data["cep"]}')
    print(f'Logradouro: {address_data["logradouro"]}')
    print(f'Complemento: {address_data["complemento"]}')
    print(f'Bairro: {address_data["bairro"]}')
    print(f'Cidade: {address_data["localidade"]}')
    print(f'Estado: {address_data["uf"]}')

else:
    print('CEP inválido!\n{cepinput}')