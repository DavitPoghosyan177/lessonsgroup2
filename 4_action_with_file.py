import os.path
def check_file_existence(fname):
	if not os.path.isfile(fname):
		print("Your files does not exists: %s. Please check" %fname)
		return False
	return True
def get_info_about(fname):
    with open(fname) as f:
        return f.readlines()
def count_symbols(a):
    md = {}
    for el in a:
        for j in el:
            if j in md:
                md[j] += 1
            else:
                md[j] = 1
    return md
def the_longest_word(b):
    st = ""
    for i in b:
        for j in i.split():
            if len(j) > len(st):
                st = j
    return st
def get_test_with_words_reversed(a):
	ml = []
	for i in a:
		for j in i.split():
			ml.append(j[::-1])
	return " ".join(ml)

def get_sentences_cnt(a):
	cnt = 0
	for i in a:
		for j in i:
			if "." == j:
				cnt += 1
	return cnt
def write_into_file(fname , info):
	with open(fname , "a") as f:
            f.write(str(info)+"\n")


def main():
    about_info = "/home/davit/Desktop/about.txt"
    write_exsercise = "/home/davit/Desktop/write_into_file.txt"
    fl = check_file_existence(about_info)
    if not fl:
        exit()
    content = get_info_about(about_info)
    if os.path.exists(write_exsercise):
        os.remove(write_exsercise)
    write_into_file(write_exsercise, count_symbols(content))
    write_into_file(write_exsercise, the_longest_word(content))
    write_into_file(write_exsercise, get_test_with_words_reversed(content))
    write_into_file(write_exsercise, get_sentences_cnt(content))


main()
