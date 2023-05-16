'''
2023.05.16
한유진
파일 입출력 - seek(o):파일의 처음으로 포인트 이동
           -read(int n):지정한 객수만큼 파일 읽어오기
'''

f=open("C:/대학sw/test.txt","r") #파일 객체 생성(읽기)

print(f.read(10),end='')    #파일에서 10개의 문자 읽어서 출력(포인터 이동)
print(f.read(10),end='')
print(f.read(10))

f.seek #파일의 처음으로 포인터 이동

print(f.read(10),end='')    #파일에서 10개의 문자 읽어서 출력(포인터 이동)
print(f.read(10),end='')
print(f.read(10))

f.close()