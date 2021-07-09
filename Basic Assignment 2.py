#!/usr/bin/env python
# coding: utf-8

#     Q1. True and False are two values of boolean data type. We write them as True and False.
#     Q2 . Three different types of boolean operators are AND , OR , NOT.
#     Q3. AND 1)True and True = True 2)True and False = False 3)False and True = False 4)False and False = False
#         OR 1) True or True = True 2) True and False = True 3) False or True = True 4) False or False = False
#         NOT 1)True = False 2) False= True
#     Q4. 1)False 2)False 3)True 4)False 5)True
#     Q5. 1) == (equal) 2) != (not equal) 3) < (less than) 4) > (greater than) 5)<= (lesser than equal) 6) >= (greater than equal)
#     Q6. 1) Equal to operator: Equal to operator is written as "==". The equal to operator checks whether the given two values are equal or not . If they are equal it returns True and if they are not equal it returns False.It is used to compare two values.eg. 5 == 5 this is True and it returns 1.
#     2) Assignment operator: Assignment operator is written as "=" . It assigns value to the variable. eg. a = 10.
#     Q7. if,if ,else this are the three blocks in the below code
#     
#         

# In[8]:


# Q8.
spam = 6
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")


# Q9. If programme is stuck in an endless loop , press CTRL + C keys to get out of an endless loop.
# Q10. Break - Break statement is used to stop the execution of remaining elements of the loop. It is used to exit or break the for and while loop in python.
# Continue - Continue statement doesnot print the current iteration of the loop .It will pass the control of the program to next iteration by skipping the current iteration.
# 
# Q11. In for loop, the output of range(10), range(0,10),range(0,10,1) are the same with no difference.The output of this three function is 0-9. In range(10) it includes range of first 10 numbers (i.e from 0 to 9), in range(0,10) it starts from first no. 0 to 9 it excludes last number. In range(0,10,1) output is 0 to 9 and 1 is the step size.

# In[5]:


#Q12.i)
for i in range(1,11):
    print(i)


# In[6]:


#Q12. ii)
i = 1
while i < 12:
    print(i)
    if i == 10:
        break
    i = i +1    
        


# Q13. After importing spam we can call this function as spam.bacon()
