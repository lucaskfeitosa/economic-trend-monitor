def data_validation(response_data):
    if not isinstance(response_data, list) or not response_data:
        raise ValueError("A entrada deve ser uma lista não vazia.")
        
    for item in response_data:
        if not isinstance(item, dict):
            raise ValueError("Todos os itens da lista devem ser dicionários.")
            
        if 'data' not in item or 'valor' not in item:
            raise ValueError("Os dicionários devem conter as chaves 'data' e 'valor'.")
            
    return True