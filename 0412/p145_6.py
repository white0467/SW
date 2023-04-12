'''
2023.04.12
한유진
두 개의 수가 모두 짝수이면 두 수를 더한 결과를 출력
그렇지 않고 둘 중 하나가 홀수면 다시 입력
#문제분석
    변수 - 숫자1(num1) 숫자2(num2)
    수식 - num1%2==0 (num1은 짝수)/ num2%2!=0(num2은 홀수)
#알고리즘
    1. 변수선언
        -num1,num2에 정수 입력
    2. 논리(선택 if~elif~else)
        num1%2==0 and num2%2!=0 
        num1%2!=0 and num2%2==0
        num1%2==0 and num2%2==0
'''


num1=int(input("정수1 : ")) #정수 입력
num2=int(input("정수2 : ")) #정수 입력
total=num1+num2

if num1%2==0 and num2%2==0:
    print("{} + {} = {}".format(num1,num2,total))
elif num2%2==0 and num1%2!=0:
    print("첫번째 정수를 짝수로 입력하세요.".format(num1))
elif num2%2!=0 and num1%2==0:
    print("두번째 정수를 짝수로 입력하세요.".format())
else:
    print("두 수를 모두 짝수로 입력하세요.")