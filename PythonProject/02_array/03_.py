
# 조건문 (if문 사용)
# if : 만약에 ~ 라면

# 조건에 따라 다른 명령을 내릴떄 사용

# 조건이 참(True) 이면 실행, 거짓(False)이면 실행하지마

# 비교연산자
a = 10
b = 3

# a와 b가 서로 같습니까?
print(a == b)

# 실행순서
# print(a == b )
# print(10 == b)
# print(10 == 10)
# print(False)

# a와 b가 서로 다릅니까?
print(a != b)

# a와 b보다 큽니까?
a = 10
b = 10
print(a > b)

# a가 b이상 이상입니까? (같거나 큽니까?)
print ( a >= b)

# b가 a보다 큽니까?
print (b < a)
# a가 b보다 작습니까?
print( a < b)

# a가 b이하입니까? (<= , >= , !=) 등호는 항상 오른쪽이다
print( a <= b)

# 주민번호 뒷자리의 첫번째 숫자
# 짝수면 여자, 홀수면 남자
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
# 1900 년도에 태어난 남자 1, 여자 2
# 2000 년도에 태어난 남자 3, 여자 4
# 1900 년도에 태어난 외국인 남자 5, 여자 6
# 2000 년도에 태어난 외국인 남자 7, 여자 8
# 1800 년도에 태어난 남자 9, 여자 0

idnum= "1234567"

# idnum 의 첫번째 숫자가 홀수면 남성 출력, 짝수면 여성 출력
print(idnum[0])


fst = idnum[0]
# fst의 타입? 문자열
print(type(fst)) # "1"

# 차이썬은 배열에 곱하기를 하면 내용이 그 수만큼 늘어남
print(fst * 2)

# 홀수, 짝수 계산을 위해 fst을 int로 변환해야함
fst = int(fst)

# 홀수, 짝수 계산하기
# 어떤 수든 2로 나누얷을때 나머지가 0이면 짝수, 1이면 홀수
print(fst % 2 ==0)

# 실행순서
# print(fst% 2 ==0)
# print(1% 2 ==0)
# print(1 == 0)
# print(False)




# 짝수일떄는 여성, 홀수일떄는 남성 출력
if fst % 2 == 0 :
    print("여성") # 탭이 있기에 if 내부 코드가 됨
print("성별체크") # 탭이 없기에 if 문과 무관한 코드

# fst가 홀수일 때는 남성이 출력되도록 if문 작성

if fst % 2 == 1 :
    print("남성")



# 두 개의 if문을 하나로 묶기
if fst % 2 == 0:
    print("여성")
elif  fst % 2 == 1:
    print("남성")


# 짝수 체크를 해서 True 면 짝수이고, Flase면 Fst가 홀수라는 뜻
fst = 4
if fst % 2 == 0 :
    print("여성")
else: #위 if문의 Flase면 조건 체크 없이 실행
    print("남성")

#  fst가 1~4이면 한국인
#  fst가 5~8이면 외국인
# 1 <= fst <= 4
fst =6
print(1 <= fst <4)
print(5 <= fst <= 8)

# fst에 대해 1~4면 한국인 , 5~8이면 외국인 출력하기
if 1 <= fst <= 4 :
    print("한국인")
else :
    print("외국인")


# 성적이 90점이상 A등급
# 성적이 80점대면 B등급
# 성적이 70점대면 C등급
# 그 외 나머지는 D등급

score = 85

# score가 90점 대인지 확인
print(score >= 90)
# score가 80점대인지 확인
print(80 <= 90)

if score >= 90:
    print("A등급")
elif 80 <= score < 90:
    print("B등급")
elif 70 <= score < 80:
    print("C등급")
else :
    print("D등급")


score = 95
if score >= 70:
    print("C등급")
elif score >= 80:
    print("B등급")
elif score >= 90:
    print("A등급")
else :
    print("D등급")