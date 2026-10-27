from economic_trend_monitor.data_collection.data_collection import get_info_api
from economic_trend_monitor.data_processing.data_processing import data_processing
from economic_trend_monitor.data_analysis.data_analysis import data_analysis

def run_pipeline(initial_date, end_date):
    resp = get_info_api(initial_date, end_date)
    processed_data = data_processing(resp)
    return data_analysis(processed_data)

