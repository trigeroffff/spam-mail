import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import from_emailcfg, passwordcfg, mailsmtpcfg
msg = MIMEMultipart()
print("████████╗██████╗░██╗░██████╗░░██████╗░███████╗██████╗░░█████╗░███████╗███████╗")
time.sleep(0.7)
print("╚══██╔══╝██╔══██╗██║██╔════╝░██╔════╝░██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝")
time.sleep(0.7)
print("░░░██║░░░██████╔╝██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝██║░░██║█████╗░░█████╗░░")
time.sleep(0.7)
print("░░░██║░░░██████╔╝██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝██║░░██║█████╗░░█████╗░░")
time.sleep(0.7)
print("░░░██║░░░██╔══██╗██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔══██╗██║░░██║██╔══╝░░██╔══╝░░")
time.sleep(0.7)
print("░░░██║░░░██║░░██║██║╚██████╔╝╚██████╔╝███████╗██║░░██║╚█████╔╝██║░░░░░██║░░░░░")
time.sleep(0.7)
print("░░░╚═╝░░░╚═╝░░╚═╝╚═╝░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░░░░░")

print("░██████╗██████╗░░█████╗░███╗░░░███╗")
time.sleep(0.4)
print("██╔════╝██╔══██╗██╔══██╗████╗░████║")
time.sleep(0.4)
print("╚█████╗░██████╔╝███████║██╔████╔██║")
time.sleep(0.4)
print("░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║")
time.sleep(0.4)
print("██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║")
time.sleep(0.4)
print("╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝")
time.sleep(0.4)
print("1.залогиньтесь в ручную 2. конфиг")
cfg = input(("==>"))
if cfg == "1":
	from_email = input(("email: "))
	password = input(("pass: ")) 
	to_email = input(("Введите почту: "))
	message = input(("Введите сообщение: "))
	n = int(input(("кол-во")))
	print("smtp.gmail.com: 587,mail.ru: 25,yandex.com: 465")
	mailsmtp = input(("==>"))
	for i in range(n): 
		msg.attach(MIMEText(message, 'plain'))
 
		server = smtplib.SMTP(mailsmtp)
		server.starttls()
		server.login(from_email, password)
		server.sendmail(from_email, to_email, msg.as_string())
		server.quit()
elif cfg == "2":
	print(from_emailcfg)
	print(passwordcfg)
	print(mailsmtpcfg)
	gmailfast = input(("1.Без @gmail.com"))
	if gmailfast == "1":


		to_email = input(("Введите почту: "))
		message = input(("Введите сообщение: "))
		n = int(input(("кол-во: ")))
		for g in range(n): 
			msg.attach(MIMEText(message, 'plain'))
 
			server = smtplib.SMTP(mailsmtpcfg)
			server.starttls()
			server.login(from_emailcfg, passwordcfg)
			server.sendmail(from_emailcfg, to_email + "@gmail.com" , msg.as_string())
			server.quit()
	else:
		to_email = input(("Введите почту: "))
		message = input(("Введите сообщение: "))
		n = int(input(("кол-во: ")))
		for g in range(n): 
			msg.attach(MIMEText(message, 'plain'))
 
			server = smtplib.SMTP(mailsmtpcfg)
			server.starttls()
			server.login(from_emailcfg, passwordcfg)
			server.sendmail(from_emailcfg, to_email, msg.as_string())
			server.quit()
