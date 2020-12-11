ohlc = [["open", "high", "low", "close"], # ohlc 변수에 2차원 리스트 값을 넣는다.
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
profit = 0 # 변수 profit에 0이라는 값을 넣는다.
for row in ohlc[1:]: # 반복문 for에 의해 변수 row는 ohlc의 처음부터 끝까지 반복한다.
    profit += (row[3] - row[0]) # profit 변수에 row의 4번째에서 1번째의 값의 차를 더한 값을 넣는다.
print(profit) # profit 변수를 출력한다.