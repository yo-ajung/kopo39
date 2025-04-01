#  CSV파일 과제
import csv

f = open('weather.csv', 'w', newline = '', encoding = 'cp949')
wr = csv.writer(f)

wr.writerow(['날짜', '요일', '날씨', '최저기온', '최고기온', '강수량'])
wr.writerow(['20230101', '월', '맑음', '-4.3', '3.8', '0'])
wr.writerow(['20230102', '화', '맑음', '-7.4', '0.4', '0'])
wr.writerow(['20230103', '수', '맑음', '-9.0', '0.6', '0'])

f.close()
