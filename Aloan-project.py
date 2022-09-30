import os
import time
import smtplib, ssl
import email
import imaplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def mailformation():
    f=open('C:/Users/ai_pc/anaconda3/envs/aloan/informConfig.txt' ,'r')#Config by yourself
    e=f.readline()#Sender address
    p=f.readline()#password
    t= i #recieve address
    msg = MIMEMultipart()
    msg['Subject']='Aloan information'
    From= e
    To= t
    text = MIMEText("join")
    msg.attach(text)
    context = ssl.create_default_context()
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls(context=context)
    s.ehlo()
    password = p
    s.login(e, password)
    s.sendmail(From,To,msg.as_string())
    s.quit()
    time.sleep(1)
    print("We sent it already.Have Fun!")

print("Hello everyone! Welcome to aloan")
print("Who are you? (client press y)(Server press n)")
k=input("y/n:")
if(k=="y"):
    print("Welcome to Client section:One time Registration Pay until bankrupt")
    i=input("please fill your email adress(we will send necessary information to you):")
    mailformation()

elif(k=="n"):
    print("Welcome to server section:One time Registration Run eternal")
    

    


else:
    print("Error")


