
staff_map={
    "motoki":{
        "rank":"topstylist",
        "position":"店長"

    },
    "ryo":{
        "rank":"jrstylist",
        "position":"無"
        
    },
    "aya":{
        "rank":"topstylist",
        "position":"manager"

    },
    "miku":{
        "rank":"facialist",
        "position":"無"

    },
    "ren":{
        "rank":"asistant",
        "position":"無"
    },
    "airi":{
        "rank":"stylist",
        "position":"無"
    },
    "kota":{
        "rank":"無",
        "position":"owner",

    }


}
for name,value in staff_map.items():
    rank=value["rank"]
    position=value["position"]

    if rank=="asistant":
        rankkyu=0,
    elif rank=="jrstylist":
        rankkyu=20000,
    elif rank=="stylist":
        rankkyu=20000,   
    elif rank=="topstylist":
        rankkyu=30000,
    elif rank=="direcotor":
        rankkyu=50000,
    elif rank=="facialist":
        rankkyu=20000,  
    if position=="店長":
        positionkyu=50000
    elif position=="無":
        positionkyu=0
    elif position=="manager":
        positionkyu=50000,
           
    print(name,"ランク",rankkyu,"役職手当",positionkyu)    
