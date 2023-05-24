'''
20230524
한유진
#문제정의
    난수를 발생시켜 num.txt 파일을 만들고, 이 파일을 이용해서 각 학생의
    평균을 구한 다음 avg.txt 파일에 저장하기
#문제분석
    변수-
#알고리즘

'''

import random   #난수 모듈 추가
with open("C:/대학sw/num.txt","w") as f:    #파일 객체
    for i in range(5):  #줄 반복
        for j in range(5):  #랜덤 수 찍기 반복
            f.write(str(random.randint(1,100)))     #랜덤 수 파일에 쓰기
            f.write(' ')    #숫자 다음 공백 찍기
        f.write('\n')   #줄 바꿈

with open("C:/대학sw/num.txt","r") as f1:   #읽기 파일 객체
    with open("C:/대학sw/avg.txt","w") as f2:   #쓰기 파일 객체
        
        j=0
        while True:
            j=j+1
            score=f1.readline() #num.txt 한 줄 읽어오기
            if score=='':   #내용이 없으면
                break
            scorelist=score.split()     #읽어온 한 줄을 공백 기준 리스트로 변환?
            
            sum=0   #합계
            for i in range(5):  #한 학생당 5과목의 점수 더하기
                sum=sum+int(scorelist[i])    #리스트의 항목 더하기
            print(j,"번 학생의 평균 : ",sum/5,file=f2)    #결과 파일에 작성
            
