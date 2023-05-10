'''
2023.05.10
한유진
#문제정의("
    입력받은 숫자 만큼 줄 반복 하면서 별 찍기
#문제분석
    변수-숫자(su)
#알고리즘
    1. 변수 초기화
        su변수에 정수 입력
    2. 논리(중첩 반복)
        (반복) for i in range(1,su+1):  #줄반복
            (반복) for j in range(1,i+1):   #별 찍기 반복
                별 찍기
'''

su=int(input("정수 입력"))
for i in range(1,su+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

#거꾸로 출력
print("\n거꾸로 출력")

su2=int(input("정수 입력"))
for i in range(1,su2+1):
    for j in range(i,su2+1):
        print("*",end="")
    print()


