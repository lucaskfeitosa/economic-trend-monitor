import requests

def get_info_api(initial_date, end_date):
    try:
        response = requests.get(f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial={initial_date}&dataFinal={end_date}', timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout as err:
        print('Timed out: {err}')
    
    except requests.exceptions.HTTPError as err:
        print(f"Erro HTTP ocorrido: {err}")

    except requests.exceptions.ConnectionError as err:
    print(f"Erro de Conexão: Não foi possível conectar ao servidor. Detalhes: {err}")

get_info_api('01/01/2026', '01/09/2026')