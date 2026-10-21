from economic_trend_monitor.data_collection.data_collection import get_info_api
import pytest

def test_data_collection(monkeypath):
    assert get_info_api != None
    