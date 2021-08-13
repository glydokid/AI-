# 인공지능 기사(TTS)
from datetime import datetime
import random

#경기 결과 입력 받는 곳
place = input("경기가 열린 곳은? ")
time = input("경기가 열린 시간은? ")
opponet = input("상대 팀은? ")
goals = input("손흥민은 몇 골을 넣었나요? ")
aids = input("도움은 몇 개인가요? ")
score_me = input("손흥민 팀이 넣은 골 수는? ")
score_you = input("상대 팀이 넣은 골 수는? ")

#기사 작성하는 곳
news ="[프리미어 리그 속보("+str(datetime.now())+")]\n"
news = news + "손흥민 선수는  "+ place+ "에서 "+time+"에 열린 경기에 출전하였습니다."
news = news + "상대팀은 " + opponet + " 입니다."

if score_me>score_you:
    wording=["상대팀은 이겼습니다.", "상대를 상대로 통쾌한 승리를 거머쥐었습니다.", "상대팀을 꺾었습니다."]
    news = news+ "손흥민 선수 팀이 "+ score_me +"골을 넣어 "+ score_you + "골을 넣은 " + random.choice(wording)
    
elif score_me<score_you:
    news + news+ "손흥민 선수의 팀이"+ score_me +"골을 넣어 "+ score_you + "골을 넣은 상대 팀에게 졌습니다."
    
else:
    new = news+ " 두 팅은"+score_me+ "대 "+ score_you +" 로 비겼습니다."
    
    
if int(goals)>0 and int(aids)>0:
    news=news+ " 손흥민 선수는 "+ goals+" 골에 도움"+ aids+" 개로 승리를 크게 이끌었습니다."
elif int(goals)>0 and int(aids)==0:
    news=news+ " 손흥민 선수는 "+ goals+" 골로 승리를 이끌었습니다."
elif int(goals)==0 and int(aids)>0:
    news=news+ " 손흥민 선수는 골은 없지만 "+aids+" 개의 도움으로 승리하는 데 공헌하였습니다"
else:
    news = news+"아쉽게도 이번 경기에서 손흥민의 발끝은 침묵을 지켰습니다."
    
 #음성으로 들려주는 곳
from gtts import gTTS
import playsound
import os #파일관리 함수
 
tts=gTTS(text=news,lang='ko')
tts.save("news.Son.mp3") #기존에 같은 이름의 파일이 존재하면 에러가 생김
playsound.playsound("news.Son.mp3",False) #True 멈춰서 해당 하나만 재생, False 밑에 코드랑 동시재생(배경음악)
playsound.playsound("THURSDAY MORNING CHILL JAZZ Sweet March Morning - Spring Jazz &amp Bossa Nova for Good Mood.mp3",True)
os.remove("news.Son.mp3")
os.remove("THURSDAY MORNING CHILL JAZZ Sweet March Morning - Spring Jazz &amp Bossa Nova for Good Mood.mp3")
print(news)