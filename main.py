import table
import character
import battle
import random
import os
# 메인 흐름과 전투의 동작 부분.


def create_job():
    joblist = list(map(str, table.job_table.keys()))

    print("============ 직업 선택 ==============")
    print('\n'.join(x for x in joblist))
    print("====================================")

    while (True):
        print("직업 이름은 한글로 입력하세요.")
        job2 = input("직업 : ")
        if job2 in joblist:
            return job2
        else:
            print("잘못 된 입력값 입니다.")


def create_user():
    name = input("이름 : ")
    job = create_job()
    userset = table.job_table[job]
    if job == "전사":
        return character.Warrior(name, userset)
    elif job == "궁수":
        return character.Archer(name, userset)
    elif job == "마법사":
        return character.Wizard(name, userset)
    else:
        print("잘못된 값을 입력하였습니다.")
        os.system("pause")
        return create_user()


def create_monster(monsters, num):
    for i in range(0, num):
        index = random.randint(0, len(table.monter_name_list)-1)
        name = table.monter_name_list[index]
        userset = table.monster_table[name]
        # Player 생성시 추가값있으면 수정.
        monsters.append(character.Monster(name, userset))


def create_team(users):
    print("같이 행동할 동료의 숫자를 골라주세요.")
    cmd = input("동료의 수 [0 ~ 3] : ")
    if cmd.isnumeric():
        cmd = int(cmd)
    else:
        return create_team(users)
    if 0 <= int(cmd) <= 3:
        for i in range(0, int(cmd)+1):
            os.system("cls||clear")
            if i == 0:
                print("주인공의 이름은 ? : ")
            else:
                print(f"{i}번째 동료의 이름은 ? : ")
            users.append(create_user())

    else:
        print("잘못된 값입니다.")
        return create_team()


def view_stage(i):
    for j in range(0, 10):
        if j == (10-i):
            print("==================")
            print(f"==   현재위치   ==")
        else:
            print("==================")
            print(f"==     {10-j}층      ==")
        print("==================")


def show_inventory(inventory, users):
    os.system("cls||clear")
    print("==  인벤토리 ==")
    if not inventory:
        print("인벤토리가 비어있습니다.")
        return 0

    for key, value in inventory.items():
        print(f"{key} : {value}")
    use_item_select(inventory, users)


def item_value_max(item_value, user):
    if item_value[0] == 'hp':
        heal = (user.hp + item_value[1]) - \
            min(user.hp + item_value[1], user.max_hp)
        total_heal = item_value[1] - heal
        user.hp = total_heal
        print(f"{user.name}의 체력이 {total_heal}만큼 회복하였다.")
    elif item_value[0] == 'mp':
        heal = (user.mp + item_value[1]) - \
            min(user.mp + item_value[1], user.max_mp)
        total_heal = item_value[1] - heal
        user.mp = total_heal
        print(f"{user.name}의 마나가 {total_heal}만큼 회복하였다.")


def use_item_select(inventory, users):
    print("인벤토리를 닫으려면 [ q ] 를 입력해주세요.")
    cmd = input("사용할 아이템을 입력하세요 : ")
    if cmd in inventory:
        item_value = table.item_value[cmd]
        if inventory[cmd] == 1:
            for user in users:
                item_value_max(item_value, user)
            inventory.pop(cmd)

        elif inventory[cmd] > 1:
            for user in users:
                item_value_max(item_value, user)
            inventory[cmd] -= 1
    elif str.lower(cmd) == 'q':
        print("인벤토리를 닫습니다.")
        return 0
    else:
        print("잘못된 입력입니다.")
        return show_inventory(inventory, users)


def start():
    stage = 1
    users = []
    monsters = []
    inventory = {}
    os.system("cls||clear")
    create_team(users)
    while (True):
        os.system('cls||clear')
        view_stage(stage)
        print("1. 상태창 보기")
        print("2. 전투 하기")
        print("3. 인벤토리 보기")
        print("0. 종료하기")
        cmd = input("고르시오 : ")
        if cmd == '1':
            for user in users:
                user.show_status()
            os.system('pause')
        elif cmd == '2':
            os.system('cls||clear')
            print(f"탑 {stage}층에 입장합니다.")
            monsters.clear()
            create_monster(monsters, stage)
            iswin = battle.battle(users, monsters, inventory)
            if not iswin:
                return start()
            stage += 1
        elif cmd == '3':
            show_inventory(inventory, users)
            os.system('pause')
        elif cmd == '0':
            exit()


if __name__ == "__main__":
    start()
