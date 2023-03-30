import table
import character
import battle
import random
import os
# 메인 흐름과 전투의 동작 부분.
def create_job():
    joblist = list(map(str,table.job_table.keys()))
    # for i, job in enumerate(joblist, start=1):
    #     print(f"{i} : {job}")
    print("============ 직업 선택 ==============")
    print('\n'.join(x for x in joblist))
    print("====================================")
    

    while(True):
        print("직업 이름은 한글로 입력하세요.")
        job2 = input("직업 : ")
        if job2 in joblist:
            return job2
        else:
            print("잘못 된 입력값 입니다.")
    
def create_user():
    #생성할 플레이어 숫자 적고 그만큼 반복.
    name = input("이름 : ")
    job = create_job()
    userset = [name]+table.job_table[job]
    return character.Player(userset) #Player 생성시 추가값있으면 수정.

def create_monster(monsters, num):
    for i in range(0, num):
        index = random.randint(0, len(table.monter_name_list)-1)
        #생성할 플레이어 숫자 적고 그만큼 반복.
        name = table.monter_name_list[index]
        userset = [name]+table.monster_table[name]
        monsters.append(character.Monster(userset)) #Player 생성시 추가값있으면 수정.
    
def create_team(users):
    print("같이 행동할 동료의 숫자를 골라주세요.")
    cmd = input("동료의 수 [0 ~ 3] : ")
    if cmd.isalnum():
        cmd = int(cmd)
    else :
        return create_team(users)
    if 0 <= int(cmd) <= 3:
        for i in range(0, int(cmd)+1):
            os.system("cls||clear")
            if i == 0:
                print("주인공의 이름은 ? : ")
            else :
                print(f"{i}번째 동료의 이름은 ? : ")
            users.append(create_user())
            
    else :
        print("잘못된 값입니다.")
        return create_team()

def view_stage(i):
    for j in range(0,10):
        if j == (10-i):
            print("==================")
            print(f"==   현재위치   ==")
        elif j == 0 :
            print("==================")
            print(f"==     {10-j}층     ==")
        else:
            print("==================")
            print(f"==     {10-j}층      ==")
        print("==================")


def start():
    stage = 1
    users = []
    monsters = []
    inventory = {}
    os.system("cls||clear")
    create_team(users)
    while(True):
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
            iswin = battle.battle(users,monsters, inventory)
            if not iswin:
                return start()
            stage += 1
        elif cmd == '3':
            print("==  인벤토리 ==")
            for key, value in inventory.items():
                print(f"{key} : {value}")
            #사용 부분 추가예정.
            
            os.system('pause')
        elif cmd == '0':
            exit()
    

if __name__ == "__main__":
    start()
