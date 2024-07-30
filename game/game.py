import json
import random
import sys
import pickle


class Character:
    def __init__(self, name, health, mana, max_health, max_mana, attack, defense, level=1, skills=[]):
        self.name = name
        self.health = health
        self.mana = mana
        self.max_health = max_health
        self.max_mana = max_mana
        self.attack = attack
        self.defense = defense
        self.level = level
        self.skills = skills

    # 加血
    def add_health(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    # 加蓝
    def add_mana(self, amount):
        self.mana += amount
        if self.mana > self.max_mana:
            self.mana = self.max_mana

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0

    def add_skill(self, skill):
        self.skills.append(skill)

    def recover(self):
        self.health = self.max_health
        self.mana = self.max_mana
        return f"{self.name} 恢复了"

    def check_state(self):
        return f'{self.name} 的状态是：\n 生命值：{self.health}/{self.max_health}\n 魔法值：{self.mana}/{self.max_mana}'


class Hero(Character):

    def __init__(self, name, health, mana, max_health, max_mana, attack, defense, level=1, skills=[], exp=0, gold=100):
        super().__init__(name, health, mana, max_health, max_mana, attack, defense, level, skills)
        self.exp = exp
        self.gold = gold
        self.items = []

    def check_items(self):
        return f'{self.name} 的物品是：\n {self.items}\n金币：{self.gold}'


class Monster(Character):
    def __init__(self, name, health, mana, max_health, max_mana, attack, defense, level='easy', drop_item=None,
                 drop_exp=0, drop_golds=0):
        super().__init__(name, health, mana, max_health, max_mana, attack, defense, level)
        self.drop_item = drop_item
        self.drop_exp = drop_exp
        self.drop_golds = drop_golds

    def be_defeated(self):
        if self.health == 0:
            return True
        else:
            return False


class Skill:

    def __init__(self, name, info, cost, amount=0, attack_percent=1.0):
        self.name = name
        self.info = info
        self.cost = cost
        self.amount = amount
        self.attack_percent = attack_percent

    def effect(self, player, target):
        damage = self.amount + player.attack * self.attack_percent - target.defense
        if damage > 0:
            damage = 1
        target.take_damage(damage)
        return f'{target.name} 受到了 {damage} 点伤害'


class Item:
    def __init__(self, name, price, info, type, amount=0, percent=0.0):
        self.name = name
        self.price = price
        self.info = info
        self.type = type
        self.amount = amount
        self.percent = percent

    def use(self, player):
        if self.info == 'health':
            total_amount = self.amount + player.max_health * self.percent
            player.add_health(total_amount)
            return f'{player.name} 使用了 {self.name} 恢复了 {total_amount} 点生命值 现在生命值为 {player.health}/{player.max_health}'
        else:
            total_amount = self.amount + player.max_mana * self.percent
            player.add_mana(total_amount)
            return f'{player.name} 使用了 {self.name} 恢复了 {total_amount} 点魔法值 现在魔法值为 {player.mana}/{player.max_mana}'


class DataBase:
    def __init__(self):
        self.heros = []
        self.monsters = []
        self.skills = []
        self.items = []

    def add_heros(self, hero):
        self.heros.append(hero)

    def add_monsters(self, monster):
        self.monsters.append(monster)

    def add_skills(self, skill):
        self.skills.append(skill)

    def add_items(self, item):
        self.items.append(item)


class View:

    def __init__(self, database: DataBase):
        self.db = database

    def game_start(self):
        print('--------------------------------')
        print('欢迎来到冒险世界')
        name = input('请输入你的名字：')
        return name

    def chose(self, num):
        while True:
            choice = int(input(f'请选择你的职业：'))
            if choice in range(1, num + 1):
                return choice
            else:
                return '请输入正确的职业'

    def hero_choice(self):
        print('--------------------------------')
        print('请选择你的职业：')
        print('1.战士')
        print('2.弓箭手')
        print('3.法师')
        print('4.野蛮人')
        res = self.chose(4)
        self.player = self.db.heros[res - 1]
        return res

    def town_choice(self):
        print('--------------------------------')
        print('欢迎来到天空之城')
        print('1,进入副本')
        print('2,购买物品')
        print('3,学习技能')
        print('4,保存进度')
        print('5,退出游戏')
        res = self.chose(5)
        return res

    def action_choice(self):
        print('-------------------------------')
        print('你已经进入副本')
        print("请选择行动：")
        print('1. 虚空索敌')
        print('2. 返回城镇')
        return self.chose(2)

    def battle_choice(self):
        print('-------------------------------')
        print(self.player.check_state())
        print('请选择：')
        print('1. 普通攻击')
        print('2. 使用技能')
        print('3. 使用物品')
        print('4. 溜之大吉')
        return self.chose(4)

    def chose_skill(self):
        print('-------------------------------')
        print('请选择技能：')
        for skill in self.player.skills:
            print(f'{skill.name}: {skill.info}')
        skill_num = self.chose(len(self.player.skills))
        skill = self.player.skills[skill_num - 1]
        print('-------------------------------')

        if self.player.mana < skill.cost:
            print('你的魔法值不足')
            return self.chose_skill()
        else:
            print(f'你使用了技能：{skill.name}')
            print(f'法力值消耗：{skill.cost}')
            return skill

    def chose_item(self):
        print('-------------------------------')
        print('请选择物品：')
        for item in self.player.items:
            print(f'{item.name}: {item.info}')
        item_num = self.chose(len(self.player.items))
        item = self.player.items[item_num - 1]
        return item

    def display_massage(self, message):
        print('-------------------------------')
        print(message)


class Controller:
    def __init__(self, view: View, database: DataBase):
        self.view = view
        self.db = database

    def game_start(self):
        name = self.view.game_start()
        res = self.view.hero_choice()
        self.player = self.db.heros[res - 1]
        self.player.name = name
        self.view.display_massage(f'{self.player.name} 加入了冒险世界')

    def town_choice(self):

        res = self.view.town_choice()
        if res == 1:
            self.view.display_massage('你进入了副本')
            self.action_choice()
        elif res == 2 or res == 3:
            self.view.display_massage('未开放')
        elif res == 4:
            self.view.display_massage('你保存了进度')
            self.save_game()
            self.town_choice()
        elif res == 5:
            self.view.display_massage('你退出了游戏')
            sys.exit()

    def action_choice(self):
        monsters = [monster for monster in self.db.monsters if monster.level == 'easy']
        while True:
            res = self.view.action_choice()
            if res == 1:
                self.view.display_massage('你遇到敌人了')
                cuurent_monster = random.choice(monsters)
                self.battle(cuurent_monster)
            elif res == 2:
                self.view.display_massage('你选择了返回城镇')
                break
        self.town_choice()

    def battle(self, current_monster):
        while current_monster.be_defeated() == False:
            result = self.view.battle_choice()
            if result == 4:
                self.view.display_massage('你溜之大吉')
                break
            elif result == 1:
                damage = self.player.attack - current_monster.defense
                current_monster.take_deamge(damage)
                self.view.display_massage(f'你对 {current_monster.name} 造成了 {damage} 点伤害')
                if current_monster.be_defeated():
                    self.view.display_massage(f'{current_monster.name} 被你打败了')
                    break
            elif result == 2:
                skill = self.view.chose_skill()
                self.player.mana -= skill.cost
                res = skill.effect(self.player, current_monster)
                self.view.display_massage(res)
                if current_monster.be_defeated():
                    self.view.display_massage(f'{current_monster.name} 被你打败了')
                    break
            elif result == 3:
                self.use_item()

            damage = current_monster.attack - self.player.defense
            self.player.take_damage(damage)
            self.view.display_massage(f'{current_monster.name} 对你造成了 {damage} 点伤害')
            if self.player.health == 0:
                self.game_over(current_monster)
        self.win_battle(current_monster)

    def use_item(self):
        item = self.view.chose_item()
        res = item.use(self.player)
        self.view.display_massage(res)
        self.player.items.remove(item)

    def win_battle(self, current_monster: Monster):
        self.view.display_massage(f'{current_monster.name} 被你打败了')
        self.player.exp += current_monster.drop_exp
        self.view.display_massage(f'你获得了 {current_monster.drop_exp} 点经验')
        self.player.gold += current_monster.drop_golds
        self.view.display_massage(f'你获得了 {current_monster.drop_golds} 点金币')
        self.player.items.append(current_monster.drop_item)
        self.view.display_massage(f'你获得了 {current_monster.drop_item.name}')

    def game_over(self, current_monster: Monster):
        self.view.display_massage(f'{self.player.name} 被 {current_monster.name} 打败了')
        self.view.display_massage('游戏结束')
        sys.exit()

    def save_game(self):
        with open('save_data.pkl', 'wb') as f:
            self.view.display_massage('正在保存进度')
            pickle.dump(self.db, f)

    def load_game(self, file='save_data.pkl'):
        with open(file, 'rb') as f:
            self.db = pickle.load(f)
            self.view.display_massage('正在加载进度')


if __name__ == '__main__':
    sword_attack = Skill("剑术攻击", "使用剑进行攻击，造成大量伤害", 10, amount=20, attack_percent=1.5)
    bow_shot = Skill("箭术射击", "使用弓箭进行远程攻击，造成中等伤害", 8, amount=15, attack_percent=1.3)
    fireball = Skill("火球术", "发射一个火球，造成魔法伤害", 15, amount=25, attack_percent=1.2)
    berserk = Skill("狂暴", "进入狂暴状态，提高攻击力", 12, amount=30, attack_percent=1.0)
    skills = [sword_attack, bow_shot, fireball, berserk]
    warrior = Hero(name="战士", health=100, mana=50, max_health=100,
                    max_mana=50, attack=20, defense=15,
                    skills=[sword_attack], exp=0, level=1, gold=0)
    archer = Hero(name="弓箭手", health=80, mana=60, max_health=80, max_mana=60,
                   attack=18, defense=12,
                   skills=[bow_shot], exp=0, level=1, gold=0)
    mage = Hero(name="法师", health=60, mana=100, max_health=60, max_mana=100,
                 attack=15, defense=10,
                 skills=[fireball], exp=0, level=1, gold=0)
    barbarian = Hero(name="野蛮人", health=120, mana=40, max_health=120,
                      max_mana=40, attack=25, defense=20,
                      skills=[berserk], exp=0, level=1, gold=0)
    heros = [warrior, archer, mage, barbarian]
    items = {
        "小治疗药水": Item("小治疗药水", 10, "恢复少量生命值", type='health', amount=20),
        "大治疗药水": Item("大治疗药水", 50, "恢复大量生命值", type='health', amount=50),
        "超级治疗药水": Item("超级治疗药水", 100, "恢复大量生命值，并根据百分比增加生命值", type='health', amount=30,percent=0.2),
        "法力药水": Item("法力药水", 30, "恢复少量法力值", type='mana', amount=40),
        "强力法力药水": Item("强力法力药水", 70, "恢复大量法力值", type='mana', amount=80)
    }
    db = DataBase()
    for skill in skills:
        db.add_skills(skill)
    for hero in heros:
        db.add_heros(hero)
    for item in items.values():
        db.add_items(item)
    with open('monsters.json', 'r', encoding='GBK') as file:
        data = json.load(file)
    for monster in data.values():
        db.add_monsters(Monster(**monster))
    view = View(db)
    controller = Controller(view, db)
    controller.game_start()
    controller.town_choice()
