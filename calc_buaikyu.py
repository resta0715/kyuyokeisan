buai_list=[0.2,0.05,0.1,0.15]
uriage_list=[100000,200000,50000,350000]
for i in range(4):
    buai=buai_list[i]
    uriage=uriage_list[i]
    buaikyuu=buai*uriage
    print("売上金額",uriage,"歩合率",buai,"歩合給",buaikyuu)

