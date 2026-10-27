def data_analysis(processed_data):
    if not processed_data:
        raise ValueError("Cannot calculate the average of an empty dataset")

    values = [item["valor"] for item in processed_data]
    return round(sum(values) / len(values), 2)