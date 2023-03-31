from character import Player
import os
import table


# 이름 : show_inventory
# 인자 : inventory(인벤토리 리스트), users(유저 리스트)
# 역할 : 인벤토리를 출력하고 아이템을 사용하는 함수
# 반환 : 없음
# 설명 : 인벤토리에 저장된 아이템을 출력하고 사용자가 선택한 아이템을 사용합니다.

def show_inventory(users):
    os.system("cls||clear")
    print("==  인벤토리  ==")
    if not Player.inventory:
        print("인벤토리가 비어있습니다.")
        return 0

    for key, value in Player.inventory.items():
        print(f"{key} : {value}")
    use_item_select(users)


# 이름 : item_value_max
# 인자 : item_value(아이템 값), user(유저 객체)
# 역할 : 아이템을 사용하여 유저의 체력과 마나를 회복하는 함수
# 반환 : 없음
# 설명 : 아이템 값을 이용하여 유저의 체력과 마나를 회복합니다.

def item_value_check(item_value, user):
    if item_value['name'] == 'hp':
        heal = (user.hp + item_value['value']) - \
            min(user.hp + item_value['value'], user.max_hp)
        total_heal = item_value['value'] - heal
        user.hp = user.hp + total_heal
        print(f"{user.name}의 체력이 {total_heal}만큼 회복하였다.")
    elif item_value['name'] == 'mp':
        heal = (user.mp + item_value['value']) - \
            min(user.mp + item_value['value'], user.max_mp)
        total_heal = item_value['value'] - heal
        user.mp = user.mp + total_heal
        print(f"{user.name}의 마나가 {total_heal}만큼 회복하였다.")


# 이름 : use_item_select
# 인자 : inventory(인벤토리 리스트), users(유저 리스트)
# 역할 : 아이템을 사용하는 함수
# 반환 : 값이 유효하지 않을 경우 재귀적 호출.
# 설명 : 인벤토리에서 아이템을 선택하여 사용합니다


def use_item_select(users):
    print("인벤토리를 닫으려면 [ q, Q ] 를 입력해주세요.")
    cmd = input("사용할 아이템을 입력하세요 : ")
    if cmd in Player.inventory:
        item_value = table.item_value.get(cmd)
        if Player.inventory[cmd] == 1:
            for user in users:
                item_value_check(item_value, user)
            Player.inventory.pop(cmd)

        elif Player.inventory[cmd] > 1:
            for user in users:
                item_value_check(item_value, user)
            Player.inventory[cmd] -= 1
    elif str.lower(cmd) == 'q':
        print("인벤토리를 닫습니다.")
        return 0
    else:
        print("잘못된 입력입니다.")
        return show_inventory(users)
