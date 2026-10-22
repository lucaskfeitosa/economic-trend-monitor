from unittest.mock import Mock

import economic_trend_monitor.data_collection.data_collection as data_collection

def test_get_info_api(monkeypatch):
    expected_data = [
        {"data": "01/01/2026", "valor": "0.33"},
        {"data": "01/02/2026", "valor": "0.70"},
    ]

    response = Mock()
    response.json.return_value = expected_data

    mock_get = Mock(return_value=response)

    monkeypatch.setattr(
        data_collection.requests,
        "get",
        mock_get,
    )

    result = data_collection.get_info_api(
        "01/01/2026",
        "01/02/2026",
    )

    assert result == expected_data
    mock_get.assert_called_once()