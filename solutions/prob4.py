n=""
for c in input():
 if c.islower()or c==",":n+="0"
 elif c.isupper():n+="1"
 if len(n)==5:print(chr(65+int(n,2)),end="");n=""
