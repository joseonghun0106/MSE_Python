def 함수0(num) : # def로 함수0(num)이라는 함수가 return num * 2를 가르킨다.
    return num * 2 # return을 통해 num * 2 의 값을 호출한다.

def 함수1(num) : # def로 함수1(num)이라는 함수가 return 함수0(num + 2)라는 값을 가르킨다.
    return 함수0(num + 2) # return을 통해 함수0(num + 2)를 호출한다.

def 함수2(num) : # def로 함수2(num)이라는 함수가 아래의 명령을 가르킨다.
    num = num + 10 # num에 num + 10인 수를 넣는다.
    return 함수1(num) # return을 통해 함수1(num)을 호출한다.

c = 함수2(2) # c라는 변수에 함수2(2)를 넣는다.
print(c) # c라는 변수를 출력한다.