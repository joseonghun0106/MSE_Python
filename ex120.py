fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"} # fruit 함수에 딕셔너리인 Key와 Value를 넣는다.
과일 = input("좋아하는 과일은?") # 과일 함수에 좋아하는 과일은? 이라는 입력을 넣는다.
if 과일 in fruit.values(): # 만약 입력한 과일이 fruit 변수에 Value 값에 있을경우 정답입니다.를 출력하고, 아닐 경우 오답입니다.를 출력한다.
    print("정답입니다.")
else:
    print("오답입니다.")