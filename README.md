# 파이썬으로 만든 텍스트 1대1 블랙잭 게임


## 1. 규칙 및 기능
* **카드 분배:** 게임 시작 시 플레이어와 상대는 무작위로 섞인 덱에서 카드를 2장씩 뽑는다.
* **플레이어 턴:** 플레이어는 21점이 넘지 않는 한 계속해서 카드를 뽑을 수 있으며(`hit`), 원할 때 멈출 수 있다(`stand`). 21점을 초과하면 즉시 패배(죽음)한다.
* **상대 턴:** 실제 블랙잭 규칙을 적용하여 봇은 자신의 카드 합계가 17점 미만일 경우 무조건 카드를 추가로 뽑는다.
* **승패 판정:** 양측의 턴이 끝나면 점수를 비교하여 21점에 가까운 사람이 승, 21점에서 먼 사람이 패, 점수가 같을 시 무승부로 판정하고, 게임 재시작 여부를 묻는다.

## 2. 코드 설명

### 1. 점수 계산 함수 

```python
def cal_score(deck):
    score = sum(deck)
    while score > 21 and 11 in deck:
        deck.remove(11)
        deck.append(1)
        score = sum(deck)
    return score
```
* **설명:** 덱패에 있는 카드 숫자의 총합을 계산하는 함수다.
* **코드:** `sum()`으로 합계를 구한 뒤, 만약 점수가 21점을 넘고(`score > 21`) 패에 11점짜리 에이스(A) 카드가 있다면(`11 in deck`), 21점 밑으로 내려갈 때까지 `while`문을 반복하여 11을 1로 바꾼다.

### 2. 게임 시작 및 카드 덱 세팅

```python
game_running = True

while game_running:
    my_deck = []
    opp_deck = []
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(cards)
```
* **설명:** 게임 시작과 카드 덱을 세팅하는 코드다.
* **코드:** 실제 트럼프 카드의 비율에 맞춰 리스트를 생성하고 `random.shuffle()`을 활용해 덱을 무작위로 섞는다.

### 3. 기본 카드 2개씩 받기

```python
        for i in range(2):
            my_deck.append(cards.pop())
            opp_deck.append(cards.pop())
```
* **설명:** 초기 내 패와 상대 패를 설정하는 코드다.
* **코드:** `cards.pop()`을 활용해 카드 리스트에서 한 장을 가져오고 그 한 장을 카드 리스트에서 지운다.

### 4. 추가 카드 받기

```python
        act = input("\n 한,,,장 더? (hit(받기) or stand(멈추기): ")
        if act == 'hit':
            my_deck.append(cards.pop())
            print("\n카드를 1장을 더 받았습니다...")
        elif act == 'stand':
            print("\n 차례를 마칩니다...")
            break
        else:
            print("잘못된 입력입니다. hit 또는 stand를 입력하세요.")

```
* **설명:** 추가 카드를 받는 코드이다.
* **코드:** hit을 입력하면 `if act == 'hit'`에 따라 카드 한 장을 더 가져오고 stand를 입력하면 `elif act == 'stand'`에 따라 차례를 마친다.

### 5. 상대방의 플레이

```python
    while cal_score(opp_deck) < 17:
        opp_deck.append(cards.pop())
```
* **설명:** 기본 카드 뽑기가 끝난 뒤 카드를 뽑는 로직이다.
* **코드:**  `cal_score(opp_deck) < 17`에 의해 점수가 17점보다 작으면 카드를 뽑고 17점 이상이 되면 멈춘다.

### 6. 최종 승패 판정 및 재시작

```python
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
```
* **설명:** 양쪽의 최종 점수를 비교하여 결과를 내고 게임을 다시 할지 묻는 코드다.
* **코드:** 무승부가 나서 `yes`를 치면 `continue` 명령어가 작동한다. 이는 프로그램 밑으로 내려가지 않고 최상단의 `while`문 시작점(카드 덱 세팅)으로 다시 올라가 새게임을 시작하게 만드는 코드다.
<img width="623" height="590" alt="image" src="https://github.com/user-attachments/assets/829536a9-24ab-4a6f-9952-c41625853f36" />

