
from urllib.request import urlopen

url = "https://ai-dev.tistory.com"
html = urlopen(url)
result = html.read()
print(result)
print(len(result), type(result)) # 타입은 bytes다.

# 엄청난 길이로 html이 표현된다. 18222

result_string = result.decode('utf-8')
temp = ''
for x in result_string:
    if x != ' ':
        temp += x
print(temp) # 우선 이렇게 하면 싹 다 볼 수 있다. (안깔끔)

