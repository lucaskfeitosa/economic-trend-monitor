import requests

def get_info_api(initial_date, end_date):
    
    response = requests.get(f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial={initial_date}&dataFinal={end_date}', timeout=10)
    response.raise_for_status()
    return response.json()