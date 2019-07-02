a1s = int(input())
b2s = list(map(int,input().split()))
c3s = []
e4 = []
for i in enumerate(b2s):
  c3s.append(i)
for i in range(0,len(b2s)):
  for j in range(0,len(b2s)):
    for k in range(0,len(b2s)):
      if(c3s[i][1] < c3s[j][1] < c3s[k][1]):
        if(c3s[i][0] < c3s[j][0] < c3s[k][0]):
          d = [c3s[i][1],c3s[j][1],c3s[k][1]]
          e4.append(d)
if(len(e4) != 0):
  print(len(e4))
else:
  print("0")
