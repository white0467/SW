'''
2023.0510
한유진
#문제저으이
    입력받은 숫자의 합이 1000이상이면 합계와 평균 출력
#문제분석
    변수-합계(sum),입력횟수(cnt),평균(avg),정수(su)
#문제정의

#문제분석
    변수
#알고리즘
    1.변수 초기화
        summ=0,cnt=0,avg=o
    2.논리(반복안에 선택 포함)
        반복 while True:
        num  키보드로 입력
        cnt 1 증가
        sum에 더하기
        (선택) if sum>=1000:
                    break
    3.합계, 평균 출력
'''
su=0
cnt=0
avt=0

while True:
    su=int(input("숫자 입력:")) #정수 입력
    cnt+=1
    sum,+=su
    if sum>=1000:
            break
    
avg=sum/cnt

print("1000을 넘은 수:%d"%sum,end=" ")
print("평균:%.2f"%avg)