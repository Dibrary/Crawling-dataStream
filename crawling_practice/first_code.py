
html_doc = """
<!doctype html>
<html>
    <head>
        <title> 크롤링 첫번째 </title>
    </head>
    <body>
        <div>크롤링 하기 1</div>
        <div>크롤링 하기 2</div>
    </body>
</html>
"""

from bs4 import BeautifulSoup

bs_obj = BeautifulSoup(html_doc, "html.parser")
head = bs_obj.find("head") # html_doc이라는 객체를 html.parser를 통해 파싱한 것 중에 <head>태그부분 추출
print(head)


body = bs_obj.find("body")
print(body)
print("========================")
print(body.find("div"))
print(bs_obj.find("div"))
print("========================")
div_obj = bs_obj.find_all("div") # list로 가져온다.

for x in div_obj:
    print(x)
    print(x.text) # 해당 태그 내부의 글자만 가져온다.










