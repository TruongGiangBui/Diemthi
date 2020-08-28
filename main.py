import os
import pandas as pd

collumns=['code','Dia li','GDCD','Hoa hoc','KHTN','KHXH','Lich su','Ngoai ngu','Ngu van','Sinh hoc','Toan','Vat li']


def processingdata():
    listfile = []
    for root, dirs, files in os.walk("."):
        for filename in files:
            listfile.append(filename)
    listfile.remove('main.py')
    listfile.remove('result.csv')
    data = pd.DataFrame()
    for i in listfile:
        print(i)
        df = pd.read_csv('Điểm thi/' + i)
        df.columns = collumns
        df['A00'] = df['Toan'] + df['Vat li'] + df['Hoa hoc']
        df['A01'] = df['Toan'] + df['Vat li'] + df['Ngoai ngu']
        df['B00'] = df['Toan'] + df['Hoa hoc'] + df['Sinh hoc']
        df['C00'] = df['Ngu van'] + df['Lich su'] + df['Dia li']
        df['D01'] = df['Toan'] + df['Ngu van'] + df['Ngoai ngu']
        data = data.append(pd.DataFrame(df[['code', 'A00', 'A01', 'B00', 'C00', 'D01']]))

    data.to_csv('result.csv')

def search_index(data):
    print("Nhap so bao danh")
    code = input()
    print("Nhap to hop")
    tohop = input()

    data = data.sort_values(by=tohop, ascending=False, na_position='last')
    data = data.reset_index(drop=True)
    a = data[data['code'] == int(code)][tohop].iloc[0]

    index=data[data[tohop]==a].first_valid_index()
    print(index)
    # print('Thu hang cua ban la: ',index+1)

def count_student_above(data):
    print("Nhap to hop")
    tohop = input()
    print("Nhap diem")
    diem=input()
    a = data[data[tohop]>=float(diem)].count()[tohop]
    print('So nguoi diem tu ',diem,' tro len la: ',a)

data=pd.read_csv('result.csv')
while(True):
    print('(1) Kiem tra thu hang\n')
    print('(2) So nguoi diem cao hon ban\n')
    i = input()
    if i=='1':
        search_index(data)
    elif i=='2':
        count_student_above(data)
    else:
        break
