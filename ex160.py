리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py'] # 리스트 변수에 intra.h, intra.c, define.h, run.py 에 넣는다.
for i in 리스트: # 반복문 for을 사용하여 변수 i를 리스트만큼 반복한다.
    split = i.split(".") # split 변수는 i에서 .을 기준으로 분리한다.
    if (split[1] == "h") or (split[1] == "c"): # 만약 .을 기준으로 하였을 때 split의 1번째 자리가 h이거나 c라면 아래 명령을 실행한다.
        print(i) # i를 출력한다.