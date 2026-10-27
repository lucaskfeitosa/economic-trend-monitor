from datetime import date
from economic_trend_monitor.data_analysis.data_analysis import data_analysis
import pytest

def test_data_analysis():
    processed_data = [
        {"data": date(2026, 1, 1), "valor": 0.33},
        {"data": date(2026, 2, 1), "valor": 0.70},
    ]

    result = data_analysis(processed_data)
    assert result == pytest.approx(0.515)
    with pytest.raises(ValueError):
        data_analysis([])