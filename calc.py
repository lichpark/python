#operator
# +,-,*,/ [수리연산] ,[대입연산],[논리연산]

# 수리연산(+,-,*,/,//(몫) ,% )
# print(7//2) #몫
# print(7 % 2) #나머지
# print( 2 ** 4) # 제곱 16

#대입연산자(=)
#비교연산자(>,<,<=,>= ,==,!=)
a= 3>0
#문자,숫자,불리언(true/false)

#논리연산자(and,or,not)
#삼항연산자 (참 if , else 거짓)

#두 정수를 입력 맏고
# 합,차 곱,나머지, 몫,제곱10

def numberins(numb):
    ins = input(f"정수{numb}:")
    return ins

in1 = numberins(1)
in2 = numberins(2)


def substrnumb(text):
    textsubstr = text.split(":")
    numb = textsubstr[1]
    return numb

if in1 =="0" or in2 =="0" :
    print("0은 입력하실 수 없습니다.")
else:
    try:
        input1 = int(in1)
        input2 = int(in2)

        res1 = input1 + input2
        res2 = input1 - input2
        res3 = input1 * input2
        res4 = input1 % input2
        res5 = input1 // input2
        res6 = input1 ** input2

        print(f"합:{res1} ,차:{res2},곱:{res3},나머지:{res4},몫:{res5},제곱:{res6} ")
    except:
        print("입력값이 숫자가 아닌게 있습니다.")









