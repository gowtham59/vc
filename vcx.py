aas = int(input())
bbs = list(map(int,input().split()))
ccs = []
ee = []
for i in enumerate(bbs):
  ccs.append(i)
for i in range(0,len(bbs)):
  for j in range(0,len(bbs)):
    for k in range(0,len(bbs)):
      if(ccs[i][1] < ccs[j][1] < ccs[k][1]):
        if(ccs[i][0] < ccs[j][0] < ccs[k][0]):
          d = [ccs[i][1],ccs[j][1],ccs[k][1]]
          ee.append(d)
if(len(ee) != 0):
  print(len(ee))
else:
  print("0")
