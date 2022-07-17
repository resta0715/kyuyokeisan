import csv

def get_uriage():
    with open("uriage2022_7.csv") as f:
        reader = csv.DictReader(f)

        uriage={}
        for row in reader:

            name=row["スタイリスト名"]
            kozinuriage={
                "総売上_内訳_技術":row["総売上_内訳_技術"],
                "総売上_内訳_店販":row["総売上_内訳_店販"],
                "総売上_内訳_オプション":row["総売上_内訳_オプション"]
            }
            uriage[name]=kozinuriage
        return uriage

