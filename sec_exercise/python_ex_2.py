'''todo 1. Get me list of odd numbers between 1 to 20 without using if condition.'''
import random

# print(list(range(1,20,2)))

'''2. Get a list of 1 to 20 then remove elements from list to get only even elements.'''
# a=[num for num in range(1,21)]
# print(a)
#
# def delete(no):
#     no%2!=0
#     a.remove(no)
# list(map(delete,a))
#
# print(a)

'''3. Get a list of 1 to 8 and then 4 to 10. Get the common elements from both the list in a new list.'''
# l1=[no for no in range(1,9)]
# l2=[num for num in range(4,11)]
# l3=[num for num in l1 if num in l2]
# print(l1)
# print(l2)
# print(l3)
'''4. Sort a shuffled list of 10 random numbers in descending order.'''
# ls=[35,45,67,23,32,34,12,87,68,90]
# ls.sort(reverse=True)
# print(ls)
'''5. x=(1,2,3,4,5), y=(4,5,6,7). Combine these two tuples in a single tuple ignoring the common elements.'''

# x=(1,2,3,4,5)
# y=(4,5,6,7)
# z=set(x).symmetric_difference(set(y))
#
# print(tuple(z))

'''6. Define two sets and perform all the set operations and validation operations.'''

# x={3,5,8,6,34}
# y={23,34,56,3,4,5}
#
# s1=x.difference(y)
# print(s1)
# s2=x.union(y)
# print(s2)
# s3=x.intersection(y)
# print(s3)
# s5=x.copy()
# s6=x
# x.add(9)
# print(x)
# print(s5)
# print(s6)
# x.remove(3)
# print(x)
# print(s5)
# x.discard(31)
# print(x)
# s8=y.pop()
# print(s8)
#
#
# #Validation operations
#
# print(x.issubset(y))
# print(x.issuperset(y))
# print(x.isdisjoint(y))

'''7. Generate a dictionary {1:1,2:1,3:1,4:1,...,10:1} in one line using dictionary's method.'''
# new_dict =dict.fromkeys(range(1,11),1)
# print(new_dict)
'''8. Print all the keys and values of a dictionary.'''
# new_dict={
#     'name':'Harsha',
#     'city':'Mehsana',
#     'country':'India'
# }
# print(list(new_dict.keys()))
# print(list(new_dict.values()))
# print(list(new_dict.items()))
'''9. Two dictionaries {'a':1,'b':2,'c':3}, {'a':4,'d':5,'e':6}. Merge these two dictionaries.'''
# dict1={'a':1,'b':2,'c':3}
# dict2={'a':4,'d':5,'e':6}
#
# new_dict=dict1 | dict2
# print(new_dict)

'''10. How to check whether a key is existing in a dictionary or not.'''
# new_dict={
#     'name':'Harsha',
#     'city':'Mehsana',
#     'country':'India'
# }
#
# print(new_dict.get('ram','not found'))

'''11. How can we have two variables refering to a single list, set and dictionary.'''
# a = [1,2,3,4,5]
# b=a
# print(id(a))
# print(id(b))
#
# a1={1,2,3,4}
# b1=a1
# print(id(a1))
# print(id(b1))
#
# a2={'a':'1','b':'2'}
# b2=a2
# print(id(a2))
# print(id(b2))

'''12. Use all the case methods of strings'''
# a='Harsha and harsh are children of Umrao Yadav'
# print(a.upper())
# print(a.lower())
# print(a.casefold())
# print(a.capitalize())
# print(a.swapcase())
# print(a.title())

'''13. How to split a string with a substring?'''
# a='Harsha and harsh are children of Umrao Yadav'
# print(a.split('ar'))

'''14. How to replace a string with a substring?'''
# a='Harsha and harsh are children of Umrao Yadav'
# print(a.replace('Umrao','Indira'))

'''15. How to join multiple strings with a substring?'''
# a=['Bella','cella','tella']
# print('ciao'.join(a))

'''16. How to make partition of a string?'''
# a='Harsha and harsh are children of Umrao Yadav'
# print(a.partition('harsh'))

'''17. How to find the no of occurences of a substring?'''
# a='Harsha Yadav and harsh yadav are children of Umrao Yadav'
# print(a.count('Yadav'))

'''18. Use all the validation methods used with string.'''
# a='Anappleadaykeepsdoctoraway'
# a1='1223.455'
# a1='1050'
# print(a.isalpha())
# print(a.isnumeric())
# print(a.isalnum())
# print(a1.isnumeric())
# print(a1.isdigit())
# print(a1.isdecimal())
# print(a.isidentifier())

'''19. Convert all the data structures to other data structures.'''
# l=[1,2,34,4,5]
# print(set(l))
# print(tuple(l))
# print(str(l))
# # print(dict(l))---Not possible
#
# s={1,2,3,4,4}
# print(list(s))
# print(tuple(s))
# print(str(s))
# # print(dict(s))---Not possible
#
# t=(2,3,4,5,5)
# t1=((2,3),(3,4))
# print(list(t))
# print(set(t))
# print(str(t))
# print(dict(t1))
#
# d={1:'a','2':'b'}
# print(set(d))
# print(list(d))
# print(tuple(d))

'''20. Get the last element of the list, tuple and string.'''
# l=[1,2,34,4,5]
# print(l[-1])
#
# t=(1,2,34,4,5)
# print(t[-1])
#
# s='Harsha'
# print(s[-1])

'''21. Get last 3 elements of the list, tuple and string'''
# l=[1,2,34,4,5]
# print(l[-1:1:-1])
#
# t=(1,2,34,4,5)
# print(t[-1:1:-1])
#
# s='Harsha'
# print(s[-1:-4:-1])

'''22. Get first 5 elements of list, tuple and string.'''
# l=[1,2,3,4,5,6,7,8,9]
# print(l[0:5:1])
# t=(1,2,3,4,5,6,7,8,12,34,2)
# print(t[0:5:1])
# s='Harsha Yadav'
# print(s[0:5:1])

'''23. Get all the elements excluding first and last elements from list, tuple and string'''
# l=[1,2,3,4,5,6,7,8,9]
# print(l[1:len(l)-1:1])
# t=(1,2,3,4,5,6,7,8,12,34,2)
# print(t[1:len(t)-1:1])
# s='Harsha Yadav'
# print(s[1:len(s)-1:1])

'''24. Get all the elements in a list using : operator.'''
# l=[1,2,3,4,5,6,7,8,9]
# print(l[::1])

'''25. Get last 5 elements from a list of 1 to 10 using negative indexing.'''
# l=[1,2,3,4,5,6,7,8,9,10]
# print(l[-1:-6:-1])

'''26. Get 4 elements of the list excluding last 2 elements using negative indexing.'''
# l=[1,2,3,4,5,6,7,8,9]
# print(l[-3:-7:-1])

'''27. Convert a list of tuple to dictionary.'''
# a=[(1,'a'),(2,'b'),(3,'c')]
# print(dict(a))

'''28. Create a dictionary using range() as following. {'a':1, 'b':2, 'c':3, 'd':4, 'e':5....'y':25, 'z':26}.'''
# Using dictionary comprehension and range()
# my_dict = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}
# # Print the resulting dictionary
# print(my_dict)

'''29. There are two lists [1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]. 
Get a third list from these two lists as [12,14,16,18,20,22,24,26,28,30].'''

# l1 = [1,2,3,4,5,6,7,8,9,10]
# l2 = [11,12,13,14,15,16,17,18,19,20]
#
# a = list(map(lambda x,y:x+y,l1,l2))
# print(a)

'''30. Get Square of all the elements in a list from 1 to 10 numbers.'''
# l1=[x*x for x  in range(1,11)]
# print(l1)
#
# y=[1,2,3,4,5,6,7,8,9,10]
# l1=list(map(lambda x:x*x,y))
# print(l1)

'''31. There are two lists [1,2,3,4,5], [4,5,6,7] get a list from these two lists [1,2,3,6,7].'''
# l1=[1,2,3,4,5]
# l2=[4,5,6,7]
# l3=set(l1).symmetric_difference(set(l2))
# print(list(l3))

'''32. Fetch the data from the following.
1. Fetch 5 which is the value of ‘e’ from below.
   x = {‘a’:1, ‘b’:2, ‘c’:3,’d’:[1,2,3,4,(5.6.7,{‘e’:5})]}
2. Fetch 2 from below which is marked in red. x = {‘a’:{‘b’:[1,2,(3,4,{‘c’:3,’d’:4,’e’:[1,2,3]})]}
3. Fetch 6 from below which is marked in red. x = [1, 2, (3, 4, 5, {‘a’:1, ‘b’:[2,3,4,(5,6)]})]
4. Fetch 2 from above which is marked in red.
x = {True:[1,2,3,{‘a’:1,’b’:2}],False:[(2,3,4,5,{1:2})]}
5. Fetch 9 from above which is marked in red.
x = {1:2,2:3,3:4,4:{‘a’:’b’,’c’:’d’,’e’:’f’,’f’:[1,2,3,{1:9,3:8}]}'''

# x = {'a':1, 'b':2, 'c':3,'d':[1,2,3,4,(5,6,7,{'e':5})]}
# print(x['d'][4][3]['e'])
#
# x={'a':{'b':[1,2,(3,4,{'c':3,'d':4,'e':[1,2,3]})]}}
# print(x['a']['b'][2][2]['e'][1])
#
# x = [1, 2, (3, 4, 5, {'a':1, 'b':[2,3,4,(5,6)]})]
# print(x[2][3]['b'][3][1])
#
# x = {True:[1,2,3,{'a':1,'b':2}],False:[(2,3,4,5,{1:2})]}
# print(x[False][0][4][1])
#
# x = {1:2,2:3,3:4,4:{'a':'b','c':'d','e':'f','f':[1,2,3,{1:9,3:8}]}}
# print(x[4]['f'][3][1])

'''33. Create a function for string that will check whether a string
 is having the first letter as Capital and not any other letter is capital.'''

# def check_string(x):
#
#          if x[0].isupper() and x[1::1].islower():
#              print("The first letter is Capital and not any other letter is capital")
#          else:
#              print("Not in the required format")
# x='Harsha Yadav'
#
# check_string(x)

'''34. Create a class Student and add member variables with False values. The variables are as listed below.
 Marks will have a default value blank list.
1. Name
2. Reg No
3. Roll No
4. Standard
5. AdmissionYear 
6. Marks
7. Result
Add a constructor that will assign Name, Reg No, Roll No, Standard, Admission year. 
In the constructor add validation for Name to be only Alphabetic, Reg No to be alphanumeric, 
Roll No, Standard nad Admission year to be numeric. All above values will be accepted as string only.

Add a method that will accept a dictionary for marks containing subject as key and marks as values. 
It will add the dictionary to the list of marks. Marks list will have multiple elements and each element will 
be a dictionary only. Here there should be a validation to accept the marks which are less than or equal to 100
only. If the obtained marks are less than 40 the result will be fail otherwise pass. In the dictionary the 
result can be added.....

Add another method that will generate the result. This method will check if there is any line
in the marks having fail as result the result will be Fail and it will print the complete result as following. 
*******************************************************************
Name : <Student Name>
Roll No : <Roll No>                           Standard: <Standard> 
*******************************************************************
Subject  Total Marks   Passing Marks    Obtained marks      Result
<Sub 1>     100             40          <Obtained marks>    result
<Sub 1>     100             40          <Obtained marks>    result
<Sub 1>     100             40          <Obtained marks>    result
*******************************************************************
TOTAL      <total>         <total>           <total>  
              
Result: PASS / FAIL                      Percentage: <percentage>'''


class Student:
    # name =""
    # reg_no=
    # roll_no=False
    # standard=False
    # admission_year=False
    # marks=False
    # result=False

    def __init__(self,name='',reg_no='',roll_no='',standard='',admission_year=''):
        if name.isalpha() and reg_no.isalnum() and roll_no.isnumeric() and standard.isnumeric() and admission_year.isnumeric() :
            self.name=name
            self.reg_no=reg_no
            self.roll_no=roll_no
            self.standard=standard
            self.admission_year=admission_year
        else:
            print("Data is not in required format")
        self.marks = []
        self.result =""

    def add_marks(self,sub_dict):
        # a=list(sub_dict.values())
        for i,j in sub_dict.items():
            if (j>100):
                print("Enter valid marks for" ,{i},"(",j,")")
            if (j<40):
                # self.marks.append({i:{j:{'result':'fail'}}})
                self.marks.append({i:{j:'fail'}})

            if(39<j<101):
                # self.marks.append({i:{j:{'result':'pass'}}})
                self.marks.append({i:{j:'pass'}})


        # print(self.marks[0])
        # print(self.marks)

        # val=list(map(lambda x:x>40,a))
    def show_result(self):
        t_marks=100
        p_marks=40
        obt_marks=0
        a = []
        print("*"*90)
        print("Name: ",self.name)
        print("Roll No: ",self.roll_no,"Standard:".rjust(65),self.standard)
        print("*" * 90)
        print("Subject","Total Marks".center(20),"Passing Marks".center(20),"Obtained Marks".center(20),"Result".center(20))
        for i in range(len(self.marks)):
             for j in self.marks[i]:
                 for k in self.marks[i][j]:
                        print(j," "*7,t_marks," "*16,p_marks," "*16,k," "*18,self.marks[i][j][k])
                        a.append(self.marks[i][j][k])
                        obt_marks += k
        # print(a)
        if 'fail' in a:
                         self.result = 'Fail'

        else:
                        self.result = 'Pass'
        print("*" * 90)
        print("TOTAL"," "*9,t_marks*3," "*15,p_marks*3," "*15,obt_marks)
        print("Result: ",self.result,"Percentage: ".rjust(65),((obt_marks)/300)*100,"%")




sub=['Maths  ','Science','English']
marks=[int(input(f"Enter marks for {x}: "))for x in sub]
# print(marks)
mark_dict={sub[i]:marks[i] for i in range(len(sub))}
# print(mark_dict)
obj=Student('Harshayadav','011','01','9','2015')
obj.add_marks(mark_dict)
obj.show_result()










