#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
import os
from gtts import gTTS
import twitter as tt
import youtube as yt

def rec():
	os.system('arecord -fdat -d 3 cmd.wav')

# Record Audio
	r = sr.Recognizer()
	demo=sr.AudioFile('cmd.wav')
	with demo as source:
		audio=r.record(source)

	order=r.recognize_google(audio)
	usr_cmd=order.split()[0]
	
	print(order.lower())
	if(usr_cmd=='show'):
		twobj=tt.authTw()
		tt.showTw(twobj)
		speak("any other help")
		rec()

	elif(usr_cmd=="like"):
		twobj=tt.authTw()
		inputN=order.replace("like ","")
		tt.likeTw(twobj,inputN.lower())
		speak("Liked " + inputN +"'s tweet")

	elif(usr_cmd=="follow"):	
		twobj=tt.authTw()
		inputN=order.replace("follow ","")
		tt.followTw(twobj,inputN.lower())
		speak("Followed " + inputN )

	elif(usr_cmd=="unfollow"):	
		twobj=tt.authTw()
		inputN=order.replace("unfollow ","")
		tt.unfollowTw(twobj,inputN.lower())
		speak("unfollowed " + inputN )

	elif(usr_cmd=="play"):
		inputN=order.replace("play ","")
		yt.play(inputN)

	elif(order=='exit'):
		speak('Exiting')
		exit()		

def speak(d):
	myobj=gTTS(text=d, lang='en-uk', slow=False)
	print(d)
	myobj.save('test.mp3')
	os.system("mpg321 -q test.mp3")
	os.system("rm test.mp3")

if __name__=='__main__':
	rec()