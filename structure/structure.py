from bs4 import BeautifulSoup

html = '''
<table>
    <tr>
        <th>A사</th>
        <th>B사</th>
        <th>C사</th>
    </tr>
    <tr>
        <td>서울</td>
        <td>강원도</td>
        <td>부산</td>
    </tr>
    <tr>
        <td>30명</td>
        <td>55명</td>
        <td>200명</td>
    </tr>
    <tr>
        <td>02-2345-2323</td>
        <td>033-223-2323</td>
        <td>051-121-1212</td>
    </tr>
    <tr>
        <td>a@a.com</td>
        <td>b@b.com</td>
        <td>c@c.com</td>
    </tr>
</table>
'''

soup = BeautifulSoup(html, 'html.parser')
# print(soup)
overall = {}
json = {}

company_name = []
theads = soup.select('tr th')
for head in theads:
    company_name_ = head.text
    company_name.append(company_name_)

addr = soup.select('tr:nth-of-type(2)')

address = []
for n in addr:
    tds = n.select('td')
    for td in tds:
        aa = td.text
        address.append(aa)
    print(address)

mem = soup.select('tr:nth-of-type(3)')

member = []
for n in mem:
    tds = n.select('td')
    for td in tds:
        aa = td.text
        member.append(aa)
    print(member)

tel = soup.select('tr:nth-of-type(4)')

telephone = []
for n in tel:
    tds = n.select('td')
    for td in tds:
        aa = td.text
        telephone.append(aa)
    print(telephone)


small_json = {}
small_json[company_name[0]] = address[0]
small_json[company_name[1]] = address[1]
small_json[company_name[2]] = address[2]
json['address']= small_json

small_json2 = {}
small_json2[company_name[0]] = member[0]
small_json2[company_name[1]] = member[1]
small_json2[company_name[2]] = member[2]
json['member'] = small_json2

small_json3 = {}
small_json3[company_name[0]] = telephone[0]
small_json3[company_name[1]] = telephone[1]
small_json[company_name[2]] = telephone[2]
json['telephone'] = small_json3


lst = []
lst.append(json)
overall['Row']=lst

print(json)

print(lst)

print(overall)

