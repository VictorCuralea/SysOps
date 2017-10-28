import smtplib
import subprocess
import commands
import os
from email.mime.text import MIMEText

me = "sysops123213@example.com"
address1 = "sysops-intern-17@mailinator.com"
address2 = "sysops-senior-17@gmail.com"
SMTPserver="mail.smtp2go.com";
SMTPport=2525;
SMTPuser="###";
SMTPpass="###";

a1 =0
a2 =0
b1 =0
b2 = 0

#check if apache is running
p = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
out, err = p.communicate()
if ('apache2' in out):
	print('Apache2 running')
	a1=2
else:
	b1=2
	
#check if website returns code 200
output = commands.getoutput('wget localhost')

if '200 OK' in output:
	print("Website is up! http://localhost returns 200 OK")
	a2=4
else:
	b2=4

a=a1+a2
b=b1+b2	

 

s = smtplib.SMTP(host=SMTPserver, port=SMTPport)
s.starttls()
s.login(SMTPuser, SMTPpass)

if a==6:
	msg = MIMEText("All your base are belong tu us")
	msg['Subject'] = 'Website is up.'
	msg['From'] = me
	msg['To'] = address2
	s.sendmail(me, [address2], msg.as_string())
else:

	
	
	if os.path.isfile('log.txt'):
		#print "OK";
		line = open('log.txt').readline()
		contor=int(line)
		z=contor+1;
		if z==6:

			msg = MIMEText("Apache is down. Website is not accessible. This problem occured at the last 5 tests")
			msg['From'] = me
			msg['Subject'] = 'WAKE UP BIG MAN. Your minions are not up to the job'
			msg['To'] = address2
			s.sendmail(me, [address2], msg.as_string())
		
			
			subprocess.check_call("apachectl start".split())
			os.remove('log.txt')
		
		else:
			contor=contor+1
			msg = MIMEText("Apache is down. Website is not accessible. ")
			msg['From'] = me
			msg['Subject'] = 'Serious error is serious'
			msg['To'] = address1
			s.sendmail(me, [address1], msg.as_string())
			
			
			subprocess.check_call("apachectl start".split())
			os.remove('log.txt')
			log = open('log.txt','w')
			log.write(str(contor))
			log.close()
		#print contor
	else:
		#print "File not here"
		log = open('log.txt','w')
		t=1
		contor=1
		log.write(str(t))
		log.close()
	



if os.path.isfile('index.html'):
	os.remove("index.html") #remove file created by wget
s.quit()
