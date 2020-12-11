class Stock: # Stock이라는 class를 만든다.
    def __init__(self, name, code, per, pbr, dividend): # def로 _init_(self, name, code, per, pbr, dividend)라는 함수가 아래의 명령을 가르킨다.
        self.name = name # 객체변수 name에 name을 넣는다.
        self.code = code # 객체변수 code에 code를 넣는다.
        self.per = per # 객체변수 per에 per을 넣는다.
        self.pbr = pbr # 객체변수 pbr에 pbr을 넣는다.
        self.dividend = dividend # 객체변수 dividend에 dividend를 넣는다.

    def set_name(self, name): # def로 set_name(self, name)라는 함수가 아래의 명령을 가르킨다.
        self.name = name # 객체변수 name에 name 값을 넣는다.

    def set_code(self, code): # def로 set_code(self, code)라는 함수가 아래의 명령을 가르킨다.
        self.code = code # 객체변수 code에 code 값을 넣는다.

    def get_name(self): # def로 get_name(self)라는 함수가 아래의 명령을 가르킨다.
        return self.name # 객체변수 name을 함수 밖으로 돌려준다.

    def get_code(self): # def로 get_code(self)라는 함수가 아래의 명령을 가르킨다.
        return self.code # 객체변수 code를 함수 밖으로 돌려준다.

    def set_per(self, per): # def로 set_per(self, per)이라는 함수가 아래의 명령을 가르킨다.
        self.per = per # 객체변수 per에 per 값을 넣는다.

    def set_pbr(self, pbr): # def로 set_pbr(self, pbr)이라는 함수가 아래의 명령을 가르킨다.
        self.pbr = pbr # 객체변수 pbr에 pbr 값을 넣는다.

    def set_dividend(self, dividend): # def로 set_dividend(self, dividend)라는 함수가 아래의 명령을 가르킨다.
        self.dividend = dividend # 객체변수 dividend에 dividend 값을 넣는다.

종목 = [] # 종목이라는 변수에 리스트 []를 넣었다.
   
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83) # 삼성이라는 변수에 Stock class에 넣은 삼성전자, 005930, 15.79, 1.33, 2.83을 넣는다.
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27) # 현대차라는 변수에 Stock class에 넣은 현대차, 005380, 8.70, 0.35, 4.27을 넣는다.
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37) # LG전자라는 변수에 Stock class에 넣은 LG전자, 0.66570, 317.34, 0.69, 1.37을 넣는다.

종목.append(삼성) # 종목이라는 리스트에 삼성을 첨부한다.
종목.append(현대차) # 종목이라는 리스트에 현대차를 첨부한다.
종목.append(LG전자) # 종목이라는 리스트에 LG전자를 첨부한다.

for i in 종목: # for 반복문을 이용하여 변수 i를 종목 갯수만큼 반복한다.
    print(i.code, i.per) # i의 code를 출력하고, i의 per을 출력한다.