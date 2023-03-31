# 아이템의 사용 정보를 가지는 딕셔너리
item_value = {
    "회복물약(소)": {'name': 'hp', 'value': 20},
    "회복물약(대)": {'name': 'hp', 'value': 50},
    "마나물약(소)": {'name': 'mp', 'value': 20},
    "마나물약(대)": {'name': 'mp', 'value': 50},
}

# 유저가 생성되기 위한 정보
job_table = {
    '전사': {'hp': 300, 'mp': 150, 'normal_power': 40, 'magic_power': 15},
    '궁수': {'hp': 230, 'mp': 300, 'normal_power': 25, 'magic_power': 40},
    '마법사': {'hp': 180, 'mp': 500, 'normal_power': 10, 'magic_power': 55},
}

# 레벨업 당 증가되는 스텟에 대한 정보
level_stat = {
    'hp': 50,
    'mp': 30,
    'normal_power': 10,
    'magic_power': 10
}

# 몬스터가 생성되기 위한 정보
monster_table = {
    '박쥐': {'hp': 50, 'normal_power': 5, 'exp': 5, 'item': ["회복물약(소)"]},
    '거미': {'hp': 80, 'normal_power': 10, 'exp': 10, 'item': ["마나물약(소)"]},
    '늑대': {'hp': 100, 'normal_power': 15, 'exp': 15, 'item': ["회복물약(대)"]},
    '곰': {'hp': 130, 'normal_power': 20, 'exp': 20, 'item': ["마나물약(대)"]},
    '고블린': {'hp': 150, 'normal_power': 25, 'exp': 30, 'item': ["회복물약(소)", "마나물약(소)"]},
    '골렘': {'hp': 180, 'normal_power': 30, 'exp': 50, 'item': ["회복물약(대)", "마나물약(대)"]}
}

