'''
2023.05.09
한유진
#문제정의
    1~1000까지의 입력받은 숫자의 배수만 더하기
#문제분석
    변수-정수(num),합계(total)
#알고리즘
    1.변수 초기화
        num변수에 정수 입력
        total=0
    2.프로그램 논리(반복for)
        for i in rage(num,1001,num):
            sum=sum+i
'''

num=int(input("합을 원하는 배수 입력:"))
total=0

for i in range(num,1001,num):
    total=total+i

print("1~1000까지의 {}의 배수의 합계:{}".format(num,total))