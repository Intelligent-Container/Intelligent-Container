import json


def data_parse(json_str):
    obj = json.loads(json_str)
    A = obj['A']
    B = obj['B']
    C = obj['C']
    D = obj['D'][0] + "-" + obj['D'][1] + "-" + obj['D'][2]
    E = obj['E'][0] + ":" + obj['E'][1] + ":" + obj['E'][2]
    # D = obj['D']
    # E = obj['E']
    F1 = obj['F']['F1']
    F2 = obj['F']['F2']
    F3 = obj['F']['F3']
    F4 = obj['F']['F4']
    F5 = obj['F']['F5']
    # F1 = obj['F1']
    # F2 = obj['F2']
    # F3 = obj['F3']
    # F4 = obj['F4']
    # F5 = obj['F5']
    G = obj['G']
    H = obj['H']
    data = [A, B, C, D, E, F1, F2, F3, F4, F5, G, H]
    # print(data)
    return data
