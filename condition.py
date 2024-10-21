import math
#조건
# num = input("숫자입력")
# num_int = int(num)
# if num_int >0:
#     print("입력한 숫자는 0보다 큽니다.")
# elif num ==0:
#     print("0")
# else:
#     print("음의정수")
# print("프로그램 종료")

#유저가 구매한 총합이 50000원 이상이면 10% 할인왼 금액 나타내고 아니면 원래금액 나타내기

# ins = input("구매금액 입력: ")
# try:
#     ins_int = float(ins)
#     ins_round_res = int(math.floor(ins_int))
#     if ins_round_res>=50000:
#         sale_price = math.floor(ins_round_res * 0.9)
#         print(f"총 금액: {sale_price} 입니다.")
#     else:
#         print(f"총 금액: {ins_int} 입니다.")
# except ValueError:
#     print("값이 제대로 입력 안되었습니다. 문자로 입력한건 아닌지 확인해주세요.")

#영어 점수를 유저에게 물어보고 90이상 A , 80이상 B , 70이상 C , 60이상 D , 그외 F

def gradechk(numb):
    grade = ""
    if numb >=90:
        grade = "A"
    elif numb > 90 and numb >= 80:
        grade = "B"
    elif numb > 80 and numb >= 70:
        grade = "C"
    elif numb > 70 and numb >= 60:
        grade = "D"
    elif numb < 60:
        grade = "F"
    return grade

ins = input("영어점수를 입력해 주세요: ")

try:
    toIns = math.floor(int(ins))
    engRes = gradechk(toIns)
    print(f"해당 사용자의 영어등급은 : {engRes} 입니다.")
except ValueError:
    print("영어점수가 제대로 입력되지 않았습니다.")

