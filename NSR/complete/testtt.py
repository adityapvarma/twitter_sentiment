
sent="textblob"
consol=[]

for i in [0,1,2,3]:
    for j in [0,1,2,3,4,5]:
        final=[]

        f=open(str(i)+"-"+str(j)+"_complete.txt","r")

        a=f.readlines()
        f.close()

        for j in range(len(a)):
            d=a[j].rstrip().split()
            if d!=[]:
                if d[0]=="Cluster":
                    temp=[]
                    temp.append(int(d[1]))

                elif d[0]==sent:
                    temp.append(float(d[1]))
                    final.append(temp)

        final.sort()

        for k in final:
            consol.append(k[1])


for i in [4]:
    for j in [0,1,2,3]:
        final=[]

        f=open(str(i)+"-"+str(j)+"_complete.txt","r")

        a=f.readlines()
        f.close()

        for j in range(len(a)):
            d=a[j].rstrip().split()
            if d!=[]:
                if d[0]=="Cluster":
                    temp=[]
                    temp.append(int(d[1]))

                elif d[0]==sent:
                    temp.append(float(d[1]))
                    final.append(temp)

        final.sort()

        for k in final:
            consol.append(k[1])

