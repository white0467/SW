'''
2023.04.05
한유진
본봉과 수당의 월급 입력 받아서 합계 평균 구하기(p116)
'''

sal=int(input("본봉:"))        #본봉 입력
allo=int(input("수당:"))        #수당 입력


tax=(sal+allo)*0.2     #세금 계산
total_sal=sal+allo-tax     #수령액 계산   

print("본봉이 {}이고, 수당은 {}이다".format(sal,allo,total_sal))