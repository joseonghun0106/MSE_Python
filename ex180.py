low_prices  = [100, 200, 400, 800, 1000] # 변수 low_prices에 100, 200, 400, 800, 1000을 넣는다.
high_prices = [150, 300, 430, 880, 1000] # 변수 high_prices에 150, 300, 430, 880, 1000을 넣는다.

volatility = [] # 변수 volatility에 []를 넣는다.
for i in range(len(low_prices)): # 반복문 for을 사용하여 변수 i를 low_prices의 양만큼 반복한다.
    volatility.append(high_prices[i] - low_prices[i]) # 리스트에 값을 추가하기 위해 변수 volatility에 append() 함수를 사용하여 같은 순서의 high_prices에서 low_prices를 뺀 값을 volatility에 넣는다.
print(volatility) # volatility 변수를 출력한다.