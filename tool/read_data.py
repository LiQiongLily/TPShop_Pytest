
import yaml

with open("../data/login_data.yaml","r",encoding="utf-8")as f:
    d=yaml.load(f)
    arr=[]
    for data in d.values():
        arr.append((data.get("username"),
                    data.get("pwd"),
                    data.get("code"),
                    data.get("login_success")))
    print(arr)

