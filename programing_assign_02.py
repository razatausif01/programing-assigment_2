#!/usr/bin/env python
# coding: utf-8

# ### Write a Python program to convert kilometers to miles?

# In[1]:


user_input=float(input("Enter your kilometer"))          ##1km=0.621371 miles
miles=0.621371
convert=user_input*miles
print(f"{user_input} = {convert} mile")


# ### 2.Write a Python program to convert Celsius to Fahrenheit?

# In[2]:


celsius = float(input("Enter Celcius: "))

#calculate fahrenheit using the formula
fahrenheit = (9/5)*celsius + 32
print("Fahrenheit ",fahrenheit)


# ### Write a Python program to display calendar?

# In[3]:


import calendar  
# Enter the month and year  
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))  
  
# display the calendar  
print(calendar.month(yy,mm))  


# ### Write a Python program to solve quadratic equation?
# 

# In[7]:


import cmath
a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


# ### Write a Python program to swap two variables without temp variable?

# In[8]:


x = 9
y = 2
print("Before swappig: ")
print("value of  x :",x," and y: ",y)
#code to swap 'x' and 'y'
x,y = y,x
print("after swapping: ")
print("Value of x :", x ," and y : ", y)


# In[ ]:




