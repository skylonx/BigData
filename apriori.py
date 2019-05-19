"""
@author Shaela Khan , 23rd feb, 2019
425 project#1 => apriori.py

Frequent itemset finding class APriori to implement Apriori algorithm using standard
libraries in Python 3. Input is provided textfile of per-row transactions of
space-separated integers for items. 
    Input : retail.txt
    Output : finds frequent pairs of 2 .
"""

from collections import Counter,defaultdict
from itertools import dropwhile

class APriori():

   
    def __init__(objcts,data,output):

        objcts.data = data
        objcts.output = output
        objcts.previous = []
        objcts.frequent = defaultdict(Counter)


    def find_frequent(objcts,support,min_set_size=2,stop_line=-1):

        objcts.threshold = support
        objcts.min_set = min_set_size
        objcts.frequent[1] = objcts.generate_data(stop_line)

        k = 2
      
        #while len(objcts.frequent[k-1]) >= k:
        if True:

            for i in range(len(objcts.previous)):
                
                k_minus_1 = [group for group in objcts.previous[i]
                if group in objcts.frequent[k-1]]

               
                cand = [tuple(sorted(frozenset(x).union(y))) for x in k_minus_1
                for y in k_minus_1 if x < y and x[:-1] == y[:-1]]

                # only those candidates need to be considered for the next pass
                objcts.previous[i] = cand

                # count objects
                for group in cand:
                    objcts.frequent[k][group] += 1

            # drop infrequent keys
            objcts.frequent[k] = objcts.dropping_infrequent(k)

            k += 1

       
       #write output file here.
        with open(objcts.output,"a") as f:
            for key in objcts.frequent.keys():
                if key >= objcts.min_set:
                    for k,v in sorted(objcts.frequent[key].items(),
                                      key=lambda x:(-x[1],x[0])):
                        print(key,v,*k,file=f)

        return


    def dropping_infrequent(objcts,k):
       
        for key,count in dropwhile(lambda key_ct: key_ct[1] >= objcts.threshold,
                                   objcts.frequent[k].most_common()):
                del objcts.frequent[k][key]

        print("Frequent {}-itemsets generated.".format(k))

        return objcts.frequent[k]


    def generate_data(objcts,stop_line):
    

        with open(objcts.data, "r") as f:
            l = 0
            for line in f.readlines():
                l += 1
                if stop_line>0 and l>stop_line: break;
             
                items = [tuple([int(item)]) for item in set(line.split())]

               
                if len(items) >= objcts.min_set:
                    # sort to avoid generating duplicate candidates
                    objcts.previous.append(sorted(items))
                    for item in items:
                        objcts.frequent[1][item] += 1

        objcts.frequent[1] = objcts.dropping_infrequent(1)

        return objcts.frequent[1]