import openpyxl
   
def get_hokenryo(salary):
    book=openpyxl.load_workbook("hokenryo.xlsx")
    sheet=book["埼玉"]

    for row in sheet .iter_rows(min_row=15, max_row=46):
        salary_min=row[2].value
        salary_max=row[4].value
        hokenryogaku=round(row[6].value,1)
        nenkingaku=row[10].value
        #print(salary_min,salary_max,hokenryogaku,nenkingaku)
        if salary>=salary_min and salary<salary_max:
            return hokenryogaku,nenkingaku
     
    hokenryo=None
    nenkin=None
    return hokenryo,nenkin

 