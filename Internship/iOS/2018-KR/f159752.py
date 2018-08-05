import math

end =("teen", "teenth", "ty", "tieth", "th")
chap = ("twen", "thir", "fif", "six" , "seven", "eigh", "nine")
dimEng = ("", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion")
operators =("+","-","^","(",")","*","/","**")

chapGer = ("ein", "zwei", "drei", "vier", "fünf", "sech", "sieb", "acht", "neun")
endGer = ("s", "en" , "zehn", "zig", "te", "ste")
dimGer = ("", "tausend", "million", "milliarde", "billion", "billiarde", "trillion")

chapUkr = ("оди","два","три","чотир","п'ят","шіст","сім","вісім","дев'ят")
endUkr = ("н","ь","надцять","дцять","сот","надцятий","дцятий","десятий","сотий","десят","десяти","дцяти")
# rodUkr = ("двох","трьох","сороко","чотирьох","п'яти","шести","семи","восьми","дев'яти")
dimUkr = ("", "тисяча", "мільйон", "мільярд", "трильйон", "квадрильйон", "квінтильйон")
dimRodUkr = ("", "тисячний", "мільйонний", "мільярдний", "трильйонний", "квадрильйонний", "квінтильйонний")

num = {0: "zero",
       1: "one",
       2: "two",
       3: "three",
       4: "four",
       5: "five",
       6: chap[3],
       7: chap[4],
       8: chap[5]+"t",
       9: chap[6],

       10: "ten",

       11: "eleven",
       12: "twelve",
       13: "thir"+end[0],
       14: "four"+end[0],
       15: chap[2]+end[0],
       16: chap[3]+end[0],
       17: chap[4]+end[0],
       18: chap[5]+end[0],
       19: chap[6]+end[0],

       20: chap[0]+end[2],
       30: chap[1]+end[2],
       40: "for"+end[2],
       50: chap[2]+end[2],
       60: chap[3]+end[2],
       70: chap[4]+end[2],
       80: chap[5]+end[2],
       90: chap[6]+end[2]
       }
place = {0: "null",
         1: "first",
         2: "second",
         3: chap[1]+"d",
         4: "fourth",
         5: chap[2]+end[4],
         6: chap[3]+end[4],
         7: chap[4]+end[4],
         8: chap[5]+end[4],
         9: "ninth",

         10: "tenth",

         11: num[11]+end[4],
         12: "twelfth",
         13: chap[1]+end[1],
         14: "four"+end[1],
         15: chap[2]+end[1],
         16: chap[3]+end[1],
         17: chap[4]+end[1],
         18: chap[5]+end[1],
         19: chap[6]+end[1],

         20: chap[0]+end[3],
         30: chap[1]+end[3],
         40: "forties",
         50: chap[2]+end[3],
         60: chap[3]+end[3],
         70: chap[4]+end[3],
         80: chap[5]+end[3],
         90: chap[6]+end[3]
         }
numGer = {0: "null",
          1: chapGer[0],
          2: chapGer[1],
          3: chapGer[2],
          4: chapGer[3],
          5: chapGer[4],
          6: chapGer[5],
          7: chapGer[6],
          8: chapGer[7],
          9: chapGer[8],

          10: "zehn",
          11: "elf",
          12: "zwölf",
          13: chapGer[2]+endGer[2],
          14: chapGer[3]+endGer[2],
          15: chapGer[4]+endGer[2],
          16: chapGer[5]+endGer[2],
          17: chapGer[6]+endGer[2],
          18: chapGer[7]+endGer[2],
          19: chapGer[8]+endGer[2],

          20: "zwanzig",
          30: "dreißig",
          40: chapGer[3]+endGer[3],
          50: chapGer[4]+endGer[3],
          60: chapGer[5]+endGer[3],
          70: chapGer[6]+endGer[3],
          80: chapGer[7]+endGer[3],
          90: chapGer[8]+endGer[3]
}

numUkr={0: "нуль",
        1: chapUkr[0]+endUkr[0],
        2: chapUkr[1],
        3: chapUkr[2],
        4: chapUkr[3]+"и",
        5: chapUkr[4]+endUkr[1],
        6: chapUkr[5]+endUkr[1],
        7: chapUkr[6],
        8: chapUkr[7],
        9: chapUkr[8]+endUkr[1],

        10: "десять",

        11: chapUkr[0]+endUkr[2],
        12: chapUkr[1]+endUkr[2],
        13: chapUkr[2]+endUkr[2],
        14: chapUkr[3]+endUkr[2],
        15: chapUkr[4]+endUkr[2],
        16: chapUkr[5]+endUkr[2],
        17: chapUkr[6]+endUkr[2],
        18: chapUkr[7]+endUkr[2],
        19: chapUkr[8]+endUkr[2],

        20: chapUkr[1]+endUkr[3],
        30: chapUkr[2]+endUkr[3],
        40: "сорок",
        50: chapUkr[4]+endUkr[9],
        60: chapUkr[5]+endUkr[9],
        70: chapUkr[6]+endUkr[9],
        80: chapUkr[7]+endUkr[9],
        90: "дев'яносто",

        100: "сто",
        200: "двісті",
        300: "триста",
        400: "чотириста",
        500: chapUkr[4]+endUkr[4],
        600: chapUkr[5]+endUkr[4],
        700: chapUkr[6]+endUkr[4],
        800: chapUkr[7]+endUkr[4],
        900: chapUkr[8]+endUkr[4]
        }
placeUkr = {0: "нульовий",
            1: "перший",
            2: "другий",
            3: "третій",
            4: "четвертий",
            5: "п'ятий",
            6: "шостий",
            7: "сьомий",
            8: "восьмий",
            9: "дев'ятий",
            10: endUkr[7],

            11: chapUkr[0] + endUkr[5],
            12: chapUkr[1] + endUkr[5],
            13: chapUkr[2] + endUkr[5],
            14: chapUkr[3] + endUkr[5],
            15: chapUkr[4] + endUkr[5],
            16: chapUkr[5] + endUkr[5],
            17: chapUkr[6] + endUkr[5],
            18: chapUkr[7] + endUkr[5],
            19: chapUkr[8] + endUkr[5],

            20: chapUkr[1] + endUkr[6],
            30: chapUkr[2] + endUkr[6],
            40: "сороковий",
            50: chapUkr[4] + endUkr[7],
            60: chapUkr[5] + endUkr[7],
            70: chapUkr[6] + endUkr[7],
            80: chapUkr[7] + endUkr[7],
            90: "дев'яностий",

            100: endUkr[8],
            200: "двох"+endUkr[8],
            300: "трьох"+endUkr[8],
            400: "чотирьох"+endUkr[8],
            500: chapUkr[4] + endUkr[8],
            600: chapUkr[5] + endUkr[8],
            700: chapUkr[6] + endUkr[8],
            800: chapUkr[7] + endUkr[8],
            900: chapUkr[8] + endUkr[8]
          }
# (,)
rodUkr = {1:"одно",
          2:"двох",
          3:"трьох",
          4:"чотирьох",
          5:"п'яти",
          6:"шести",
          7:"семи",
          8:"восьми",
          9:"дев'яти",

          10: endUkr[10],
          11: chapUkr[0] + "надцяти",
          12: chapUkr[1] + "надцяти",
          13: chapUkr[2] + "надцяти",
          14: chapUkr[3] + "надцяти",
          15: chapUkr[4] + "надцяти",
          16: chapUkr[5] + "надцяти",
          17: chapUkr[6] + "надцяти",
          18: chapUkr[7] + "надцяти",
          19: chapUkr[8] + "надцяти",

          20:"два"+endUkr[11],
          30:"три"+endUkr[11],
          40:"сороковий",
          50:"п'яти"+endUkr[10],
          60:"шести"+endUkr[10],
          70:"семи"+endUkr[10],
          80:"восьми"+endUkr[10],
          90:"дев'яност",

          100: "сто",
          200: "двох",
          300: "трьох",
          400: "чотирьох",
          500: chapUkr[4],
          600: chapUkr[5],
          700: chapUkr[6],
          800: chapUkr[7],
          900: chapUkr[8]
          }

def trip(mass, last):
    pos=[]
    for i in mass:
        pos.append(int(i))
    if len(pos)==1:
        if last == False:
            return num[pos[0]]
        else:
            return place[pos[0]]
    elif len(pos)==2:
        if last == False:
            if pos[1]!=0:
                if pos[0]==1:
                    return num[pos[0] * 10 + pos[1]]
                else:
                    return num[pos[0] * 10] + " " +num[pos[1]]
            else:
                return num[pos[0]*10]
        else:
            if pos[1]!=0:
                if pos[0]==1:
                    return place[pos[0] * 10 + pos[1]]
                else:
                    return num[pos[0] * 10]+ " " + place[pos[1]]
            else:
                return place[pos[0]*10]
    elif len(pos)==3:
        # print("A = {0} B = {1} C = {2} L = {3}".format(pos[0],pos[1],pos[2], last))
        if last==False:
            if pos[1]!=0:
                if pos[2]!=0:
                    if pos[1]==1:
                        return hundred(num[pos[0]]) + " " + num[pos[1]*10+pos[2]]
                    else:
                        return hundred(num[pos[0]]) + " " + num[pos[1]*10]+" "+num[pos[2]]
                else:
                    return hundred(num[pos[0]]) + " " +num[pos[1]*10]
            else:
                if pos[2]!=0:
                    return hundred(num[pos[0]]) +" "+num[pos[2]]
                else:
                    return hundred(num[pos[0]])
        else:
            if pos[1]!=0:
                if pos[2]!=0:
                    if pos[1]==1:
                        return hundred(num[pos[0]]) + " " + place[pos[1]*10+pos[2]]
                    else:
                        return hundred(num[pos[0]]) + " " + num[pos[1]*10]+" "+place[pos[2]]
                else:
                    return hundred(num[pos[0]]) + " " +place[pos[1]*10]
            else:
                if pos[2]!=0:
                    return hundred(num[pos[0]]) +" "+place[pos[2]]
                else:
                    return hundred(num[pos[0]]) + "th"
def hundred(a):
    if a.find("zero")==-1:
        return " "+a+" hundred"
    else:
        return ""

def tripGer(mass, last):
    pos = []
    for i in mass:
        pos.append(int(i))
    if len(pos) == 1:
        if pos[0]==1:
            return numGer[pos[0]]+endGer[0]
        else:
            return numGer[pos[0]]
    elif len(pos)==2:
        if pos[1]!=0:
            if pos[0]==1:
                return numGer[pos[0]*10+pos[1]]
            else:
                return numGer[pos[0]]+"und"+numGer[pos[1]*10]
        else:
            return numGer[pos[0]*10]
    elif len(pos)==3:
        if pos[2]!=0:
            if pos[1]==1:
                return hundert(numGer[pos[0]])+numGer[pos[1]*10+pos[2]]
            else:
                return hundert(numGer[pos[0]]) + numGer[pos[2]] + "und" + numGer[pos[1]*10]
        else:
            if pos[1]==0:
                return hundert(numGer[pos[0]])
            else:
                return hundert(numGer[pos[0]]) + numGer[pos[1] * 10]
def hundert(a):
    if a.find("null")==-1:
        return a+"hundert"
    else:
        return ""


def tripUkr(mass):
    mass_flag = []
    dimU = []
    dimRU = []
    for i in range(0,len(mass)):
        dimU.append(dimUkr[i])
        dimRU.append(dimRodUkr[i])
    dimU.reverse()
    dimRU.reverse()

    mass_flag = getMassFlag(mass)
    # print(mass_flag)
    last_position=0
    for i in range(0,len(mass_flag)):
        if mass_flag[i]=="-":
            last_position=i
    # print("last position"+" = "+str(last_position))
    output=""
    for i in range(0,len(mass)):
        pos = []
        for j in mass[i]:
            pos.append(int(j))
        # print("pos ="+str(pos))
        if i!=last_position:
            if len(pos) == 1:
                output+= " "+ numUkr[pos[0]]
            if len(pos) == 2:
                if pos[1]!=0:
                    if pos[0]==1:
                        output += " " + numUkr[pos[0]*10+pos[1]]
                    elif pos[0]==0:
                        output += " " + numUkr[pos[1]]
                    else:
                        output += " " + numUkr[pos[0]*10]+" "+numUkr[pos[1]]
                else:
                    if pos[0]==1:
                        output += " " + numUkr[pos[0]*10]
                    elif pos[0]==0:
                        output += ""
                    else:
                        output += " " + numUkr[pos[0]*10]
            if len(pos) == 3:
                if pos[0]!=0:
                    if pos[1]!=0:
                        if pos[2]!=0:
                            if pos[1]==1:
                                output += " " + numUkr[pos[0]*100]+" "+numUkr[pos[1]*10+pos[2]]
                            elif pos[1]==0:
                                output += " " + numUkr[pos[0]*100]+" "+numUkr[pos[2]]
                            else:
                                output += " " + numUkr[pos[0]*100]+" "+numUkr[pos[1]*10]+" "+numUkr[pos[2]]
                        else:
                            if pos[1]==1:
                                output += " " + numUkr[pos[0]*100]+" "+numUkr[pos[1]*10]
                            elif pos[1]==0:
                                output += " " + numUkr[pos[0]*100]
                            else:
                                output += " " + numUkr[pos[0]*100]+" "+numUkr[pos[1]*10]
                    else:
                        if pos[2]!=0:
                            output += " " + numUkr[pos[0]*100]+" "+numUkr[pos[2]]
                        else:
                            output += " " + numUkr[pos[0]*100]
                else:
                    if pos[1]!=0:
                        if pos[2]!=0:
                            if pos[1]==1:
                                output += " " + numUkr[pos[1]*10+pos[2]]
                            elif pos[1]==0:
                                output += " " + numUkr[pos[2]]
                            else:
                                output += " " + numUkr[pos[1]*10]+" "+numUkr[pos[2]]
                        else:
                            if pos[1]==1:
                                output += " " + numUkr[pos[1]*10]
                            elif pos[1]==0:
                                output += ""
                            else:
                                output += " " + numUkr[pos[1]*10]
                    else:
                        if pos[2]!=0:
                            output += " " + numUkr[pos[2]]
                        else:
                            output += ""
        else:
            #если mass_flag[i]=="+"
            # output += "+++"
            # id1 = id(mass[last_position])
            # id2 = id(mass[-1])
            # p1 = mass[last_position]
            # p2 = mass[-1]
            if id(mass[last_position]) != id(mass[-1]):
                if len(pos)==1:
                    output+=" "+rodUkr[pos[0]]#####
                if len(pos)==2:
                    if pos[1]!=0:
                        if pos[0]==1:
                            output+=" "+rodUkr[pos[0]*10+pos[1]]
                        elif pos[0]==0:
                            output += " " +rodUkr[pos[1]]
                        else:
                            output += " " +rodUkr[pos[0]*10]+" "+rodUkr[pos[1]]
                    else:
                        if pos[0]==1:
                            output+=" "+rodUkr[pos[0]*10]
                        elif pos[0]==0:
                            output += " "
                        else:
                            output += " " +rodUkr[pos[0]*10]
                if len(pos)==3:
                    if pos[2]!=0:
                        if pos[1]!=0:
                            if pos[0]!=0:# есть все
                                if pos[1]==1:
                                    output+=" "+rodUkr[pos[0]*100]+endUkr[4]+" "+rodUkr[pos[1]*10+pos[2]]
                                else:
                                    output += " " + rodUkr[pos[0] * 100] +endUkr[4]+" "+ rodUkr[pos[1] * 10]+" " + rodUkr[pos[2]]

                            else:#нету первого
                                if pos[1] == 1:
                                    output += " " + rodUkr[pos[1] * 10 + pos[2]]
                                else:
                                    output += " " + rodUkr[pos[1] * 10] + " " + rodUkr[pos[2]]
                        else:#нету второго
                            if pos[0]!=0:
                                output+=" "+rodUkr[pos[0]*100]+endUkr[4]+" "+rodUkr[pos[2]]
                            else:
                                output += " " + rodUkr[pos[2]]
                    else:#нету последнего
                        if pos[1]!=0:
                            if pos[0]!=0:
                                output+=" "+rodUkr[pos[0]*100]+endUkr[4]+" "+rodUkr[pos[1]*10]
                            else:
                                output += " "+rodUkr[pos[1] * 10]
                        else:
                            if pos[0]!=0:
                                output += " " + rodUkr[pos[0] * 100]+endUkr[4]
                            else:
                                output+=""
            else:
                if len(pos)==3:
                    if pos[0]!=0:
                        if pos[1]!=0:
                            if pos[2]!=0:
                                if pos[1]==1:
                                    output+=" "+numUkr[pos[0]*100]+" "+placeUkr[pos[1]*10+pos[2]]
                                else:
                                    output += " " + numUkr[pos[0] * 100] + " "+ numUkr[pos[1] * 10] + " " + placeUkr[pos[2]]
                            else:
                                if pos[1]==1:
                                    output+=" "+numUkr[pos[0]*100]+" "+placeUkr[pos[1]*10]
                                else:
                                    output += " " + numUkr[pos[0] * 100] + " "+ placeUkr[pos[1] * 10]
                        else:
                            if pos[2]!=0:
                                output+=" "+numUkr[pos[0]*100]+" "+placeUkr[pos[2]]
                            else:
                                output+=" "+placeUkr[pos[0]*100]
                    else:
                        if pos[1]!=0:
                            if pos[2]!=0:
                                if pos[1]==1:
                                    output+=" "+placeUkr[pos[1]*10+pos[2]]
                                else:
                                    output += " " +numUkr[pos[1] * 10] + " " + placeUkr[pos[2]]
                            else:
                                if pos[1]==1:
                                    output+=" "+" "+placeUkr[pos[1]*10]
                                else:
                                    output += " " + " "+ placeUkr[pos[1] * 10]
                        else:
                            if pos[2]!=0:
                                output+=" "+" "+placeUkr[pos[2]]
                            else:
                                output+=""
        if i!=last_position:
            if dimU[i]=="":
                output+=" "+dimU[i]
            else:
                output += " " + dimU[i] + "ів"
        else:
            if id(mass[last_position]) != id(mass[-1]):
                output+=dimRU[i]

        # print("**"+output)



    return output[1:]
def getMassFlag(m):
    mass_flag = []
    for i in m:
        if i[0]=="0" and i[1]=="0" and i[2]=="0":
            mass_flag.append("+")
        else:
            mass_flag.append("-")
    return mass_flag

print("Input num")
inp = input()

def ready(number):
    count = len(number)
    nimb = int(number)
    n = []
    t = int(math.fmod(count,3))#количество цифр в самом старшем разряде
    if t !=0:
        n.append(number[0:t])
        number=number[t:]
        while len(number)>0:
            n.append(number[0:3])
            number = number[3:]
    else:
        while len(number)>0:
            n.append(number[0:3])
            number = number[3:]
    dimentionEng=[]
    dimentionGer=[]
    dimentionUkr=[]
    for i in range(0,len(n)):
        dimentionEng.append(dimEng[i])
        dimentionGer.append(dimGer[i])
        # dimentionUkr.append(dimUkr[i])
    dimentionEng.reverse()
    dimentionGer.reverse()
    # dimentionUkr.reverse()
    english=""
    german=""
    ukrainian=""
    k = 0
    for i in n:
        q = trip(i, id(i) == id(n[-1]))
        if q!="":
            english+=q +" "+dimentionEng[k]
        else:
            english+=q
        k+=1

    k=0
    for i in n:
        # print("*"+i)
        q = tripGer(i, id(i) == id(n[-1]))
        # print("**"+q)
        if q!="":
            if dimentionGer[k]!="":
                german+=q + " " + dimentionGer[k] + endGer[1] + " "
            else:
                german += q
        k+=1
    german=german[0:-1]
    if nimb>19:
        german+=endGer[5]
    else:
        german+=endGer[4]

    ukrainian = tripUkr(n)

    print("English : " + english)
    print("German : " + german)
    print("Ukrainian : " + ukrainian)


numb = inp
for i in operators:
    if inp.find(i)!=-1:
        if inp.find("^")!=-1:
            inp = inp.replace("^","**")
        numb = str(eval(inp))
        break
ready(numb)

