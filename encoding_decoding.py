import random
#encoding
word=input("Enter Taxt to convert into secreat langauage :")
if len(word)<=2:
    a=word[::-1]
    print(a)
elif len(word)>=3:
    s1=[]
    for i in range(1):
        s1.append(chr(random.randrange(ord('a'),ord('z')))+chr(random.randrange(ord('a'),ord('z')))+chr(random.randrange(ord('a'),ord('z')))) 
    
    starting=""
    starting=starting.join(s1)
    
    s2=[]
    for i in range(1):
        s2.append(chr(random.randrange(ord('a'),ord('z')))+chr(random.randrange(ord('a'),ord('z')))+chr(random.randrange(ord('a'),ord('z')))) 
    
    last=""
    last=last.join(s2)
    
    modify=word[1:]+word[0]
    add=starting+modify+last
    print(add)
   
#decoding  

word=input("Enter Taxt to decoding :")
if len(word)<=2:
    b=word[::-1]
    print(b)
else :
    mod=add[3:-3]
    org=mod[-1]+mod[0:-1]
    print(org)
    
       