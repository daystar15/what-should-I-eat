# 오늘 뭐 먹지
날씨에 따라 먹기 좋은 음식들을 추천해주는 프로그램

## 제작기간

8/1 ~ 8/5


## 개발환경
visual studio code, python


## 개발문서
* ppt

  <https://www.miricanvas.com/v/12aj7jc>

* 시연영상

  <https://www.youtube.com/watch?v=vOPF8Kixgak>

## 기능명세
* weather.py
  
  네이버 검색창에 '날씨'를 검색하여 날씨 페이지에 있는 기온, 습도, 풍향 정보를 받아온다.
* main.py

  weather.py에서 받아온 날씨 데이터를 question이라는 변수에 저장을 하고 chat gpt api와 연결하여 결과값을 result라는 변수에 저장시킨다.
  tkinter를 사용하여 '오늘 뭐 먹지'라는 버튼을 클릭하면 result 값이 나오도록 설정하고 '닫기'버튼을 클릭하면 프로그램을 종료한다.
  
* config.py

  오픈API키는 공개가 되면 안되기 때문에 공개되지 않도록 따로 보관하여 처리할 변수를 만들어 파일에 저장한다.

## 향후과제
|버전|설명|완료여부|
|:---:|:---:|:---:|
|2|휴대폰 어플리케이션으로 변환하여 구현|미완료|
