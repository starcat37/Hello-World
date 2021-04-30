#!/usr/bin/env python
# coding: utf-8

#header

from pyfiglet import Figlet
f = Figlet(font='starwars')
print(f.renderText("Hello World!"))

#국가명을 input으로 받아 해당 국가의 언어 인사를 출력하는 프로그램

dic_coun_lan = {'South Korea':"안녕하세요!", 'USA':"Hello!", 'Japan':'こんにちは！', 'China':'你好！'}

print("Supported country: South Korea, USA, Japan, China")
country = input("Please enter your country. (English) : ")

if dic_coun_lan.get(country) == None:
    b = input("There's no data about your country.\nPlease enter 'Hello!' in your country language.: ")
    dic_coun_lan[country] = b #해당하는 국가가 없을 경우 이용자가 직접 해당 인사 데이터를 입력

print(dic_coun_lan.get(country))
#딕셔너리에서 key로 value 찾기: dic.get(a)

"""if country == "South Korea": 
    print("안녕하세요!")
elif country == "USA": 
    print("Hello!")
elif country == "Japan": 
    print("こんにちは！")
elif country == "China": 
    print("你好！")
else: print("Unsupported country.")"""

  #문자열 비교에서 or은 쓰면 안되는 것 같다...
  
  #국가명이 다양한 나라들이 있는데, 이런 데는 리스트로 관리하는 게 나으려나
  #utf 같은 거 신경 안 써도 되나
  #저녁 뭐 먹지
