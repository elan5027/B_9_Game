#아이템의 딕셔너리가 설정될 파일.

item_value = {
    "회복물약(소)":['hp', 20],
    "회복물약(대)":['hp', 50],
    "마나물약(소)":['mp', 20],
    "마나물약(대)":['mp', 50],
}

#직업 테이블(스텟)
#Hp, Mp, power, magic_power
job_table = {
    '전사':{'hp':300,'mp':150,'normal_power':40,'magic_power':15},
    '궁수':{'hp':230,'mp':300,'normal_power':25,'magic_power':40},
    '마법사':{'hp':180,'mp':500,'normal_power':10,'magic_power':55},
}


level_stat = {
    'hp':50,
    'mp':30,
    'normal_power':10,
    'magic_power':10
}

#동물(늑대 곰) 동물2 (박쥐 거미) 판타지(고블린) 보스 (골렘)
# 나중에 [hp,power,exp,아이템] 맞는 대로 수정해주셔도 됩니다!
monster_table = {
    '박쥐':{'hp':50,'normal_power':5, 'exp':5, 'item':["회복물약(소)"]},
    '거미':{'hp':80,'normal_power':10,'exp':10,'item':["마나물약(소)"]},
    '늑대':{'hp':100,'normal_power':15,'exp':15,'item': ["회복물약(대)"]},
    '곰':{'hp':130,'normal_power':20,'exp':20,'item':["마나물약(대)"]},
    '고블린':{'hp':150,'normal_power':25,'exp':30,'item':["회복물약(소)","마나물약(소)"]},
    '골렘':{'hp':180,'normal_power':30,'exp':50,'item':["회복물약(대)","마나물약(대)"]}
}

monter_name_list = list(map(str,monster_table.keys()))

#test_code


#몬스터 테이블 (스텟)