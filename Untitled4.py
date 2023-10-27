#!/usr/bin/env python
# coding: utf-8

# #Q1
# 
# answer : a=6
# 
# a=0              # the value of a is zero at first
# def b():         #"b" function has the value "a" as a global value .a=c(a)
#     
#     global a     #the first time that "b" function is called,"a"=2,second time 2+2=4 and the third time 4+2=6
# 
#     a=c(a)
# def c(a):
#     return a+2
# #value a has been changed by b functions
# 

# #Q2
# 

# In[16]:


def fileLength(filename):
    try:
        infile = open(filename, 'r')
        content = infile.read()
        length = len(content)
        infile.close()
        print(length)
    except FileNotFoundError:
        print(f"File {filename} not found")
        # Ex:
fileLength('midterm.py')
fileLength('idterm.py')
fileLength('/Users/donyabonyadian/Downloads/Filelength.txt')



     


# #Q3
# 

# In[17]:


class Marsupial:
    def __init__(self):
        self.pouch = []

    def put_in_pouch(self, item):
        self.pouch.append(item)

    def pouch_contents(self):
        return self.pouch


class Kangaroo(Marsupial):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def jump(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"I am a Kangaroo located at coordinates ({self.x},{self.y})"


# Ex:
k = Kangaroo(0, 0)
print(k)  # O.p: I am a Kangaroo located at coordinates (0,0)
k.put_in_pouch('kitten')
k.put_in_pouch('doll')
k.put_in_pouch('firetruck')

print(k.pouch_contents())  # O.p: ['doll', 'firetruck', 'kitten']

k.jump(1, 0)
k.jump(1, 0)
k.jump(1, 0)
print(k)  # O.p: I am a Kangaroo located at coordinates (3,0)

    


# In[21]:


def collatz(x):
    if x == 1:
        print(x)
    else:
        print(x)
        if x % 2 == 0:
            collatz(x // 2)
        else:
            collatz(3 * x + 1)

# Ex:
collatz(10)


# In[22]:


#Q5
def binary(n):
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        binary(n // 2)
        print(n % 2)

# Ex:
binary(0)
binary(1)
binary(3)
binary(9)


# In[24]:


#Q6
from html.parser import HTMLParser

class HeadingParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_heading = False
        self.heading_level = 0

    def handle_starttag(self, tag, attrs):
        if tag.startswith('h') and len(tag) == 2 and tag[1].isdigit():
            self.in_heading = True
            self.heading_level = int(tag[1])

    def handle_endtag(self, tag):
        if self.in_heading:
            self.in_heading = False

    def handle_data(self, data):
        if self.in_heading:
            indentation = " " * self.heading_level
            print(f"{indentation}{data}")

# Ex:
with open('/Users/donyabonyadian/Downloads/w3c (2).txt') as infile:
    content = infile.read()

hp = HeadingParser()
hp.feed(content)


# In[29]:


#Q7
import requests
from bs4 import BeautifulSoup

def webdir(url, depth, indent):
    if depth < 0:
        return

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        print(' ' * indent + url)

        if depth > 0:
            for link in soup.find_all('a'):
                href = link.get('href')
                if href and href.startswith('http'):
                    webdir(href, depth - 1, indent + 2)
    except requests.exceptions.RequestException:
        pass

# Ex:
webdir('https://gc.blackboard.com/ultra/courses/_366152_1/outline/assessment/_10140789_1/overview/attempt/_25890886_1?courseId=_366152_1', 2, 1)


# In[10]:


#Q8

SELECT temperature FROM weather_data;
SELECT DISTINCT city FROM weather_data;
SELECT * FROM weather_data WHERE country = 'India';
SELECT * FROM weather_data WHERE season = 'Fall';


# In[7]:


#Q9
words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
upper_words = [word.upper() for word in words]
lower_words = [word.lower() for word in words]
word_lengths = [len(word) for word in words]
word_info = [[word.upper(), word.lower(), len(word)] for word in words]
long_words = [word for word in words if len(word) >= 4]
print(upper_words )
print(lower_words)
print(word_lengths)
print(word_info)
print(long_words)


# In[ ]:




