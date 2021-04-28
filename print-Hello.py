#!/usr/bin/env python
# coding: utf-8

#국가명을 input으로 받아 해당 국가의 언어 인사를 출력하는 프로그램

print("Supported country: South Korea, USA, Japan, China")
country = input("Please enter your country. (English) : ")

if country == "Korea" or "South Korea" or "Republic of Korea":
  print("안녕하세요!")
elif country == "USA" or "America":
  print("Hello!")
elif country == "Japan":
  print("こんにちは！")
elif country == "China":
  print("你好！")
else:
  print("Unsupported country.")

  
  #국가명이 다양한 나라들이 있는데, 이런 데는 리스트로 관리하는 게 나으려나
  #utf 같은 거 신경 안 써도 되나
  #저녁 뭐 먹지
