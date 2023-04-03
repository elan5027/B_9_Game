
import random
import os
import sys
from inventory import show_inventory
from character import Player

# 이름 : select_battle_menu
# 인자 : 없음
# 역할 : 전투 메뉴를 선택하는 함수
# 반환 : 선택한 메뉴 번호(1 또는 2)
# 설명 : 전투 메뉴를 출력하고 사용자로부터 입력을 받아 선택한 메뉴 번호를 반환합니다.


def select_battle_menu():
    battle_manu = {
        '1': '공격',
        '2': '아이템 사용'
    }
    for key, value in battle_manu.items():
        print(f"{key}. {value}")
    cmd = input("메뉴를 선택해 주세요 : ")
    return cmd if cmd in battle_manu else select_battle_menu()


# 이름 : select_monster
# 인자 : monsters(몬스터 리스트)
# 역할 : 몬스터를 선택하는 함수
# 반환 :
#   - 선택한 몬스터의 인덱스
#   - 값이 유효하지 않을 경우 재귀적 호출.
# 설명 : 몬스터 리스트에서 사용자가 선택한 몬스터를 반환합니다.


def select_monster(monsters):
    print("어떤 몬스터를 공격하시겠습니까? ")
    for i, monster in enumerate(monsters):
        print(f"{i}. 이름 : {monster.name} HP : {monster.hp}")
    index = input(f"[ 0 ~ {len(monsters)-1} ]")
    if not index.isnumeric():
        return select_monster(monsters)
    
    index = int(index)
    if index >= len(monsters) or not alive_check(monsters[index]):
        print("잘못된 선택이거나 이미 사망한 몬스터를 선택하셨습니다.")
        return select_monster(monsters)
    
    return index

# 이름 : user_attack
# 인자 : user(유저), monsters(몬스터 리스트)
# 역할 : 유저가 몬스터를 공격하는 함수
# 반환 : 값이 유효하지 않을 경우 재귀적 호출.
# 설명 : 유저가 몬스터를 공격합니다.


def user_attack(user, monsters):
    if dead_check_list(monsters):
        return
    for key, value in user.action.items():
        print(f"{key}. {value['verbose']}")
    action = input("어떤 공격을 사용하시겠습니까? ")
    if action not in user.action:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        return user_attack(user, monsters)
    index = select_monster(monsters)
    user.action[action]['action'](monsters[index])


# 이름 : monster_attack
# 인자 : users(유저 리스트), monster(몬스터)
# 역할 : 몬스터가 유저를 공격하는 함수
# 반환 : 값이 유효하지 않을 경우 재귀적 호출.
# 설명 : 몬스터가 유저를 공격합니다.

def monster_attack(users, monster):
    if dead_check_list(users):
        return

    random_user = random.randint(0, len(users)-1) if len(users) != 1 else 0

    if alive_check(users[random_user]):
        attck_type = random.randint(1, 10)

        if attck_type == 1:
            monster.wait()
        elif 4 >= attck_type >= 2:
            if monster.name() in ['거미', '박쥐']:
                monster.absorb(users[random_user])
            else:
                addtional = random.randint(0, 3)
                monster.normal_attack(users[random_user])
                if addtional == 0:
                    monster.addtional_damage(users[random_user])
        else:
            addtional = random.randint(0, 3)
            monster.normal_attack(users[random_user])
            if addtional == 0:
                monster.addtional_damage(users[random_user])
    else:
        return monster_attack(users, monster)


# 이름 : looting
# 인자 : monsters(몬스터 리스트), users(유저 리스트)
# 역할 : 몬스터가 드랍한 아이템을 획득하고 경험치를 얻는 함수입니다.
# 반환 : 없음
# 설명 :
#   - 몬스터의 리스트를 순회하며 아이템리스트에 아이템 추가 및 유저에게 경험치를 추가한다.
#   - 받아온 아이템 리스트를 순회하며 유저가 공통적으로 관리하는 Player 객체안의 inventory에 아이템을 추가한다.

def looting(monsters, users):
    drop_item = []
    for monster in monsters:
        monster_drop = monster.drop_item()
        if len(monster_drop) > 1:  # 2개이상의 아이템이 담겻을 경우.
            for item in monster_drop:
                drop_item.append(item)
        else:
            drop_item.append(monster_drop[0])
        for user in users:
            user.get_exp(monster.drop_exp(user))

    for item in drop_item:
        # 딕셔너리의 키값에는 리스트가 들어가지 않기때문에 주의하셔야됩니다.
        if str(item) in Player.inventory.keys():
            Player.inventory[str(item)] += 1
        else:
            Player.inventory[str(item)] = 1


# 이름 : show_monsters
# 인자 : users(유저 리스트), monsters(몬스터 리스트)
# 역할 : 유저와 몬스터의 상태를 출력하는 함수
# 반환 : 없음
# 설명 : 유저와 몬스터의 상태를 출력합니다.

def show_monsters(users, monsters):
    print("==   아군   ==")
    for user in users:
        user.show_status()
    print("==   적군   ==")
    for mon in monsters:
        mon.show_status()

# 이름 : alive_check
# 인자 : chricter(캐릭터)
# 역할 : 캐릭터가 살아있는지 확인하는 함수
# 반환 : 살아있으면 True, 아니면 False
# 설명 : 캐릭터가 살아있는지 확인합니다.


def alive_check(chricter):
    if chricter.hp > 0:
        return True
    else:
        return False


# 이름 : dead_check_list
# 인자 : chricters(캐릭터 리스트)
# 역할 : 캐릭터가 모두 죽었는지 확인하는 함수
# 반환 : 모두 죽었으면 True, 아니면 False
# 설명 : 캐릭터 리스트에서 모든 캐릭터가 죽었는지 확인합니다.

def dead_check_list(chricters):
    users = len(chricters)
    count = 0  # 죽은놈 숫자체크 용도.
    for user in chricters:
        if not alive_check(user):
            count += 1  # 죽을대마다 1씩 증가.
    if users == count:
        return True
    else:
        return False


def win():
    print("승리하였습니다.")


def lose():
    print("패배하였습니다.")


# 이름 : battle
# 인자 : users(유저 리스트), monsters(몬스터 리스트), inventory(인벤토리 딕셔너리)
# 역할 : 유저와 몬스터가 싸우는 전투를 진행하는 함수
# 반환 : 전투 결과 (bool)
# 설명 :
#   - 이 함수에서는 전투가 진행되는 동안 유저와 몬스터의 상태를 보여주고 승패여부를 판단한다.
#   - 만약 승리하면 경험치와 아이템을 획득하고, 패배하면 게임 오버 처리한다.
#   - select_battle_menu() 함수를 호출하여 메뉴를 선택할 수 있다.
#   - 메뉴 1을 선택하면 유저가 몬스터에게 공격하고, 메뉴 2를 선택하면 인벤토리를 확인할 수 있다.

def battle(users, monsters):
    print("전투를 시작합니다.")
    while True:
        if dead_check_list(users):
            lose()
            os.system("pause")
            return False
        elif dead_check_list(monsters):
            looting(monsters, users)
            win()
            os.system("pause")
            return True
        show_monsters(users, monsters)
        menu = select_battle_menu()
        if menu == '1':
            for user in users:
                if alive_check(user):
                    user_attack(user, monsters)
            for monster in monsters:
                if alive_check(monster):
                    monster_attack(users, monster)
        elif menu == '2':
            show_inventory(users)
        os.system("pause")
        os.system('cls||clear')
