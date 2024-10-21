#몇년생인지 물어보고, 2005년생 이하면 성인입니다.아니면 미성년자 입니다.

# inp = input("년생을 입력해 주세요: ")
# inp_ins = int(inp)
#
# if inp_ins < 2006 :
#     print("성인입니다.")
# else:
#     print("미성년입니다.")

#e ,i 물어보기 | s,n물어보기 | t,f물어보기 | j,p물어보기
#외향/내향, 감각/직관 , 이성,감성, 계획,즉흥

arrlist = []
def question(numb):
    ques = ""
    if numb ==0:
        ques ="e or i :"
    elif numb ==1:
        ques = "s or n :"
    elif numb ==2:
        ques = "t or f :"
    elif numb ==3:
        ques = "j or p :"
    rest = input(ques)

    return rest

def resfunc(ins,numb):
    ins = ins.lower()
    if numb ==0:
        if ins =='e':
            arrlist.append("외향")
        elif ins =='i':
            arrlist.append("내향")
        else:
            arrlist.append("invalded")
    elif numb ==1:
        if ins == 's':
            arrlist.append("감각")
        elif ins == 'n':
            arrlist.append("직관")
        else:
            arrlist.append("invalded")
    elif numb ==2:
        if ins == 't':
            arrlist.append("이성")
        elif ins == 'f':
            arrlist.append("감성")
        else:
            arrlist.append("invalded")
    elif numb ==3:
        if ins == 'j':
            arrlist.append("계획")
        elif ins == 'p':
            arrlist.append("즉흥")
        else:
            arrlist.append("invalded")

for i in range(4):
    insstr = question(i)
    resfunc(insstr ,i)

#
# input1 = question(1)
# input2 = question(2)
# input3 = question(3)
# input4 = question(4)
#
# result1 = resfunc(input1,1)
# result2 = resfunc(input2,2)
# result3 = resfunc(input3,3)
# result4 = resfunc(input4,4)

print(f"당신의 성향은 {arrlist[0]} {arrlist[1]} {arrlist[2]} {arrlist[3]} 이군요")
