import os
import time
import email
import imaplib
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import json
import requests 
import random

def mailRequest():
    RD=[]
    f=open('C:/Users/ai_pc/anaconda3/envs/aloan/informConfig.txt' ,'r')#Config by yourself
    e=f.readline()#Sender address
    p=f.readline()#password
    EMAIL = e
    PASSWORD = p
    SERVER = 'imap.gmail.com'
    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select('inbox')
    _,data = mail.search(None, 'ALL')
    for email_id in data[0].split():
        _,data = mail.fetch(email_id, '(RFC822)' )
        raw_email = data[0][1]
        raw_email = raw_email.decode('utf-8')
        email_content = email.message_from_string(raw_email)
        if 'I want to join Aloan community' in email_content['Subject']: #Change this line to the subject you are searching for
            m = email_content['From']
            RD.append(m)
            for part in email_content.walk():
                u = part.get_payload()
                RD.append(u)
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
            return RD
    
            
def mailinformation():
    f=open('C:/Users/ai_pc/anaconda3/envs/aloan/informConfig.txt' ,'r')#Config by yourself
    e=f.readline()#Sender address
    p=f.readline()#password
    t= i #recieve address
    msg = MIMEMultipart()
    msg['Subject']='How to join Aloan community:pay to earn society'
    From= e
    To= t
    text = MIMEText("Freedom to pay. No currency problem ,No age restriction! description about participate community is in the picture")
    msg.attach(text)
    ImgFileName='C:/Users/ai_pc/anaconda3/envs/aloan/JoinAloanCommunity.png'
    img_data = open(ImgFileName, 'rb').read()
    image = MIMEImage(img_data,name=os.path.basename("JoinAloanCommunity.png"))
    msg.attach(image)
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

def generate_id(x):
    now1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    l=str(random.choice(now1))
    o=str(random.choice(now1))
    y=str(random.choice(now1))
    allp=l + o + y + x
    return allp

def verification():
    CN=[]
    emailSender=g[0]
    c=emailSender.find('<')
    d=emailSender.find('>')
    i=emailSender[c+1:d]
    CN.append(i)
    emailSender1=g[2]
    u=len(emailSender1)
    v=emailSender1[0:u-2]
    v1=v.find(',')
    v2=v[0:v1]
    v3=v[v1+1:]
    CN.append(v2)
    CN.append(v3)
    print(CN)
    response = requests.get("https://api.bscscan.com/api?module=transaction&action=gettxreceiptstatus&txhash="+v3+"&apikey=YMG8X5GCURDS95NEV3DE9G5RVNKR9BJ9BH").text
    response1 = requests.get("https://api.bscscan.com/api?module=account&action=balance&address="+v2+"&apikey=YMG8X5GCURDS95NEV3DE9G5RVNKR9BJ9BH").text
    response_info = json.loads(response)
    response_info1 = json.loads(response1)
    k=response_info["status"]
    j=response_info1["result"]
    if(k=="1"):
        j=int(j)
        BNBB=j/(10**18)
        print("BNB:",BNBB,"BNB")
        BNNB=str(BNBB)
        hp=generate_id(BNNB[5:8])
        f=open('C:/Users/ai_pc/anaconda3/envs/aloan/informConfig.txt' ,'r')#Config by yourself
        en=f.readline()#Sender address
        pm=f.readline()#password
        tt= i #recieve address
        msg = MIMEMultipart()
        msg['Subject']='This is your ID For Aloan payment'
        From= en
        To= tt
        text = MIMEText("Your ID:"+ hp)
        msg.attach(text)
        context = ssl.create_default_context()
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.ehlo()
        s.starttls(context=context)
        s.ehlo()
        password = pm
        s.login(en, password)
        s.sendmail(From,To,msg.as_string())
        s.quit()
        time.sleep(1)
        
print("Hello everyone! Welcome to aloan")
print("Who are you? (client press y)(Server press n)")
k=input("y/n:")
if(k=="y"):
    print("Welcome to Client section:One time Registration Pay until bankrupt")
    i=input("please fill your email adress(we will send necessary information to you):")
    mailinformation()
   

elif(k=="n"):
    print("Welcome to server section:One time Registration Run eternal")
    g=mailRequest()
    verification()
    

    


else:
    print("Error")


