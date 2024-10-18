# 첫번째 숫자입력:
# 두번째 숫자 입력:
# 두 수의 합은 ~입니다.

# n1chk =0
# n2chk =0
# 
# number1 = input("input number1:")
# try:
#     n1 = int(number1)
# except:
#     n1chk = 1
# 
# if n1chk >0:
#     number1 = input("input number1:")
# else:
#     number2 = input("input number2:")
# 
# try:
#     n2 = int(number2)
# except:
#     n2chk = 1
# 
# if n2chk >0:
#     number2 = input("input number2:")
# else:
#     print(f"두 수의 합은: {n1 + n2}")

#나이가 어떻게 되세요?
#나이가 ~~ 이니 ~~년생이군요.
current_year = 2024

age = input("나이가 어떻게 되세요?")
try:
    int_age = int(age)
    if int_age <1:
        print("나이는 1보다 작을 수 없습니다.")
    else:
        birth_year = current_year - int_age
        print(f"나이가 {int_age} 이니 {birth_year}년생이시군요")
except:
    print("나이를 숫자로 입력해 주세요")


