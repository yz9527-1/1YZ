
import requests
import json,string,random,sys


for i in range(0,2):
    a = ''.join(random.sample(string.digits, 8))
    b = "测试%d"%(i)
    #c= b.decode('unicode_escape')
    #print(c)
    url = "http://192.168.0.223:8030/api/UserCard/adduser"
    payload = {"userId":0,"userName":b,"name":b,"cardType":"00","workNum":a,"label":"","cardNum":a}
    headers = {
      'token': 'nEPt3+qHubZH9Vf0K+V7Prv+YVcQeFXznX++/oOU2WQdrnr89U1WGFLmtd/DZIwq4vGHOQYuSzEUlpcRXS8jKWTu0wserGYviN5rtY/ThgGn3LsBSpzwhZeaOgdIlt/NlvGVgTQvMVXDea89stRNbIg67/ca015wqvW4HtMHToXwcPDs03wIxQH88qBstb+M6TblTqD9TwESieFEg02Z8Gfz9i+aSgMYZOoCiUUbaffS3evl7cTWJMY1vXHV+VYg8nZSVK3/4T+0H+n9rmnyf2n1qQAWEG6/DxQAt/ZO2Iq7cMuqBzHoQmF1ZugfzMYn5HPWsGVU8DNqplAa4n5yYX5G8SqnDry/lyJ2YSgT5CXVWFEKNI6B84pPwp9baSWSe1OuuoFJUg6ns2j7wzXP84AFRK8jQl9ktFGo0s7WjUZWH8+HyzE2fJkoxbw8qkxbpiED98F7B5NJ9OMPYo2qpWbxpMbm+3bjhB/WwnsSuG/3ZC62CBTYdv+ulv9X3MNZmfU6ksBZGYu7+uHUWiSHcOnZOEnX4N+Z3GWaMxrstPkotSO0IH8VWA==',
      'Content-Type': 'application/json;charset=UTF-8'
    }
    a=+1
    response=requests.post(url, headers=headers, data = json.dumps(payload,ensure_ascii=False).encode())
    print(response.text)
