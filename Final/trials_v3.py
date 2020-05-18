Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/admin/AppData/Local/Programs/Python/Python35/Twitter_Project/query_list.py 
>>> f=open("nfl_consolidated.pickle","rb")
>>> nf=open("nfl_complete_V2.pickle","wb")
>>> l=[]
>>> for i in range(100):
	a=pickle.load(f)
	l.append(a[0])

	
>>> len(l)
100
>>> d=api.statuses_lookup(l)
>>> 
 RESTART: C:/Users/admin/AppData/Local/Programs/Python/Python35/Twitter_Project/query_list.py 
>>> f=open("nfl_consolidated.pickle","rb")
>>> nf=open("nfl_complete_V2.pickle","wb")
>>> l=[]
>>> for i in range(100):
	a=pickle.load(f)
	l.append(a[0])

	
>>> len(l)
100
>>> d=api.statuses_lookup(l)
>>> ld=get_dat(d)
>>> len(ld)
91
>>> ld[0]
{'user_id': 355683606, 'user_screen': 'MSmitty25', 'user_name': 'Matt Smith \U0001f3d2\U0001f945', 'tweet_coordinates': None, 'user_location': 'Edmonton, Alberta', 'tweet_source': 'Twitter for Android', 'tweet_hashtags': ['SuperBowl'], 'user_created_at': datetime.datetime(2011, 8, 15, 18, 47, 1), 'user_geo_status': True, 'tweet_text': 'Who is going to win the #SuperBowl today?', 'tweet_id': 1224071763761385472, 'tweet_rt_count': 0, 'tweet_rt_status': False, 'tweet_fav_count': 0, 'user_follower_count': 381, 'tweet_created_at': datetime.datetime(2020, 2, 2, 20, 47, 5)}
>>> for i in ld:
	pickle.dump(i,nf)

	
>>> while 1:
	try:
		l=[]
		for i in range(100):
			a=pickle.load(f)
			l.append(a[0])
	except EOFError:
		pass

	
Traceback (most recent call last):
  File "<pyshell#30>", line 5, in <module>
    a=pickle.load(f)
KeyboardInterrupt
>>> nf.close()
>>> nf.open("nfl_complete_V2.pickle","rb")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    nf.open("nfl_complete_V2.pickle","rb")
AttributeError: '_io.BufferedWriter' object has no attribute 'open'
>>> nf=open("nfl_complete_V2.pickle","rb")
>>> while 1:
	try:
		a=pickle.load(f)
		print(a["tweet_id"])
	except
	
SyntaxError: invalid syntax
>>> while 1:
	try:
		a=pickle.load(f)
		print(a["tweet_id"])
	except EOFError:
		print("Done")

		
Traceback (most recent call last):
  File "<pyshell#42>", line 4, in <module>
    print(a["tweet_id"])
TypeError: list indices must be integers or slices, not str
>>> while 1:
	try:
		a=pickle.load(nf)
		print(a["tweet_id"])
	except EOFError:
		print("Done")

		
1224071763761385472
1224071766068420608
1224071761421131777
1224071770921029633
1224071770199773185
1224071763933499398
1224071761387511813
1224071762813620226
1224071768387788807
1224071766772838400
1224071769323188224
1224071765879590912
1224071769897697281
1224071771248373760
1224071772745629698
1224071765376237570
1224071764931698688
1224071769054568450
1224071767637004288
1224071760615813120
1224071765002944515
1224071762956242944
1224071761915936775
1224071760472993792
1224071762901684224
1224071770879275008
1224071759709732866
1224071758568808448
1224071762079600641
1224071772502462464
1224071771382583297
1224071760691240962
1224071764151537666
1224071763719573515
1224071765845999616
1224071765833535488
1224071758858330118
1224071767557312514
1224071766219227136
1224071761035255813
1224071771453886466
1224071762037608448
1224071764864466944
1224071768303980548
1224071770203815936
1224071768408608770
1224071762524000256
1224071761064611846
1224071769159585798
1224071769838866433
1224071764889595904
1224071761236516865
1224071758749134848
1224071769776164864
1224071762863894528
1224071772603109382
1224071761253347329
1224071759550394369
1224071762457059328
1224071771583930369
1224071766210945027
1224071761458868226
1224071760309559296
1224071767909642240
1224071761412743169
1224071763665080320
1224071760242528256
1224071759630082050
1224071770032025602
1224071772401614848
1224071766919860225
1224071763291566080
1224071764038373379
1224071771978072069
1224071763857899520
1224071758342434817
1224071769180512256
1224071772540194816
1224071766269513728
1224071768664674304
1224071762696196096
1224071763862212608
1224071760456376321
1224071761807007744
1224071770023612417
1224071767108542468
1224071768576593922
1224071764382060544
1224071771525087234
1224071759864922116
1224071769335701505
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Done
Traceback (most recent call last):
  File "<pyshell#44>", line 3, in <module>
    a=pickle.load(nf)
EOFError: Ran out of input

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#44>", line 6, in <module>
    print("Done")
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\lib\idlelib\PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> nf.close()
>>> f.close()
>>> 
