#!/usr/bin/env python
# coding: utf-8

# In[5]:


animals={1:'name',
        'wild':"tiger",
        'domestic':'dog'}


# In[6]:


animals


# In[7]:


animals[1]


# In[8]:


animals.get('domestic')


# In[10]:


animals[1]='jungle'


# In[11]:


animals


# In[12]:


animals['cruel']='jaguar'


# In[13]:


animals


# In[14]:


txt=""
x = txt.zfill(10)

print(x)


# In[16]:


#Sting Methods
# To capitalize first letter
txt="lower case"
x=txt.capitalize()
print(x)


# In[17]:


#to convert Lowercase to Upper
txt="gowda"
x=txt.upper()
print(x)


# In[18]:


#to convert Upper to Lower
txt="GOWDA"
x=txt.lower()
print(x)


# In[19]:


# To convert upper to lower
x=txt.casefold()
print(x)


# In[20]:


# To convert all starting letters to upper case
txt=" i'm byre gowda from kolar"
x=txt.title()
print(x)


# In[ ]:


"""capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found

format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found


# In[25]:


#To return number of times a value occur
txt="apple,grapes,banana,pine apple"
x=txt.count("apple")
print(x)


# In[28]:


#To encode the given string
txt="Kolar Byre Gowda@1218"
x=txt.encode()
print(x)


# In[34]:


#Returns true if string ends with specified character
txt="pulsar,victor,glamour,gladiator,splendor"
x=txt.endswith("k")
y=txt.endswith("r")
print(x)
print(y)


# In[37]:


#Set tabspace of string
txt="h\te\tl\tl\to\t"
x=txt.expandtabs(5)
print(x)


# In[40]:


#find()	Searches the string for a specified value and returns the position of where it was found

txt="welcome to Golden city Kolar"
x=txt.find("to")
print(x)


# In[49]:


#format()	Formats specified values in a string
txt="Now it's only for{Price:5} Rupees"
print(txt.format(Price=10))


# In[51]:


#isalnum()	Returns True if all characters in the string are alphanumeric
txt="Kolar1218"
x=txt.isalnum()
print(x)


# In[52]:


#isalpha()	Returns True if all characters in the string are in the alphabet
txt="Kolar"
x=txt.isalpha()
print(x)


# In[56]:


#isascii()	Returns True if all characters in the string are ascii characters
txt="123455"
x=txt.isascii()
print(x)


# In[55]:


#isdecimal()	Returns True if all characters in the string are decimals
txt="1218.1"
txt1="1218"
x=txt.isdecimal()
y=txt1.isdecimal()
print(x)
print(y)


# In[58]:


#isdigit()	Returns True if all characters in the string are digits
txt="Kolar"
txt1="1218"
x=txt.isdigit()
y=txt1.isdigit()
print(x)
print(y)


# In[61]:


#isidentifier()	Returns True if the string is an identifier
txt="Fact"
txt1="123"
x=txt.isidentifier()
y=txt1.isidentifier()
print(x)
print(y)


# In[62]:


#islower()	Returns True if all characters in the string are lower case
txt="Gowda"
txt1="gowda"
x=txt.islower()
y=txt1.islower()
print(x)
print(y)


# In[63]:


#isnumeric()	Returns True if all characters in the string are numeric
txt="Kolar1218"
txt1="123"
x=txt.isnumeric()
y=txt1.isnumeric()
print(x)
print(y)


# In[64]:


#isprintable()	Returns True if all characters in the string are printable
txt="Golden City"
x=txt.isprintable()
print(x)


# In[66]:


#isspace()	Returns True if all characters in the string are whitespaces
txt="welcome to Kolar"
txt1=" "
x=txt.isspace()
y=txt1.isspace()
print(x,y)


# In[68]:


#istitle()	Returns True if the string follows the rules of a title
txt="Welcome to Kolar"
txt1="Welcome To Kolar"
x=txt.istitle()
y=txt1.istitle()
print(x,y)


# In[70]:


#join()	Converts the elements of an iterable into a string
details=("Name","DOB","Mob")
x="$".join(details)
print(x)


# In[71]:


#ljust()	Returns a left justified version of the string
txt="Kolar"
x=txt.ljust(2)
print(x,"is my favorite city")


# In[72]:


#lstrip()	Returns a left trim version of the string
txt="     kolar    "
x=txt.lstrip()
print("In Karnataka",x,"is my Favorite")


# In[76]:


#maketrans()	Returns a translation table to be used in translations
txt="fisk kit"
x=txt.maketrans("k","h")
print(txt.translate(x))


# In[80]:


#partition()	Returns a tuple where the string is parted into three parts
txt="Kolar Is Golden City"
x=txt.partition("Golden")
print(x)


# In[81]:


#replace()	Returns a string where a specified value is replaced with a specified value
txt="Kolar Gowda"
x=txt.replace("Kolar","Byre")
print(x)


# In[84]:


#rfind()	Searches the string for a specified value and returns the last position of where it was found
txt=" python is  object oriented programming language"
x=txt.rfind("o")
y=txt.rfind("z")
print(x, y)


# In[86]:


#rindex()	Searches the string for a specified value and returns the last position of where it was found
txt="asdfghjklasfa"
x=txt.rindex("a")
print(x)


# In[87]:


#rjust()	Returns a right justified version of the string
txt="Kolar"
x=txt.rjust(20)
print(x,"is my Favorite")


# In[ ]:


#rpartition()	Returns a tuple where the string is parted into three parts


# In[88]:


#rsplit()	Splits the string at the specified separator, and returns a list
txt="Name, Fnmae,Mname"
x=txt.rsplit(",")
print(x)


# In[90]:


#rstrip()	Returns a right trim version of the string
txt="     Upendra     "
x=txt.rstrip()
print("In Kannada",x,"is my Role model")


# In[92]:


#split()	Splits the string at the specified separator, and returns a list
txt="one two three four"
x=txt.split()
print(x)


# In[93]:


#splitlines()	Splits the string at line breaks and returns a list
txt="welcome to Kolar\nGolden city of Karnataka"
x=txt.splitlines()
print(x)


# In[95]:


#startswith()	Returns true if the string starts with the specified value
txt="Python is Programming Language"
x=txt.startswith("s")
y=txt.startswith("P")
z=txt.startswith("p")
print(x,y,z)


# In[96]:


#strip()	Returns a trimmed version of the string
txt="    Kolar    "
x=txt.strip()
print("My native is",x,"and its a largest city")


# In[99]:


#swapcase()	Swaps cases, lower case becomes upper case and vice versa
txt="kolar Is golden CITY"
x=txt.swapcase()
print(x)


# In[105]:


#translate()	Returns a translated string
txt="Hello"
x=txt.translate("e")
print(x)


# In[103]:


#upper()	Converts a string into upper case
txt="GowdA"
x=txt.upper()
print(x)


# In[108]:


#zfill()	Fills the string with a specified number of 0 values at the beginning"""
txt="50"
x=txt.zfill(10)
print(x)

