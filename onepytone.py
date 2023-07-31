#title
def mytitle(mstr):
    for i in range(len(mstr)):
        if mstr[i] == " ":
            if 122 >= ord(mstr[i+1]) >= 97:
                ordlet = ord(mstr[i+1]) - 32
                mstr = mstr[:i+1] + chr(ordlet)+ mstr[i+2:]
    return mstr[1:]
print(mytitle(mstr = " " + input("Enter your string: ")))

#Swapcase

def myswap(mstr):
    swapstr = ""
    for i in range(len(mstr)):
        if 122 >= ord(mstr[i]) >= 97:
            swapstr += chr(ord(mstr[i]) - 32)
        elif 90 >= ord(mstr[i]) >= 65:
            swapstr += chr(ord(mstr[i]) + 32)
    for j in range(len(mstr)):
        if " " in mstr[j]:
            return (swapstr[:j] + " " + swapstr[j:])
            exit()
    return (swapstr)
print(myswap(mstr = input("Enter your string: ")))

#lower
def mylow(mstr):
    swapstr = ""
    for i in range(len(mstr)):
        if 122 >= ord(mstr[i]) >= 97:
            swapstr += chr(ord(mstr[i]))
        elif 90 >= ord(mstr[i]) >= 65:
            swapstr += chr(ord(mstr[i]) + 32)
    for j in range(len(mstr)):
        if " " in mstr[j]:
            return (swapstr[:j] + " " + swapstr[j:])
            exit()
    return (swapstr)
print(mylow(mstr = input("Enter your string: ")))
        
#capitalize

def mycap(mstr):
    swapstr = ""
    if 122 >= ord(mstr[0]) >= 97:
        swapstr += chr(ord(mstr[0]) -32 )
    elif 90 >= ord(mstr[0]) >= 65:
        swapstr += chr(ord(mstr[0]))
            
    return (swapstr + mstr[1:])
print(mycap(mstr = input("Enter your string: ")))

#count
def mycnt(mstr , let):
    cnt = 0
    for i in mstr:
        if i == let:
            cnt += 1
        else:
            continue
    return (cnt)
print(mycnt(mstr = input("Enter your string: "),let = input("Enter letter: ")))

#index
def myix(mstr , let):
    for i in range(len(mstr)):
        if mstr[i] == let[0]:
            return i
            break
        else:
            continue
print(myix(mstr = input("Enter your string: ") ,let = input("Enter letter: ")))