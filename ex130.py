import requests # requests 모듈을 추가한다.
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data'] # btc 함수에 오른쪽 url에 들어가 파이썬에 사용할 수 있는 코드로 바꾼다.

변동폭 = float(btc['max_price']) - float(btc['min_price']) # 변동폭 함수에 실수로 된 최고가에서 최저가를 뺀 값을 넣는다.
시가 = float(btc['opening_price']) # 시가 함수에 실수로 된 btc의 시작값을 넣는다.
최고가 = float(btc['max_price']) # 최고가 함수에 실수로 된 btc의 최고가를 넣는다.

if (시가+변동폭) > 최고가: # 만약 시가 + 변동폭의 값이 최고가 보다 크다면 상승장을 출력하고, 아닐경우 하락장을 출력한다.
    print("상승장")
else:
    print("하락장")