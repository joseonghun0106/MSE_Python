import random # random 모듈을 추가한다.


class Account: #Account라는 클래스를 만든다.
    # class variable 
    account_count = 0 # 변수 account_count에 0을 넣는다.

    def __init__(self, name, balance): #def로 __init__(self, name, balance)이라는 함수가 아래의 명령을 가르킨다. 
        self.deposit_count = 0 # 객체변수 deposit_count에 0을 넣는다.
        self.deposit_log = [] # 객체변수 deposit_log에 [] 리스트를 넣는다.
        self.withdraw_log = [] # 객체변수 withdraw_log에 [] 리스트를 넣는다.

        self.name = name # 객체변수 name에 name을 넣는다.
        self.balance = balance # 객체변수 balance에 balance를 넣는다.
        self.bank = "SC은행" # 객체변수 bank에 SC은행을 넣는다.

        # 3-2-6
        num1 = random.randint(0, 999) # 변수 num1에 0과 999 사이 중 랜덤으로 하나의 수를 넣는다.
        num2 = random.randint(0, 99) # 변수 num2에 0과 99 사이 중 랜덤으로 하나의 수를 넣는다.
        num3 = random.randint(0, 999999) # 변수 num3에 0과 999999 사이 중 랜덤으로 하나의 수를 넣는다.

        num1 = str(num1).zfill(3)  # 변수 num1에 문자열로 zfill 함수로 인해 ()안에 수 중 남는 자리를 앞에서부터 0으로 채운다.
        num2 = str(num2).zfill(2)  # 변수 num2에 문자열로 zfill 함수로 인해 ()안에 수 중 남는 자리를 앞에서부터 0으로 채운다.
        num3 = str(num3).zfill(6)  # 변수 num3에 문자열로 zfill 함수로 인해 ()안에 수 중 남는 자리를 앞에서부터 0으로 채운다.
        self.account_number = num1 + '-' + num2 + '-' + num3  # 객체변수 account_number에 num1, -, num2, -, num3의 값을 넣는다.
        Account.account_count += 1

    @classmethod
    def get_account_num(cls): # def로 get_account_num(cls)라는 함수가 아래의 명령을 가르킨다
        print(cls.account_count)  # cls.account_count를 출력한다.

    def deposit(self, amount): # def로 deposit(self, amount)라는 함수가 아래의 명령을 가르킨다.
        if amount >= 1: # 만약 amount가 1보다 크거나 같을 경우 아래의 명령을 실행한다.
            self.deposit_log.append(amount) # 객체변수 deposit_log에 amount를 끝에 추가한다.
            self.balance += amount # 객체변수 balance에 amount를 더한 값을 넣는다..

            self.deposit_count += 1 # 객체변수 deposit_count에 1을 더한 값을 넣는다.
            if self.deposit_count % 5 == 0:         # 만약 객체변수 deposit_count의 값이 5의 배수라면 아래의 명령을 실행한다.
                # 이자 지금
                self.balance = (self.balance * 1.01) # 객체변수 balance에 객체변수 balance * 1.01 값을 넣는다.


    def withdraw(self, amount): # def로 withdraw(self, amount)라는 함수가 아래의 명령을 가르킨다.
        if self.balance > amount: # 만약 객체변수 balance가 amount보다 크다면 아래의 명령을 실행한다.
            self.withdraw_log.append(amount) # 객체변수 withdraw_log 끝에 amount 값을 추가한다.
            self.balance -= amount # 객체변수 balance에 amount의 값을 뺀 값을 넣는다.

    def display_info(self): # def로 display_info(self)라는 함수가 아래의 명령을 가르킨다.
        print("은행이름: ", self.bank) # 은행이름:, 객체변수 bank를 출력한다.
        print("예금주: ", self.name) # 예금주:, 객체변수 name을 출력한다.
        print("계좌번호: ", self.account_number) # 계좌번호:, 객체변수 account_number을 출력한다.
        print("잔고: ", self.balance) # 잔고:, 객체변수 balance를 출력한다.

    def withdraw_history(self): # def로 withdraw_history(self)라는 함수가 아래의 명령을 가르킨다.
        for amount in self.withdraw_log: # for 반복문을 사용하여 변수 amount가 객체변수 withdraw_log만큼 반복한다.
            print(amount) # amount를 출력한다.

    def deposit_history(self): # def로 deposit_history(self)라는 함수가 아래의 명령을 가르킨다.
        for amount in self.deposit_log: # for 반복문을 사용하여 변수 amount가 객체변수 deposit_log만큼 반복한다.
            print(amount) # amount를 출력한다.


k = Account("Kim", 1000) # 변수 k에 Account("Kim", 1000)을 넣는다.
k.deposit(100) # k의 deposit함수 (100)을 넣는다.
k.deposit(200) # k의 deposit함수 (200)을 넣는다.
k.deposit(300) # k의 deposit함수 (300)을 넣는다.
k.deposit_history() # 위에 넣었던 함수들을 k의 deposit_history에 넣어 출력한다.

k.withdraw(100) # k의 withdraw함수 (100)을 넣는다.
k.withdraw(200) # k의 withdraw함수 (200)을 넣는다.
k.withdraw_history() # 위에 넣었던 함수들을 k의 withdraw_history에 넣어 출력한다.