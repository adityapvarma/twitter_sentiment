Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/admin/AppData/Local/Programs/Python/Python35/Twitter_Project/query_list.py 
>>> f=open("nfl_consolidated.pickle","rb")
>>> nf=open("NFL_Complete_V3.pickle","wb")
>>> l=[]
>>> 
>>> 
>>> while 1:
	l=[
	try:
		for i in range(100):
			a=pickle.load(f)
			l.append(a[0])
	except EOFError:
		pass
	
SyntaxError: invalid syntax
>>> count=0
>>> while 1:
	l=[
	try:
		for i in range(100):
			a=pickle.load(f)
			l.append(a[0])
	except EOFError:
		pass
	ld=get_dat(l)
	
SyntaxError: invalid syntax
>>> while 1:
	l=[
	try:
		for i in range(100):
			a=pickle.load(f)
			l.append(a[0])
	except EOFError:
		pass
	ld=get_dat(l)
	
SyntaxError: invalid syntax
>>> while 1:
	if count==10000:
		print(
	count+=1
	l=[]
	f=0
	try:
		for i in range(100):
			a=pickle.load(f)
			l.append(a[0])
	except EOFError:
		f=1
		pass
	ld=get_dat(l)
	for j in ld:
	
SyntaxError: invalid syntax
>>> over_ct=0
>>> while 1:
	if count==10000:
		over_ct+=1
		print(over_ct)
		count=0
		sleep(30)
	count+=1
	l=[]
	f=0
	try:
		for i in range(100):
			a=pickle.load(f)
			l.append(a[0])
	except EOFError:
		f=1
		pass
	ld=get_dat(l)
	for j in ld:
		pickle.dump(j,nf)
	if f:
		break

	
Traceback (most recent call last):
  File "<pyshell#27>", line 12, in <module>
    a=pickle.load(f)
TypeError: file must have 'read' and 'readline' attributes
>>> a=pickle.load(f)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a=pickle.load(f)
TypeError: file must have 'read' and 'readline' attributes
>>> f.close()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    f.close()
AttributeError: 'int' object has no attribute 'close'
>>> count
1
>>> over_ct
0
>>> f=open("nfl_consolidated.pickle","rb")
>>> nf.close()
>>> nf=open("NFL_Complete_V4.pickle","wb")
>>> while 1:
	if count==10000:
		over_ct+=1
		print(over_ct)
		count=0
		sleep(30)
	count+=1
	l=[]
	fg=0
	try:
		for i in range(100):
			a=pickle.load(f)
			l.append(a[0])
	except EOFError:
		f=1
		pass
	ld=get_dat(l)
	for j in ld:
		pickle.dump(j,nf)
	if fg:
		break

	
Rate limit reached. Sleeping for: 542
Rate limit reached. Sleeping for: 563
Rate limit reached. Sleeping for: 600
Rate limit reached. Sleeping for: 550
Rate limit reached. Sleeping for: 39
Rate limit reached. Sleeping for: 361
Rate limit reached. Sleeping for: 415
Rate limit reached. Sleeping for: 567
Rate limit reached. Sleeping for: 589
Rate limit reached. Sleeping for: 616
Rate limit reached. Sleeping for: 316
Rate limit reached. Sleeping for: 495
Rate limit reached. Sleeping for: 516

