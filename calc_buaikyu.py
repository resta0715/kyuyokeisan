
staff_map={
    "moto":{
        "buai":0.2,
        "uriage":100000,
    },
    "ryo":{
        "buai":0.05,
        "uriage":200000,
    },
    "aya":{
        "buai":0.1,
        "uriage":50000,
    },
    "miku":{
        "buai":0.15,
        "uriage":350000,
    },

}

for name,value in staff_map.items():
    
    buai=value["buai"]
    uriage=value["uriage"]
    
    if name=="moto"or name=="ryo":
        buaikyuu=buai*uriage
    else:
        buaikyuu=0
    print(name,"売上金額",uriage,"歩合率",buai,"歩合給",buaikyuu)

