import re
import difflib

# pattern = re.compile('\.\"|\.\s')
# pattern2 = re.compile('\t')
# # htm_1 = html_1s.splitlines()
# # htm_2 = html_2s.splitlines()
# # d2 = difflib.HtmlDiff()
# # diffHtml = d2.make_file(htm_1, htm_2)
# # print("\n\n\n\n htm_1>>>>> ", htm_1)
# # print("\n\n\n\n htm_2>>>>> ", htm_2)
# # print(diffHtml)

# # pattern = re.compile('\.\"|\.\s')
# # pattern2 = re.compile('\t')
htm_1 = '''In Korea, there has been a fierce controversy on universities’ tuition fees. In fact, in 2013, Korea has been ranked at fourth out of twelve countries on the amount of tuition fee both in public and private university. It is a serious problem because GDP of Korea is ranked relatively lower among OECD countries. However, high tuition fees do not mean that universities in Korea are advanced than before. Many universities in capital area reserve a huge amount of tuition without a clear usage. Those universities, therefore, always have a conflict with a student council who raise voice of students. Without any specific reasons, universities should stop saving tuition and have to use more money on students.
The most important reason why tuition reserve comes into question is that universities do not comply with students’ requirements although they already piled up a lot of tuition fees, insisting lack of money. 
For example, although the government had legislated tuition regulatory policy, which require universities to present specific amount of reserve they will have and where to invest that money, more than a trillion won is accumulated during four years. It is problematic because facilities in universities did not get better despite a lot of accumulated money without any purposes. The demand for improving facilities or higher pay of employers of service companies have always came into conflicts between students or workers and universities. However, universities in capital area insist that they cannot afford to do that while they save more than one hundred billion won per year.
 	The accumulated money is primarily used for constructing new buildings, and for research, and scholarship. However, in case of Hongik University, there is not enough construction site, and scholarship system is also controversial. Although the university has constructed Hongmun building with ten billion won of reserved money a few years ago, many empty spaces are not spared to students but used for commercial purposes. 
The second reason is that universities are educational institutions, not companies. This means that universities work as nonprofit organizations, are not made for making money. Thirty three universities invest part of reserved money financially. The size of investment has increased rapidly for three years, and eighteen of them lost money until 2014. The size of investment has increased twice for three years. The loss of invested money is directly returned to students’ burden. Without considerable improvement of educational environment, universities keep trying to make more profit.
Nelson Mandela once said, “Education is the most powerful weapon which you can use to change the world.” The competitiveness of universities in the world leads to national competitiveness. If universities continue to saving too much money for nothing related to students but for making their own profit, they may fall behind in the world. They have to make an effort to break down the convention of closed decision of budget and should consider students’ requirement first.'''

htm_2 = '''In Korea, there has been a fierce controversy over universities’ tuition fees. In fact, in 2013, Korea has been ranked fourth out of twelve countries on the amount of tuition fee both in public and private university. It is a serious problem because the GDP of Korea is ranked relatively low among OECD countries. However, high tuition fees do not mean that universities in Korea are more advanced than before. Many universities in the capital area reserve a huge amount of tuition without a clear purpose. Those universities, therefore, always have a conflict with their student councils who raise voice of the students. Without any specific reasons, universities should stop saving tuition and invest more money on students.
The most important reason why the tuition reserve comes into question is that universities do not comply with students’ requirements, although they have already accumulated a lot of tuition fees, insisting they lack money. For example, although the government had legislated a regulatory tuition policy, which requires universities to present a specific amount of reserve they will have and where to invest that money, more than a trillion won was accumulated in four years. This is problematic because the facilities in universities did not get better despite having a lot of accumulated money without any purposes. The demands for improving facilities or higher pay of employers of service companies have always came under conflicts between students or workers and universities. However, universities in the capital area insist that they cannot afford to improve those problems while they save more than one hundred billion won per year.
The second reason for lowering the reserve is that universities are educational institutions, not companies. This means that universities work as nonprofit organizations, and are not made for making money. Thirty three universities invest part of reserved money financially. The size of an investment has increased rapidly for three years, and eighteen universities lost money until 2014. The size of whose investment in what has increased twice for three years. The loss of invested money is directly connected to students’ burden. Without considerable improvement of educational environment, universities keep trying to make more profit.
However, most universities insist that accumulated money has to be seen as a measure for long-term policies. Also, they claim that they have a tight budget with current reserve fund system because of lowering tuition fees. Nevertheless, the claim is not plausible, given that universities in the capital area has lowered the tuition fee by in less than two percent while require much more money as a reserve fee according to KEHI statistics. For example, Hongik University has lowered the tuition fee about 1.5 percent while other universities in Korea lowered it by four percent on average, insisting lack of funds. In spite of lack of funds, they expanded reserve about forty billion one that year. It is contradictory that the university has no money to enhance educational factors while they saved more than a thousand billions.
Nelson Mandela once said, “Education is the most powerful weapon which you can use to change the world.” The competitiveness of universities in the world leads to national competitiveness. If universities continue to save too much money, doing nothing related to students but only for making profit, they may fall behind in the world. Universities have to make an effort to break down the convention of closed decisions about budget and should consider students’ requirements first.'''

# html_1 = re.sub(pattern, '.\n', htm_1)
# html_1s = re.sub(pattern2, '', html_1)
# html_2 = re.sub(pattern, '.\n', htm_2)
# html_2s = re.sub(pattern2, '', html_2)
# h1 = html_1s.splitlines()

def diff(html):
	pattern = re.compile('\.\s')
	aa = re.sub(pattern, '.\n', html)
	# cc=[]
	xx = aa.split("\n")
	# cc.append(bb)	
	# print(bb)
	# xx =  html.split('.')
	yy = []
	for h in xx:
		if len(h)>= 200 and len(h)<400:
			idx = h.index(',')
			if idx == None:
				h_1 = h[0:199]
				h_2 = h[199:]
			else:
				h_1 = h[0:idx+1]
				h_2 = h[idx+1:]
			yy.append(h_1)
			yy.append(h_2)
		else:
			yy.append(h)
	return yy

h1 = diff(htm_2)
h2 = diff(htm_1)

d2 = difflib.HtmlDiff()
diffHtml = d2.make_file(h1, h2)
print(diffHtml)
# # print(h1)
# html2_2s2 = re.sub(pattern3, ',\n', html_2s)
# h2 = html2_2s2.splitlines()
# print(diffHtml)
# pattern = re.compile('\.\s')
# a = 'aweta. ateajwe. awteatq.'
# aa = re.sub(pattern, '.\n', a)
# cc=[]
# bb = aa.split("\n")
# cc.append(bb)	
# print(bb)
# html_1 = re.sub(pattern, '.\n', htm_1)
# print(aa)
# b = a.split('.')
# print(b)