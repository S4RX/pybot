from __future__ import unicode_literals
import youtube_dl
import misc
import glob 
import os
from sys import argv
import telebot

chat_id = '474564840'
TOKEN = misc.token
tb = telebot.TeleBot(TOKEN)

# Download data and config

download_options = {
	'format': 'bestaudio/best',
	'outtmpl': '%(title)s.%(ext)s',
	'nocheckcertificate': True,
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
}

# Song Directory
if not os.path.exists('Songs'):
	os.mkdir('Songs')
else:
	os.chdir('Songs')


def remove(file):
	os.remove(file, dir_fd = None)

def send_audio(chat_id, text = 'ПАДАЖи ....'):
	shlyah = r'C:\pybot\Songs'
	files_path = os.path.join(shlyah, '*')
	files = sorted(
    	glob.iglob(files_path), key=os.path.getctime, reverse=True)
	file = files[0]
	print (file)
	audio = open(file, 'rb')
	tb.send_audio(chat_id, audio)
	
	
# Download Songs
def skachat():
	with youtube_dl.YoutubeDL(download_options) as dl:
		#with open('../' + argv[1], 'r') as f:
		#	for song_url in f:
		print('Vvedite url')
		link = input()
		dl.download([link])
		send_audio(chat_id)
		print("fail skachan")
		os.remove(file, dir_fd = None)
		print("papka ochischena")
		answer = input("Hotite prodolzhit y/n:")
		if answer == 'y':
			skachat()
		elif answer == 'n':	
			
			exit()

skachat()
