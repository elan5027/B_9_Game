# 공통될 케릭터 기본 디자인
# 몬스터와 유저는 기본 디자인을 상속받아서 사용.
# 모든 몬스터랑 유저가 공통으로 가질속성을 같이 정의.

#속성값

# 스킬 포함
# 직업 시스템
# 레벨 시스템(경험치)
# 아이템 (리스트)


#함수는 오버라이딩을 하면되는데.
#이름을 같되 기능은 다른걸구현하려면 이렇게 하면됨니다. 
#부모에 함수 작성하고 자식에는 이름을 불러와서 다른기능넣으면 자식꺼로 동작.

# 함수
# HP상태정보 
# 기본공격 

#랜덤하게 해도되고 뭐 15개 해서 분배하게 하셔도되고
#유저디자인 하시는 분 마음대로 일단해보죠
import random
from table import monster_table
#캐릭터 베이스
class Character:
    def __init__(self, stat) :
        self.name = stat[0]
        self.max_hp = stat[1]
        self.hp = self.max_hp
        self.normal_power = 2*stat[3]
       
           
        
    def normal_attack(self, target):
        # 랜덤 값은 생각해봅시다!
        ## 실수값은 randint가 아니라 uniform 으로 해야됨니다.
        #damage = int(self.normal_power*random.randint(0.8, 1.2))
        damage = int(self.normal_power*random.uniform(0.8, 1.2))
        target.hp = max(target.hp - damage, 0)
        print(f'{self.name}의 공격 {target.name}에게 {damage}의 데미지를 입혔습니다')
        if target.hp == 0:
            print(f'{target.name}(이)가 쓰러졌습니다')
    
    def show_status(self):
        print(f"이름 : {self.name} ")
        print(f"체력 : {self.hp} / {self.max_hp}")
        
class Player(Character):
    def __init__(self, stat):
        super().__init__(stat)
        self.max_mp = 5*stat[2]
        self.mp = self.max_mp
        self.magic_power = 4*stat[4]
        self.level = 1
        self.exp =0
        self.get_level_up = 100
        self.required_exp = self.get_level_up * self.level
        
        ##추가 작성
        ## 아이템을 가질 클레스
        self.item = []
        

    def get_exp(self, exp):
        self.exp += exp
        if self.exp >= self.required_exp:
            self.player_level_up()

    
    #레벨 업
    def player_level_up(self):
        self.level += 1
        self.max_hp += 10
        self.hp = self.max_hp
        self.max_mp += 5
        self.mp = self.max_mp
        self.normal_power += 2
        self.magic_power += 4
        self.exp -= self.required_exp
        self.required_exp = self.get_level_up * self.level
        print(f"{self.name}이 레벨 업 하였습니다.현재 레벨: {self.level}")
    
    def get_damege(self, scale):
        damage = self.magic_power*scale
        return damage


    # 변경을해서 마나가 유효한지 판단하는걸로 바꾸고
    def is_mana(self, mp):
        if self.mp < mp :
            print("마나가 부족합니다.")
            return False
        else :
            return True

    def magic_attack(self, target):
        # 랜덤 값은 생각해봅시다!
            mana = self.is_mana()
            if mana:
                self.mp -= 10
                print(f'{self.name}의 공격 {target.name}에게 {damage}의 데미지를 입혔습니다')
                
                damage = int(self.magic_power*random.uniform(0.8, 1.2))
                target.hp = max(target.hp - damage, 0)
                
                if target.hp == 0:
                    print(f'{target.name}(이)가 쓰러졌습니다')

    #상태창
    def show_status(self):
        print("=============================================")
        super().show_status()
        print(f"마나 : {self.mp} / {self.max_mp}")
        print(f"레벨 : {self.level}")
        print(f"경험치 : {self.exp} / {self.required_exp}")
        print("=============================================")
        
## 1. 직업별로 특수공격
class Warrior(Player):
    def __init__(self, stat):
        super().__init__(stat)
        self.job = "전사"
        self.magic_power = 2*stat[4] #전사는 마법 공격력이 낮게

    def magic_attack(self, target):
        mp = 10
        mana = self.is_mana(mp)
        if mana:
            self.mp -= mp
            damage = self.magic_power*2
            print(f"{self.job}{self.name}의 특수 공격 {target.name}에게 {damage}의 데미지를 입혔습니다.")
            target.hp = max(target.hp - damage, 0)
                    
            if target.hp == 0:
                print(f'{target.name}(이)가 쓰러졌습니다')
        else :
            print("마나가 부족합니다.")

class Wizard(Player):
    def __init__(self, stat):
        super().__init__(stat)
        self.job = "마법사"
        self.magic_power = 6*stat[4] #마법사는 마법 공격력이 높게

    def magic_attack(self, target):
        mp = 20
        mana = self.is_mana(mp)
        if mana:
            self.mp -= mp
            damage = self.magic_power*4
            print(f"{self.job}{self.name}의 특수 공격 {target.name}에게 {damage}의 데미지를 입혔습니다.")
            target.hp = max(target.hp - damage, 0)
                    
            if target.hp == 0:
                print(f'{target.name}(이)가 쓰러졌습니다')
        else :
            print("마나가 부족합니다.")

class Archer(Player):
    def __init__(self, stat):
        super().__init__(stat)
        self.job = "궁수"
        self.magic_power = 4*stat[4] #궁수는 마법 공격력이 중간

    #애만 사용됨.
    def magic_attack(self, target):
        mp = 15
        mana = self.is_mana(mp)
        if mana:
            self.mp -= mp
            damage = self.magic_power*3
            print(f"{self.job}{self.name}의 특수 공격 {target.name}에게 {damage}의 데미지를 입혔습니다.")
            target.hp = max(target.hp - damage, 0)
                    
            if target.hp == 0:
                print(f'{target.name}(이)가 쓰러졌습니다')
        else :
            print("마나가 부족합니다.")

## 2. 아이템 착용 고려.



# 보상 및 아이템 --> 경험치 뭐 주는지, 드랍테이블에서 가져오기..?
class Monster(Character):
    def __init__(self, stat): 
        super().__init__(stat)
    
    #확률적으로 몬스터가 아무런 행동을 하지 않음
    def wait(self):
        print(f"{self.name}이(가) 잠시 숨을 고릅니다.")
    #박쥐,거미가 일반공격 대신 확률적으로 흡혈 사용
    # 0~10 10% 휴식(공격안함) 20%로 흡혈공격 70% 일반공격
    # =======================
    def absorb(self,target):
        absorb_damage = int(self.normal_power*0.3)
        target.hp = max(target.hp - absorb_damage, 0)
        absorb_need = (self.hp + absorb_damage) - min(self.hp + absorb_damage , self.max_hp)
        total_absorb = absorb_damage - absorb_need
        self.hp += total_absorb
        print(f"{self.name}이(가) {target.name}에게 흡혈하였습니다!")
        print(f"{target.name}은(는) {absorb_damage}만큼의 데미지를 입었습니다.")
        print(f"{self.name}은(는) {total_absorb}만큼 회복하였다.")

    def drop_item(self):
        drop_list = monster_table[self.name][3]
        #drop_item_list = list(map(str, drop_monster[3]))
        drop_item = []
        for _drop_item in drop_list:
            print(f"{self.name}에게서 {_drop_item}을 획득하였다!")
            drop_item.append(_drop_item)          
        return drop_item

    def drop_exp(self, target):
        drop_monster = monster_table.get(self.name)
        exp = drop_monster[2]
        print(f"{target.name}은(는) {self.name}에게서 경험치를 {exp}만큼 획득했다!")
        return exp

    # 몬스터의 추가 데미지
    def addtional_damage(self, target):
        add_damage = random.randint(1, 5)
        target.hp -= max(target.hp - add_damage, 0)
        print(f'{self.name}의 추가 공격! {target.name}에게 {add_damage}의 추가 데미지를 입혔습니다')


