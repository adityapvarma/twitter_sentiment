Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from pickle import load
>>> f=open("NFL_Complete_V6_Pre_Processed.pickle","rb")
>>> a=load(f)
>>> a
{'tweet_rt_count': 0, 'tweet_hashtags': ['SuperBowl'], 'user_id': 355683606, 'snowball': ['go', 'win', '#superbowl', 'today', '?'], 'tokens': ['who', 'is', 'going', 'to', 'win', 'the', '#superbowl', 'today', '?'], 'user_geo_status': True, 'tweet_rt_status': False, 'user_name': 'Matt Smith \U0001f3d2\U0001f945', 'tweet_text': 'Who is going to win the #SuperBowl today?', 'tweet_id': 1224071763761385472, 'tweet_coordinates': None, 'user_created_at': datetime.datetime(2011, 8, 15, 18, 47, 1), 'tweet_fav_count': 0, 'porter': ['go', 'win', '#superbowl', 'today', '?'], 'user_follower_count': 380, 'tweet_source': 'Twitter for Android', 'user_screen': 'MSmitty25', 'tweet_created_at': datetime.datetime(2020, 2, 2, 20, 47, 5), 'user_location': 'Edmonton, Alberta'}
>>> a=load(f)
>>> a
{'tweet_rt_count': 12223, 'tweet_hashtags': [], 'user_id': 52190807, 'snowball': ['@superbowl', 'interview', '3:30', 'p', '.', '.', '@foxnetwork', '.', 'enjoy', '!'], 'tokens': ['my', '@superbowl', 'interview', 'at', '3:30', 'p', '.', 'm', '.', 'on', '@foxnetworks', '.', 'enjoy', '!'], 'user_geo_status': True, 'tweet_rt_status': True, 'user_name': 'Peni Basse ⭐️⭐️⭐️ Text TRUMP to 88022', 'tweet_text': 'My @SuperBowl Interview at 3:30 P.M. on @foxnetworks. Enjoy!', 'tweet_id': 1224071766068420608, 'tweet_coordinates': None, 'user_created_at': datetime.datetime(2009, 6, 29, 21, 11, 38), 'tweet_fav_count': 0, 'porter': ['@superbowl', 'interview', '3:30', 'p', '.', '.', '@foxnetwork', '.', 'enjoy', '!'], 'user_follower_count': 14331, 'tweet_source': 'Twitter Web App', 'user_screen': 'pmbasse', 'tweet_created_at': datetime.datetime(2020, 2, 2, 20, 47, 5), 'user_location': 'TEXAS'}
>>> a=load(f)
>>> a
{'tweet_rt_count': 12535, 'tweet_hashtags': [], 'user_id': 3093894347, 'snowball': ['watch', 'super', 'bowl', 'seen', '54', 'season', 'footbal', 'need', 'start', 'begin'], 'tokens': ['can', 'i', 'watch', 'the', 'super', 'bowl', 'if', 'i', "haven't", 'seen', 'all', '54', 'seasons', 'of', 'football', 'or', 'do', 'i', 'need', 'to', 'start', 'from', 'the', 'beginning'], 'user_geo_status': False, 'tweet_rt_status': True, 'user_name': 'Nick Bailey', 'tweet_text': "Can I watch the Super Bowl if I haven't seen all 54 seasons of football or do I need to start from the beginning", 'tweet_id': 1224071761421131777, 'tweet_coordinates': None, 'user_created_at': datetime.datetime(2015, 3, 18, 3, 16, 6), 'tweet_fav_count': 0, 'porter': ['watch', 'super', 'bowl', 'seen', '54', 'season', 'footbal', 'need', 'start', 'begin'], 'user_follower_count': 40, 'tweet_source': 'Twitter for iPhone', 'user_screen': 'ZakuNick', 'tweet_created_at': datetime.datetime(2020, 2, 2, 20, 47, 4), 'user_location': 'Crofton, MD'}
>>> a=load(f)
>>> a
{'tweet_rt_count': 4, 'tweet_hashtags': ['SB19GoUpSaBillboard'], 'user_id': 1186065659341369349, 'snowball': ['@chameleonemde', '@mor1019', '@sb19offici', 'vote', 'caus', 'watch', 'superbowl', 'later', '.', '#sb19goupsabillboard', '#morhot10', 'alab', 'sb19', '@mor1019', '#sb19', '@sb19offici'], 'tokens': ['@chameleonemdee', '@mor1019', '@sb19official', 'voting', 'now', 'cause', 'will', 'be', 'watching', 'the', 'superbowl', 'later', '.', '#sb19goupsabillboard', '#morhot10', 'alab', 'by', 'sb19', '@mor1019', '#sb19', '@sb19official'], 'user_geo_status': False, 'tweet_rt_status': False, 'user_name': 'Elle \U0001f525', 'tweet_text': '@ChameleonEmdee @mor1019 @SB19Official Voting now cause will be watching the Superbowl later.\n\n#SB19GoUpSaBillboard\n#MORHot10 Alab by SB19 @mor1019\n#SB19 @SB19Official', 'tweet_id': 1224071770921029633, 'tweet_coordinates': None, 'user_created_at': datetime.datetime(2019, 10, 20, 23, 44, 49), 'tweet_fav_count': 2, 'porter': ['@chameleonemde', '@mor1019', '@sb19offici', 'vote', 'caus', 'watch', 'superbowl', 'later', '.', '#sb19goupsabillboard', '#morhot10', 'alab', 'sb19', '@mor1019', '#sb19', '@sb19offici'], 'user_follower_count': 319, 'tweet_source': 'Twitter for Android', 'user_screen': 'Elle24169177', 'tweet_created_at': datetime.datetime(2020, 2, 2, 20, 47, 6), 'user_location': ''}
>>> a=load(f)
>>> a
{'tweet_rt_count': 0, 'tweet_hashtags': [], 'user_id': 305755481, 'snowball': ['seen', 'moron', 'footbal', 'opinion', 'time', 'peopl', 'defend', 'refere', 'neymar', 'incid', 'top', 'lot', '.', 'scrap', 'footbal', 'dont', 'want', 'best', 'player', 'around', 'gannin', 'express', '.', 'utter', 'farc', '.', '#neymarjr'], 'tokens': ['seen', 'some', 'moronic', 'footballing', 'opinions', 'in', 'my', 'time', 'but', 'people', 'defending', 'the', 'referee', 'over', 'the', 'neymar', 'incident', 'tops', 'the', 'lot', '.', 'just', 'scrap', 'football', 'if', 'you', 'dont', 'want', 'the', 'best', 'players', 'around', 'gannin', 'out', 'and', 'expressing', 'themselves', '.', 'utter', 'farce', '.', '#neymarjr'], 'user_geo_status': True, 'tweet_rt_status': False, 'user_name': 'Paul W', 'tweet_text': 'Seen some moronic footballing opinions in my time but people defending the referee over the Neymar incident tops the lot. \n\nJust scrap football if you dont want the best players around gannin out and expressing themselves. Utter farce.\n\n#NeymarJr', 'tweet_id': 1224071770199773185, 'tweet_coordinates': None, 'user_created_at': datetime.datetime(2011, 5, 26, 19, 3, 52), 'tweet_fav_count': 1, 'porter': ['seen', 'moron', 'footbal', 'opinion', 'time', 'peopl', 'defend', 'refere', 'neymar', 'incid', 'top', 'lot', '.', 'scrap', 'footbal', 'dont', 'want', 'best', 'player', 'around', 'gannin', 'express', '.', 'utter', 'farc', '.', '#neymarjr'], 'user_follower_count': 290, 'tweet_source': 'Twitter for Android', 'user_screen': 'PJ_Walker88', 'tweet_created_at': datetime.datetime(2020, 2, 2, 20, 47, 6), 'user_location': 'Newcastle Upon Tyne, England'}
>>> a=load(f)
>>> a
{'tweet_rt_count': 1087, 'tweet_hashtags': ['SuperBowl'], 'user_id': 1108532879108259840, 'snowball': ['shakira', '#superbowl', ':', '’', 'wolf', 'closet', ',', 'open', 'set', 'free', ':', 'https://t.co/snufaowrfi'], 'tokens': ['shakira', 'at', 'the', '#superbowl', ':', 'there', '’', 's', 'a', 'she', 'wolf', 'in', 'the', 'closet', ',', 'open', 'up', 'and', 'set', 'it', 'free', 'me', ':', 'https://t.co/snufaowrfi'], 'user_geo_status': True, 'tweet_rt_status': True, 'user_name': 'sergio', 'tweet_text': 'Shakira at the #SuperBowl: There’s a she wolf in the closet, open up and set it free\n\nMe:\n\n https://t.co/SnUfAowrFi', 'tweet_id': 1224071763933499398, 'tweet_coordinates': None, 'user_created_at': datetime.datetime(2019, 3, 21, 0, 56, 48), 'tweet_fav_count': 0, 'porter': ['shakira', '#superbowl', ':', '’', 'wolf', 'closet', ',', 'open', 'set', 'free', ':', 'https://t.co/snufaowrfi'], 'user_follower_count': 169, 'tweet_source': 'Twitter for iPhone', 'user_screen': 'turboserch', 'tweet_created_at': datetime.datetime(2020, 2, 2, 20, 47, 5), 'user_location': ''}
>>> a=load(f)
>>> a
{'tweet_rt_count': 3998, 'tweet_hashtags': ['SBLIV'], 'user_id': 1179070232163422208, 'snowball': ['today', '\U0001f3c8', 'watch', 'demi', 'perform', 'nation', 'anthem', '#sbliv', '!', '@nfl', 'https://t.co/tj7ufuiakf'], 'tokens': ['today', '\U0001f3c8', 'watch', 'demi', 'perform', 'the', 'national', 'anthem', 'during', 'the', '#sbliv', '!', '@nfl', 'https://t.co/tj7ufuiakf'], 'user_geo_status': False, 'tweet_rt_status': True, 'user_name': 'pedro \U0001f174', 'tweet_text': 'TODAY \U0001f3c8 Watch Demi perform the National Anthem during the #SBLIV! @NFL https://t.co/TJ7uFUiAKF', 'tweet_id': 1224071761387511813, 'tweet_coordinates': None, 'user_created_at': datetime.datetime(2019, 10, 1, 16, 27, 17), 'tweet_fav_count': 0, 'porter': ['today', '\U0001f3c8', 'watch', 'demi', 'perform', 'nation', 'anthem', '#sbliv', '!', '@nfl', 'https://t.co/tj7ufuiakf'], 'user_follower_count': 719, 'tweet_source': 'Twitter for Android', 'user_screen': 'lovatofemales', 'tweet_created_at': datetime.datetime(2020, 2, 2, 20, 47, 4), 'user_location': 'Rj'}
>>> a["tweet_text"]
'TODAY \U0001f3c8 Watch Demi perform the National Anthem during the #SBLIV! @NFL https://t.co/TJ7uFUiAKF'
>>> import emojis
>>> emojis.encode(a["tweet_text"])
'TODAY \U0001f3c8 Watch Demi perform the National Anthem during the #SBLIV! @NFL https://t.co/TJ7uFUiAKF'
>>> emojis.decode(a["tweet_text"])
'TODAY :football: Watch Demi perform the National Anthem during the #SBLIV! @NFL https://t.co/TJ7uFUiAKF'
>>> for i in a:
	print(i)

	
tweet_rt_count
tweet_hashtags
user_id
snowball
tokens
user_geo_status
tweet_rt_status
user_name
tweet_text
tweet_id
tweet_coordinates
user_created_at
tweet_fav_count
porter
user_follower_count
tweet_source
user_screen
tweet_created_at
user_location
>>> for i in a:
	print(i," : ",type(a[i]))

	
tweet_rt_count  :  <class 'int'>
tweet_hashtags  :  <class 'list'>
user_id  :  <class 'int'>
snowball  :  <class 'list'>
tokens  :  <class 'list'>
user_geo_status  :  <class 'bool'>
tweet_rt_status  :  <class 'bool'>
user_name  :  <class 'str'>
tweet_text  :  <class 'str'>
tweet_id  :  <class 'int'>
tweet_coordinates  :  <class 'NoneType'>
user_created_at  :  <class 'datetime.datetime'>
tweet_fav_count  :  <class 'int'>
porter  :  <class 'list'>
user_follower_count  :  <class 'int'>
tweet_source  :  <class 'str'>
user_screen  :  <class 'str'>
tweet_created_at  :  <class 'datetime.datetime'>
user_location  :  <class 'str'>
>>> emojis.count(a["tweet_text"])
1
>>> for i in a:
	print(emojis.count(a[i]))

	
Traceback (most recent call last):
  File "<pyshell#28>", line 2, in <module>
    print(emojis.count(a[i]))
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\lib\site-packages\emojis\emojis.py", line 70, in count
    return len([match.group() for match in  RE_EMOJI_TO_TEXT.finditer(msg)])
TypeError: expected string or bytes-like object
>>> for i in a:
	print(emojis.count(str(a[i])))

	
0
0
0
1
1
0
0
0
1
0
0
0
0
1
0
0
0
0
0
>>> for i in a:
	print(i,":",emojis.count(str(a[i])))

	
tweet_rt_count : 0
tweet_hashtags : 0
user_id : 0
snowball : 1
tokens : 1
user_geo_status : 0
tweet_rt_status : 0
user_name : 0
tweet_text : 1
tweet_id : 0
tweet_coordinates : 0
user_created_at : 0
tweet_fav_count : 0
porter : 1
user_follower_count : 0
tweet_source : 0
user_screen : 0
tweet_created_at : 0
user_location : 0
>>> a["porter"]
['today', '\U0001f3c8', 'watch', 'demi', 'perform', 'nation', 'anthem', '#sbliv', '!', '@nfl', 'https://t.co/tj7ufuiakf']
>>> emojis.decode(a["porter"])
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    emojis.decode(a["porter"])
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\lib\site-packages\emojis\emojis.py", line 46, in decode
    msg = RE_EMOJI_TO_TEXT.sub(lambda match: EMOJI_TO_ALIAS[match.group(0)], msg)
TypeError: expected string or bytes-like object
>>> emojis.decode(a["porter"][1])
':football:'
>>> 
