import time
g=1
z='trun.txt'
while g==1:
  for i in range(1000000):
  #while g==1:
    with open(z,'a') as v:
      v.write('1')
      time.sleep(5)
