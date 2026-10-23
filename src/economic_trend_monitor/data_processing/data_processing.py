from economic_trend_monitor.data_collection.data_collection import get_info_api
from datetime import datetime

def data_processing(data):
    processed_data = []
    for record in data:
        processed_record = record.copy()
        try:
            processed_record['data'] = datetime.strptime(processed_record['data'], '%d/%m/%Y').date()
            processed_record['valor'] = float(processed_record['valor'])
            processed_data.append(processed_record)
        except (ValueError, TypeError, KeyError) as err:
            print(f"Erro encontrado no registro {record}: {err}")
            continue

    return processed_data