a = "오류가 발생하는 이유는 def print()의 ()안에는 어떠한 단어도 없지만, myStock.print()의 ()안에는 myStock이라는 단어가 들어있기 때문에 오류가 발생한다."
print(a)
class OMG : # OMG라는 class를 만든다.
    def print() : # class 안에 print()라는 함수가 아래의 print("Oh my god")을 가르킨다.
        print("Oh my god") # Oh my god이라는 단어를 출력한다.

myStock = OMG() # myStock이라는 객체를 생성한다.
myStock.print() # OMG.print(myStock)과 같은 명령을 보낸다.