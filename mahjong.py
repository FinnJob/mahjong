import numpy as np
import rlcard
import matplotlib.pyplot as plt

def is_pair(card_index, cur_hand): 
    # 判断card_index的牌在手牌cur_hand中个数是否大于1 
    # card_index未放缩至0-8区间
    if cur_hand[card_index].sum() > 1:
        return True
    else:
        return False

def is_three(card_index, cur_hand):
    # 判断card_index的牌在手牌cur_hand中个数是否大于2 
    # card_index未放缩至0-8区间
    if cur_hand[card_index].sum() > 2:
        return True
    else:
        return False

def is_four(card_index, cur_hand):
    # 判断card_index的牌在手牌cur_hand中个数是否等于4 
    # card_index未放缩至0-8区间
    if cur_hand[card_index].sum() == 4:
        return True
    else:
        return False

def set_num(card_index, start, cur_hand):
    # 判断card_index的牌在手牌cur_hand中能构成的顺子列表 
    # 若顺子为 1，2，3则返回[1,1,1,0,0,0,0,0]
    # card_index放缩至0-8区间 
    # start表示card_index放缩后从哪里出发
    # 条（bamboo）从0出发
    # 万（characters）从9出发 
    # 筒（dots）从18出发
    set_array = np.zeros(9,dtype=int)
    if card_index == 0:
        for i in range(0,9):
            if cur_hand[i+start].sum() > 0:
                set_array[i] += 1
                if i == 8:
                    return set_array
            else:
                return set_array
    elif card_index == 8:
        for i in range(8,-1,-1):
            if cur_hand[i+start].sum() > 0:
                set_array[i] += 1
                if i == 0:
                    return set_array
            else:
                return set_array
    else:
        for i in range(card_index,-1,-1):
            if cur_hand[i+start].sum() > 0:
                set_array[i] += 1
            else:
                break
        for i in range(card_index+1,9):
            if cur_hand[i+start].sum() > 0:
                set_array[i] += 1
                if i == 8:
                    return set_array
            else:
                return set_array

def select_card(la, cur_hand, card_set, start):
    # 第一轮舍牌
    # 根据当前手牌cur_hand和合法动作la选择一张牌打出，若未能选择则返回None
    # card_set表示判断合法动作（la）的牌在手牌cur_hand中能构成的顺子列表
    # la表示当前合法动作，未放缩至0-8区间 
    # start表示card_index放缩后从哪里出发
    # 条（bamboo）从0出发
    # 万（characters）从9出发 
    # 筒（dots）从18出发
    if card_set.sum() == 1 and not is_pair(la,cur_hand):
        return la
    elif card_set.sum() == 3:
        for i in range(9):
            if card_set[i] > 0:
                if is_pair(i+start,cur_hand) and not is_three(i+start,cur_hand):
                    return i+start
 
    elif card_set.sum() == 4:
        for i in range(9):
            if card_set[i] > 0:
                if is_pair(i+start+1,cur_hand) and not is_three(i+start+1,cur_hand):
                    return i+start+1
                elif is_pair(i+start+2,cur_hand) and not is_three(i+start+2,cur_hand):
                    return i+start+2
                elif not is_pair(i+start,cur_hand) and not is_pair(i+start+3,cur_hand):
                    return i+start
                break
    elif card_set.sum() == 6:
        for i in range(9):
            if card_set[i] > 0:
                if is_pair(i+start,cur_hand) and not is_three(i+start,cur_hand):
                    return i+start
                    
    elif card_set.sum() == 7:
        for i in range(9):
            if card_set[i] > 0:
                if not is_pair(i+start,cur_hand):
                    return i+start
                elif not is_pair(i+start+3,cur_hand):
                    return i+start+3
                elif not is_pair(i+start+6,cur_hand):
                    return i+start+6
                break
    return None

def select_card2(la, cur_hand, card_set, start):
    # 第二轮舍牌
    # 根据当前手牌cur_hand和合法动作la选择一张牌打出，若未能选择则返回None
    # card_set表示判断合法动作（la）的牌在手牌cur_hand中能构成的顺子列表
    # la表示当前合法动作，未放缩至0-8区间 
    # start表示card_index放缩后从哪里出发
    # 条（bamboo）从0出发
    # 万（characters）从9出发 
    # 筒（dots）从18出发
    if card_set.sum() == 1:
        if is_four(la, cur_hand):
            return la
    elif card_set.sum() == 2:
        for i in range(9):
            if card_set[i] > 0:
                if not is_pair(i+start,cur_hand):
                    return i+start
 
    elif card_set.sum() == 5:
        for i in range(9):
            if card_set[i] > 0:
                if is_pair(i+start,cur_hand) and not is_three(i+start,cur_hand):
                    return i+start
    return None

def select_card3(la, cur_hand, card_set, start):
    # 第三轮舍牌
    # 根据当前手牌cur_hand和合法动作la选择一张牌打出，若未能选择则返回None
    # card_set表示判断合法动作（la）的牌在手牌cur_hand中能构成的顺子列表
    # la表示当前合法动作，未放缩至0-8区间 
    # start表示card_index放缩后从哪里出发
    # 条（bamboo）从0出发
    # 万（characters）从9出发 
    # 筒（dots）从18出发
    if card_set.sum() == 1:
        if not is_three(la, cur_hand):
            return la
    elif card_set.sum() == 2:
        for i in range(9):
            if card_set[i] > 0:
                if is_pair(i+start,cur_hand) and not is_three(i+start,cur_hand):
                    return i+start
    elif card_set.sum() == 4:
        for i in range(9):
            if card_set[i] > 0:
                if not is_three(i+start,cur_hand):
                    return i+start
                elif not is_three(i+start+3,cur_hand):
                    return i+start+3
                break
    elif card_set.sum() == 5:
        for i in range(9):
            if card_set[i] > 0:
                if not is_three(i+start,cur_hand):
                    return i+start
                elif not is_three(i+start+4,cur_hand):
                    return i+start+4
                break
    elif card_set.sum() == 7:
        for i in range(9):
            if card_set[i] > 0:
                if is_pair(i+start,cur_hand):
                    return i+start
    elif card_set.sum() == 8:
        for i in range(9):
            if card_set[i] > 0:
                if is_pair(i+start,cur_hand) and not is_three(i+start,cur_hand):
                    return i+start
    elif card_set.sum() == 9:
        for i in range(9):
            if card_set[i] > 0:
                if is_pair(i+start,cur_hand):
                    return i+start
    return None

def select_card4(la, cur_hand, card_set, start):
    # 第四轮舍牌
    # 根据当前手牌cur_hand和合法动作la选择一张牌打出，若未能选择则返回None
    # card_set表示判断合法动作（la）的牌在手牌cur_hand中能构成的顺子列表
    # la表示当前合法动作，未放缩至0-8区间 
    # start表示card_index放缩后从哪里出发
    # 条（bamboo）从0出发
    # 万（characters）从9出发 
    # 筒（dots）从18出发
    if card_set.sum() == 1:
        return la
    elif card_set.sum() == 2:
        for i in range(9):
            if card_set[i] > 0:
                if is_four(i+start,cur_hand):
                    return i+start
    elif card_set.sum() == 3:
        for i in range(9):
            if card_set[i] > 0:
                return i+start
    elif card_set.sum() == 4:
        for i in range(9):
            if card_set[i] > 0:
                return i+start
    elif card_set.sum() == 6:
        for i in range(9):
            if card_set[i] > 0:
                return i+start
    elif card_set.sum() == 8:
        for i in range(9):
            if card_set[i] > 0:
                if not is_three(i+start,cur_hand):
                    return i+start
                elif not is_three(i+start+7,cur_hand):
                    return i+start+7
                else:
                    return i+start
    return None

def Rule_Policy(last_action, state):
    # 基于规则的麻将博弈算法，根据麻将规则选择合法动作 
    # last_action表示上一个玩家出牌动作 
    # state表示当前出牌玩家的状态，包含当前手牌和可以执行的合法动作
    legal_actions = list(state['legal_actions'].keys()) #可以执行的合法动作
    cur_hand = state['obs'][0] #当前手牌
    
    if 36 in legal_actions: # gong（若有杠动作则按以下规则采取动作）
        if last_action in [0,1,2,3,4,5,6,7,8]:
            Bamboo_set = set_num(last_action, 0, cur_hand)
            if Bamboo_set.sum() == 3:
                for la in legal_actions:
                    if la in [0,1,2,3,4,5,6,7,8]:
                        if set_num(la, 0, cur_hand).sum() != 3:
                            return 34
                    elif la in [9,10,11,12,13,14,15,16,17]:
                        if set_num(la-9, 9, cur_hand).sum() != 3:
                            return 34
                    elif la in [18,19,20,21,22,23,24,25,26]:
                        if set_num(la-18, 18, cur_hand).sum() != 3:
                            return 34
                return 37
            elif Bamboo_set.sum() == 4:
                if last_action == 0 or 8:
                    return 36
                elif Bamboo_set[last_action-1] == 0 or Bamboo_set[last_action+1] == 0:
                    return 36
                return 34
             
        elif last_action in [9,10,11,12,13,14,15,16,17]:
            Characters_set = set_num(last_action-9, 9, cur_hand)
            if Characters_set.sum() == 3:
                for la in legal_actions:
                    if la in [0,1,2,3,4,5,6,7,8]:
                        if set_num(la, 0, cur_hand).sum() != 3:
                            return 34
                    elif la in [9,10,11,12,13,14,15,16,17]:
                        if set_num(la-9, 9, cur_hand).sum() != 3:
                            return 34
                    elif la in [18,19,20,21,22,23,24,25,26]:
                        if set_num(la-18, 18, cur_hand).sum() != 3:
                            return 34
                return 37
            elif Characters_set.sum() == 4:
                if last_action == 9 or 17:
                    return 36
                elif Characters_set[last_action-9-1] == 0 or Characters_set[last_action-9+1] == 0:
                    return 36
                return 34
            
        elif last_action in [18,19,20,21,22,23,24,25,26]:
            Dots_set = set_num(last_action-18, 18, cur_hand)
            if Dots_set.sum() == 3:
                for la in legal_actions:
                    if la in [0,1,2,3,4,5,6,7,8]:
                        if set_num(la, 0, cur_hand).sum() != 3:
                            return 34
                    elif la in [9,10,11,12,13,14,15,16,17]:
                        if set_num(la-9, 9, cur_hand).sum() != 3:
                            return 34
                    elif la in [18,19,20,21,22,23,24,25,26]:
                        if set_num(la-18, 18, cur_hand).sum() != 3:
                            return 34
                return 37
            elif Dots_set.sum() == 4:
                if last_action == 18 or 26:
                    return 36
                elif Dots_set[last_action-18-1] == 0 or Dots_set[last_action-18+1] == 0:
                    return 36
                return 34
        return 36
            
    if 34 in legal_actions: # pong（若有碰动作则按以下规则采取动作）
        if last_action in [0,1,2,3,4,5,6,7,8]:
            Bamboo_set = set_num(last_action, 0, cur_hand)
            if Bamboo_set.sum() == 3:
                return 37
            elif Bamboo_set.sum() == 4:
                if last_action == 0 or 8:
                    return 34
                elif Bamboo_set[last_action-1] == 0 or Bamboo_set[last_action+1] == 0:
                    return 34
                return 37
            
        elif last_action in [9,10,11,12,13,14,15,16,17]:
            Characters_set = set_num(last_action-9, 9, cur_hand)
            if Characters_set.sum() == 3:
                return 37
            elif Characters_set.sum() == 4:
                if last_action == 9 or 17:
                    return 34
                elif Characters_set[last_action-9-1] == 0 or Characters_set[last_action-9+1] == 0:
                    return 34
                return 37
            
        elif last_action in [18,19,20,21,22,23,24,25,26]:
            Dots_set = set_num(last_action-18, 18, cur_hand)
            if Dots_set.sum() == 3:
                return 37
            elif Dots_set.sum() == 4:
                if last_action == 18 or 26:
                    return 34
                elif Dots_set[last_action-18-1] == 0 or Dots_set[last_action-18+1] == 0:
                    return 34
                return 37
        return 34

    if 35 in legal_actions: # chow（吃牌）
        return 35

    for action in range(27,34): # Dragons、Winds 若无以上动作则先打出Dragons、Winds中的单牌
        if action in legal_actions:
            if not is_pair(action, cur_hand):
                return action
    # print('1 round')
    # 条（Bamboo）、万（Characters）、筒（Dots）第一轮舍牌
    for la in legal_actions: # set
        if la in [0,1,2,3,4,5,6,7,8]:
            Bamboo_set = set_num(la, 0, cur_hand)
            # print('Bamboo_set {}, la {}, cur_hand {}, legal_actions {}'.format(Bamboo_set,la,cur_hand,legal_actions))
            discard = select_card(la, cur_hand, Bamboo_set, 0)
            if discard == None:
                continue
            else:
                return discard 
        elif la in [9,10,11,12,13,14,15,16,17]:
            Characters_set = set_num(la-9, 9, cur_hand)
            # print('Characters_set {}, la {}, cur_hand {}, legal_actions {}'.format(Characters_set,la,cur_hand,legal_actions))
            discard = select_card(la, cur_hand, Characters_set, 9)
            if discard == None:
                continue
            else:
                return discard 
        elif la in [18,19,20,21,22,23,24,25,26]:
            Dots_set = set_num(la-18, 18, cur_hand)
            # print('Dots_set {}, la {}, cur_hand {}, legal_actions {}'.format(Dots_set,la,cur_hand,legal_actions))
            discard = select_card(la, cur_hand, Dots_set, 18)
            if discard == None:
                continue
            else:
                return discard
    
    # 拆掉Dragons、Winds中的对子打出
    for action in range(27,34): # Dragons、Winds
        if action in legal_actions:
            if not is_three(action, cur_hand) or is_four(action, cur_hand):
                return action

    # print('2 round')
    # 条（Bamboo）、万（Characters）、筒（Dots）第二轮舍牌
    for la in legal_actions: # set
        if la in [0,1,2,3,4,5,6,7,8]:
            Bamboo_set = set_num(la, 0, cur_hand)
            discard = select_card2(la ,cur_hand, Bamboo_set, 0)
            if discard == None:
                continue
            else:
                return discard 
        elif la in [9,10,11,12,13,14,15,16,17]:
            Characters_set = set_num(la-9, 9, cur_hand)
            discard = select_card2(la, cur_hand, Characters_set, 9)
            if discard == None:
                continue
            else:
                return discard 
        elif la in [18,19,20,21,22,23,24,25,26]:
            Dots_set = set_num(la-18, 18, cur_hand)
            discard = select_card2(la, cur_hand, Dots_set, 18)
            if discard == None:
                continue
            else:
                return discard
    # print('3 round')
    # 条（Bamboo）、万（Characters）、筒（Dots）第三轮舍牌
    for la in legal_actions: # set
        if la in [0,1,2,3,4,5,6,7,8]:
            Bamboo_set = set_num(la, 0, cur_hand)
            discard = select_card3(la, cur_hand, Bamboo_set, 0)
            if discard == None:
                continue
            else:
                # print("Bamboo_set")
                return discard 
        elif la in [9,10,11,12,13,14,15,16,17]:
            Characters_set = set_num(la-9, 9, cur_hand)
            discard = select_card3(la, cur_hand, Characters_set, 9)
            if discard == None:
                continue
            else:
                # print("Characters_set")
                return discard 
        elif la in [18,19,20,21,22,23,24,25,26]:
            Dots_set = set_num(la-18, 18, cur_hand)
            discard = select_card3(la, cur_hand, Dots_set, 18)
            if discard == None:
                continue
            else:
                # print("Dots_set")
                return discard

    #拆开 Dragons、Winds 的三个一样的牌打出
    for action in range(27,34): # Dragons、Winds
        if action in legal_actions:
            return action
            
    # print('4 round')
    # 条（Bamboo）、万（Characters）、筒（Dots）第四轮舍牌
    for la in legal_actions: # set
        if la in [0,1,2,3,4,5,6,7,8]:
            Bamboo_set = set_num(la, 0, cur_hand)
            discard = select_card4(la, cur_hand, Bamboo_set, 0)
            if discard == None:
                continue
            else:
                return discard 
        elif la in [9,10,11,12,13,14,15,16,17]:
            Characters_set = set_num(la-9, 9, cur_hand)
            discard = select_card4(la, cur_hand, Characters_set, 9)
            if discard == None:
                continue
            else:
                return discard 
        elif la in [18,19,20,21,22,23,24,25,26]:
            Dots_set = set_num(la-18, 18, cur_hand)
            discard = select_card4(la, cur_hand, Dots_set, 18)
            if discard == None:
                continue
            else:
                return discard
            
def game():
    # 四个玩家打一局麻将游戏，返回游戏结束四个玩家的payoff
    env = rlcard.make('mahjong')
    state0, player0 = env.reset()
    while player0 != 0:
        state0, player0 = env.reset()
    action0 = Rule_Policy(None, env.get_state(0))
    
    # print("player0 {}".format(player0))
    # print("action0 {}".format(action0))
    while True:
        state1, player1 = env.step(action0)
        state0 = env.get_state(player0)
        # if action0 == actionid: 
        #     print("last player {}".format(player0))
        #     print(env.get_state(player0)['obs'])
        #     break
        if env.is_over():break
        if player1 == 0:
            action1 = Rule_Policy(action0,env.get_state(0)) #基于规则算法
            # action1 = np.random.choice(list(state1['legal_actions'].keys())) #随机算法
        elif player1 == 1:
            action1 = Rule_Policy(action0,env.get_state(1))
            # action1 = np.random.choice(list(state1['legal_actions'].keys()))
        elif player1 == 2:
            action1 = Rule_Policy(action0,env.get_state(2))
            # action1 = np.random.choice(list(state1['legal_actions'].keys()))
        elif player1 == 3:
            # action1 = Rule_Policy(action0,env.get_state(3))
            action1 = np.random.choice(list(state1['legal_actions'].keys()))
        # card_list = []
        # for card in env.get_state(player1)['raw_obs']['current_hand']:
        #     card_list.append(card.get_str())
        # card_list.sort()
        # print(card_list)
        # print("legal_actions {}".format(list(env.get_state(player1)['legal_actions'].keys())))
        # print("player1 {}".format(player1))
        # print("action1 {}".format(action1))

        state2, player2 = env.step(action1)
        state1 = env.get_state(player1)
        # if action1 == actionid: 
        #     print("last player {}".format(player1))
        #     print(env.get_state(player1)['obs'])
        #     break
        if env.is_over():break
        if player2 == 0:
            action2 = Rule_Policy(action1,env.get_state(0))
            # action2 = np.random.choice(list(state2['legal_actions'].keys()))
        elif player2 == 1:
            action2 = Rule_Policy(action1,env.get_state(1))
            # action2 = np.random.choice(list(state2['legal_actions'].keys()))
        elif player2 == 2:
            action2 = Rule_Policy(action1,env.get_state(2))
            # action2 = np.random.choice(list(state2['legal_actions'].keys()))
        elif player2 == 3:
            # action2 = Rule_Policy(action1,env.get_state(3))
            action2 = np.random.choice(list(state2['legal_actions'].keys()))
        # card_list = []
        # for card in env.get_state(player2)['raw_obs']['current_hand']:
        #     card_list.append(card.get_str())
        # card_list.sort()
        # print(card_list)
        # print("legal_actions {}".format(list(env.get_state(player2)['legal_actions'].keys())))
        # print("player2 {}".format(player2))
        # print("action2 {}".format(action2))

        state3, player3 = env.step(action2)
        state2 = env.get_state(player2)
        # if action2 == actionid: 
        #     print("last player {}".format(player2))
        #     print(env.get_state(player2)['obs'])
        #     break
        if env.is_over():break
        if player3 == 0:
            action3 = Rule_Policy(action2,env.get_state(0))
            # action3 = np.random.choice(list(state3['legal_actions'].keys()))
        elif player3 == 1:
            action3 = Rule_Policy(action2,env.get_state(1))
            # action3 = np.random.choice(list(state3['legal_actions'].keys()))
        elif player3 == 2:
            action3 = Rule_Policy(action2,env.get_state(2))
            # action3 = np.random.choice(list(state3['legal_actions'].keys()))
        elif player3 == 3:
            # action3 = Rule_Policy(action2,env.get_state(3))
            action3 = np.random.choice(list(state3['legal_actions'].keys()))
        # card_list = []
        # for card in env.get_state(player3)['raw_obs']['current_hand']:
        #     card_list.append(card.get_str())
        # card_list.sort()
        # print(card_list)
        # print("legal_actions {}".format(list(env.get_state(player3)['legal_actions'].keys())))
        # print("player3 {}".format(player3))
        # print("action3 {}".format(action3))

        state0, player0 = env.step(action3)
        state3 = env.get_state(player3)
        # if action3 == actionid: 
        #     print("last player {}".format(player3))
        #     print(env.get_state(player3)['obs'])
        #     break
        if env.is_over():break
        if player0 == 0:
            action0 = Rule_Policy(action3,env.get_state(0))
            # action0 = np.random.choice(list(state0['legal_actions'].keys()))
        elif player0 == 1:
            action0 = Rule_Policy(action3,env.get_state(1))
            # action0 = np.random.choice(list(state0['legal_actions'].keys()))
        elif player0 == 2:
            action0 = Rule_Policy(action3,env.get_state(2))
            # action0 = np.random.choice(list(state0['legal_actions'].keys()))
        elif player0 == 3:
            # action0 = Rule_Policy(action3,env.get_state(3))
            action0 = np.random.choice(list(state0['legal_actions'].keys()))
        # card_list = []
        # for card in env.get_state(player0)['raw_obs']['current_hand']:
        #     card_list.append(card.get_str())
        # card_list.sort()
        # print(card_list)
        # print("legal_actions {}".format(list(env.get_state(player0)['legal_actions'].keys())))
        # print("player0 {}".format(player0))
        # print("action0 {}".format(action0))
    return env.get_payoffs()

if __name__ == '__main__':
    player0_win = 0 #玩家player0 胜利次数
    player1_win = 0
    player2_win = 0
    player3_win = 0
    round = 1000 #麻将局数
    money = 3000 #每个玩家开局筹码
    average_time = 10 #打几场取一次平均，一场中有round局麻将游戏
    total_player0_money = np.zeros(round+1,dtype=int) #表示average_time场麻将玩家player0的筹码总数
    total_player1_money = np.zeros(round+1,dtype=int)
    total_player2_money = np.zeros(round+1,dtype=int)
    total_player3_money = np.zeros(round+1,dtype=int)
    for _ in range(average_time):
        # 打一场麻将，一场中有round局麻将游戏
        player0_money = [money]
        player1_money = [money]
        player2_money = [money]
        player3_money = [money]
        for _ in range(round):
            # 记录每局麻将游戏四个玩家的筹码以及胜利次数
            score = game()
            if score[0] == 1: player0_win += 1
            if score[1] == 1: player1_win += 1
            if score[2] == 1: player2_win += 1
            if score[3] == 1: player3_win += 1 
            player0_money.append(player0_money[-1]+score[0])
            player1_money.append(player1_money[-1]+score[1])
            player2_money.append(player2_money[-1]+score[2])
            player3_money.append(player3_money[-1]+score[3])
        total_player0_money = np.sum([total_player0_money, player0_money], axis=0).tolist()
        total_player1_money = np.sum([total_player1_money, player1_money], axis=0).tolist()
        total_player2_money = np.sum([total_player2_money, player2_money], axis=0).tolist()
        total_player3_money = np.sum([total_player3_money, player3_money], axis=0).tolist()
    # 打印每个玩家的胜利次数和胜率
    print('player0 win {}, win rate {}'.format(player0_win,np.array(player0_win/(round*average_time),dtype='float64')))
    print('player1 win {}, win rate {}'.format(player1_win,np.array(player1_win/(round*average_time),dtype='float64')))
    print('player2 win {}, win rate {}'.format(player2_win,np.array(player2_win/(round*average_time),dtype='float64')))
    print('player3 win {}, win rate {}'.format(player3_win,np.array(player3_win/(round*average_time),dtype='float64')))

    # 画出每个玩家平均每场筹码数量变化
    x = list(range(round+1))
    plt.figure()
    plt.plot(x,list(np.array(np.divide(total_player0_money, average_time),dtype=int)),'red', label='player0')
    plt.plot(x,list(np.array(np.divide(total_player1_money, average_time),dtype=int)),'blue', label='player1')
    plt.plot(x,list(np.array(np.divide(total_player2_money, average_time),dtype=int)),'black', label='player2')
    plt.plot(x,list(np.array(np.divide(total_player3_money, average_time),dtype=int)),'darkorange', label='player3')
    plt.xlabel('Number of Round')
    plt.ylabel('Average_money')
    plt.title('player3 is Random_Policy,others are Rule_Policy')
    plt.legend()
    plt.show()