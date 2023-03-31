import random
from table import monster_table, level_stat
from abc import *


class Character:

    # 이름 : __init__
    # 인자 : self(인스턴스 자신), name(캐릭터의 이름), stat(캐릭터의 스탯 정보)
    # 역할 : 인스턴스가 생성될 때 인자로 전달된 정보를 바탕으로 Character의 정보를 초기화하는 함수 
    # 반환 : 없음
    # 설명 : 캐릭터의 이름, 체력, 공격력을 저장한다.
    def __init__(self, name, stat):
        self.name = name
        self.max_hp = stat['hp']
        self.hp = self.max_hp
        self.normal_power = stat['normal_power']
    
    # 이름 : normal_attack
    # 인자 : self(인스턴스 자신), target(normal_attack 메소드를 적용할 대상)
    # 역할 : 캐릭터가 normal_attack을 할 때 호출되는 함수
    # 반환 : 없음
    # 설명 : 캐릭터의 일반 공격
    def normal_attack(self, target):
        damage = int(self.normal_power*random.uniform(0.8, 1.2))
        target.hp = max(target.hp - damage, 0)
        print(f'{self.name}의 공격 {target.name}에게 {damage}의 데미지를 입혔습니다')
        if target.hp == 0:
            print(f'{target.name}(이)가 쓰러졌습니다')
    
    def show_status(self):
        print(f"이름 : {self.name} ")
        print(f"체력 : {self.hp} / {self.max_hp}")


class Player(Character, metaclass=ABCMeta):
    inventory = {} #Player 객체가 공유자원으로 관리할 인벤토리 딕셔너리

    def __init__(self, name, stat):
        super().__init__(name, stat)
        self.max_mp = stat['mp']
        self.mp = self.max_mp
        self.magic_power = stat['magic_power']
        self.level = 1
        self.exp = 0
        self.get_level_up = 100
        self.required_exp = self.get_level_up * self.level

        self.item = []

    # 이름 : get_exp
    # 인자 : self(인스턴스 자신), exp(캐릭터의 경험치)
    # 역할 : 캐릭터의 경험치를 증가시킬때 호출되는 함수
    # 반환 : 없음
    # 설명 : 경험치가 필요 경험치보다 크거나 같으면 Player의 레벨업을 실행
    def get_exp(self, exp):
        self.exp += exp
        if self.exp >= self.required_exp:
            self.player_level_up()

    # 이름 : player_level_up
    # 인자 : self(인스턴스 자신)
    # 역할 : 캐릭터의 레벨업을 처리하는 함수
    # 반환 : 없음
    # 설명 : player의 레벨업이 진행 될 때 스탯을 증가시키고 레벨에 따라 레벨업에 필요한 경험치양을 늘림
    def player_level_up(self):
        self.level += 1
        self.max_hp += level_stat['hp']
        self.hp = self.max_hp
        self.max_mp += level_stat['mp']
        self.mp = self.max_mp
        self.normal_power += level_stat['normal_power']
        self.magic_power += level_stat['magic_power']
        self.exp -= self.required_exp
        self.required_exp = self.get_level_up * self.level
        print(f"{self.name}이 레벨 업 하였습니다.현재 레벨: {self.level}")
    
    
    def get_damege(self, scale):
        damage = self.magic_power*scale
        return damage

    def is_mana(self, mp):
        if self.mp < mp:
            print("마나가 부족합니다.")
            return False
        else:
            return True
    
    # 이름 : magic_attack
    # 인자 : target(몬스터)
    # 역할 : 캐릭터가 특수한 공격을 하기위해 작성될 함수
    # 반환 : 없음
    # 설명 : 모든 캐릭터는 1개이상의 특수공격을 가지게 할것이기 떄문에 추상화 매서드로 지정하였다.
    @abstractclassmethod
    def magic_attack(self, target):
        pass

    def show_status(self):
        print("=============================================")
        super().show_status()
        print(f"마나 : {self.mp} / {self.max_mp}")
        print(f"레벨 : {self.level}")
        print(f"경험치 : {self.exp} / {self.required_exp}")
        print("=============================================")


class Warrior(Player):
    def __init__(self, name, stat):
        super().__init__(name, stat)
        self.job = "전사"

    # 이름 : magic_attack
    # 인자 : self(인스턴스 자신), target(몬스터)
    # 역할 : 캐릭터별 특수한 공격을 하기위해 작성될 함수
    # 반환 : 없음
    # 설명 : 직업에 따라 소모 마나량이 다름, 캐릭터의 마나가 충분한지 확인하고 target에게 마법 공격을 가합니다.
    def magic_attack(self, target):
        mp = 10
        mana = self.is_mana(mp)
        if mana:
            self.mp -= mp
            damage = self.magic_power*2
            print(
                f"{self.job}{self.name}의 특수 공격 {target.name}에게 {damage}의 데미지를 입혔습니다.")
            target.hp = max(target.hp - damage, 0)

            if target.hp == 0:
                print(f'{target.name}(이)가 쓰러졌습니다')
        else:
            print("마나가 부족합니다.")


class Wizard(Player):
    def __init__(self, name, stat):
        super().__init__(name, stat)
        self.job = "마법사"

    #Warrior의 주석 참조
    def magic_attack(self, target):
        mp = 20
        mana = self.is_mana(mp)
        if mana:
            self.mp -= mp
            damage = self.magic_power*4
            print(
                f"{self.job}{self.name}의 특수 공격 {target.name}에게 {damage}의 데미지를 입혔습니다.")
            target.hp = max(target.hp - damage, 0)

            if target.hp == 0:
                print(f'{target.name}(이)가 쓰러졌습니다')
        else:
            print("마나가 부족합니다.")


class Archer(Player):
    def __init__(self, name, stat):
        super().__init__(name, stat)
        self.job = "궁수"

    #Warrior의 주석 참조
    def magic_attack(self, target):
        mp = 15
        mana = self.is_mana(mp)
        if mana:
            self.mp -= mp
            damage = self.magic_power*3
            print(
                f"{self.job}{self.name}의 특수 공격 {target.name}에게 {damage}의 데미지를 입혔습니다.")
            target.hp = max(target.hp - damage, 0)

            if target.hp == 0:
                print(f'{target.name}(이)가 쓰러졌습니다')
        else:
            print("마나가 부족합니다.")


class Monster(Character):
    def __init__(self, name, stat):
        super().__init__(name, stat)
    
    #몬스터가 대기할 때
    def wait(self):
        print(f"{self.name}이(가) 잠시 숨을 고릅니다.")

    #몬스터가 흡혈할 때(박쥐, 거미)
    #absorb_need는 흡혈후에 최대체력보다 높아졌을 때의 잉여체력
    def absorb(self, target):
        absorb_damage = int(self.normal_power*0.3)
        target.hp = max(target.hp - absorb_damage, 0)
        absorb_need = (self.hp + absorb_damage) - \
            min(self.hp + absorb_damage, self.max_hp)
        total_absorb = absorb_damage - absorb_need
        self.hp += total_absorb
        print(f"{self.name}이(가) {target.name}에게 흡혈하였습니다!")
        print(f"{target.name}은(는) {absorb_damage}만큼의 데미지를 입었습니다.")
        print(f"{self.name}은(는) {total_absorb}만큼 회복하였다.")
    
    # 몬스터를 처리했을 시 보상으로 얻는 아이템
    def drop_item(self):
        drop_monster = monster_table.get(self.name)
        drop_list = drop_monster['item']
        drop_item = []
        for _drop_item in drop_list:
            print(f"{self.name}에게서 {_drop_item}을 획득하였다!")
            drop_item.append(_drop_item)
        return drop_item

    # 몬스터를 처리했을 시 보상으로 얻는 경험치
    def drop_exp(self, target):
        drop_monster = monster_table.get(self.name)
        exp = drop_monster['exp']
        print(f"{target.name}은(는) {self.name}에게서 경험치를 {exp}만큼 획득했다!")
        return exp

    # 몬스터가 1~5사이의 랜덤으로 추가 데미지를 준다
    def addtional_damage(self, target):
        add_damage = random.randint(1, 5)
        target.hp -= max(target.hp - add_damage, 0)
        print(f'{self.name}의 추가 공격! {target.name}에게 {add_damage}의 추가 데미지를 입혔습니다')
