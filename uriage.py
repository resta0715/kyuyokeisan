import csv
def get_uriage(file_name):
    with open(file_name) as f:
        reader = csv.DictReader(f)
       
        uriage_data={}
        for row in reader:
            name=row.get("スタイリスト名") or row.get("スタッフ名")
            print(name)
            ku={
                "service_sale":int(row.get("総売上_内訳_技術") or row.get("総売上_内訳_施術")),
                "product_sale":int(row["総売上_内訳_店販"]),
                "option_sale":int(row["総売上_内訳_オプション"])
             
            }
            uriage_data[name]=ku
        return uriage_data
        

                       
            
  