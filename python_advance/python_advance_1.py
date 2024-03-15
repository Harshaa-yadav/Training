'''1. Create a decorator that adds two random values between 1 to 10 to the functions
where this decorator is used. Create 4 functions add, sub, mul, div which will have this
decorator and call the 4 functions. When you’re calling the function you should not pass any parameter however
all the functions will be defined with parameters.'''
# import random
#
#
# def dec_create_random_val(func):
#     def inner_func():
#         a = random.randint(1, 10)
#         b = random.randint(1, 10)
#         c=a+b
#         print(a,b)
#         return func(c,a)
#     return inner_func
#
#
#
# @dec_create_random_val
# def add(x,y):
#     print("Addition: ",end="")
#     return x+y
#
# @dec_create_random_val
# def sub(x,y):
#     print("Subtraction: ",end="")
#     return x-y
#
# @dec_create_random_val
# def mul(x,y):
#     print("Multiplication: ",end="")
#     return x*y
#
# @dec_create_random_val
# def div(x,y):
#     print("Division: ",end="")
#     return x/y
#
# print(add())
# print(sub())
# print(mul())
# print(div())

'''2. Create two different decorators. One will give the square of a number and the other one
 will increase the number by 10. Assign these two decorators to a function such that first the 
 square of the no will be done and then 10 will be added and then the function operation will be done.'''

# def dec_squaring_num(func):
#     print("Decorator 1",func)
#     def inner_func(x):
#          sq=x**2
#          print(f"Square of {x}: ",sq)
#          return func(sq)
#     return inner_func
#
# def dec_add_10(func):
#     print("Decorator 2",func)
#     def inner_func(x):
#         val=x+10
#         print("Addition by 10: ",val)
#         return func(val)
#     return inner_func
#
# @dec_squaring_num
# @dec_add_10
# def main_func(x):
#     print("Final value:  ",end="")
#     return x*1000
#
# print(main_func(10))

'''3. Create a decorator with 2 parameters. Assign these decorator to a function 
which also has 2 parameters. Multiply the parameters passed in the decorator and pass it to the function 
which is decorated by this decorator as an argument when calling the function from decorator.'''

# def dec_with_args(x,y):
#     def dec_func(func):
#         def inner_func(a):
#             print(x,y)
#             z=x*y
#             return func(z,a)
#         return inner_func
#     return dec_func
#
# @dec_with_args(5,3)
# def main_func(x,y):
#     print(x,y)
#     z=x*y
#     return z
#
# print(main_func(4))

'''4. Send an email using only plain text.'''

# import smtplib
# import email
#
# msg =input("Enter your msg here: ")
# server=smtplib.SMTP('smtp.gmail.com')
# server.starttls()
# server.login('yadavharsha2799@gmail.com','ltrwgbuemhrtuemo')
# server.sendmail('yadavharsha2799@gmail.com','vishal.smarty1234@gmail.com',msg)
# server.quit()
# print("Mail sent")

'''5. Send an email using HTML Text.'''

# import smtplib
# from email.mime.text import MIMEText
#
# sender_id ='yadavharsha2799@gmail.com'
# reciever_id='vishal.smarty1234@gmail.com'
# pwd='ltrwgbuemhrtuemo'
#
# html_text ='''
# <html>
#   <body>
#     <p>Hi,<br>
#        This is html text msg...<br>
#     </p>
#   </body>
# </html>
# '''
# msg =MIMEText(html_text,"html")
#
# server =smtplib.SMTP_SSL('smtp.gmail.com')
# server.login(sender_id,pwd)
# server.sendmail(sender_id,reciever_id,msg.as_string())
# server.quit()
# print("Mail sent")

'''6.Send an email including HTML text and also 2 attachments one pdf file and one jpeg file.'''
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email import encoders
# from email.mime.base import MIMEBase
# from email.mime.image import MIMEImage
#
# sender_id ='yadavharsha2799@gmail.com'
# reciever_id='vishal.smarty1234@gmail.com'
# pwd='ltrwgbuemhrtuemo'
#
# html_text ='''
# <html>
#   <body>
#     <p>Hi,<br>
#        This is html text msg...<br>
#     </p>
#   </body>
# </html>
# '''
# msg=MIMEMultipart()
# html_msg =MIMEText(html_text,"html")
# msg.attach(html_msg)
# filename = "Python.pdf"
# img="bird.jpeg"
#
# with open(filename, "rb") as attachment:
#
#     part = MIMEBase("application", "octet-stream")
#     part.set_payload(attachment.read())
#
# encoders.encode_base64(part)
# part.add_header(
#     "Content-disposition",
#     f"attachment; filename= {filename}",
# )
#
# with open(img, "rb") as attachment:
#     part2=MIMEImage(attachment.read(),"jpeg")
#
# encoders.encode_base64(part2)
# part2.add_header(
#     "Content-disposition",
#     f"attachment; filename= {img}",
# )
# msg.attach(part)
#
# msg.attach(part2)
#
# server =smtplib.SMTP_SSL('smtp.gmail.com')
# server.login(sender_id,pwd)
# server.sendmail(sender_id,reciever_id,msg.as_string())
# server.quit()
# print("Mail sent")

'''7. Receive an email and print the detial of from, to, subject. Also parse the content of the attachment and if pdf or jpeg file'''
# import imaplib
# import email
#
# imap_server='imap.gmail.com'
# emai_id='yadavharsha2799@gmail.com'
# pwd='ltrwgbuemhrtuemo'
#
# imap=imaplib.IMAP4_SSL(imap_server)
# imap.login(emai_id,pwd)
#
# imap.select("Inbox")
# _, msgnums=imap.search(None,"FROM","Phonepe")
# print(msgnums)
# for msgnum in msgnums[0].split():
#     _,data = imap.fetch(msgnum,"(RFC822)")
#
#     message =email.message_from_bytes(data[0][1])
#     print(f"From: {message.get('From')}")
#     print(f"To: {message.get('To')}")
#     print(f"Subject: {message.get('Subject')}")
#     print("Content: ")
#     for part in message.walk():
#         if part.get_content_type() == "text/plain":
#             print(part.as_string())
#         elif part.get_content_type() == 'text/html':
#             print("TH", part.get_payload())
#         elif part.get_content_type() == 'image/jpeg':
#             print("IJ", part.get_payload())
#         elif part.get_content_type() == 'application/pdf':
#             print("AP", part.get_payload())
# imap.close()
'''8. Create a module which has 4 methods. Create another python file where this module’s methods will be
 used multiple times. Check the time utilized for these methods. Add different sleeping durations for all the methods. 
 Display the profiling using the pstats library.'''

# import func_file
# import pstats
# import time
# import cProfile
#
# pr = cProfile.Profile()
# pr.enable()
#
# cProfile.run("print(func_file.add(5,6))")
# time.sleep(3)
# cProfile.run("print(func_file.div(5,6))")
# time.sleep(6)
# cProfile.run("print(func_file.sub(5,6))")
# time.sleep(9)
# cProfile.run("print(func_file.mul(5,6))")
#
# pr.disable()
# ps = pstats.Stats(pr)
# ps.print_stats()




'''9. Read a python file and perform profiling on it.'''
# import cProfile
# f1 = open('half_diamond.py', 'r')
# f_str = f1.read()
# cProfile.run(f_str)

'''10. Create a Thread that will print random numbers between the given number at the time of Thread Creation.
 Create 3 objects with different numbers. Thread 1 (1-10),Thread 2(11-20, Thread 3(21-30). 
 Add different sleep time for each thread and print the random numbers between the given numbers by specific threads.'''

# import threading
# import time
# import random
#
# class myThread(threading.Thread):
#     def __init__(self, threadID, name, counter, delay,s_num,end_num):
#         super(myThread, self).__init__()
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#         self.delay = delay
#         self.s_num=s_num
#         self.end_num=end_num
#     def run(self):
#         print("Starting: "+self.name)
#         create_rand_val(self.name,self.counter,self.delay,self.s_num,self.end_num)
#         print("\nExiting: "+self.name)
#
#
# def create_rand_val(threadname,counter,delay,a,b):
#     while counter:
#          time.sleep(delay)
#          print(f"{threadname}:",random.randint(a,b))
#          counter -=1
#
# thread1 = myThread(1, "Thread-1", 3, 3,1,10)
# thread2 = myThread(2, "Thread-2", 4, 2,11,20)
# thread3 = myThread(3, "Thread-3", 5, 5,21,30)
#
# thread1.start()
# thread2.start()
# thread3.start()
#
# print("Exiting Main Thread")

'''11. The same above example should first print 5 random numbers from first thread then 5 random 
numbers from second thread and then it should print 5 random numbers from 3rd thread using syncrhonization.'''

# import threading
# import time
# import random
#
# class myThread (threading.Thread):
#
#     def __init__(self, threadID, name, counter, delay, s_num, end_num):
#         super(myThread, self).__init__()
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#         self.delay = delay
#         self.s_num = s_num
#         self.end_num = end_num
#
#     def run(self):
#       print("Starting " + self.name)
#       threadLock.acquire()
#       create_rand_val(self.name,self.counter,self.delay,self.s_num,self.end_num)
#       print("Exiting " + self.name)
#       threadLock.release()
#
#
# def create_rand_val(threadname,counter,delay,a,b):
#     while counter:
#          time.sleep(delay)
#          print(f"{threadname}:",random.randint(a,b))
#          counter -=1
#
# threadLock = threading.Lock()
# print("LOCK", threadLock)
#
#
#
# thread1 = myThread(1, "Thread-1", 5, 3,1,10)
# thread2 = myThread(2, "Thread-2", 5, 2,11,20)
# thread3 = myThread(3, "Thread-3", 5, 5,21,30)
#
#
# thread1.start()
# thread2.start()
# thread3.start()

# print("Exiting Main Thread")

'''12. Make your main thread to wait until all the child threads have completed their execution.'''
# import threading
# import time
# import random
#
# class myThread (threading.Thread):
#
#     def __init__(self, threadID, name, counter, delay, s_num, end_num):
#         super(myThread, self).__init__()
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#         self.delay = delay
#         self.s_num = s_num
#         self.end_num = end_num
#
#     def run(self):
#       print("Starting " + self.name)
#       threadLock.acquire()
#       create_rand_val(self.name,self.counter,self.delay,self.s_num,self.end_num)
#       print("Exiting " + self.name)
#       threadLock.release()
#
#
# def create_rand_val(threadname,counter,delay,a,b):
#     while counter:
#          time.sleep(delay)
#          print(f"{threadname}:",random.randint(a,b))
#          counter -=1
#
# threadLock = threading.Lock()
# print("LOCK", threadLock)
#
#
#
# thread1 = myThread(1, "Thread-1", 3, 3,1,10)
# thread2 = myThread(2, "Thread-2", 4, 2,11,20)
# thread3 = myThread(3, "Thread-3", 5, 5,21,30)
#
#
# thread1.start()
# thread2.start()
# thread3.start()
#
# threads = []
#
# threads.append(thread1)
# threads.append(thread2)
# threads.append(thread3)
#
# for t in threads:
#     t.join()
#
#
# print("Exiting Main Thread")

'''13. Create 4 methods in the Server Socket file. Call these methods from child. 
Specify the method in the send() method from the child and interpret it in the server. 
Send minimum 2 parameters for each method. The result should be returned to the client socket and printed over there.'''

import socket

host = socket.gethostname()
port = 2323
s = socket.socket()
s.bind((host, port))

s.listen(5)


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def sub(a, b):
    return a - b

while True:
    conn, addr = s.accept()
    print("Connected by ", addr)
    data = conn.recv(1024)
    print(conn)
    if data:
        print("Data Received", data)
        dt = data.decode('utf-8')
        print("DT", dt)
        d = dt.split(",")
        print("Data Received string", d)


        if d[0] =="1":
            data_add = add(int(d[1]), int(d[2]))
        if d[0] =="2":
            data_add = sub(float(d[1]), float(d[2]))
        if d[0] =="3":
            data_add = mul(float(d[1]), float(d[2]))
        if d[0] =="4":
            data_add = div(float(d[1]), float(d[2]))

        conn.send(str(data_add).encode('utf-8'))
conn.close()

'''14. Call any URL and receive the response for it. Print the response text and url.'''

# import requests
#
# response = requests.get("https://www.instagram.com/")
# print(response, type(response))
# print(response.text)
# print(response.url)

'''15. Call a URL which accepts input and pass it in json format and receive the response in json format.'''
import requests

user_dict = {
    "jsonrpc": "2.0",
    "params": {
        "db": "",
        "login": "admin",
        "password": "admin"
    }
}
# #
response = requests.post('http://0.0.0.0:5432/web/session/authenticate', json=user_dict)
print(response.json())