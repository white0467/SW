
'''
2023.05.09
한유진
#문제정의
    두 개의 숫자를 입력 받아서 두 사이의 합계 
#문제분석
    변수-정수1(num1), (정수2sum2),합계(합계),임시변수(temp)
#알고리즘
    1. 변수선언 (변수 초기화)
    num1,num2는 정수를 입력 받는다
    sum=0, temp=0
    2.프로그램 논리(선택<=반복)
        2-1 (선택조건) 0
    '''     
num1=int(input("첫 번째 숫자"))
num2=int(input("두 번째 숫자"))
sum=0
temp=0

if num1>num2:
    temp=num1
    num1=num2
    num2=temp

i=num1
while i <=num2:
    sum=sum+i
    i=i+1

print("{}~{}까지의 합계는 {}".format(num1,num2,sum))