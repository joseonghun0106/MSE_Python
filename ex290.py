class 부모: # 부모라는 class를 만든다.
    def __init__(self): # def로 _init_(self)라는 함수가 아래의 명령을 가르킨다.
        print("부모생성") # 부모생성을 출력한다.

class 자식(부모): # 부모 class를 상속받는 자식 class를 만든다.
    def __init__(self): # def로 _init_(self)라는 함수가 아래의 명령을 가르킨다.
        print("자식생성") # 자식생성을 출력한다.
        super().__init__() # 부모 class의 _init_()을 호출한다.

나 = 자식() # 자식 class의 객체를 나로 설정한다.

a = "자식()을 실행하면 자식생성을 먼저 출력하고, 부모 class의 부모생성을 다음으로 출력한다." # 정답을 변수 a에 기입한다.
print(a) # a라는 변수를 출력한다.