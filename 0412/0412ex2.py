'''
2023.04.12
한유진
입력받은 두 수의 크기 비교
#문제분석
    변수 - 숫자1(num1),숫자2(num2)
#알고리즘
    1. 변수선언
        num1,num2에 정수 입력
    2. 논리(선택)
        if num1>num2:
            (참)큰 수는 num1, 작은 수는 num2
        else:
            (거짓)큰 수는 num2, 작은 수는 num1
'''

num1=int(input("숫자1 : ")) #점수 정수로 입력
num2=int(input("숫자2 : ")) #점수 정수로 입력

if num1>num2:   #선택 조건
    print("두 수 중 큰 수는 {}, 작은 수는 {}".format(num1,num2))
else:
    print("두 수 중 큰 수는 {}, 작은 수는 {}".format(num2,num1))
