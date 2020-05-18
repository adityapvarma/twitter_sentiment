#MySQL Data Entry 
#Add entry into user table first and then tweet table
#use single entry. Cross check with a locally maintained userid list and
#tweet id list

import unicodedata as ud
from pickle import load
from mysql.connector import connect,Error



query_user="""insert into user (user_created_at,user_follower_count,user_geo_status,user_id,user_location,user_name,user_screen)
values (%s, %s, %s, %s, %s, %s, %s);"""

query_tweet="""insert into tweet (porter,snowball,tokens,tweet_coordinates,tweet_created_at,tweet_fav_count,tweet_hashtags,
tweet_id,tweet_rt_count,tweet_rt_status,tweet_source,tweet_text,user_id)
values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

l_u=['user_created_at', 'user_follower_count', 'user_geo_status', 'user_id', 'user_location', 'user_name', 'user_screen']
l_t=['porter', 'snowball', 'tokens', 'tweet_coordinates', 'tweet_created_at', 'tweet_fav_count', 'tweet_hashtags',
     'tweet_id', 'tweet_rt_count', 'tweet_rt_status', 'tweet_source', 'tweet_text', 'user_id']

#Global vars
user_list=[]
tweet_list=[]



f=open("NFL_Complete_V6_Pre_Processed_with_emoji.pickle","rb")
nf=open("writing trials_2.txt","w")

#Replaces Unicode Chars
#Reverse function
#Try writing data to a file - ALt to print.. hits UnicodeEncodeError
def repl(val):
    
    temp=''
    """
    for i in val:
        
        if ud.category(i)in ["So","Sk","Sm","Sc"]:
            
            temp+=(":"+ud.name(i)+":")
        else:
            
            temp+=i
    """

    for k in val:
        try:
            nf.write(k)
            temp+=k
        except UnicodeEncodeError:
            try:
                temp+=(":"+ud.name(k)+":")
            except ValueError:
                #print("Value Error Hit!")
                continue
            
    return temp


#Serialising function for lists. Delimiter Used " "
def serl(lt):
    temp=''
    for i in lt:    
        temp+=(str(i)+" ")
    return temp

#Insert Function
#Update user table first then tweet table
def insert_1k(lt_u,lt_t):
    global user_list
    global tweet_list

    try:
        db=connect(host="proj-mysql.uopnet.plymouth.ac.uk",
			database="prco304_avarma",
			user="prco304_avarma",
			password="avarma_304")
        c=db.cursor()
    except:
        print("Check Connection.")
        return None
    """
    c=db.cursor()
    for i in range(len(lt_u)):

        if lt_u[i][3] not in user_list:
            try:
                c.execute(query_user,lt_u[i])
            except Error as e:
                print(e)
                return 0
            user_list.append(lt_u[i][3])
    """
    """
    for i in lt_u:

        if i[3] not in user_list:
            try:
                c.execute(query_user,i)
            except Error as e:
                print(e,i[3])
                #return 0
            user_list.append(i[3])
        else:
            continue

    for i in lt_t:

        if i[7] not in tweet_list:
            try:
                c.execute(query_tweet,i)
            except Error as e:
                print(e,i[7])
                #return 0
            tweet_list.append(i[7])
        else:
            continue
    """

    try:
        c.executemany(query_user,lt_u)

    except Error as e:
        print(e,"user")

    try:
        c.executemany(query_tweet,lt_t)

    except Error as e:
        print(e,"tweet")
        
    db.commit()
    c.close()
    db.close()
    return "Yes"
            
                

        
        



###Get initial vals for id lists
db=connect(host="proj-mysql.uopnet.plymouth.ac.uk",
			database="prco304_avarma",
			user="prco304_avarma",
			password="avarma_304")
c=db.cursor()
c.execute("SELECT tweet_id FROM TWEET;")
if c!=None:
    for i in c:
        tweet_list.append(i[0])

c.execute("SELECT user_id FROM USER;")
if c!=None:
    for i in c:
        user_list.append(i[0])

c.close()
db.close()

print(len(user_list))
print(len(tweet_list))

flag=0

count=0
over_ct=0

dat_u=[]
dat_t=[]

while 1:

    #dat_u=[]
    #dat_t=[]

    for i in range(500):

        try:
            a=load(f)
            temp_t=[]
            temp_u=[]

            #Serialise Variables
            temp1_u,temp1_t=[],[]

            #Replace all Unicode Chars vars
            temp2_u,temp2_t=[],[]

            #Do user stuff first

            if a["user_id"] not in user_list:
                for j in l_u:
                    temp_u.append(a[j])

                #Change Date format
                temp_u[0]=temp_u[0].strftime('%Y-%m-%d %H:%M:%S')


                #Serialise
                for j in temp_u:
                    if isinstance(j,list):
                        temp1_u.append(serl(j))
                    elif isinstance(j,dict):
                        temp1_u.append(serl(j["coordinates"]))
                    else:
                        temp1_u.append(j)


                #Replace
                for j in temp1_u:
                    if isinstance(j,str):
                        temp2_u.append(repl(j))
                    else:
                        temp2_u.append(j)

                user_list.append(a["user_id"])
                dat_u.append(tuple(temp2_u))

            else:
                pass

            if a["tweet_id"] not in tweet_list:
                for j in l_t:
                    temp_t.append(a[j])

                #Change Date format
                #temp_u[0]=temp_u[0].strftime('%Y-%m-%d %H:%M:%S')
                temp_t[4]=temp_t[4].strftime('%Y-%m-%d %H:%M:%S')


                #Serialise
                for j in temp_t:
                    if isinstance(j,list):
                        temp1_t.append(serl(j))
                    elif isinstance(j,dict):
                        temp1_t.append(serl(j["coordinates"]))
                    else:
                        temp1_t.append(j)


                #Replace
                for j in temp1_t:
                    if isinstance(j,str):
                        temp2_t.append(repl(j))
                    else:
                        temp2_t.append(j)

                tweet_list.append(a["tweet_id"])
                dat_t.append(tuple(temp2_t))

            else:
                pass



        except EOFError:
            flag=1

        except KeyboardInterrupt:
            break

    count+=1
    

    if dat_u !=[] and dat_t!=[]:
        print("Here Count :",count)
        b=insert_1k(dat_u,dat_t)
        if b==None:
            flag=1
        dat_u=[]
        dat_t=[]

    """
    if b!=None: 
        count+=1
        #print(count)
    else:
        break
    """

    if count>100:
        over_ct+=1
        print(over_ct)
        count=0

    if flag:
        break
        

        

        

        


        
