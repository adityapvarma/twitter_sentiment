Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> f=open("NFL_Complete_V6_Pre_Processed_with_emoji.pickle","rb")
>>> import pickle
>>> a=pickle.load(f)
>>> for i in a:
	print(i," : ",a[i])

	
tokens  :  ['who', 'is', 'going', 'to', 'win', 'the', '#superbowl', 'today', '?']
user_geo_status  :  True
user_name  :  Matt Smith :ice_hockey::goal_net:
user_screen  :  MSmitty25
user_location  :  Edmonton, Alberta
user_created_at  :  2011-08-15 18:47:01
porter  :  ['go', 'win', '#superbowl', 'today', '?']
tweet_rt_status  :  False
tweet_id  :  1224071763761385472
user_id  :  355683606
tweet_rt_count  :  0
tweet_source  :  Twitter for Android
tweet_created_at  :  2020-02-02 20:47:05
tweet_fav_count  :  0
snowball  :  ['go', 'win', '#superbowl', 'today', '?']
tweet_text  :  Who is going to win the #SuperBowl today?
tweet_coordinates  :  None
user_follower_count  :  380
tweet_hashtags  :  ['SuperBowl']
>>> l={'porter': 1623,
 'snowball': 1623,
 'tokens': 1635,
 'tweet_hashtags': 125,
 'tweet_source': 49,
 'tweet_text': 1854,
 'user_location': 299,
 'user_name': 437,
 'user_screen': 16}
>>> for i in a.keys().sort():
	print(i," : ",a[i])

	
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    for i in a.keys().sort():
AttributeError: 'dict_keys' object has no attribute 'sort'
>>> s.keys()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s.keys()
NameError: name 's' is not defined
>>> a.keys()
dict_keys(['tokens', 'user_geo_status', 'user_name', 'user_screen', 'user_location', 'user_created_at', 'porter', 'tweet_rt_status', 'tweet_id', 'user_id', 'tweet_rt_count', 'tweet_source', 'tweet_created_at', 'tweet_fav_count', 'snowball', 'tweet_text', 'tweet_coordinates', 'user_follower_count', 'tweet_hashtags'])
>>> for i in list(a.keys()).sort():
	print(i," : ",a[i])

	
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    for i in list(a.keys()).sort():
TypeError: 'NoneType' object is not iterable
>>> list(a.keys())
['tokens', 'user_geo_status', 'user_name', 'user_screen', 'user_location', 'user_created_at', 'porter', 'tweet_rt_status', 'tweet_id', 'user_id', 'tweet_rt_count', 'tweet_source', 'tweet_created_at', 'tweet_fav_count', 'snowball', 'tweet_text', 'tweet_coordinates', 'user_follower_count', 'tweet_hashtags']
>>> list(a.keys()).sort()
>>> o=
SyntaxError: invalid syntax
>>> o=list(a.keys()).sort()
>>> o
>>> o
>>> o=a
>>> o=list(a.keys())
>>> o.sort()
>>> for i in o:
	print(i," : ",a[i])

	
porter  :  ['go', 'win', '#superbowl', 'today', '?']
snowball  :  ['go', 'win', '#superbowl', 'today', '?']
tokens  :  ['who', 'is', 'going', 'to', 'win', 'the', '#superbowl', 'today', '?']
tweet_coordinates  :  None
tweet_created_at  :  2020-02-02 20:47:05
tweet_fav_count  :  0
tweet_hashtags  :  ['SuperBowl']
tweet_id  :  1224071763761385472
tweet_rt_count  :  0
tweet_rt_status  :  False
tweet_source  :  Twitter for Android
tweet_text  :  Who is going to win the #SuperBowl today?
user_created_at  :  2011-08-15 18:47:01
user_follower_count  :  380
user_geo_status  :  True
user_id  :  355683606
user_location  :  Edmonton, Alberta
user_name  :  Matt Smith :ice_hockey::goal_net:
user_screen  :  MSmitty25
>>> l
{'porter': 1623, 'tokens': 1635, 'user_name': 437, 'tweet_hashtags': 125, 'tweet_text': 1854, 'user_location': 299, 'snowball': 1623, 'user_screen': 16, 'tweet_source': 49}
>>> for i in l:
	print(i,":",l[i])

	
porter : 1623
tokens : 1635
user_name : 437
tweet_hashtags : 125
tweet_text : 1854
user_location : 299
snowball : 1623
user_screen : 16
tweet_source : 49
>>> for i in o:
	if "user" in i:
		print(i," : ",a[i])

		
user_created_at  :  2011-08-15 18:47:01
user_follower_count  :  380
user_geo_status  :  True
user_id  :  355683606
user_location  :  Edmonton, Alberta
user_name  :  Matt Smith :ice_hockey::goal_net:
user_screen  :  MSmitty25
>>> for i in o:
	if "tweet" in i:
		print(i," : ",a[i])

		
tweet_coordinates  :  None
tweet_created_at  :  2020-02-02 20:47:05
tweet_fav_count  :  0
tweet_hashtags  :  ['SuperBowl']
tweet_id  :  1224071763761385472
tweet_rt_count  :  0
tweet_rt_status  :  False
tweet_source  :  Twitter for Android
tweet_text  :  Who is going to win the #SuperBowl today?
>>> for i in o:
	if "tweet" not in i and "user" not in i:
		print(i," : ",a[i])

		
porter  :  ['go', 'win', '#superbowl', 'today', '?']
snowball  :  ['go', 'win', '#superbowl', 'today', '?']
tokens  :  ['who', 'is', 'going', 'to', 'win', 'the', '#superbowl', 'today', '?']
>>> for i in o:
	if "id" in i:
		print(i," : ",type(i))

		
tweet_id  :  <class 'str'>
user_id  :  <class 'str'>
>>> for i in o:
	print(i," : ",type(i))

	
porter  :  <class 'str'>
snowball  :  <class 'str'>
tokens  :  <class 'str'>
tweet_coordinates  :  <class 'str'>
tweet_created_at  :  <class 'str'>
tweet_fav_count  :  <class 'str'>
tweet_hashtags  :  <class 'str'>
tweet_id  :  <class 'str'>
tweet_rt_count  :  <class 'str'>
tweet_rt_status  :  <class 'str'>
tweet_source  :  <class 'str'>
tweet_text  :  <class 'str'>
user_created_at  :  <class 'str'>
user_follower_count  :  <class 'str'>
user_geo_status  :  <class 'str'>
user_id  :  <class 'str'>
user_location  :  <class 'str'>
user_name  :  <class 'str'>
user_screen  :  <class 'str'>
>>> f=open("NFL_Complete_V6_Pre_Processed.pickle","rb")
>>> a=pickle.load(f)
>>> f=open("NFL_Complete_V6_Pre_Processed_with_emoji.pickle","rb")
>>> a=pickle.load(f)
>>> for i in a:
	print(i," ",type(a[i]))

	
tokens   <class 'list'>
user_geo_status   <class 'bool'>
user_name   <class 'str'>
user_screen   <class 'str'>
user_location   <class 'str'>
user_created_at   <class 'datetime.datetime'>
porter   <class 'list'>
tweet_rt_status   <class 'bool'>
tweet_id   <class 'int'>
user_id   <class 'int'>
tweet_rt_count   <class 'int'>
tweet_source   <class 'str'>
tweet_created_at   <class 'datetime.datetime'>
tweet_fav_count   <class 'int'>
snowball   <class 'list'>
tweet_text   <class 'str'>
tweet_coordinates   <class 'NoneType'>
user_follower_count   <class 'int'>
tweet_hashtags   <class 'list'>
>>> 18446744073709551615>1224262535307833345
True
>>> 80864105>2147483648
False
>>> l
{'porter': 1623, 'tokens': 1635, 'user_name': 437, 'tweet_hashtags': 125, 'tweet_text': 1854, 'user_location': 299, 'snowball': 1623, 'user_screen': 16, 'tweet_source': 49}
>>> for i in l:
	print(i,":",l[i])

	
porter : 1623
tokens : 1635
user_name : 437
tweet_hashtags : 125
tweet_text : 1854
user_location : 299
snowball : 1623
user_screen : 16
tweet_source : 49
>>> """1224262535307833345
1224260701272690688
80864105"""
'1224262535307833345\n1224260701272690688\n80864105'
>>> 
