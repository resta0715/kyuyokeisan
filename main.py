staff_map={
    "motoki":{
        "buai":0.2,
        "uriage":100000,
        "working_status":"月給",
        "rank":"topstylist",
        "position":"店長"

    },
    "ryo":{
        "buai":0.05,
        "uriage":200000,
        "working_status":"月給",
        "rank":"jrstylist",
        "position":"無"

    },
    "aya":{
        "buai":0.1,
        "uriage":50000,
        "working_status":"役員報酬",
        "rank":"topstylist",
        "position":"manager"

    },
    "miku":{
        "buai":0.15,
        "uriage":350000,
        "working_status":"時給",
        "rank":"無",
        "position":"無",
        "time":120,
        "zikyu":960

    },
    "ren":{
        "buai":0.1,
        "uriage":10000,
        "working_status":"月給",
        "rank":"asistant",
        "position":"無"

    },
    "airi":{
        "buai":0.1,
        "uriage":200000,
        "working_status":"月給",
        "rank":"stylist",
        "position":"無",
        
    },
    "kota":{
        "buai":0,
        "uriage":200000,
        "working_status":"役員報酬",
        "rank":None,
        "position":"owner",


    }

}

def calc_zikyu(staff_data):
    zikyu=staff_data["zikyu"]
    time=staff_data["time"]
    zikyukyuyo=zikyu*time
    return zikyukyuyo

def calc_kihonkyu(kihonkyu1,kihonkyu2):
    kihonkyu=kihonkyu1*kihonkyu2
    return kihonkyu

def calc_buaikyu(staff_data):
    buai=staff_data["buai"]
    uriage=staff_data["uriage"]
    buaikyu=buai*uriage
    return buaikyu
 
def calc_rankkyu(staff_data):
    rank=staff_data["rank"]
    if rank=="asistant":
        rankkyu=0
    elif rank=="jrstylist":
        rankkyu=20000
    elif rank=="stylist":
        rankkyu=20000   
    elif rank=="topstylist":
        rankkyu=30000
    elif rank=="direcotor":
        rankkyu=50000
    elif rank=="facialist":
        rankkyu=20000  
    else:
        rankkyu=0    
    return rankkyu


def calc_positionkyu(staff_data):
    position=staff_data["position"]
    if position=="店長":
        positionkyu=50000
    elif position=="無":
        positionkyu=0
    elif position=="manager":
        positionkyu=50000
    elif position=="owner":
        positionkyu=50000
       
    return positionkyu
    


def calc_gekyu(staff_data):
    kihonkyu1=450000
    kihonkyu2=0.45
    kihonkyu=calc_kihonkyu(kihonkyu1,kihonkyu2)
    buaikyu=calc_buaikyu(staff_data)
    rankkyu=calc_rankkyu(staff_data)
    positionkyu=calc_positionkyu(staff_data)
    salary=kihonkyu+buaikyu+rankkyu+positionkyu
    return salary



def calc_salary(staff_data):
    if staff_data["working_status"]=="時給":
        salary=calc_zikyu(staff_data)
    else:
        salary=calc_gekyu(staff_data)
    return salary 

sum_salary=0

for name in staff_map:
    sd=staff_map[name]
    salary=calc_salary(sd)
    sum_salary=sum_salary+salary
    #sum_salary+=salary
    print(name,salary)
    
print(sum_salary)




