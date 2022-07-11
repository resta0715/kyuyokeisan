import openpyxl


   
def get_hokenryo(salary):
    book=openpyxl.load_workbook("hokenryo.xlsx")
    
    sheet=book["埼玉"]

    for row in sheet .iter_rows(min_row=15, max_row=46):
    
        salary_min=row[2].value
        salary_max=row[4].value
        hokenryogaku=round(row[6].value,1)
        nenkingaku=row[10].value
        if salary>=salary_min and salary<salary_max:
            return hokenryogaku,nenkingaku

        print(salary_min,salary_max,hokenryogaku,nenkingaku)

    hokenryo=0
    nenkin=0
    return hokenryo,nenkin

    
hokenryo,nenkin=get_hokenryo(300000) 
print(hokenryo,nenkin)  