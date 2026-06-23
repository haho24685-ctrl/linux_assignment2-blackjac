import random

def cal_score(deck):
    score = sum(deck)
    while score > 21 and 11 in deck:
        deck.remove(11)
        deck.append(1)
        score = sum(deck)
    return score

game_running = True

while game_running:
    my_deck = []
    opp_deck = []

    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(cards)

    print("죽음의 1대1 블랙잭 게임을 하겠습니다.")

    for i in range(2):
        my_deck.append(cards.pop())
        opp_deck.append(cards.pop())

    while True:
        my_score = cal_score(my_deck)
        print(f"내 덱: {my_deck} (현재 점수: {my_score})")
        print(f"상대 덱: [{opp_deck[0]}] (???)")

        if my_score > 21:
            print("\n 펑!!! 당신은 21점이 넘어 사망하셨습니다...")
            game_running = False
            break

        act = input("\n 한,,,장 더? (hit(받기) or stand(멈추기): ")
        if act == 'hit':
            my_deck.append(cards.pop())
            print("\n카드를 1장을 더 받았습니다...")
        elif act == 'stand':
            print("\n 차례를 마칩니다...")
            break
        else:
            print("잘못된 입력입니다. hit 또는 stand를 입력하세요.")


    if not game_running:
        break

    print("\n 상대의 턴이 시작됩니다...")
    while cal_score(opp_deck) < 17:
        opp_deck.append(cards.pop())
        print("상대가 카드를 1장 더 받았습니다.")
            
    my_last = cal_score(my_deck)
    opp_last = cal_score(opp_deck)

    print(f"나의 최종 카드: {my_deck} (최종 점수: {my_last})")
    print(f"상대의 최종 카드: {opp_deck} (최종 점수: {opp_last})")
        
    if opp_last > 21:
        print("\n 상대의 패가 21점을 넘었습니다. 나의 승리!")
        break 
    elif my_last > opp_last:
        print("\n 내 패가 21점에 더 가깝다. 나의 승리!")
        break
    elif my_last < opp_last:
        print("\n 펑!!! 상대방에게 졌다...")
        break
    else:
        retry = input("\n 비겼다! 한 판 더? (yes or no): ")
        if retry == 'yes':
            print("\n\n새로운 게임을 시작합니다 \n")
            continue 
        else:
            print("\n당신은 도망갔습니다")
            break
