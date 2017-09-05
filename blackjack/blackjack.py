#coding:utf-8
import random

RANK, SUIT = 0, 1

#勝敗判定 判定結果と計算後の持ちチップを返す
def win_lose(dealer_hand, player_hand, bet, player_money):
    player_point = get_point(player_hand)
    dealer_point = get_point(dealer_hand)
    if player_point <= 21:
        if (player_point > dealer_point) or (dealer_point > 21):
            if player_point == 21:
                return ('<<プレイヤーの勝ち>>', player_money + int(bet*2.5))
            else:
                return ('<<プレイヤーの勝ち>>', player_money + int(bet*2.0))
        elif player_point == dealer_point:
            return ('<<プッシュ>>', player_money + bet)
        else:
            return ('<<プレイヤーの負け>>', player_money)
    else:
        return ('<<プレイヤーの負け>>', player_money)

#プレイヤーの操作
def player_op(deck, player_hand, op):
    doubled, ending = False, False
    if op == '1':
        print('[プレイヤー：スタンド]')
        doubled, ending = False, True

    elif op == '2':
        print('[プレイヤー：ヒット]')
        player_hand.append(deck.pop())
        print_player_hand(player_hand)
        doubled, ending = False, False

    elif op == '3':
        print('[プレイヤー：ダブル]')
        if len(player_hand) == 2:
            print('[プレイヤー：ダブル]')
            player_hand.append(deck.pop())
            print_player_hand(player_hand)
            doubled, ending = True, True
        else:
            print('(ダブルはできません。)')

    if get_point(player_hand) > 21: #バスト判定
        print('[プレイヤーはバストした!]')
        ending = True
    elif get_point(player_hand) == 21:
        print('21です!')
        ending = True

    return doubled, ending

#手札のポイント計算
def get_point(hand):
    result = 0
    ace_flag = False

    for card in hand:
        if card[RANK] == 1:
            ace_flag = True #エースかどうか
        if card[RANK] > 10:
            num = 10
        else:
            num = card[RANK]
        result = result + num
    if ace_flag and result <= 11: #Aが含まれていて、合計が11以下か？
        result += 10 #Aを11と考え、resultに10を加える
    return result

#ディーラーの操作
def dealer_op(deck,player_hand,dealer_hand):
    while get_point(dealer_hand) <= 21:
        if get_point(dealer_hand) >= 17:
            print('[ディーラー：スタンド]')
            break
        else:
            print('[ディーラー：ヒット]')
            dealer_hand.append(deck.pop())
        print_dealer_hand(dealer_hand, False)

#print_player_hand関数
def print_player_hand(player_hand):
    print('プレイヤー(', get_point(player_hand),'):')
    for card in player_hand:
        print('[', card[SUIT], card[RANK], ']')
        #print() #空行

# print_dealer_hand関数
def print_dealer_hand(dealer_hand, uncovered):
    if uncovered:
        print('ディーラー（', get_point(dealer_hand), '):   ')
    else:
        print('ディーラー(??):   ')
    flag = True
    for card in dealer_hand:
        if flag or uncovered:
            print('[', card[SUIT], card[RANK], ']')
            flag = False
        else:
            print('[ * * ]')
    print()

#デッキを作る
def make_deck():
    suits = ['S', 'H', 'D', 'C'] #スートの定義
    ranks = range(1, 14) #ランクの定義
    deck = [(x,y) for x in ranks for y in suits]
    random.shuffle(deck) #シャッフルする
    return deck

def main():
    # 初期化
    turn = 1
    player_money = 100
    deck = make_deck()

    while(player_money > 0):

        print('-'*20)
        print('ターン:',turn)
        print('所持金:',player_money)
        print('-' * 20)

        player_hand = []
        dealer_hand = []

        try:
            bet = int(input('ベット額 > '))
        except:
            print('整数で入力してください')
            continue

        #入力値が所持金を超えていたらやり直し
        if bet > player_money:
            print('所持金が不足しています')
            continue
        #入力値が0より小さかったらやり直し
        elif bet <= 0:
            print('ベットできる額は1以上です。')
            continue

        player_money -= bet
        #デッキの残りが10枚以下ならデッキを再構築&シャッフル
        if len(deck) < 10:
            deck = make_deck()

        for i in range(2): #お互いに2枚ずつ引く
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())

        print('-' * 20)
        #print(player_hand)
        print_player_hand(player_hand)

        #print(dealer_hand)
        print_dealer_hand(dealer_hand, False) #本来はTrue
        print('-' * 20)

        #プレイヤーターン
        while True:
            op = input('スタンド：1, ヒット：2, ダブル：3 > ')
            doubled, ending = player_op(deck, player_hand, op)
            if doubled:
                player_money -= bet
                bet += bet
            if ending:
                break

        #ディーラーターン
        dealer_op(deck, player_hand, dealer_hand)

        print('-' * 20)
        print_player_hand(player_hand)
        print_dealer_hand(dealer_hand,True) #ゲーム終了時のみディーラーの手札開示
        print('-' * 20)

        message, player_money = win_lose(dealer_hand, player_hand, bet, player_money)
        print(message)

        turn += 1
        input('次のターンへ')
    print('game over')

if __name__ == '__main__':
    main()