from urllib.request import urlopen
from bs4 import BeautifulSoup

url="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8"

html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
all_info = soup.find_all('div','sort')

# 기온
temp_list = all_info[0].text.split()
temp = temp_list[1]

# 습도
humid_list = all_info[1].text.split()
humid = humid_list[1]

# 풍속
wind_list = all_info[2].text.split()
wind = wind_list[1]

#print(f'기온은 {temp}이고, 습도는 {humid}이고, 풍속은 {wind}일 때 뭐먹을지 추천해줘')