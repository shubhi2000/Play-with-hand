import pygame
import time
import serial
from mutagen.mp3 import MP3
ser=serial.Serial('COM9',baudrate=9600,timeout=1)
def displaytext(text,size,color,x,y):
	font=pygame.font.SysFont("Times New Roman",size)
	text_surface=font.render(text,True,color)
	text_rect=text_surface.get_rect()
	text_rect.midtop=(x,y)
	screen.blit(text_surface,text_rect)

def play(track):
	pygame.mixer.music.load(track)
	pygame.mixer.music.play(loops=1,start=0.0)
	audio=MP3(track)
	t=0
	while t<audio.info.length:
		arduinoData=str(ser.readline())
		if arduinoData=="Down":
			pygame.mixer.music.pause()
			time.sleep(3)
		if arduinoData=="Up":
			pygame.mixer.music.unpause()
		if arduinoData=="Back":
			pygame.mixer.music.stop()
			menu(165)
		t+=1
	#print(audio.info.length)

def menu(y):
	screen.fill((0,0,0))
	displaytext("SELECT THE CATEGORY OF SONG",30,(200,200,200),600,20)
	pygame.draw.circle(screen,(255,192,203),(100,y),10)
	displaytext("YOU WANT TO LISTEN",30,(200,200,200),600,60)
	displaytext("POP",48,(255,192,203),600,140)
	displaytext("INSTRUMENTAL",48,(255,192,203),600,240)
	displaytext("PARTY SONGS",48,(255,192,203),600,340)
	displaytext("BOLLYWOOD 90s",48,(255,192,203),600,440)
	displaytext("BLUES",48,(255,192,203),600,540)
	pygame.display.flip()
	time.sleep(2)
	while 1:
		arduinoData=str(ser.readline())
		if arduinoData[2:4]=="Up":
			if y==165:
				y=565
			else:
				y-=100
			menu(y)
			break
			time.sleep(2)
		if arduinoData[2:6]=="Down":
			if y==565:
				y=165
			else:
				y+=100
			menu(y)
			time.sleep(2)
		if arduinoData[2:6]=="Back":
			pygame.display.quit()
			break
		if arduinoData[2:8]=="Select":
			if y==165:
				pop(165)
			if y==265:
				instrumental(165)
			if y==365:
				party(165)
			if y==465:
				bollywood(165)
			if y==565:
				blues(165)
			time.sleep(2)

def pop(y):
	screen.fill((244,69,226))
	displaytext("SELECT THE SONG",30,(0,0,0),600,40)
	pygame.draw.circle(screen,(0,0,0),(100,y),10)
	displaytext("Girls Like You",48,(0,0,0),600,140)
	displaytext("Havana",48,(0,0,0),600,240)
	displaytext("Last Hurrah",48,(0,0,0),600,340)
	displaytext("Despacito",48,(0,0,0),600,440)
	displaytext("Cold Water",48,(0,0,0),600,540)
	pygame.display.flip()
	while 1:
		arduinoData=str(ser.readline())
		if arduinoData[2:4]=="Up":
			if y==165:
				y=565
			else:
				y-=100
			pop(y)
			time.sleep(2)
		if arduinoData[2:6]=="Down":
			if y==565:
				y=165
			else:
				y+=100
			pop(y)
			time.sleep(2)
		if arduinoData[2:6]=="Back":
			menu(165)
			break
		if arduinoData[2:8]=="Select":
			if y==465:
				play("Despacito-pop.mp3")
			if y==165:
				play("Girls Like You - pop.mp3")
			if y==265:
				play("Havana - pop.mp3")
			if y==365:
				play("last hurrah-pop.mp3")
			if y==565:
				play("Cold Water- pop.mp3")
			pop(y)

def instrumental(y):
	screen.fill((244,69,226))
	displaytext("SELECT THE SONG",30,(0,0,0),600,40)
	pygame.draw.circle(screen,(0,0,0),(100,y),10)
	displaytext("Chariots of Fire",48,(0,0,0),600,440)
	displaytext("Love Theme",48,(0,0,0),600,140)
	displaytext("Soul Finger",48,(0,0,0),600,240)
	displaytext("Wonderland By Night",48,(0,0,0),600,340)
	displaytext("In the Hall of The",48,(0,0,0),600,540)
	displaytext("Mountain King",48,(0,0,0),600,600)
	pygame.display.flip()
	while 1:
		arduinoData=str(ser.readline())
		if arduinoData[2:4]=="Up":
			if y==165:
				y=565
			else:
				y-=100
			instrumental(y)
			time.sleep(2)
		if arduinoData[2:6]=="Down":
			if y==565:
				y=165
			else:
				y+=100
			instrumental(y)
			time.sleep(2)
		if arduinoData[2:6]=="Back":
			menu(165)
			break
		if arduinoData[2:8]=="Select":
			if y==465:
				play("Chariots of Fire - Instrumental.mp3")
			if y==165:
				play("Love Theme - Instrumental.mp3")
			if y==265:
				play("Soul Finger - Instrumental.mp3")
			if y==365:
				play("Wonderland by Night- Instrumental.mp3")
			if y==565:
				play("In the Hall of the Mountain King-Instrumental.mp3")
			instrumental(y)

def party(y):
	screen.fill((244,69,226))
	displaytext("SELECT THE SONG",30,(0,0,0),600,40)
	pygame.draw.circle(screen,(0,0,0),(100,y),10)
	displaytext("Let's Nacho",48,(0,0,0),600,440)
	displaytext("Sweety Tera Drama",48,(0,0,0),600,140)
	displaytext("Nachange Saari Raat",48,(0,0,0),600,240)
	displaytext("Gallan Goodiyaan",48,(0,0,0),600,340)
	displaytext("Badri Ki Dulhaniya",48,(0,0,0),600,540)
	pygame.display.flip()
	while 1:
		arduinoData=str(ser.readline())
		if arduinoData[2:4]=="Up":
			if y==165:
				y=565
			else:
				y-=100
			party(y)
			time.sleep(2)
		if arduinoData[2:6]=="Down":
			if y==565:
				y=165
			else:
				y+=100
			party(y)
			time.sleep(2)
		if arduinoData[2:6]=="Back":
			menu(165)
			break
		if arduinoData[2:8]=="Select":
			if y==465:
				play("Let’s Nacho Lyric Video - party.mp3")
			if y==165:
				play("Sweety Tera Drama-party.mp3")
			if y==265:
				play("Nachange Saari Raat - party.mp3")
			if y==365:
				play("'Gallan Goodiyaan' -party.mp3")
			if y==565:
				play("Badri Ki Dulhania-party.mp3")
			party(y)

def bollywood(y):
	screen.fill((244,69,226))
	displaytext("SELECT THE SONG",30,(0,0,0),600,40)
	pygame.draw.circle(screen,(0,0,0),(100,y),10)
	displaytext("Koi Mil Gaya",48,(0,0,0),600,440)
	displaytext("Ek ladki To Dekha To",48,(0,0,0),600,140)
	displaytext("Mera Dil Bhi Kitna Pagal Hai",48,(0,0,0),600,240)
	displaytext("Pehla Nasha",48,(0,0,0),600,340)
	displaytext("Tujhe Dekha To",48,(0,0,0),600,540)
	pygame.display.flip()
	while 1:
		arduinoData=str(ser.readline())
		if arduinoData[2:4]=="Up":
			if y==165:
				y=565
			else:
				y-=100
			bollywood(y)
			time.sleep(2)
		if arduinoData[2:6]=="Down":
			if y==565:
				y=165
			else:
				y+=100
			bollywood(y)
			time.sleep(2)
		if arduinoData[2:6]=="Back":
			menu(165)
			break
		if arduinoData[2:8]=="Select":
			if y==465:
				play("Koi Mil Gaya - Shahrukh Khan-bolly.mp3")
			if y==165:
				play("Ek Ladki Ko Dekha Toh Aisa Laga-bolly.mp3")
			if y==265:
				play("Mera Dil Bhi Kitna Pagal Hai - Saajan - bolly.mp3")
			if y==365:
				play("Pehla Nasha  - Sanam -bolly.mp3")
			if y==565:
				play("Tujhe Dekha To-bolly.mp3")
			bollywood(y)

def blues(y):
	screen.fill((244,69,226))
	displaytext("SELECT THE SONG",30,(0,0,0),600,40)
	pygame.draw.circle(screen,(0,0,0),(100,y),10)
	displaytext("BOOM",48,(0,0,0),600,440)
	displaytext("Crossroad",48,(0,0,0),600,140)
	displaytext("Dust My Broom",48,(0,0,0),600,240)
	displaytext("The Thrill is Gone",48,(0,0,0),600,340)
	displaytext("Sweet Home Chicago",48,(0,0,0),600,540)
	pygame.display.flip()
	while 1:
		arduinoData=str(ser.readline())
		if arduinoData[2:4]=="Up":
			if y==165:
				y=565
			else:
				y-=100
			blues(y)
			time.sleep(2)
		if arduinoData[2:6]=="Down":
			if y==565:
				y=165
			else:
				y+=100
			blues(y)
			time.sleep(2)
		if arduinoData[2:6]=="Back":
			menu(165)
			break
		if arduinoData[2:8]=="Select":
			if y==465:
				play("BOOM - blues.mp3")
			if y==165:
				play("Crossroad- blues.mp3")
			if y==265:
				play("Dust My Broom - Blues.mp3")
			if y==365:
				play("the thrill is gone - blues.mp3")
			if y==565:
				play("Blues Brothers - Sweet Home Chicago.mp3")
			blues(y)

pygame.init()
screen = pygame.display.set_mode((1500,1000), 0, 32)
pygame.display.set_caption("SONGS YOU LIKE !!!")
background = pygame.surface.Surface((640,640)).convert()
menu(165)
time.sleep(2)
