from unittest.mock import Mock

import economic_trend_monitor.data_collection.data_collection as data_collection

def test_get_info_api(monkeypatch):
    # Cria os dados esperados para comparar com o resultado da função.
    expected_data = [
        {"data": "01/01/2026", "valor": "0.33"},
        {"data": "01/02/2026", "valor": "0.70"},
    ]
    # Cria um objeto Mock para simular a resposta da API.
    # Configura o método json() para retornar os dados esperados.
    response = Mock()
    response.json.return_value = expected_data

    # Cria um Mock para simular requests.get().
    # Quando chamado, retorna o objeto response criado acima.
    mock_get = Mock(return_value=response)

    # Substitui temporariamente requests.get pelo mock,
    # evitando uma requisição HTTP real durante o teste.
    monkeypatch.setattr(
        data_collection.requests,
        "get",
        mock_get,
    )
    # Executa a função real com as datas informadas.
    result = data_collection.get_info_api(
        "01/01/2026",
        "01/02/2026",
    )
    
    # Verifica se o resultado obtido corresponde aos dados esperados.
    assert result == expected_data

    # Verifica se requests.get (substituído pelo mock)
    # foi chamado exatamente uma vez.
    mock_get.assert_called_once()