#!/usr/bin/env python
# coding: utf-8

# In[5]:


string1="Kolar"
string2="Gowda"
findStr=" Kolar District"
if string1 in findStr:
    print("There is " + string1 + " in " + findStr)
if string2 not in findStr:
    print("Huf! No " + string2 +" in " + findStr)
    


# In[28]:


myList=[10,20,3,0,50,60,"Fname","Lname",]
print(myList)
myList[2]=30
print(myList)
myList.append("DOB")
print(myList)
myList.insert(3,40)
print(myList)
del myList[4]
myList


# In[30]:


var = "python_interpreter"
val="python_interpreter"
print(var[1:3])
print(var[0:5])
print(var[-5:-2])
print(var[:3])
print(var[3:])
print(var[:])
print(val[3:10])
print(val[2:5])
print(val[0:10])
print(val[5:-5])
print(val[2:8])
print(val[:8])
print(val[5:])
print(val[8:12])
print(val[12:5])


# In[34]:


var = "java_compiler_go"
print(var[2:10])
print(var[2:10:1])
print(var[2:10:2])
print(var[2:10:3])
print(var[-12:10])
print(var[-12:10:1])
print(var[-12:10:2])
print(var[-12:10:3])
print(var[5::1])
print(var[5::2])
print(var[:5:1])
print(var[:-5:1])
print(var[-8::2])


# In[35]:


val="arithmetic_operator"
print(val[3:10:1])
print(val[3:10:2])
print(val[3:10:3])
print(val[5:-5:1])
print(val[5:-5:2])
print(val[5:-5:5])
print(val[:8:4])
print(val[5::3])
print(val[::2])
print(val[12:5:3])


# In[ ]:




