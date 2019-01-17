from bs4 import BeautifulSoup
from pprint import pprint

html = html = '''
<table>
    <tr>
        <th>회사</th>
        <th>A사</th>
        <th>B사</th>
        <th>C사</th>
    </tr>
    <tr>
        <th>주소</th>
        <td>서울</td>
        <td>강원도</td>
        <td>부산</td>
    </tr>
    <tr>
        <th>직원수</th>
        <td>30명</td>
        <td>55명</td>
        <td>200명</td>
    </tr>
    <tr>
        <th>전화번호</th>
        <td>02-2345-2323</td>
        <td>033-223-2323</td>
        <td>051-121-1212</td>
    </tr>
    <tr>
        <th>대표메일</th>
        <td>a@a.com</td>
        <td>b@b.com</td>
        <td>c@c.com</td>
    </tr>
</table>
'''


soup = BeautifulSoup(html, 'html.parser')
json = {}

# ------------------------------------------------------------column명 구하기------------------------------------------------------------
trs = soup.select('tr')
heads = []
for tr in trs:
    a = tr.select_one('th:nth-of-type(1)').text
    heads.append(a)


# ------------------------------------------------------------회사 이름 구하기------------------------------------------------------------
names = soup.select('tr:nth-of-type(1) th')
company_name = []
for i in range(1, len(names)):
    name = names[i].text
    company_name.append(name)
# print(company_name)

     
# ------------------------------------------------------------주소 구하기------------------------------------------------------------
address = soup.select("tr:nth-of-type(2) td")
addr = []
for i in range(len(address)):
    addrs = address[i].text
    addr.append(addrs)
# print(addr)

json_1 = {}
for k in range(len(addr)):    
    json_1[company_name[k]] = addr[k]

json[heads[1]]= json_1



# ------------------------------------------------------------직원수 구하기------------------------------------------------------------
members = soup.select("tr:nth-of-type(3) td")
member = []
for i in range(len(members)):
    addrs = members[i].text
    member.append(addrs)
# print(member)

json_2 = {}
for k in range(len(member)):    
    json_2[company_name[k]] = member[k]
json[heads[2]] = json_2



# ------------------------------------------------------------전화번호 구하기------------------------------------------------------------
tels = soup.select("tr:nth-of-type(4) td")
tel = []
for i in range(len(tels)):
    addrs = tels[i].text
    tel.append(addrs)
# print(tel)

json_3 = {}
for k in range(len(tel)):    
    json_3[company_name[k]] = tel[k]
json[heads[3]] = json_3


#------------------------------------------------------------메일 구하기------------------------------------------------------------
emails = soup.select("tr:nth-of-type(5) td")
email = []
for i in range(len(emails)):
    addrs = emails[i].text
    email.append(addrs)
# print(email)

json_4 = {}
for k in range(len(email)):    
    json_4[company_name[k]] = email[k]
json[heads[4]] = json_4

lst = []
lst.append(json)
# print(lst)

companies = {}
companies[heads[0]]=lst

pprint(companies)

while (True):

    cmds = input("\n\n=====================\n회사와 알고 싶은 항목을 입력하세요 Usage: A사, 주소\n멈추려면 quit \n=====================\n\n")
    cmd = cmds.split(', ')

    if cmds == 'quit':
        break

    elif len(cmd) != 2:


        print("두 가지를 입력해주세요. Usage: A사, 주소\n\n")

    elif cmd[0] not in company_name or cmd[1] not in heads:
        print("실제 존재하는 회사와 항목명을 입력해주세요. Usage: A사, 주소\n\n")

    else:
        print("\n\n",lst[0][cmd[1]][cmd[0]],"\n\n")