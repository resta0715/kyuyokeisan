import openpyxl
  

def get_gensen(salary,resta_data):
    book=openpyxl.load_workbook("gensen2022.xlsx")
    sheet=book["月額表"]
    fuyosu=resta_data["扶養人数"]
      
    for row in sheet.iter_rows(min_row=10,max_row=302):
        salary_min=row[1].value
        salary_max=row[2].value
        gensenfuyo0=row[3].value
        gensenfuyo1=row[4].value
        gensenfuyo2=row[5].value
        gensenfuyo3=row[6].value
        gensenfuyo4=row[7].value
        gensenfuyo乙=row[11].value
        if salary_min==None:
            continue
             
        if salary>=salary_min and salary<salary_max:
            if fuyosu=="乙":
                return gensenfuyo乙
            elif fuyosu==0:
                return gensenfuyo0
            elif fuyosu==1:
                return gensenfuyo1
            elif fuyosu==2:
                return gensenfuyo2
            elif fuyosu==3:
                return gensenfuyo3
            elif fuyosu==4:
                return gensenfuyo4 
            else:
                return None    
    
         
    return None




    




