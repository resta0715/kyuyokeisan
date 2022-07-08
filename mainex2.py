from msilib.schema import Error
import openpyxl
import math


def calc_total_salary_hour(resta_data):
    time=resta_data["time"]
    zikyu=resta_data["zikyu"]
    total_salary_hour=time*zikyu
    return total_salary_hour


def calc_percentage(resta_data):
    resta_service_sale=resta_data["resta_service_sale"]
    staff_number=resta_data["staff_number"]
    productivity=resta_service_sale/staff_number

    if productivity<500000:
        percentage=0.05
    
    elif 500000<=productivity and productivity<600000:
        percentage=0.06
    
    elif 600000<=productivity and productivity<700000:
        percentage=0.07

    elif 700000<=productivity and productivity<800000:
        percentage=0.08

    elif 800000<=productivity and productivity<900000:
        percentage=0.09

    elif 900000<=productivity and productivity<1000000:
        percentage=0.1

    elif 1000000<=productivity and productivity<1100000:
        percentage=0.11

    elif 1100000<=productivity:
        percentage=0.12   

    else:
        percentage=None
    
    return percentage


def calc_per_salary(resta_data):
    service_sale=resta_data["service_sale"]
    percentage=calc_percentage(resta_data)
    
    per_salary=service_sale*percentage

    return per_salary


def calc_basic_salary(basic_salary1,basic_salary2):
    basic_salary=basic_salary1*basic_salary2
    return basic_salary


def calc_position_salary(resta_data):
    position=resta_data["position"]
    if position=="店長":
         position_salary=50000
    
    elif position=="manager":
        position_salary=50000
    
    elif position=="owner":
        position_salary=80000
    
    else:
        position_salary=0

    return position_salary


def calc_rank_salary(resta_data):
    rank=resta_data["rank"]
    if rank=="asistant":
        rank_salary=0
    
    elif rank=="stylist":
        rank_salary=5000
    
    elif rank=="topstylist":
        rank_salary=30000

    
    elif rank=="focialist":
        rank_salary=50000
    
    else:
        rank_salary=0
    
    return rank_salary

    

def calc_total_salary(resta_data):
    basic_salary1=450000
    basic_salary2=0.45
    position_salary=calc_position_salary(resta_data)
    per_salary=calc_per_salary(resta_data)
    rank_salary=calc_rank_salary(resta_data)
    basic_salary=calc_basic_salary(basic_salary1,basic_salary2)
    total_salary=basic_salary+per_salary+rank_salary+position_salary

    return total_salary

def calc_salary(resta_data):
    if resta_data["working_status"]=="hour":
        salary=calc_total_salary_hour(resta_data)
    
    else:
        salary=calc_total_salary(resta_data)
    
    return salary

def get_staff_map():
    book = openpyxl.load_workbook("staff_list.xlsx")
    print(len(book.sheetnames))
    sheet=book.get_sheet_by_name('Sheet1')
    resta_data={}
    
    for row in sheet.rows:
        name=row[0].value
        if name=="名前" or name==None:
            continue
        sd={
            "name":row[0].value,
            "working_status":row[2].value,
            "rank":row[3].value,
            "position":row[4].value,
            "hire_date":row[5].value,
            "time":row[6].value,
            "zikyu":row[7].value,
            "parking":row[8].value,
            "社会保険":row[9].value,
            "雇用保険":row[10].value,
            "service_sale":row[11].value,
            "product_sale":row[12].value,
            "resta_service_sale":row[13].value,
            "staff_number":row[14].value

        }
        resta_data[name]=sd
    return resta_data 

def calc_koyohoken(salary):
    koyohoken=salary*0.003
    
    a=int(koyohoken)
    b=koyohoken-int(koyohoken)

  
    if b<=0.5:
        b=0
    if 0.5<b:
        b=1
    
    koyohoken=a+b
    print(koyohoken)



   
    #少数部を取り出す
    #　0.5以下はきりすて、0.5より大きかったら繰り上げ
 



sum_salary=0
resta_data=get_staff_map()



for name in resta_data:
    sd=resta_data[name]
    rank=sd["rank"]
    #rank=resta_data[name]["rank"]  
    salary=calc_salary(sd)

    koyohoken=salary*0.003

    print(name,salary,round(koyohoken))



