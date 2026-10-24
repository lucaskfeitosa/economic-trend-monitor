from economic_trend_monitor.data_processing.data_processing import data_processing
from datetime import date
import pytest



def test_data_processing():
    #Cria os dados brutos manuais
    data_api = [
        {"data": "01/01/2026", "valor": "0.33"},
        {"data": "01/02/2026", "valor": "0.70"},
    ]

    #Executa a função passando os dados diretamente pelo argumento 'data'
    result = data_processing(data=data_api)

    #Valida se a transformação dos tipos ocorreu perfeitamente
    assert isinstance(result, list)
    assert len(result) == 2

    for registro in result:
        assert isinstance(registro, dict)
        #Verifica se as strings viraram os tipos corretos
        assert isinstance(registro["data"], date)
        assert isinstance(registro["valor"], float)