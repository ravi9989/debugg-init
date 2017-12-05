def replace(s,s0,si):
	s=list(s)
	s0=list(s0)
	for i in range(len(s)):
		if s0[i] is si:
			s[i]=si
	return "".join(s)
HANGMAN = [
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
"""]
import random
l = open('word','r').read().splitlines()
t=input("enter 1 to continue or -1 to terminate:")
while t!="-1":
    d=random.randint(0,len(l))
    n=len(l[d])
    s0=l[d]
    s="_"*n
    i=0
    while "_" in s and i<12:
    	print(s)
    	c=input("enter your choice:")
    	if c in s0:
    		s=replace(s,s0,c)
    	else:
    		print("---------------------------------------------------------",HANGMAN[i])
    		i+=1
    	if s == s0:
    		print("congrats you won :)")
    		break
    	if i==11:
    		print("you loose -_-")
    		break
    t=input("enter 1 to continue or -1 to terminate:")