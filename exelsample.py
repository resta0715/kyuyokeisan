import openpyxl
book = openpyxl.load_workbook("staff_list.xlsx")
print(len(book.sheetnames))
sheet=book.get_sheet_by_name('Sheet1')
resta_data={}
#i=0
for row in sheet.rows:
    #i+=1
    # 一行目を読み飛ばす
    #if i==1:
       # continue
    
    #print(row)
  
    name=row[0].value
    if name=="名前" or name==None:
        continue
    
    sd={
        "name":row[0].value,
        "working_status":row[1].value,
        "rank":row[2].value,
        "position":row[3].value,
        "hire_date":row[4].value,
        "time":row[5].value,
        "zikyu":row[6].value,
        "parking":row[7].value,
        "社会保険":row[8].value,
        "雇用保険":row[9].value,
        "service_sale":row[10].value,
        "product_sale":row[11].value

    }
    resta_data[name]=sd
    print(sd)

print(resta_data)