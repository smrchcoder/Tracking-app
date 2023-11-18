import requests
BASE="http://127.0.0.1:5000/"
data=[{"name":"test","likes":10,"views":20},{"name":"test1","likes":10,"views":20}]
for i in range(len(data)):
    response=requests.post(BASE+"video/"+str(i),data[i])
    print(response.json())
requests.delete(BASE+"video/0")
print(response)
print(response.json())