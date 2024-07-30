import random


class Player:
    def __init__(self, name, score=1000):
        self.name = name
        self.score = score
        self.hand = []

    def draw_cards(self, card_pool):
        self.hand = random.sample(card_pool, 2)
        self.hand = sorted(self.hand)

    def show_hand(self):
        return ','.join(map(str, self.hand))

    def clear_hand(self):
        #请空手牌
        self.hand = []


class InfoList:
    def __init__(self, name):
        self.players = [Player(name)]
        self.player = self.players[0]
        self.public_scores = 0
        self.card_pool = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def add_score(self, score):
        self.public_scores += score

    def clear_score(self):
        self.public_scores = 0

    def clear_public(self):
        self.card_pool = []

    def reset_card_pool(self):
        self.card_pool = [i for i in range(2, 15)] * 4
        random.shuffle(self.card_pool)

    def calculate_power(self, player: Player, public_pool):
        # 牌共计4张，牌力计算，炸弹 >顺子 >三条> 两对 >-对 > 散牌
        cards = (player.hand + public_pool)
        num = len(set(cards))
        if num == 1:
            return (1, cards[0])
        elif num == 2:
            if cards[1] == cards[2]:
                return (3, cards[1])
            else:
                return (4, cards[-1] * 100 + cards[0])
        elif num == 3:
            if cards[0] == cards[1]:
                return (5, cards[0] * 100 + cards[-1])
            elif cards[1] == cards[2]:
                return (5, cards[1] * 100 + cards[-1])
            else:
                return (5, cards[-1] * 100 + cards[1])
        elif num == 4:
            if cards[0] == cards[1] - 1 == cards[2] - 2 == cards[3] - 3:
                return (2, cards[-1])
            else:
                return (6, cards[-1] * 100 + cards[-2])

    def winner(self, current_player, public_pool):
        winner = current_player[0]
        max_power = self.calculate_power(current_player[0], public_pool)
        for player in current_player[1:]:
            power = self.calculate_power(player, public_pool)
            if power[0] < max_power[0]:
                max_power = power
                winner = player
            elif power[0] == max_power[0] and power[1] > max_power[1]:
                max_power = power
                winner = player
        return winner


class View:
    def __init__(self, info_list: InfoList):
        self.info_list = info_list
        self.turns = 1
        self.player = self.info_list.players[0]

    def game_start(self):
        print('游戏开始')
        print('添加机器人')
        num = int(input('请输入机器人数量(1~7)：'))
        return num

    def new_turn(self, public_pool):
        print("-----------------------")
        print(f'第{self.turns}回合开始')
        self.turns += 1
        print(f'手牌：{self.player.show_hand()}')
        print(f'公牌：{public_pool}')
        print('请选择：')
        print('1. 叫分')
        print('2. 弃牌')
        print('3. 结束游戏')
        while True:
            choice = int(input('请输入：'))
            if choice in range(1, 3):
                return choice
            else:
                print('请输入正确的选项')

    def show_result(self, winner: Player, public_pool):
        print("-----------------------")
        print(f'第几轮{self.turns}')
        self.turns += 1
        print(f'公牌：{public_pool}')
        print(f'所有手牌：')
        for player in self.info_list.players:
            print(f'{player.name}手牌：{player.show_hand()}')
        winner.score += self.info_list.public_scores
        for player in self.info_list.players:
            print(f'玩家：{player.name}积分： {player.score}')

    def game_end(self):
        print("-----------------------")
        print('游戏结束')
        for player in self.info_list.players:
            print(f'玩家：{player.name}积分： {player.score}')

    def display_message(self, message):
        print(message)


class Controller:

    def __init__(self, view: View, info_list: InfoList):
        self.view = view
        self.info_list = info_list

        self.player = self.info_list.players[0]

    def start_game(self):
        num = self.view.game_start()
        for i in range(num):
            self.info_list.add_player(Player(f'机器人{i+1}'))

    def new_turn(self):
        self.info_list.reset_card_pool()
        current_player = self.info_list.players[:]
        for player in current_player:
            player.draw_cards(self.info_list.card_pool)
            player.score -= 10
            self.info_list.public_scores += 10
        public_pool = random.sample(self.info_list.card_pool, 2)
        num = len(current_player)
        choice = self.view.new_turn(public_pool)
        if choice == 1:
            score = int(input('请输入分数：'))
        else:
            score = 50
            current_player.remove(self.player)

        for player in current_player:
            player.score -= score
            self.info_list.public_scores += score

        winner = self.info_list.winner(current_player, public_pool)
        self.view.show_result(winner, public_pool)

    def end_turn(self):
        if self.info_list.public_scores < 300:
            self.end_game()
        elif self.info_list.public_scores >= 3000:
            self.win_game()
        for player in self.info_list.players:
            if player.score < 300:
                self.info_list.players.remove(player)
            elif player.score > 3000:
                self.end_game()

        self.info_list.clear_score()
        self.info_list.clear_public()
        for player in self.info_list.players:
            player.clear_hand()

    def end_game(self):
        self.view.display_message('遗憾')
        self.view.game_end()

    def win_game(self):
        self.view.display_message('恭喜')
        self.view.game_end()


if __name__ == '__main__':
    name = input('请输入玩家姓名')
    info_list = InfoList(name)
    view = View(info_list)
    controller = Controller(view, info_list)
    controller.start_game()
    while True:
        controller.new_turn()
        controller.end_turn()

