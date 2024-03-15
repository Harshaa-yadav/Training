'''todo:Exception Handling, Modules, File Management and Python Modules / Standard Libraries, Power of Python, Built In Functions'''
import datetime
from _stat import S_IWGRP
from stat import S_IXUSR

'''1. Generate Atleast 5 different Errors.'''

# #ZeroDivisionError: division by zero
# x= 5
# y=0
# z=x/y
# print(z)


# #IndexError: list index out of range
# x=[]
# print(x[0])

# # ValueError: invalid literal for int() with base 10: 'd'
# x=int(input("Enter any number: "))
# print(x)

# ValueError: too many values to unpack (expected 2)
# x=(1,2,3)
# a,b=x

# # KeyError: 'gamma'
# my_dict={'alpha':"Mall",'beta':"Square"}
# print(my_dict['gamma'])

# # FileNotFoundError: [Errno 2] No such file or directory: 'testing.txt'
# f1=open("testing.txt",'r')
# f_str=f1.read()
# print(f_str)

'''2. Handle all the 5 different Erros using Exception Handling.'''

# a= 5
# b=0
# x=[]
# my_dict={'alpha':"Mall",'beta':"Square"}
# x=(1,2,3)
#
#
# try:
#     # z=a/b
#     # print(z)
#     # print(x[0])
#     # print(my_dict['gamma'])
#     # a, b = x
#     f1 = open("testing.txt", 'r')
#     f_str=f1.read()
#     print(f_str)
#
#
#
# except ZeroDivisionError as ze:
#     print(ze)
# except IndexError as ie:
#     print(ie)
# except KeyError as ke:
#     print(ke +" key not found")
# except ValueError as ve:
#     print(ve)
# except FileNotFoundError as fe:
#     print(fe)
# except Exception as e:
#       print(e)

'''3. Handle an error with try-except-else.'''

# x=int(input("Enter dividend: "))
# y=int(input("Enter divisor: "))
# try:
#     div=x/y
#     print(div)
# except ZeroDivisionError as e:
#     print("ERROR: ",e)
# else:
#     print(divmod(x,y))

'''4. Handle an error with try-except-else-finally.'''
# x=int(input("Enter dividend: "))
# y=int(input("Enter divisor: "))
# try:
#     div=x/y
#     print(div)
# except ZeroDivisionError as e:
#     print("ERROR: ",e)
# else:
#     print(divmod(x,y))
# finally:
#     del(div)

'''5. Use raise for generating User Defined Exception for minimum length of a list
should be 5.'''
#
# lis=[1,2,3,4,5]
# if(len(lis)<5):
#     raise Exception("List should have atleast 5 elements")
# lis.append(6)
# print(lis)

'''6. Create a file 'mod.py' with a class with multiple methods and few member
variables. Also create an individual methods outside the class as well. Create
another file 'test.py' and without executing the 'mod.py' get it executed using the
'test.py' file.'''
# import mod

'''7. Using the above mentioned files 'test.py' and 'mod.py'. In 'test.py' create an object
of the class defined in the 'mod.py'. Call the methods using the object. Make sure
only that class is accessible and not the individual method to execute.'''
### In test.py
# from mod import Operation
#
# op=Operation()
# res=op.sub(10,5)
# print(res)
# res=op.mul(10,5)
# print(res)
# res=op.power(10,5)
# print(res)

'''8. Using the files 'test.py' and 'mod.py' call the individual method which is defined
outside the class in 'mod.py' and call in it test.py. Make sure only that method
from the file 'mod.py' is accessible in 'test.py'.'''

# from mod import add
#
# print(add(15,5))
# # op=Operation() #NameError: name 'Operation' is not defined

'''9. Create a package containing multiple modules. Import the package and use the
features of the modules inside the package.'''
#
# from my_package import mod,mod2
# import my_package
# #
# print(my_package.mod.add(11,11))
#
# row =int(input("Enter number of rows : "))
# my_package.mod2.pattern(row)

'''10. Use the above package’s only one module.'''

# from my_package import mod2
# import my_package.mod2
# row =int(input("Enter number of rows : "))
# my_package.mod2.pattern(row)

'''11. Use only specific class and methods of one of the module of the package.'''
#
# from my_package.mod import Operation
# op= Operation()
#
#
# print(op.mul(66,7))
# # print(mod.add(6,7))  #Errorrrrr

'''12.Create a script/program to open a file to write a string. Write a string in a file
'test_file.txt'.'''
# f1=open('test_file.txt','w')
# f1.write("This File is created programmatically!!! \n This is python exercise -3. \n Next topic is advance python.")
# f1.close()

'''13.Create a script/program to open a file 'test_file.txt' to read a string. Read the
whole string content from the file and print it.'''

# f1=open('test_file.txt','r')
# # print(f1.readline())
# # print(f1.readline())
# # # print(f1.readline())
# print(f1.read())
# f1.close()

'''14.Create a script/program to open a file 'test_file.txt' to read the content line by line
and print it.'''

# f1=open('test_file.txt','r')
# print(f1.readline())
# # print(f1.readline())
# print(f1.read())
# f1.close()

'''15.Create a script/program to open a file 'test_file.txt' to append a string at the end of
the existing string in a file.'''

# f1=open('test_file.txt','a')
# f1.write("\n This File is being appended by new line.......")
# f1.close()

'''16.Create a script/program to write and read binary data in a file 'test_file.data'.'''

# import pickle
# # f1=open('test_file.data','wb')
# # pickle.dump("Hello World",f1)
# # f1.close()
# f1=open('test_file.data','rb')
# print(pickle.load(f1))
# f1.close()

'''17. Using pickle dump no of variables with different data types in a file
'my_variables.data'.'''

# import pickle
#
# x=0
# y=0.5
# z='alpha'
# k=True
# lis=[1,2,3,4]
# tup=(1,2,3)
# st={1,25,9}
# dic={'a':1,'b':3}
# f1= open('my_variables.data','wb')
# pickle.dump(x,f1)
# pickle.dump(y,f1)
# pickle.dump(z,f1)
# pickle.dump(k,f1)
# pickle.dump(lis,f1)
# pickle.dump(tup,f1)
# pickle.dump(st,f1)
# pickle.dump(dic,f1)
# f1.close()

'''18.Create another script/program and read the dumped variables in the file
'my_variables.data'.'''
# import pickle
# f1 =open('my_variables.data','rb')
# x=pickle.load(f1)
# y=pickle.load(f1)
# z=pickle.load(f1)
# k=pickle.load(f1)
# lis=pickle.load(f1)
# tup=pickle.load(f1)
# st=pickle.load(f1)
# dic=pickle.load(f1)
# # x=pickle.load(f1)
# print(x,type(x))
# print(y,type(y))
# print(z,type(z))
# print(k,type(k))
# print(lis,type(lis))
# print(tup,type(tup))
# print(st,type(st))
# print(dic,type(dic))
# f1.close()
# # print(x)   #EOFError: Ran out of input



'''19.Print the current date using datetime and date libraries.'''

# import datetime
# print(datetime.date.today())
# print(datetime.datetime.now())
# print(datetime.date(2024,2,6))


'''20.Convert a datetime to a string.'''
# from datetime import date
#
# dt=date.today()
# print(dt,type(dt))
#
# cr_dt=date(2024,2,6)
# cdt=cr_dt.strftime('%d.%m.%y')
# print(cdt,type(cdt))
#
# cr_time=datetime.datetime.now()
# c_time=cr_time.strftime('%H:%M:%S')
# print(cr_time,type(cr_time))
# print(c_time,type(c_time))

'''21.Get the difference between two dates in days.'''
# import datetime
# dt1=datetime.date(1999,3,27)
# dt2=datetime.date.today()
# diff=dt2-dt1
# print(diff.days,type(diff))

'''22.Calculate your age in years, months and days.'''
#
# from dateutil.relativedelta import relativedelta
# import datetime
# # birthdate = "27-03-1999"
# # birthdate = datetime.datetime.strptime(birthdate, '%d-%m-%Y').date()
# birthdate=datetime.date(1999,3,27)
# cur_dt = datetime.date.today()
# age_year = relativedelta(cur_dt, birthdate).years
# age_months = relativedelta(cur_dt, birthdate).months
# age_days = relativedelta(cur_dt, birthdate).days
# print(f"your age is {age_year} years {age_months} months {age_days} days")

'''23.Get the date which is 1 week from today's date.'''
# from dateutil.relativedelta import relativedelta as rd
# import datetime
#
# cur_dt=datetime.date.today()
# new_dt=cur_dt+rd(weeks=1)
# print(new_dt)

'''24.Get the date which is 1 year from today's date.'''
# from dateutil.relativedelta import relativedelta as rd
# import datetime
#
# cur_dt=datetime.date.today()
# new_dt=cur_dt+rd(years=1)
# print(new_dt)

'''25.Get the date which is 1 month from today's date.'''
# from dateutil.relativedelta import relativedelta as rd
# import datetime
#
# cur_dt=datetime.date.today()
# new_dt=cur_dt+rd(months=1)
# print(new_dt)

'''26.Get the 1st day of the current month from today's date.'''
# import datetime
#
# cur_dt=datetime.date.today()
# x = cur_dt.replace(day = 1)
# print(x.weekday())
# print(datetime.date.strftime(x,'%A'))

'''27.Get the 1st month of the current year from today's date.'''

# import datetime
#
# cur_dt=datetime.date.today()
# x = cur_dt.replace(month = 1)
# print(x.month)
# print(datetime.date.strftime(x,'%B'))

'''28.Get the dates of current month starting from Monday to Sunday in a list.'''
# import calendar
# print(calendar.monthcalendar(2024,2))

'''29. Get the first date and last date of the current month.'''
# import datetime
# from dateutil.relativedelta import relativedelta as rd
# first_dt=datetime.date.today().replace(day=1)
# print("First date of the month:",datetime.datetime.strftime(first_dt,'%d.%m.%Y'))
# # res=calendar.monthrange(2024,2)
# l_date=first_dt + rd(day=31)
# print("Last date of the month:",l_date.strftime('%d.%m.%Y'))

'''30.Get me the 1st and last date of the current month in the format as following. '14th
June 2016 Tuesday 10:00:00 AM' '''

# import datetime
# from dateutil.relativedelta import relativedelta as rd
#
# def special_strftime(dic,x):
#     x = datetime.datetime.strftime(x,'%d')
#     return  ('th' if x[-2]=='1' else dic.get(x[-1],'th'))
# first_dt=datetime.datetime.now().replace(day=1)
# l_date=first_dt + rd(day=31)
#
# dic = {'1':'st','2':'nd','3':'rd'}
# suffix=special_strftime(dic,first_dt)
# print(f"First date of the month:",datetime.datetime.strftime(first_dt,f'%d{suffix} %B %Y %A %I:%M:%S %p '))
#
# suffix=special_strftime(dic,l_date)
#
# print(f"Last date of the month:",l_date.strftime(f'%d{suffix} %B %Y %A %I:%M:%S %p'))
#
# #



'''31.Get me random number from 1 to 100.'''

# import random
# print(random.randint(1,100))

'''32.Get me a random combination of 4 different numbers between 1 to 100.'''
# import random
# print(random.sample(list(range(1,101)),4))

'''33.You have a sorted list from 1 to 10 you have to unsort it.'''
# import random
# x=[1,2,3,4,5,6,7,8,9,10]
# random.shuffle(x)
# print(x)

'''34.Execute a shell script command from python code.'''
# import os
# os.system('ls')
# os.system('ls -l')
# os.chmod('swap.py',448)         #511
# print(os.getcwd())
# os.chdir('/Users/harshayadav')
# print(os.getcwd())
# os.chdir('/Users/harshayadav/PycharmProjects/PythonSky')
# print(os.getcwd())
# print(os.getgid())
# print(os.getgroups())
# # os.mkdir("Test_Package")
# # os.rmdir("Test_Package")
# print(os.times())

'''35.Create a regular expression to check a valid URL.'''
import re
str_1 = 'https://wwskyscendbs.com'
# mt = re.compile(r'^https?://(www/.)?[a-z]{1}[a-zA-Z0-9]*(\.[a-z]{2,3})*$')
mt = re.compile(r'^(https?|ftp)://(?:www\.)?[^\s/$.?#]+\.[^\s]*$')

res=mt.match(str_1)
print(res)

'''36. Create a regular expression to check a valid email.'''
'''37. Create a regular expression to check a valid Pin code of India.'''
import re
pin_code='384002'
pin_match_pattrn=re.compile('[1-9]{1}[0-9]{5}')
res=pin_match_pattrn.match(pin_code)
print(res)

'''38. Create a class Student and add member variables with False values. The variables
are as listed below. Marks will have a default value blank list.
1. Name
2. Reg No
3. Roll No
4. Standard
5. Admission Year
6. Marks
7. Result
Add a constructor that will assign Name, Reg No, Roll No, Standard, Admission
year. In the constructor add validation for Name to be only Alphabetic, Reg No to be
alphanumeric, Roll No, Standard nad Admission year to be numeric. All abobve
values will be accepted as string only. If the passed parameters are not string raise
and Error to the user.
Add a method that will accept a dictionary for marks containing subject as key and
marks as values. It will add the dictionary to the list of marks. Marks list will have
multiple elements and each element will be a dictionary only. Here there should be a
validation to acccept the marks which are less than or equal to 100 only. If the
obtained marks are less than 40 the result willl be fail otherwise pass. In the
dictionary the result can be added.

Add another method that will generate the result. This method will check if there
is any line in the marks having fail as result the result will be Fail and it will print the
complete result as following.
If any of the result is Fail the Percentage will not be shown and only -- will be
printed instead.
Define a function to calculate the grade. For Example if the result is fail for any
subject it will be F grade. If the Percentage is 95+ it will be O+. If the percentage is
90+ and less than 95 then it will be O. If the percentage is 85+ and less than 90 it will
be A+. If the Percentage is 80+ and less than 85 it will be A. If the Percentage is 75+
and less than 80 it will be a B+. If the percentgae is 70+ and less than 75 it will be B.
If the Percentage is 60+ and less than 70 it will be C. If the percentage is 50+ and
less than 60 it will be D. If the percetage is 40+ and less than 50 it will be E. The
Grade must be displayed on the result which is shown below.
*******************************************************************
Name : <Student Name>
Roll No : <Roll No> Standard: <Standard>
*******************************************************************
Subject Total Marks Passing Marks Obtained Marks Result
<Sub 1>    100       40     <obtained marks> <result>
<Sub 1>    100       40     <obtained marks> <result>
<Sub 1>    100       40     <obtained marks> <result>
*******************************************************************
TOTAL     <total>   <total>      <total>                 
Result: PASS / FAIL                         Percentage: <percentage>
Grade : <Obtained Grade>'''

# class Student:
#
#     def __init__(self,name='',reg_no='',roll_no='',standard='',admission_year=''):
#         if name.isalpha() and reg_no.isalnum() and roll_no.isnumeric() and standard.isnumeric() and admission_year.isnumeric() :
#             self.name=name
#             self.reg_no=reg_no
#             self.roll_no=roll_no
#             self.standard=standard
#             self.admission_year=admission_year
#         else:
#             print("Data is not in required format")
#         self.marks = []
#         self.result =""
#         self.grade=''
#
#     def add_marks(self,sub_dict):
#         # a=list(sub_dict.values())
#         for i,j in sub_dict.items():
#             if (j>100):
#                 print("Enter valid marks for" ,{i},"(",j,")")
#             if (j<40):
#                 # self.marks.append({i:{j:{'result':'fail'}}})
#                 self.marks.append({i:{j:'fail'}})
#
#             if(39<j<101):
#                 # self.marks.append({i:{j:{'result':'pass'}}})
#                 self.marks.append({i:{j:'pass'}})
#
#     def gradecal(self,percent):
#         if (percent >= 95):
#             self.grade = "O+"
#         elif (90 <= percent < 95):
#             self.grade = "O"
#         elif (85 <= percent < 90):
#             self.grade = 'A+'
#         elif (80 <= percent < 85):
#             self.grade = 'A'
#         elif (75 <= percent < 80):
#             self.grade = 'B+'
#         elif (70 <= percent < 75):
#             self.grade = 'B'
#         elif (60 <= percent < 70):
#             self.grade = 'C'
#         elif (50 <= percent < 60):
#             self.grade = 'D'
#         elif (40 <= percent < 50):
#             self.grade = 'E'
#         else:
#             self.grade = 'F'
#
#     def show_result(self):
#         t_marks=100
#         p_marks=40
#         a = []
#         obt_marks = 0
#
#
#
#         print("*"*90)
#         print("Name: ",self.name)
#         print("Roll No: ",self.roll_no,"Standard:".rjust(65),self.standard)
#         print("*" * 90)
#         print("Subject","Total Marks".center(20),"Passing Marks".center(20),"Obtained Marks".center(20),"Result".center(20))
#         for i in range(len(self.marks)):
#             for j in self.marks[i]:
#                  for k in self.marks[i][j]:
#                         print(j," "*7,t_marks," "*16,p_marks," "*16,k," "*18,self.marks[i][j][k])
#                         a.append(self.marks[i][j][k])
#                         obt_marks += k
#         # print(a)
#
#         percentage =obt_marks/3
#         percentage=round(percentage,2)
#
#         self.gradecal(percentage)
#         if 'fail' in a:
#                          self.result = 'Fail'
#                          prnt_per='--'
#
#         else:
#                         self.result = 'Pass'
#                         prnt_per = str(percentage) +"%"
#         print("*" * 90)
#         print("TOTAL"," "*9,t_marks*3," "*15,p_marks*3," "*15,obt_marks)
#         print("Result: ",self.result,"Percentage: ".rjust(65),prnt_per)
#         print("Grade: ",self.grade)
#
#
# sub=['Maths  ','Science','English']
# marks=[int(input(f"Enter marks for {x}: "))for x in sub]
# # print(marks)
# mark_dict={sub[i]:marks[i] for i in range(len(sub))}
# # print(mark_dict)
# obj=Student('Harshayadav','011','01','9','2015')
# obj.add_marks(mark_dict)
#
# obj.show_result()


'''39. Optimize the following code and make it in two lines.
x = {'a':1, 'b':2} – No Change
if 'c' in x:
y = x['c']
else:
y = 0'''

# x={'a':1,'b':2}
# y='c' in x and x['c'] or 0
# print(y)

'''40. Consider a variable which has string value “Skyscend Business Solutions Pvt.
Ltd.” print the following in one line.
◦ SKY
◦ SKYSCEND
◦ Bus
◦ solutions'''

# x='Skyscend Business Solutions Pvt.Ltd.'
# print(x[:3].upper(),x[:8].upper(),x[9:12],x[18:27].lower(),sep='\n')

'''41. Create a function using 'lambda' for exponent of a given number. Take two
arguments one as the number and the other one as the exponent.'''
# a=int(input("Enter first number: "))
# b=int(input("Enter Second number: "))
# z=lambda a,b:a**b
# print(z(a,b))

'''42. Create an assertion for a string to check the length of the string being minimum of
10 letters.'''

# x="HarshaYadav"
# print(len(x))
# assert len(x)>9,"Length of the string should be  minimum of 10 letters."

'''43. Read a file 'python.txt' which is containing python code and execute the python
code which is read from the file.'''
# f=open('python.txt','w')
# f.write('print("Hello, This is python.txt file")')
# f.close()
# f=open('python.txt','r')
# f_read=f.read()
# f.close()
# exec (f_read)

'''44. Using range get me a list of 1 to 10 and from this list generate a list as
[13,15,17,19,21,23,25,27,29,31]. Code needs to be done in one line only.'''

# lis_no=[ele for ele in range(1,11)]
# new_lis=list(map(lambda a,b:a+b,lis_no,range(12,22)))
# print(lis_no)
# print(new_lis)

# res = [num * 2+11 for num in range(1,11)]
# print(res)

'''45. Using range get me a list of even numbers between 1 to 100. Code needs to be
done in one line only.'''

# even_no_lis=[ele for ele in range(2,101,2)]
# print(even_no_lis)

# even_no_lis=[ele for ele in range(1,101) if ele%2==0]
# print(even_no_lis)

'''46. Generate a list of exponents of first 25 integers. Code needs to be in one line only.'''
# expo_lis=list(map(lambda x:x*x,range(1,26)))
# print(expo_lis)

'''47. Create a generator method to have the prime numbers using yield between 1 to 100.'''
# def gen_prime_no():

#     for x in range(2,101):
#         prime = True
#         for j in range(2,x):
#             if x%j ==0:
#                 prime=False
#         if prime :
#             yield x
#
# print(list(gen_prime_no()))

'''48. Create a generator method which gives random numbers between 1 to 100 and the
number not being repeated. Make sure it generates only 10 numbers.'''

# import random
# def gen_rand_no():
#     yield random.sample(range(1,101),10)
#
# print(list(gen_rand_no()))

'''49. Convert a decimal number '15' to binary, hexadecimal, octal numbers.'''
# x=15
# print(bin(x))
# print(hex(x))
# print(oct(x))

'''50. Convert a Hexadecimal number '10' to binary, decimal and octal numbers.'''
# x=0x10
# print(bin(x))
# print(int(x))
# print(oct(x))

'''51. Convert an Octal number '13' to binary, decimal and hexadecimal numbers.'''
# x=0o13
# print(bin(x))
# print(int(x))
# print(hex(x))

'''52. Convert Binary number '11010001111100111' to decimal, hexadecimal and octal
numbers.'''
# x=0b11010001111100111
# print(int(x))
# print(hex(x))
# print(oct(x))

'''53. Create a dictionary containing all the Capital Letters 'A-Z', Small Letters 'a-z', and
Digits '0-9' as keys and their ascii values as values using generators.'''
# my_dict={chr(i):i for i in range(65,91)}|{chr(i):i for i in range(97,121)}|{chr(i):i for i in range(48,58)}
#
# print(my_dict)


'''54. Get an absolute value of any negative integer.'''
# print(abs(-13))

'''55. Compare two numbers and get me the maximum number with a built-in function.'''
# print(max(66,666))

'''56. Create a class with member variables. Now perform the following.
1. Check whether an attribute exists in the class or not.
2. Fetch the value of an attribute of a class.
3. Update the value of an attribute of a class.
4. Delete the attribute of a class.'''

# class test:
#     mem_val=4
#     mem_str='hello'
#
# obj=test()
# print(hasattr(obj,"mem_val"))
# print(getattr(obj,'mem_str'))
# setattr(obj,'mem_str',44)
# print(getattr(obj,'mem_str'))
# delattr(obj,'mem_str')
# print(getattr(obj,'mem_str'))

'''57. Generate a list of having 10 elements using random but the numbers shoudl be
either 1 or 0. Check if all the elements are 1 print “ALL” and if any of the single
element is 1 print “ANY” and if all the elements are 0 print “NONE”.'''
# import random
# x=[random.randint(0,1) for i in range(10) ]
# print(x)
# if all(x) ==1:
#     print("ALL")
# elif any(x) ==1:
#     print("ANY")
# else:
#     print("NONE")

'''58. Get 10 random numbers in a list and get the maximum number from the list.'''
# import random
# res=[random.randrange(1,100) for i in range(10)]
# print(res)
# print(max(res))

'''59. Get 10 random numbers in a list and get the minimum number from the list.'''
# import random
# res=[random.randrange(1,100) for i in range(10)]
# print(res)
# print(min(res))

'''60. Get 10 random numbers from 1 to 100 in a list and create two separate lists from
it for odd and even numbers using filter.'''
# import random
# res=[random.randrange(1,100) for i in range(10)]
# print(res)
# even_lis=list(filter(lambda x:x%2==0,res))
# print(even_lis)
# odd_lis=list(filter(lambda x:x%2!=0,res))
# print(odd_lis)


'''61. Using map generate cubes of first 10 numbers.'''
# print(list(map(lambda x:x*x*x,range(1,11))))

'''62. Using map generate a list from two lists by multiplying the elements in the two
lists on the identical indexes in both the lists.'''
# l1=[1,5,7,8]
# l2=[3,5,6,7,8]
# print(list(map(lambda x,y:x*y,l1,l2)))

'''63. Generate 15 random numbers from 1 to 100 and get the total of all these numbers.'''
# import random
# res=[random.randrange(1,100) for i in range(15)]
# print(sum(res))

'''64. Get a list of 10 random characters and then merge all the characters in a single string.'''
# import random
# res=[chr(random.randrange(65,91)) for i in range(15)]
# print(res)
# print(''.join(res))

'''65. Create a class with few methods and in one of the method get all the global attributes that can be 
used in that method and also the local attributes that can be used in that method.'''

# class attr_test:
#     glb_var="global"
#     def __init__(self,loc_var_con):
#         self.local_var1=loc_var_con
#     def meth(self):
#         self.loc_var_meth="local var of meth"
#         return self.loc_var_meth
#
#     def meth2(self):
#         self.meth()
#         loc_var_meth2=self.glb_var
#         loc_var2_meth2=self.local_var1
#         loc_var3_meth2=self.loc_var_meth
#         return loc_var_meth2,loc_var2_meth2,loc_var3_meth2
#
#
# obj=attr_test("local")
# res=obj.meth2()
# print(res)

'''66. Create two classes one as a parent and the other as a child. Make a validation whether the child is a 
subclass of parent or not.'''
# class Parent:
#     def p_meth(self):
#         print("Parent method...")
#
# class Child(Parent):
#     def c_meth(self):
#         print("Child Method...")
#
# print(issubclass(Parent,Child))
# print(issubclass(Child,Parent))

'''67. Get two lists ['a','b','c','d','e'],[1,2,3,4,5] and generate a single dictionary 
{'a':1,'b':2,'c':3,'d':4,'e':5} with the identical indexed items.'''

# alpha_lis=[chr(ele) for ele in range(97,102)]
# num_lis=[ele for ele in range(1,6)]
# my_dict={alpha_lis[i]:num_lis[i] for i in range(len(alpha_lis))}
# print(my_dict)
#
# #todo:Optimized code
# my_dict={chr(i+96):i for i in range(1,6)}
# print(my_dict)

'''68. Sort a list of random 25 numbers between 1 to 100 without using the sort method.'''
# import random
#
# def sort_num(lis):
#     for i in range(len(lis)-1):
#         for j in range(len(lis)-1):
#             if lis[j]>lis[j+1]:
#                 lis[j],lis[j+1]=lis[j+1],lis[j]
#     return lis
#
# rand_num_lis = [random.randrange(1, 101) for i in range(25)]
# print(rand_num_lis)
# sort_lis=sort_num(rand_num_lis)
# print(sort_lis)

'''69. Sort the following list with the second element of the inner list. 
[[4, ’a’], [9, ’x’], [10, ’c’], [25,’z’], [32, ‘b’]].'''

# lis=[[4, 'a'], [9, 'x'], [10, 'c'], [25,'z'], [32, 'b']]
# lis.sort(key=lambda e:e[1])
# print(lis)
# print(sorted(lis,key=lambda e:e[1]))

'''70. Create a function for addition of two numbers. 
Create a validation that both of them must be either float or integer using a built in method.'''

# def addition(x,y):
#    res= isinstance(x,(int,float)) and isinstance(y,(int,float)) and x+y or 0
#    return res
# res=addition(4,5)
# print("Additon: ",res)

'''71. Create a function and a nested function inside this function. Assign variables outsie both the functions, 
define two variables inside the first function. Make on of the variables to be global. Define other two variable
inside the nested function and make one of them global. Now call the locals() and globals() function from 
outside both the functions, inside first function and inside the nested function and check what is available
as local and global variables which can be accessed.'''

# var1="Python"
# var2=5.6

# def outer_func():
#     global out_a
#     out_b=6.4
#
#     print("Local variables in outer_func: ",locals())
#     print("\nGlobal variables from outer_func: ",globals())
#
#
#     def inner_func():
#         global in_a
#         in_b=4
#         print("\nLocal variables in inner_func: ", locals())
#         print("\nGlobal variables from inner_func: ", globals())
#
#     inner_func()
#
# outer_func()
# print("\nLocal variables: ", locals())
# print("\nGlobal variables: ", globals())


