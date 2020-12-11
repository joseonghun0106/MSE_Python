def print_max(a, b, c) : # def로 print_max(a, b, c)라는 함수는 아래의 명령의 가르킨다.
    if a > b and a > c: # 만약 a가 b와 c보다 클 경우 a를 출력한다.
        print(a)
    elif b > c and b > a: # 만약 b가 a와 c보다 클 경우 b를 출력한다.
        print(b)
    else: # 무엇도 아닌 경우에는 c를 출력한다.
        print(c)

print_max(10, 2, 3)
print_max(10, 20, 3)
print_max(10, 20, 30)