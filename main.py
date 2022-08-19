import random
import pickle
import asyncio
from time import sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import textwrap
import os
import json, pickle

app = Client('admin', api_id=19391779, api_hash='5d862c7657a0f2a5ba27cf560b52240b')

if os.sys.platform == "win32":
	os.system("cls")
else:
	os.system("clear")

# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
	orig_text = msg.text.split(".type ", maxsplit=1)[1]
	text = orig_text
	tbp = "" # to be printed
	typing_symbol = "▒"

	while(tbp != orig_text):
		try:
			msg.edit(tbp + typing_symbol)
			sleep(0.05) # 50 ms

			tbp = tbp + text[0]
			text = text[1:]

			msg.edit(tbp)
			sleep(0.05)

		except FloodWait as e:
			sleep(e.x)

 # Шаблон текста в строчки
@app.on_message(filters.command("yaebalsya", prefixes=".") & filters.me)
def valentine(app, msg):
	app.send_message(msg.chat.id, f'''
	<b>Я ебался лишь однажды</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Где и как,зачем и с кем</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Не помню я,да и не важно</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Я был очень пьян в тот день</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>И не важен пол и возраст</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Имя,цвет волос и глаз</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Да,я пидорас,возможно</b>
	''')
	sleep(1)
	app.send_message(msg.chat.id, f'''
	<b>Но ведь это был лишь раз</b>
	''')

	sleep(0.5)
	global number
	number = number + 1
	
#Рандомайзер
@app.on_message(filters.command("random", prefixes=".") & filters.me)
def random_(_, msg):
	random_number = str(random.randint(0, int(msg.command[1])))
	msg.edit(roi + random_number)



too = random.randint(0, 100)
roi = f'<b> Случайное число: </b>'

#1000-7
@app.on_message(filters.command("ghoul", prefixes=".") & filters.me)
def valentine(app, message):
	global number
	i = 1000
	while i > 0:
		try:
			app.send_message(message.chat.id, f'{i} - 7 = {i-7}')
		except FloodWait as e:
			sleep(e.x)

		i -= 7
		sleep(0)

	if(end_message != ''):
		app.send_message(message.chat.id, end_message)

#Спамер
@app.on_message(filters.command("spam", prefixes=".") & filters.me)
def spam(app, msg):
	spams = " ".join(msg.command[2:])

	global number

	if not spams:
		msg.edit(f'''
			**Error: Что-то пошло не так...\nИспользование: .spam <кол-во спама> <слово>**''')
		sleep(1.5)
		msg.delete()
	else:
		for _ in range(int(msg.command[1])):
			app.send_message(msg.chat.id, spams)

#Правда/Ложь
@app.on_message(filters.command("tf", prefixes=".") & filters.me)
def betaloves(_, msg):
	t = ["[Правда]", "[Ложь]"]

	try0 = random.choice(t)
	try1 = " ".join(msg.command[1:])

	if not try1:
		msg.edit(f'''
			**Error: Вы не ввели вопрос!\nИспользование: .tf <вопрос>**''')
		sleep(1.5)
		msg.delete()
	else:
		msg.edit(f'''
			{try1} {try0}''')

	sleep(5)
	global number
	number = number + 1		
	
app.run()