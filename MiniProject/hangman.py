# Module exists
try:
    import os
except (Exception, TypeError, AttributeError) as e:
    print("You dont have 'os' module:Install it")
    exit()
# Make questions form

def question_spl(fname):
    ques = fname.index("?")
    quesfull = fname[:ques]
    ans = fname[ques+1:]
    ans1 = ans.strip()
    return quesfull , ans1

# Check file existance
def check_file_existance(fname):
    os.path.isfile(fname)
    try:
        with open(fname) as f:
            for j in f.readlines():
                return j
                
    except OSError as err:
        print("OS error:" , err)
        exit()
def draw_hangman(chances):
    if chances == 0:
        print("________ ")
        print("|  | ")
        print("| ")
        print("| ")
        print("| ")
        print("| ")
    elif chances == 1:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| ")
        print("| ")
        print("| ")
    elif chances == 2:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /  ")
        print("| ")
        print("| ")
    elif chances == 3:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /| ")
        print("| ")
        print("| ")
    elif chances == 4:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /|\ ")
        print("| ")
        print("| ")
    elif chances == 5:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /|\ ")
        print("| / ")
        print("| ")
    elif chances == 6:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| /|\ ")
        print("| / \ ")
        print("| ")
def main():
    cnt = 0
    content = check_file_existance("hangman_ques.txt")
    quest = question_spl(content)
    print(quest[0])
    ans = quest[1]
    c = "-"*(len(ans))
    while True:
        if c == ans:
            print("You WIN")
            break
        b = input("Enter a letter: ")
        if b not in ans:
            cnt +=1
        for j in range(len(ans)):
            if ans[j] == b:
                c = c[:j] + b + c[j+1:]
        draw_hangman(cnt)
        if cnt == 6:
            print("You Lose try again::")
            break
        print(c)
main()
