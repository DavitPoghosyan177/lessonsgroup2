#!/usr/bin/python3
import os
import xlsxwriter

def get_content(fname):
        with open(fname) as f:
                return f.readlines()

def check_file_existence(fname):
        if not os.path.isfile(fname):
                print("Input file does not exists. Please check")

def get_human(human_data):
        tmp = {}
        human_list = human_data.split()
        tmp['name'] = human_list[0].strip()
        tmp['surname'] = human_list[1].strip()
        tmp['age'] = int(human_list[2].strip())
        tmp['profession'] = human_list[3].strip()
        return tmp

def get_humans_list(ml):
        return [get_human(line) for line in ml if len(line) > 1]

def sort_by_criteria(humans, criteria):
        if criteria == "surname":
                humans.sort(key=lambda el: el["surname"])
        if criteria == "name":
                humans.sort(key=lambda el: el["name"])
        if criteria == "age":
                humans.sort(key=lambda el: el["age"])
        if criteria == "profession":
                humans.sort(key=lambda el: el["profession"])
        return humans

def write_into_xlsx(fname, content):
        row = 1
        column = 0
        wb = xlsxwriter.Workbook(fname)
        wsh = wb.add_worksheet()
        bold = wb.add_format({"bold":1})
        bold.set_bg_color("#FFFF00")
        wsh.write("A1" , "Name"  ,bold)
        wsh.write("B1" , "Surname" , bold)
        wsh.write("C1" , "Age" , bold)
        wsh.write("D1" ,"Profession" , bold)
        
        for human in content:
                wsh.write(row , column , human["name"] )
                wsh.write(row , column +1 , human["surname"])
                wsh.write(row , column +2 ,str(human["age"]))
                wsh.write(row , column +3 ,human["profession"])
                if human["age"] >= 35:
                        color1 = wb.add_format({"bg_color":"green"})
                        wsh.write(row , column , human["name"] , color1 )
                        wsh.write(row , column +1 , human["surname"],color1)
                        wsh.write(row , column +2 ,str(human["age"]),color1)
                        wsh.write(row , column +3 ,human["profession"],color1)
                row += 1
        wb.close()
                
def main():
        fname= "/home/davit/Desktop/humans_list"
        check_file_existence(fname)
        cnt = get_content(fname)
        humans_list = get_humans_list(cnt)
        criteria = input("""Please enter the criteria of sorting:
                                1. name
                                2. surname
                                3. age
                                4. profession
                        """)
        humans_list = sort_by_criteria(humans_list, criteria)
        write_into_xlsx("/home/davit/Desktop/humans.xlsx", humans_list)

main()
