s=input().split()
n,m=s[0],s[1]
if(n[0]=="-"):n=n[1:]+"-"
if(m[0]=="-"):m=m[1:]+"-"
if float(n[::-1])>float(m[::-1]):print(n[::-1])
else:print(m[::-1])
