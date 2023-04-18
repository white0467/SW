'''
2023.04.18
한유진
3장 연습문제 7번
두 정수 입력 x>y->x//y, x<y->x+y, x==y->x*y
단, 나눗셈 몫 계산할 때 y는 0 안됨
#문제분석
    변수: 정수1(su1),정수2(su2)
    수식: su1//su2,su1+su2,su1*su2
#알고리즘
    1. 변수선언
    - s1, su2u에 정수 입력 받기
    2. 논리(선택 if~elif~else)
    if (su2)>=1


'''

su1=int(input("x : ")) #정수 입력
su2=int(input("y : ")) #정수 입력

if su1>su2:
    if su2!=0:
        print("{} // {} = {}".format(su1,su2,su1//su2))
    else:
        print("y의 값이 0입니다.")
if su1<su2:
    print("{} + {} = {}".format(su1,su2,su1+su2))
if su1==su2:
    print("{} * {} = {}".format(su1,su2,su1*su2))


