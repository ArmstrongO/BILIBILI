import requests


date_pass=""
def login():
    global date_pass
    url="https://chat.rj.run/test/api/v1/auth/captcha"
    date={
        "mobile":"18000000099"
    }
    res=requests.post(url=url,json=date)
    print ( res.text )
    date_pass=res.json()['date']
    # assert res.status_code == 200
    print(date_pass)

