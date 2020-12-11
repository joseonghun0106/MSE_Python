apart = [ [101, 102], [201, 202], [301, 302] ] # apart 변수에 리스트 [101, 102], [201, 202], [301,302]를 넣는다.
for row in apart: # 변수 row를 apart만큼 반복한다.
    for col in row: # 변수 col을 row만큼 반복한다.
        print(col, "호") # 변수 col과 호를 출력한다.
print("-" * 5) #모든 층과 집을을 출력한 후 -----를 출력한다.