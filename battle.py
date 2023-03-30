#전투에 관여될 직접적인 함수
#몬스터와 1:N or N:M 전투가 가능해야 합니다.

import random
import os




def select_monster(monsters):
    print("어떤 몬스터를 공격하시겟습니까? ")
    for i, mon in enumerate(monsters):
        print(f"{i}. 이름 : {mon.name} HP : {mon.hp}")
    index = input(f"[ 0 ~ {len(monsters)-1} ]")
    if index.isalnum():
        index = int(index)
    else :
        return select_monster(monsters)
    for i, mon in enumerate(monsters):
        if i == index and isalive(mon):
            return index
    
    print("잘못된 선택이거나 이미 사망한 몬스터를 선택하셧습니다.")
    return select_monster(monsters)

def user_attack(user, monsters):
    if is_win_lose(monsters):
        return
    
    action = input("어떤 공격을 사용하시겠습니까? (1: 일반 공격, 2: 마법 공격)")
    if action == '1':
        index = select_monster(monsters)
        user.normal_attack(monsters[index])

    elif action == '2':
        index = select_monster(monsters)
        user.magic_attack(monsters[index])
    
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        return user_attack(user, monsters)

def monster_attack(users, monster):
    if is_win_lose(users):
        return
    if not isalive(monster):
        return
    if len(users) != 1:    
        random_user = random.randint(0,len(users)-1)
    else :
        random_user = 0
    
    if isalive(users[random_user]):
        attck_type = random.randint(0, 10)
        
        if attck_type == 0:
            monster.wait()
        elif 3 >= attck_type >= 1:
            monster.absorb(users[random_user])
        else :
            monster.normal_attack(users[random_user])
    else:
        return monster_attack(users, monster)

def isalive(chricter):
    if chricter.hp > 0 :
        return True
    else :
        return False

def is_win_lose(chricters):
    users = len(chricters)
    count = 0
    for user in chricters:
        if not isalive(user):
            count += 1
    if users == count:
        return True
    else :
        return False
    
def win():
    print("승리하였습니다.")

def lose():
    print("패배하였습니다.")
    os.system("pause")

def show_monsters(users, monsters):
    print("==   아군   ==")
    for user in users:
        user.show_status()
    print("==   적군   ==")
    for mon in monsters:
        mon.show_status()

def battle(users, monsters, inventory):
    print("전투를 시작합니다.")
    while(True):
        show_monsters(users, monsters)
        #선택지 유형 추가. 1. 공격 , 2. 아이템 사용 
        #유저 수만큼 공격 방법 설정하고 공격하기.
        
        for user in users:
            if isalive(user):
                user_attack(user, monsters)
        if is_win_lose(users):
            lose()
            os.system("pause")
            return False

        ## 사망판단.
        for mon in monsters:
            monster_attack(users, mon)
        if is_win_lose(monsters):
            for mon in monsters:
                for user in users:
                    user.get_exp(mon.drop_exp(user))
            
            drop_item = mon.drop_item()
            print(drop_item)
            print(inventory.keys())
            if len(drop_item) > 1:
                for item in drop_item:
                    if item in inventory.keys():
                        inventory[item] += 1
                    else :
                        inventory[item] = 1
            if drop_item[0] in inventory.keys():
                inventory[drop_item[0]] += 1
            else :
                inventory[drop_item[0]] = 1
            win()
            os.system("pause")
            
            return True
        
        os.system("pause")
        os.system('cls||clear')

            
