'''
2023.05.10
한유진
#문제정의
    입력받은 숫자가 소수인지 아닌지 판별하는 프로그램
#문제분석
    변수-숫자(su)
#알고리즘
    1.변수 초기화
        su에 정수 입력
    2.논리(반복언애 선택포함)
        (반복) for i in range(2,num+1):
            (선택) su%i==0:
        else:
            소수 아님
'''

su=int(input("소수 검증 숫자:"))
for i in range(2,su+1):
    if su%i==0:
        break
if su==1:
    print('{}는 소수'.format(su))
else:
    print('{}는 소수 아님'.formats(su))