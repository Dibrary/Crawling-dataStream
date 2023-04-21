
from bs4 import BeautifulSoup

html_doc = """
<!doctype html>
<html>
<head>
    <title>기초 웹 크롤링</title>
</head>

<body>
<table border="1">
    <caption>과일가격</caption>
    <tr>
        <th>상품</th>
        <th>가격</th>
    </tr>
    <tr>
        <th>오렌지</th>
        <th>100</th>
    </tr>
    <tr>
        <th>사과</th>
        <th>250</th>
    </tr>
</table>
<table border="2">
    <caption>옷가격</caption>
    <tr>
        <th>상품</th>
        <th>가격</th>
    </tr>
    <tr>
        <th>셔츠</th>
        <th>30000</th>
    </tr>
    <tr>
        <th>바지</th>
        <th>50000</th>
    </tr>
</table>
</body>
</html>
"""

bs_obj = BeautifulSoup(html_doc, "html.parser")
all = bs_obj.find_all("table")
print(all)

clothes = bs_obj.find_all("table", {"border":"2"}) # 그냥 table만 적으면 table이 모두 나옴
# 위 코드는 table 중에 border가 2인 것을 가져온다.
print(clothes)

'''
즉 이런 식으로 같은 태그를 쓰는 게 여러 개인 경우

속성을 사용해서 원하는 것만 가져올 수 있다는 것
'''