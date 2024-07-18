def check_data(use_data, data):
    if data in use_data:
        return False
    return True

def check_answer(answer):
    if answer not in ['A','B']:
        return False
    return True