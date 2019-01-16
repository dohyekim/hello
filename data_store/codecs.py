import csv, codecs
import random

filename = "c:\workspace/hello/exam/students.csv"
fp = codecs.open(filename, "r", "utf-8")
# 파일을 읽어서 가져가준다.
# codecs.open은 stream을 뚫어주는 거
reader = csv.reader(fp, delimiter=',', quotechar='"')

with codecs.open('./output.csv', 'w', 'utf-8') as ff:
    writer = csv.writer(ff, delimiter=',', quotechar='"')
    # csv의 row단위로 stream에 띄워 보낸다.
    for cells in reader:
        writer.writerow([cells[0], random.randrange(1,100)])    
