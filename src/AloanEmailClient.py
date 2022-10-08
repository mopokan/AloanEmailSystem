#This program is free software. It comes without any warranty, to
#the extent permitted by applicable law. You can redistribute it
#and/or modify it under the terms of the Do What The Fuck You Want
#To Public License, Version 2, as published by Sam Hocevar. See
#http://www.wtfpl.net/ for more details. 


#import all necessary library
from web3 import Web3 
import time
import json
import requests
#Chain and wallet configuration
bsc= "https://bsc-dataseed.binance.org/"
web3= Web3(Web3.HTTPProvider(bsc))
account_1="Your wallet address"
private= "Your wallet private key"
CN=[]
#The duty of balanceCheck() function is to check your total BNB balance and Your message quota
def balanceCheck():
    print(" "" "" "" ")
    balance= web3.eth.get_balance(account_1)
    ETHBalance= web3.fromWei(balance, 'ether')
    Quota= int(float(ETHBalance)/(0.000001+0.000000005+0.000105))
    print("Your HODL-Value:",ETHBalance,"BNB",",(Quota remain:",Quota,"mails)")
    print(" "" "" "" ")
#The duty of message_sender(n,t) function is to send an email from the client to opponent
def message_sender(n,t):
    account_2= n
    nonce = web3.eth.getTransactionCount(account_1)
    tx={
        'nonce': nonce,
        'to' : account_2,
        'value' : web3.toWei(0.000001, 'ether'),
        'gas' : 65000,
        'gasPrice': web3.toWei('5', 'gwei'),
        'data' : t ,
    }

    signed_tx = web3.eth.account.signTransaction(tx, private)
    web3.eth.sendRawTransaction(signed_tx.rawTransaction)
#The duty of Aloan_mail_read() function is to receive the latest email from an opponent
def Aloan_mail_read():
    print(" "" "" "" ")
    response =requests.get("https://api.bscscan.com/api?module=account&action=txlist&address="+account_1+"&startblock=0&endblock=99999999&page=1&offset=100&sort=desc&apikey=YOURAPIKEY").text
    response_info = json.loads(response)
    CN.append(response_info["result"])
    l=CN[0][0]
    UI=l["from"]
    UI1=Web3.toChecksumAddress(UI)
    if(UI1==n):
        inputana=l["input"]
        z=Web3.toText(hexstr=inputana)
        print("opponent latest mail:")
        print(" "" "" "" ")
        print("--->",z)
        print(" "" "" "" ")
        CN.clear()
    else:
        print("opponent:Don't have latest mail.")
        print(" "" "" "" ")
#The duty of Aloan_mail_write() function is to write an email and send it to an opponent
def Aloan_mail_write():
    print(" "" "" "" ")
    p=input("Your script:")
    t=Web3.toHex(text=p)
    message_sender(n,t)
    time.sleep(1)
    print(" "" "" "" ")
    print("successfully to delivered email.")

#main 
print(" "" "" "" ")
print("Welcome to Aloan email system. Please fill your information:")
time.sleep(1)
print("The Aloan mail system is a decentralized email system. That means no server fail incident")
time.sleep(1)
print(" "" "" "" ")

if (web3.isConnected() == True):#checking connection status
    print("--->Go-Online :)")

n=input("Who do you want to talk(wallet address):")#input opponent wallet address
balanceCheck()
while(True):
    print("latest mail(e),write some email(w),Your Quota(yq),Exit(!ex!)")
    r=input("You:")#input your command
    if(r=="e"):
        Aloan_mail_read()
    elif(r=="w"):
        Aloan_mail_write()
    elif(r=="yq"):
        balanceCheck()
    elif(r=="!ex!"):
        print("Aloan system has been deactivate")
        time.sleep(1)
        break
    else:
        print("error")
         















