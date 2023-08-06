#1
def mysum(*args):
    num = 0
    for i in args:
        if type(i) == int or type(i) == float:
            num += i
    return num
print(mysum(1 , 2 , "hello" , 4 , "5"))

#2
def lenstring(*args):
    cnt = 0
    for i in args:
        if type(i) == str:
            cnt+=1
    return cnt
print(lenstring(1 , "hello" , "World" ,"5" , "55" , 5))

#3
def middlesum(*args):
    d = 0
    d1 = 0
    for i in args:
        if type(i) == int or type(i) == float:
            d += i
            d1 += 1            
    return d / d1
print(middlesum(1 , 2 , 3.2, "h"))


#4
def main(num1 , num2):
    suma = num1 + num2
    mul = num1 * num2
    if num1 >= num2:
        print("divison: " , num1 / num2)
    else:
        print("divison: " , num2 / num1)
    if num1 >= num2:
        print("deduction: " , num1 - num2)
    else:
        print("deduction: " , num2 - num1)
    print("sum: " , suma)
    print("multiplication: " , mul)
main(2 , 8)

#5
def myupper(mstr):
    swapstr = ""
    for i in range(len(mstr)):
        if 122 >= ord(mstr[i]) >= 97:
            swapstr += chr(ord(mstr[i])-32)
        elif 90 >= ord(mstr[i]) >= 65:
            swapstr += chr(ord(mstr[i]))
    for j in range(len(mstr)):
        if " " in mstr[j]:
            return (swapstr[:j:] + " " + swapstr[j::])
            exit()
    return (swapstr)
print(myupper(mstr = "hello world"))
    
#6
def mylow(mstr):
    swapstr = ""
    for i in range(len(mstr)):
        if 122 >= ord(mstr[i]) >= 97:
            swapstr += chr(ord(mstr[i]))
        elif 90 >= ord(mstr[i]) >= 65:
            swapstr += chr(ord(mstr[i])+32)
    for j in range(len(mstr)):
        if " " in mstr[j]:
            return (swapstr[:j:] + " " + swapstr[j::])
            exit()
    return (swapstr)
print(mylow(mstr = "hELLo world"))

#7
def mytitle(mstr):
    for i in range(len(mstr)):
        if mstr[i] == " ":
            if 122 >= ord(mstr[i+1]) >= 97:
                ordlet = ord(mstr[i+1]) - 32
                mstr = mstr[:i+1] + chr(ordlet)+ mstr[i+2:]
    return mstr[1:]
print(mytitle(mstr = " " + "hello world"))

#8
def myrev(mstr):
    return mstr[::-1]
print(myrev("Hello world"))

#9
def indexing_string(mstr, number1 ,number2):
    if type(number1) == int and type(number2) == int: 
        return mstr[number1:number2+1]
print(indexing_string("hello" , 1,3))

#10
def my_longest_word(mstr):
    long = ""
    for i in mstr.split():
        if len(i) > len(long):
            long = i
    return long
print(my_longest_word("hello myyyyy good world"))

#11
def string_most_letter(mstr):
    md = {}
    for i in mstr:
        if i in md:
            md[i] += 1
        else:
            md[i] = 1
    return max(md , key = md.get)
print(string_most_letter("hello wwwworld"))

#12
def string_long_word_most_letter(mstr):
    long = ""
    md = {}
    for i in mstr.split():
        if len(i) > len(long):
            long = i
    for i in long:
        if i in md:
            md[i] += 1
        else:
            md[i] = 1
    return max(md , key = md.get)
print(string_long_word_most_letter("hello worldddd hhhhh"))

#13
def indexing_start(mstr , ind):
    if type(ind) == int:
        return mstr[ind] , mstr[-ind]
print(indexing_start(("hello world") , 2))

#15
def is_polindrom(number):
    nnum = str(number)
    if nnum == nnum[::-1]:
        return True
    else:
        return False
#16


#17
def mymulti(num):
    if type(num) == int:
        num = str(num)
        first = int(num[0])
        last = int(num[-1])
        multi = first * last
    return multi
print(mymulti(526))

#18
def list_string_cnt(ml):
    cnt = 0
    for i in ml:
        if type(i) == str:
            cnt += 1
    return cnt
print(list_string_cnt(["hello" , "world" , "22" , 5 , 45 , [4]]))

#19  
def largest_number(ml):
    nml = []
    for i in ml:
        if type(i) == int:
            nml.append(i)
            nml.sort()
    return nml[-1]
print(largest_number([1 , 2 , 7 , "Hello" , "55" , 177 , 455]))

#20
def even_doubleDigit(ml):
    nml = []
    for i in ml:
        if type(i) == int and (2 <= len(str(i)) <=2) and i % 2 == 0:
            nml.append(i)
    return nml
print(even_doubleDigit([1 , 2 , 11 , "Hello" , "55" , 12 , 455 , 452 , 28]))

#21
def my_middleing_list(ml):
    d = 0
    c = 0
    for i in ml:
        if type(i) == int or type(i) == float:
            d += i
            c += 1
    return d / c

print(my_middleing_list([1 , 2 , 3 ,4 , "hello" , "7"]))

#22
def string_lenght(ml):
    nml = []
    for i in ml:
        if type(i) == str:
            nml.append(len(i))
    return nml
print(string_lenght(["hello" , "12" , 4 , 5 , "177"]))

#23
def number_lowing(ml):
    nml = []
    for i in ml:
        if type(i) == int or type(i) == float:
            nml.append(i)
            nml.sort()
            nml.reverse()
    return nml
print(number_lowing(["hello" , 1 , 2 , 5 , 177 , "25"]))

#24
def number_lowing(ml):
    nml = []
    for i in ml:
        if type(i) == str:
            nml.append(i)
            nml.sort(key = len)
            nml.reverse()
    return nml
print(number_lowing(["hello" , 1 , 2 , 5 , 177 , "25" , "good world", "lenght"]))

#25
def vowel_scanner(ml):
    vow = "AaEeIiOoUu"
    st = ''
    mlen = 0
    for i in ml:
        if type(i) == str:
            vlen = len([el for el in i if el in vow])

            if vlen > mlen:
                mlen = vlen
                st = i
    return str(st)
print(vowel_scanner(["hello" , "this" , "aei" , 5]))

#26
def string_most_word(ml):
    nml = []
    for i in ml:
        if type(i) == str:
            nml.append(i)
            nml.sort(key = len)
    return  nml[-1]
print(string_most_word(["hello this beatuiful world" , "good night everybody" , "122" , 25]))

#27
import re
def sum_number_inString(mstr):
    num = re.findall("\d+" , mstr)
    num= map(int, num)
    return max(num)
print(sum_number_inString("hello this 177 12 , 544"))
