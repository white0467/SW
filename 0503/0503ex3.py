'''
2023.05.03
한유진
#문제정의
    1~입력받은 숫자까지의 합계 구하기
#문제분석
    변수-숫자(su),합계(total)
#알고리즘
    1. 변수선언
        su에 정수 입력
        total=0
    2. 논리(반복)
        (조건) for i in range(1,num+1)
'''
#for반복
su=int(input("합계 구할 숫자:"))
total=0 #합계

for i in range(1,su+1): #조건
    total=total+i   #합계

print('1~{}까지의 합계는 {}'.format(su,total))