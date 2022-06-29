staff_map={
    "motoki":{
        "buai":0.2,
        "uriage":100000,
        "working_status":"月給",
        "time":200,
        "zikyu":0


    },
    "ryo":{
        "buai":0.05,
        "uriage":200000,
        "working_status":"月給",
        "time":150,
        "zikyu":0
    

    },
    "aya":{
        "buai":0.1,
        "uriage":50000,
        "working_status":"役員報酬",
        "time":250,
        "zikyu":0


    },
    "miku":{
        "buai":0.15,
        "uriage":350000,
        "working_status":"時給",
        "time":120,
        "zikyu":960
    },
    "ren":{
        "buai":0.1,
        "uriage":10000,
        "working_status":"月給",
        "time":160,
        "zikyu":0

    },
    "airi":{
        "buai":0.1,
        "uriage":200000,
        "working_status":"月給",
        "time":130,
        "zikyu":0
        
    },
    "kota":{
        "buai":0,
        "uriage":200000,
        "working_status":"役員報酬",
        "time":0,
        "zikyu":0


    }

}

for name,value in staff_map.items():
    zikyu=value["zikyu"]
    time=value["time"]
    working_status=value["working_status"]
    zikyukyuyo=zikyu*time

    if "working_status"=="時給":
        zikyukyuyo=zikyu*time


    print(zikyukyuyo)


