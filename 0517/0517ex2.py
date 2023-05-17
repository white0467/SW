'''
2023.05.17
한유진
#문제정의
    기존파일을 새로운 파일에 복사하는 프로그램 만들기
#문제분석
    변수: 원본파일(source),복사할파일(target),
            원본파일의 내용(texts)
#알고리즘
    1. source에 원본파일 이름 입력
    2. target에 복사할파일 이름 입력
    3. 파일처리
        source파일 객체생성
            한 줄씩 읽어오기    
            내용물 texts변수에 저장
        target파일 객체생성 
            texts파일 쓰기
        파일생성 메세지 출력
'''

source=input("source 파일 입력: ")
target=input("target 파일 입력: ")

with open("C:/대학sw/linetest.txt","r") as f:   #읽기파일 객체
    texts=f.read()  #파일 한꺼번에 문자열로 읽기

with open("C:/대학sw/copylinetest.txt","w") as fp:
    fp.write(texts) #원본파일에서 읽어온 내용 파일에 출력

    print(target+"파일이 생성되었습니다.") #메세지 출력
