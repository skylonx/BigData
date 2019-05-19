import sys
import apriori
import time

output = open("times_with_support6","w")

for i in [0.01,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]:
    starttime = time.time()
    AP = apriori.APriori(data="retail.txt",output="out")
    AP.find_frequent(6, stop_line=int(i*88000))
    totaltime = time.time()-starttime
    print("%.2f %.2f"%(i,totaltime), file=output)
    sys.stdout.flush()