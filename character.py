import random
from table import monster_table, level_stat
from abc import *


class Character:
    def __init__(self, name, stat):
        self.name = name
        self.max_hp = stat['hp']
        self.hp = self.max_hp
        self.normal_power = stat['normal_power']

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
    inventory = {}

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

    def get_exp(self, exp):
        self.exp += exp
        if self.exp >= self.required_exp:
            self.player_level_up()

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

    def wait(self):
        print(f"{self.name}이(가) 잠시 숨을 고릅니다.")

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

    def drop_item(self):
        drop_monster = monster_table.get(self.name)
        drop_list = drop_monster['item']
        drop_item = []
        for _drop_item in drop_list:
            print(f"{self.name}에게서 {_drop_item}을 획득하였다!")
            drop_item.append(_drop_item)
        return drop_item

    def drop_exp(self, target):
        drop_monster = monster_table.get(self.name)
        exp = drop_monster['exp']
        print(f"{target.name}은(는) {self.name}에게서 경험치를 {exp}만큼 획득했다!")
        return exp

    def addtional_damage(self, target):
        add_damage = random.randint(1, 5)
        target.hp -= max(target.hp - add_damage, 0)
        print(f'{self.name}의 추가 공격! {target.name}에게 {add_damage}의 추가 데미지를 입혔습니다')
