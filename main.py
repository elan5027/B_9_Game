import table
import character
import battle
import random
import os
from inventory import show_inventory


# 이름  :   select_job
# 인자  :   없음
# 역할  :   직업의 정보를 보여주고 값을 입력받기 위한 함수
# 반환  :   선택한 직업의 이름
# 설명  :   존재하는 직업의 정보를 보여주고 값을 입력받는다.


def select_job():
    joblist = list(map(str, table.job_table.keys()))

    print("============ 직업 선택 ==============")
    print('\n'.join(x for x in joblist))
    print("====================================")

    while (True):
        print("직업 이름은 한글로 입력하세요.")
        jobname = input("직업 : ")
        if jobname in joblist:
            return jobname
        else:
            print("잘못 된 입력값 입니다.")
            continue

# 이름  :   create_user
# 인자  :   없음
# 역할  :   캐릭터를 생성하기 위한 함수
# 반환  :
#   - 구성된 정보로 캐릭터 클레스의 인스턴스를 반환한다.
#   - 만약, 유저의 이름값이 비어있다면 함수를 재귀적 호출한다.
# 설명  :
#   - select_job 함수에서 직업이름을 받아온다.
#   - 받아온 이름으로 job_table에서 해당 직업의 설정값을 받아온다.


def create_user():
    name = input("이름 : ")
    if not name:
        print("비어있는 값을 입력하였습니다.")
        os.system("pause")
        return create_user()
    job = select_job()
    userset = table.job_table[job]
    if job == "전사":
        return character.Warrior(name, userset)
    elif job == "궁수":
        return character.Archer(name, userset)
    elif job == "마법사":
        return character.Wizard(name, userset)


# 이름  :  create_monster
# 인자  :  monsters (몬스터 리스트), num (몬스터 생성 수)
# 역할  :  몬스터를 인자값으로 받아온 수만큼 생성하는 함수
# 반환  :  없음
# 설명  :
#   - 랜덤한 값으로 몬스터의 이름을 가져온다.
#   - 가져온 이름을 통해 해당 몬스터의 설정값을 가져온다.
#   - 인자값 monsters 리스트에 몬스터의 객체를 추가한다.


def create_monster(monsters, num):
    for i in range(0, num):
        index = random.randint(0, len(table.monter_name_list)-1)
        name = table.monter_name_list[index]
        userset = table.monster_table[name]
        monsters.append(character.Monster(name, userset))

# 이름  :   create_team:
# 인자  :   users (유저 리스트)
# 역할  :   사용자로부터 입력받은 수 만큼 유저를 생성하는 함수
# 반환  :   값이 유효하지 않을경우 재귀적 호출
# 설명  :
#   - 유저에게 숫자값을 입력받고 해당 수 만큼 유저의 목록 리스트에 추가한다.
#   - 입력받은 값이 0~3 사이의 정수인지 검사하여 올바른 값만 받도록 한다.


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
        return create_team(users)

# 이름  :   view_stage
# 인자  :   i (정수 값)
# 역할  :   유저가 현재 위치하는 스테이지의 정보 출력
# 반환  :   없음
# 설명  :
#   - 인자값으로 받아온 스테이지 위치정보를 기반으로 총 10층의 스테이지를 콘솔창에 그려준다.


def view_stage(i):
    for j in range(0, 10):
        if j == (10-i):
            print("==================")
            print(f"==   현재위치   ==")
        else:
            print("==================")
            print(f"==     {10-j}층      ==")
        print("==================")

# 이름  :   start
# 인자  :   없음
# 역할  :   게임이 시작되면 사실상 가장먼저 실행되는 메인 함수.
# 반환  :   없음
# 설명  :
#   - 최초 실행시 각종 설정값을 세팅하고 유저가 할수 있는일을 그려준다.
#   - 선택된 행동하는 함수를 호출해준다.
#   - 유저가 전투에서 패배 또는 사용자가 종료할때 까지 무한히 반복한다.


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
