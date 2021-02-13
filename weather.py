#한국만 가능
#only korean
import requests 
from bs4 import BeautifulSoup
location = input()
Finallocation = location + '날씨' 
LocationInfo = "" 
NowTemp = "" 
CheckDust = [] 
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + Finallocation 
hdr = {'User-Agent': ('mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.70 safari/537.36')} 
req = requests.get(url, headers=hdr) 
html = req.text 
soup = BeautifulSoup(html, 'html.parser') 
# 오류 체크 
ErrorCheck = soup.find('span', {'class' : 'btn_select'}) 
if 'None' in str(ErrorCheck): 
    print("Error! 지역 검색 오류!") 
else: # 지역 정보 
    for i in soup.select('span[class=btn_select]'): 
        LocationInfo = i.text # 현재 온도 
        NowTemp = soup.find('span', {'class': 'todaytemp'}).text + soup.find('span', {'class' : 'tempmark'}).text[2:] 
        # 날씨 캐스트 
        WeatherCast = soup.find('p', {'class' : 'cast_txt'}).text 
        # 오늘 오전온도, 오후온도, 체감온도 
        TodayMorningTemp = soup.find('span', {'class' : 'min'}).text 
        TodayAfternoonTemp = soup.find('span', {'class' : 'max'}).text 
        TodayFeelTemp = soup.find('span', {'class' : 'sensible'}).text[5:] 
        # 자외선 지수 
        TodayUV = soup.find('span', {'class' : 'indicator'}).text[4:-2] + " " + soup.find('span', {'class' : 'indicator'}).text[-2:] 
        # 미세먼지, 초미세먼지, 오존 지수 
        CheckDust1 = soup.find('div', {'class': 'sub_info'}) 
        CheckDust2 = CheckDust1.find('div', {'class': 'detail_box'}) 
        for i in CheckDust2.select('dd'): 
            CheckDust.append(i.text) 
        FineDust = CheckDust[0][:-2] + " " + CheckDust[0][-2:] 
        UltraFineDust = CheckDust[1][:-2] + " " + CheckDust[1][-2:] 
        Ozon = CheckDust[2][:-2] + " " + CheckDust[2][-2:] 
        # 내일 오전, 오후 온도 및 상태 체크 
        tomorrowArea = soup.find('div', {'class': 'tomorrow_area'}) 
        tomorrowCheck = tomorrowArea.find_all('div', {'class': 'main_info morning_box'}) 
        # 내일 오전온도 
        tomorrowMoring1 = tomorrowCheck[0].find('span', {'class': 'todaytemp'}).text 
        tomorrowMoring2 = tomorrowCheck[0].find('span', {'class' : 'tempmark'}).text[2:] 
        tomorrowMoring = tomorrowMoring1 + tomorrowMoring2 
        # 내일 오전상태 
        tomorrowMState1 = tomorrowCheck[0].find('div', {'class' : 'info_data'}) 
        tomorrowMState2 = tomorrowMState1.find('ul', {'class' : 'info_list'}) 
        tomorrowMState3 = tomorrowMState2.find('p', {'class' : 'cast_txt'}).text 
        tomorrowMState4 = tomorrowMState2.find('div', {'class' : 'detail_box'}) 
        tomorrowMState5 = tomorrowMState4.find('span').text.strip() 
        tomorrowMState = tomorrowMState3 + " " + tomorrowMState5 
        # 내일 오후온도 
        tomorrowAfter1 = tomorrowCheck[1].find('p', {'class' : 'info_temperature'}) 
        tomorrowAfter2 = tomorrowAfter1.find('span', {'class' : 'todaytemp'}).text 
        tomorrowAfter3 = tomorrowAfter1.find('span', {'class' : 'tempmark'}).text[2:] 
        tomorrowAfter = tomorrowAfter2 + tomorrowAfter3 
        # 내일 오후상태 
        tomorrowAState1 = tomorrowCheck[1].find('div', {'class' : 'info_data'}) 
        tomorrowAState2 = tomorrowAState1.find('ul', {'class' : 'info_list'}) 
        tomorrowAState3 = tomorrowAState2.find('p', {'class' : 'cast_txt'}).text 
        tomorrowAState4 = tomorrowAState2.find('div', {'class' : 'detail_box'}) 
        tomorrowAState5 = tomorrowAState4.find('span').text.strip() 
        tomorrowAState = tomorrowAState3 + " " + tomorrowAState5 
        print("=========================================") 
        print(LocationInfo + " 날씨 정보입니다.") 
        print("=========================================") 
        print("현재온도: " + NowTemp) 
        print("체감온도: " + TodayFeelTemp) 
        print("오전/오후 온도: " + TodayMorningTemp + "/" + TodayAfternoonTemp) 
        print("현재 상태: " + WeatherCast) 
        print("현재 자외선 지수: " + TodayUV) 
        print("현재 미세먼지 농도: " + FineDust) 
        print("현재 초미세먼지 농도: " + UltraFineDust) 
        print("현재 오존 지수: " + Ozon) 
        print("=========================================") 
        print(LocationInfo + " 내일 날씨 정보입니다.") 
        print("=========================================") 
        print("내일 오전 온도: " + tomorrowMoring) 
        print("내일 오전 상태: " + tomorrowMState) 
        print("내일 오후 온도: " + tomorrowAfter) 
        print("내일 오후 상태: " + tomorrowAState)

#출처: https://it-neicebee.tistory.com/48 [IT's Portfolio]
