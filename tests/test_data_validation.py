from economic_trend_monitor.data_validation.data_validation import data_validation
import pytest

def test_data_validation():
    expected_data = [
            {"data": "01/01/2026", "valor": "0.33"},
            {"data": "01/02/2026", "valor": "0.70"},
        ]

    assert data_validation(expected_data) is True

    with pytest.raises(ValueError):
            data_validation("Dado inválido")
