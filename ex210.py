def message1(): # def로 message1이라는 함수가 print("A")를 가르킨다.
    print("A") # A를 출력한다.

def message2(): # def로 message2이라는 함수가 print("B")를 가르킨다.
    print("B") # B를 출력한다.

def message3(): # def로 message3이라는 함수가 반복문의 내용을 가르킨다.
    for i in range (3) : # for 반복문으로 i를 3번 반복한다.
        message2() # message2는 print("B")를 출력한다.
        print("C") # C를 출력한다.
    message1() # message1은 print("A")를 출력한다.

message3() # message3은 뱐복문을 출력한다.