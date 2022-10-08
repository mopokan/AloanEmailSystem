# AloanEmailSystem
>### AloanEmailSystem เป็นโปรเจคที่สาธิตวิธีการสร้างระบบอีเมลอย่างง่ายโดยใช้ decentralized smart contract แทนที่การใช้ระบบ server แบบดั้งเดิม

AloanEmailSystem เป็นระบบอีเมลอย่างง่าย โดยระบบนี้สามารถรับ-ส่งอีเมลจากคนหนึ่งสู่อีกคนหนึ่งได้โดยอาศัยเทคโนโลยีบล็อกเชน ข้อได้เปรียบของการใช้เทคโนโลยีนี้คือ AloanEmailSystem จะเป็นระบบอีเมลที่มี       โอกาสล่มตํ่ามากเมื่อเทียบกับระบบเซิร์ฟเวอร์แบบดั้งเดิม เนื่องจากรูปแบบการทำงานแบบกระจายศูนย์(Decentralized)ของบล็อกเชน ทำให้เมื่อเกิดเหตุการณ์ที่อาจจะทำให้คอมพิวเตอร์ หรือ เซิร์ฟเวอร์บางส่วนในระบบเสียหาย 
บล็อกเชนก็ยังคงสามารถรับ-ส่งอีเมลได้ต่อไป เพราะ ยังมีคอมพิวเตอร์หรือเซิร์ฟเวอร์อื่นๆในเครือข่ายที่สามารถทำหน้าที่รับ-ส่งอีเมลได้ ในขณะที่ระบบเซิร์ฟเวอร์แบบดั้งเดิมถ้าหากเกิดเหตุขัดข้องอาจจะทำให้ไม่สามารถรับ-ส่งอีเมล
ได้ เนื่องจากเป็นเซิร์ฟเวอร์เดียวที่สามารถรับ-ส่งอีเมลได้ ซึ่งคอมพิวเตอร์ หรือ เซิร์ฟเวอร์เครื่องอื่นไม่สามารถทำหน้าที่แทนได้ และข้อได้เปรียบอีก1ข้อของการใช้เทคโนโลยีนี้คือ มีความเป็นส่วนตัวสูง เพราะ ไม่ต้องส่งข้อมูลต่างๆ
ให้กับผู้ให้บริการก่อนเริ่มใช้งาน

## หลักการทำงานของ AloanEmailSystem

**โปรเจคนี้จะใช้ Decentralized smart contract ของ Binance smart chain ในการสาธิตหลักการทำงานของ AloanEmailSystem**
<p align="center">
  <img alt="Working diagram of Email System and AloanEmailSystem." src="https://github.com/mopokan/AloanEmailSystem/blob/main/imgfolder/Email%26AloanEmailSystem_workingDiagram.jpg" width="848" height="500">
</p>

ในส่วนของหลักการทำงานของ AloanEmailSystem จะเริ่มต้นการทำงานเมื่อผู้ใช้ทำการรันโปรแกรม AloanEmailClient.py โดยโปรแกรมนี้จะทำการเก็บข้อมูลผู้ส่งที่เราต้องการจะติดต่อ และให้ผู้ใช้เลือก1ใน3โหมดที่ต้องการใช้งาน ได้แก่
1. โหมด latest mail-->ทำหน้าที่อัปเดตอีเมลล่าสุดที่ได้รับจากฝั่งตรงข้าม(ผู้ใช้คนอื่น)
2. โหมด write some email-->ทำหน้าที่เขียนและส่งอีเมลจากผู้ใช้ถึงฝั่งตรงข้าม(ผู้ใช้คนอื่น)
3. โหมด Your Quota-->ทำหน้าที่เช็คโควตาคงเหลือที่สามารถใช้ในการส่งอีเมล

เมื่อผู้ใช้ทำการ เลือกโหมด 1. โหมด latest mail โปรแกรมจะทำการเช็คอีเมลที่ส่งมาจากฝั่งตรงข้าม โดยเช็คจาก API ของ bscscan 
- ถ้าหาก**พบ** โปรแกรมจะทำการแสดงผลข้อความออกมา
- ถ้าหาก**ไม่พบ** โปรแกรมจะแสดงผล "opponent:Don't have latest mail."

หรือ เมื่อผู้ใช้ทำการ เลือกโหมด 2. โหมด write some mail เมื่อผู้ใช้เขียนข้อความเสร็จเรียบร้อยแล้ว โปรแกรมจะทำการส่งข้อความผ่านการโอน BNB Token ไปยังฝั่งตรงข้ามโดยใช้ Binance smart chain ดังรูปFig 1.2
หรือ เมื่อผู้ใช้ทำการ เลือกโหมด 3. โหมด Your Quota โปรแกรมจะทำการเช็คโควตาคงเหลือที่สามารถใช้ในการส่งอีเมล 
เมื่อโปรแกรมทำงานตามโหมดที่เราได้เลือกไว้เสร็จเรียบร้อยแล้ว โปรแกรมจะทำการวนกลับมาให้ผู้ใช้เลือก1ใน3โหมดที่ต้องการใช้งานและจะทำงานไปเรื่อยๆ จนกว่าจะใช้โหมด 

4. โหมด Exit-->ทำหน้าที่ออกจากระบบ

โดยถ้าหากสังเกตกระบวนการส่งข้อความจากภาพด้านบน ก็จะปรากฏว่าการส่งโดยใช้ AloanEmailSystem จะมีกระบวนการการส่งอีเมลที่ซับซ้อนน้อยกว่า Email System

## SET UP

ก่อนที่จะเริ่มทำการรันโปรแกรมจะต้องมีการติดตั้ง library ที่จำเป็นต่างๆเพื่อให้โปรแกรมสามารถทำงานได้อย่างสมบูรณ์ โดยสามารถติดตั้งได้2วิธี ได้แก่
1. PIP install-->วิธีนี้แนะนำสำหรับผู้ที่มีความรู้พื้นฐานการจัดการ environment ของโปรแกรม 
   - ทำการ install web3.py และ requests
     - ``` 
       pip install web3 
       pip install requests
       ```
2. Anaconda environment.yml install-->วิธีนี้แนะนำสำหรับผู้ที่เป็นมือใหม่ โดยโปรแกรมนี้จะทำการติดตั้งlibraryที่จำเป็นอัตโนมัติและช่วยในการจัดการ environment ของโปรแกรม
   - ทำการ install [Anaconda](https://www.anaconda.com/products/distribution)
   - เมื่อ install Anaconda เรียบร้อยแล้ว ให้ทำการ download [environment.yml](https://github.com/mopokan/AloanEmailSystem/blob/main/src/environment.yml) โดยให้ไฟล์นี้อยู่ใน PATH C:\Users\USER
   - จากนั้น ทำการเปิด Anaconda prompt และพิมพ์คำสั่งดังต่อไปนี้ โดยพิมพ์และรันครั้งละ1บรรทัด
     - ```
       conda env create -f environment.yml
       conda activate Aloan
       ```
   - เมื่อสำเร็จจะมีชื่อนำหน้า PATH เช่น
     - ```
       (Aloan) C:\Users\USER>
       ```

## Parameter Configuration

ในการที่จะรันโปรแกรมนี้ให้ทำงาน นอกจากการติดตั้งlibrary ที่จำเป็นแล้วต้องมีการตั้งค่าparameter ใน AloanEmailClient.py ด้วย โดยได้แก่
 ``` 
 account_1="Your wallet address" #ตั้งค่า wallet address ของตนเอง  
 
 private="Your private key" #ตั้งค่า private key จากwallet address ของตนเอง
 
 apikey="Your apikey" #ตั้งค่า apikey ของตนเอง ซึ่งอยู่ที่บรรทัดที่45
 ```
โดย [APIKEY สามารถขอได้จากที่นี่](https://bscscan.com/apis)

## RUN the program

### การรันโปรแกรมบน IDLE

1. ทำการ download [AloanEmailClient.py](https://github.com/mopokan/AloanEmailSystem/blob/main/src/AloanEmailClient.py)
2. ทำการเปิดไฟล์ AloanEmailClient.py บน IDLE และทำการรัน

### การรันบน CMD

1. ทำการ download [AloanEmailClient.py](https://github.com/mopokan/AloanEmailSystem/blob/main/src/AloanEmailClient.py)
2. ทำการเปลี่ยน PATH บน CMD ให้ตรงกับ PATH ของไฟล์ AloanEmailClient.py โดยใช้คำสั่งcd เช่น
   ```
   C:\Users\USER>cd desktop
   
   C:\Users\USER\Desktop>
   ```
3. ทำการรันโปรแกรม โดยใช้คำสั่งดังนี้
   ```
   python AloanEmailClient.py
   ```

### การรันบน Anaconda Prompt

1. ทำการ download [AloanEmailClient.py](https://github.com/mopokan/AloanEmailSystem/blob/main/src/AloanEmailClient.py)
2. ทำการเปิด Anaconda prompt จากนั้นทำการ Activate environment โดยใช้คำสั่ง
   ```
   conda activate Aloan
   ```
3. หลังจากนั้น ให้ทำการเปลี่ยน PATH ของ CMD ให้อยู่ในPATH เดียวกับ AloanEmailClient.py โดยใช้คำสั่งcd เช่น
   ```
   (Aloan) C:\Users\USER>cd desktop
   
   (Aloan) C:\Users\USER\Desktop>
   ```
4. ทำการรันโดยใช้คำสั่งดังต่อไปนี้
   ```
   python AloanEmailClient.py
   ```
5. โดยเมื่อรันแล้ว โปรแกรมจะแสดงผลลักษณะดังนี้
   ```
   (Aloan) C:\Users\USER\Desktop>python AloanEmailClient.py

   Welcome to Aloan email system. Please fill your information:
   The Aloan mail system is a decentralized email system. That means no server fail incident

   --->Go-Online :)
   Who do you want to talk(wallet address):0xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

   Your HODL-Value: 0.00xxxxxxxxx BNB ,(Quota remain: xx mails)

   latest mail(e),write some email(w),Your Quota(yq),Exit(!ex!)
   You:
   ```
   
