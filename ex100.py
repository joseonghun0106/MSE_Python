data = ['09/05', '09/06', '09/07', '09/08', '09/09'] # data 변수에 리스트 값을 넣는다.
close_price = [10500, 10300, 10100, 10800, 11000] # close_price 변수에 리스트 값을 넣는다.
close_table = dict(zip(data, close_price)) # close_table 변수를 딕셔너리 안에 data, close_price 순서로 묶어서 넣는다.
print(close_table) # close_table 변수를 출력한다.