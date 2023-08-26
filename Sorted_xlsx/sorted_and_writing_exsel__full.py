try:
    import os
except ImportError:
    print("Please download os module:")
try:
    import xlsxwriter
except ImportError:
    print("Please download xlsxwriter module:")
try:
    import argparse
except ImportError:
    print("Please download argparse module:")

def check_file_existence(fname):
    os.path.isfile(fname)
    try:
        with open(fname) as f:
                return f.readlines()
    except OSError as err:
        print("OS error:", err)
        exit()
    except ValueError:
        print("Could not convert data to an integer.")
        exit()
    except Exception as err:
        print("Exception")        
        exit()

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
        if criteria == "name" :
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
        wsh.set_column(0, 1, 15)
        wsh.set_column(0, 3, 15)

        
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
        parser = argparse.ArgumentParser()
        parser.add_argument('-i','--input',help='enter input filename')
        parser.add_argument('-o','--output',help='enter output filename')
        parser.add_argument('-so','--sort_option',default='name',
                help='enter sort option:name,surname,age,profession')
        args = parser.parse_args()
        input1=args.input
        output1=args.output
        sortop=args.sort_option
        fname= input1
        checkf=check_file_existence(fname)
        humans_list = get_humans_list(checkf)
        humans_list = sort_by_criteria(humans_list, sortop)
        write_into_xlsx(output1, humans_list)

main()
