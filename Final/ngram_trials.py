Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/admin/AppData/Local/Programs/Python/Python35/Twitter_Project/slot_collect.py 
>>> c.execute("select tweet_id,tweet_created_at,hour(tweet_created_at) from tweet limit 10;")
>>> l=[]
>>> for i in c:
	l.append(i)

	
>>> len(i)
3
>>> len(l)
10
>>> l[0]
(1224071758342434817, datetime.datetime(2020, 2, 2, 20, 47, 3), 20)
>>> type(l[0][2])
<class 'int'>
>>> 
 RESTART: C:/Users/admin/AppData/Local/Programs/Python/Python35/Twitter_Project/slot_collect.py 
Traceback (most recent call last):
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\lib\site-packages\mysql\connector\connection_cext.py", line 395, in cmd_query
    raw_as_string=raw_as_string)
_mysql_connector.MySQLInterfaceError: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '"select tweet_id,user_id,tweet_text,tweet_created_at,snowball,porter,hour(tweet_' at line 1

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/admin/AppData/Local/Programs/Python/Python35/Twitter_Project/slot_collect.py", line 18, in <module>
    c.execute(""""select tweet_id,user_id,tweet_text,tweet_created_at,snowball,porter,hour(tweet_created_at) from tweet;""")
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\lib\site-packages\mysql\connector\cursor_cext.py", line 266, in execute
    raw_as_string=self._raw_as_string)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\lib\site-packages\mysql\connector\connection_cext.py", line 398, in cmd_query
    sqlstate=exc.sqlstate)
mysql.connector.errors.ProgrammingError: 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '"select tweet_id,user_id,tweet_text,tweet_created_at,snowball,porter,hour(tweet_' at line 1
>>> 
 RESTART: C:/Users/admin/AppData/Local/Programs/Python/Python35/Twitter_Project/slot_collect.py 
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
>>> len(d)
14
>>> a=d.keys()
>>> a
dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 21, 22, 23])
>>> v=0
>>> for i in d:
	v+=len(d[i])

	
>>> v
1525050
>>> len(d[20])
18597
>>> sample=d[20][0][4]
>>> sample
"lol despit homemad bbq i'm gonna tonight watch #superbowl break fast , i'm still gonna make sure there room sardin spinach #cantgetenough "
>>> sample=["lol despit homemad bbq i'm gonna tonight watch #superbowl break fast , i'm still gonna make sure there room sardin spinach #cantgetenough "]
>>> sample
["lol despit homemad bbq i'm gonna tonight watch #superbowl break fast , i'm still gonna make sure there room sardin spinach #cantgetenough "]
>>> sample.append(d[20][1][4])
>>> sample
["lol despit homemad bbq i'm gonna tonight watch #superbowl break fast , i'm still gonna make sure there room sardin spinach #cantgetenough ", 'matter broadcast network respons million peopl watch . fox awar @realdonaldtrump lie . know spread disinform ? interview alreadi tape - ampl time #factcheck https://t.co/q7t2ouvbxd ']
>>> from sklearn.feature_extraction.text import CountVectorizer

>>> sample2=["this is a test",
	 "how are you",
	 "this is you"]
>>> vec=CountVectoriser(ngram_range=(1,1))
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    vec=CountVectoriser(ngram_range=(1,1))
NameError: name 'CountVectoriser' is not defined
>>> vec=CountVectorizer(ngram_range=(1,1))
>>> vec
CountVectorizer(analyzer='word', binary=False, decode_error='strict',
        dtype=<class 'numpy.int64'>, encoding='utf-8', input='content',
        lowercase=True, max_df=1.0, max_features=None, min_df=1,
        ngram_range=(1, 1), preprocessor=None, stop_words=None,
        strip_accents=None, token_pattern='(?u)\\b\\w\\w+\\b',
        tokenizer=None, vocabulary=None)
>>> f_index=vec.get_feature_names()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    f_index=vec.get_feature_names()
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\lib\site-packages\sklearn\feature_extraction\text.py", line 1125, in get_feature_names
    self._check_vocabulary()
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\lib\site-packages\sklearn\feature_extraction\text.py", line 366, in _check_vocabulary
    check_is_fitted(self, 'vocabulary_', msg=msg),
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\lib\site-packages\sklearn\utils\validation.py", line 951, in check_is_fitted
    raise NotFittedError(msg % {'name': type(estimator).__name__})
sklearn.exceptions.NotFittedError: CountVectorizer - Vocabulary wasn't fitted.
>>> f_index=vec.vocabulary_.get("you")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    f_index=vec.vocabulary_.get("you")
AttributeError: 'CountVectorizer' object has no attribute 'vocabulary_'
>>> f_index=vec.vocabulary.get("you")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    f_index=vec.vocabulary.get("you")
AttributeError: 'NoneType' object has no attribute 'get'
>>> f_index=vec.vocabulary.get("this")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    f_index=vec.vocabulary.get("this")
AttributeError: 'NoneType' object has no attribute 'get'
>>> type(vec)
<class 'sklearn.feature_extraction.text.CountVectorizer'>
>>> x1=vec.fit_transform(sample2).toarray()
>>> x1
array([[0, 0, 1, 1, 1, 0],
       [1, 1, 0, 0, 0, 1],
       [0, 0, 1, 0, 1, 1]], dtype=int64)
>>> vec2=CountVectorizer(ngram_range=(2,2))
>>> x2=vec2.fit_transform(sample2).toarray()
>>> x2
array([[0, 0, 1, 0, 1],
       [1, 1, 0, 0, 0],
       [0, 0, 0, 1, 1]], dtype=int64)
>>> n2=CountVectorizer(ngram_range(2,2))
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    n2=CountVectorizer(ngram_range(2,2))
NameError: name 'ngram_range' is not defined
>>> n2=CountVectorizer(ngram_range=(2,2))
>>> snow_20=[]
>>> for i in d[20]:
	snow_20.append(i[4])

	
>>> len(snow_20)
18597
>>> snow_20[0]
"lol despit homemad bbq i'm gonna tonight watch #superbowl break fast , i'm still gonna make sure there room sardin spinach #cantgetenough "
>>> tr_20_s=n2.fit_transform(snow_20)
>>> sc=(tr_20_s.toarray())
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    sc=(tr_20_s.toarray())
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\lib\site-packages\scipy\sparse\compressed.py", line 962, in toarray
    out = self._process_toarray_args(order, out)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\lib\site-packages\scipy\sparse\base.py", line 1187, in _process_toarray_args
    return np.zeros(self.shape, dtype=self.dtype, order=order)
MemoryError
>>> tr_20_s=n2.fit_transform(snow_20[:50])
>>> sc=(tr_20_s.toarray())
>>> sc
array([[0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 0],
       ...,
       [0, 0, 0, ..., 0, 0, 0],
       [0, 0, 0, ..., 0, 0, 1],
       [0, 0, 0, ..., 0, 0, 0]], dtype=int64)
>>> ft=tr_20_s.get_feature_names()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    ft=tr_20_s.get_feature_names()
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\lib\site-packages\scipy\sparse\base.py", line 689, in __getattr__
    raise AttributeError(attr + " not found")
AttributeError: get_feature_names not found
>>> ft=n2.get
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    ft=n2.get
AttributeError: 'CountVectorizer' object has no attribute 'get'
>>> ft=n2.get_feature_names()
>>> ft
['02 black', '144th annual', '15 take', '16 comment', '16 follow', '16 retweet', '16 rt', '18 minut', '1st team', '1st vote', '20 free', '2019 joy', '204 breed', '2nd 2019', '30 foxnetwork', '30 pm', '35 year', '3am earli', '49er jersey', '49er nfl', '54 season', '630 entri', '67 year', '70 like', '700 leagu', '75 american', 'a_riggs6 realdonaldtrump', 'abort pleas', 'acmilan 35', 'action https', 'actual gameplay', 'ad cc', 'ad featur', 'allow commerci', 'alreadi tape', 'amaz perform', 'american citizen', 'american footbal', 'american want', 'among 630', 'ampl time', 'annual wkcdogshow', 'anthem sbliv', 'anyth like', 'ap lamar', 'app https', 'app yahoo', 'appar there', 'appreci retweet', 'area super', 'arriv super', 'arrow variation', 'arsenal fan', 'arsenal play', 'ask nfl', 'associ press', 'attack slam', 'averag american', 'awar realdonaldtrump', 'award unanim', 'babysit grandkid', 'back hous', 'badg colour', 'bbq gonna', 'bc mistook', 'becam american', 'befor elect', 'berni make', 'berni sander', 'best play', 'best show', 'best way', 'bet must', 'better kurt13warn', 'big day', 'big game', 'big snack', 'big thing', 'big win', 'bigot breed', 'black heart', 'black rightwards', 'bloomberg goe', 'bonus point', 'born rais', 'bowl debut', 'bowl fox', 'bowl held', 'bowl seen', 'break fast', 'break leg', 'breath realli', 'breed ground', 'breed varieti', 'brilliant https', 'broadcast network', 'broadcast smiley', 'call superhug', 'call work', 'car walk', 'card pictur', 'card superbowl', 'cardsfromatt black', 'care footbal', 'cc donaldjtrumpjr', 'cc realdonaldtrump', 'cd 15', 'challeng offici', 'chief 49er', 'chief superbowl', 'chiefskingdom via', 'chip wing', 'citi born', 'citizen 1st', 'clintbowy look', 'closest score', 'closet open', 'club ll', 'co 1tcjcvtrha', 'co 2wijvl9suy', 'co 3u6i44yidi', 'co 5piifiizuc', 'co 5y4mbur1fq', 'co a27oemvtkl', 'co c81hmpcjji', 'co ciqicdrszt', 'co d6gowz2rfi', 'co ddryxawezo', 'co hhknc4fdy', 'co ieanzgwdur', 'co ilglblx3y4', 'co j2dmca1v0b', 'co ooela4vaut', 'co q7t2ouvbxd', 'co rp245if6fi', 'co rr4xajksfi', 'co rrxjqvf622', 'co snufaowrfi', 'co tj7ufuiakf', 'co tm66dtbw44', 'co wqmphsulmr', 'co xkrxlsv5k6', 'co yewlrzmbuj', 'co zmithoqdqd', 'colour stadium', 'come littl', 'comment favorit', 'comment win', 'comment winner', 'commerci featur', 'compet take', 'competit start', 'complain foxtv', 'complain sacrific', 'complet tight', 'contain 18', 'correct score', 'could face', 'course what', 'cozierpanda yep', 'crazi berni', 'daniel maldini', 'day footbal', 'day got', 'ddlovato relish', 'death chief', 'debut acmilan', 'debut chiefskingdom', 'delici thing', 'dem primari', 'demi perform', 'democrat join', 'democrat parti', 'despit homemad', 'disgust disrespect', 'disinform interview', 'disrespect neymar', 'donaldjtrumpjr https', 'done less', 'doubl oof', 'downfal superbowl', 'drag queen', 'dude look', 'earli flight', 'earn associ', 'earn posit', 'el paso', 'elect talk', 'elizabeth pocahonta', 'emoji modifier', 'end one', 'ensur realdonaldtrump', 'entri compet', 'entri pass', 'ericbeachgop appreci', 'esmuellert_ nfl', 'et fox', 'everyth fake', 'everyth need', 'exclus sneak', 'fa fine', 'face berni', 'face crazi', 'face fa', 'factcheck https', 'fail miser', 'fake hair', 'fan point_down', 'fan real', 'fast still', 'fast superbowl', 'father 67', 'favorit footbal', 'favourit footbal', 'featur drag', 'featur peopl', 'feel need', 'fine action', 'finish la', 'fitzpatrick type', 'flight go', 'follow cardsfromatt', 'footbal brilliant', 'footbal club', 'footbal fan', 'footbal game', 'footbal https', 'footbal lad', 'footbal much', 'footbal need', 'footbal season', 'footbal sinc', 'footbal team', 'footbal wise', 'football predict', 'football watch', 'forget presid', 'forward see', 'fox allow', 'fox awar', 'fox iphone', 'foxnetwork doubl', 'foxnetwork enjoy', 'foxnetwork wow', 'foxnetwork yes', 'foxtv nflonfox', 'foxtv superbowlliv', 'francisco met', 'free bet', 'free card', 'free entri', 'free https', 'full season', 'game contain', 'game day', 'game footbal', 'game gone', 'game got', 'game today', 'game watch', 'gameplay superbowlliv', 'gave open', 'general best', 'get infrastructur', 'get know', 'get year', 'girl ddlovato', 'giveaway 02', 'giveaway football', 'gkittle46 point_down', 'global heat', 'go babysit', 'go superbowl', 'go win', 'goe attack', 'golf course', 'golf twitter', 'gone shit', 'gonna make', 'gonna tonight', 'goof golf', 'gop tell', 'got big', 'got everyth', 'got yell', 'grandfath footbal', 'grandkid sarahhuckabe', 'grandson call', 'grow fast', 'guardiola could', 'hair obes', 'happen tri', 'hard would', 'haymacsue2011 matthewjshow', 'heard singl', 'heart variation', 'heat death', 'heavy black', 'held year', 'histori know', 'home best', 'homemad bbq', 'honest never', 'hope win', 'hous repres', 'https co', 'human traffick', 'husband go', 'increas area', 'incred superbowl', 'infrastructur done', 'interview 30', 'interview alreadi', 'interview poor', 'invit https', 'involv gop', 'iphone nfl', 'jackson stun', 'jersey upcom', 'join team', 'joke fail', 'joke lmaooo', 'joy arsenal', 'joy joy', 'judg badg', 'justic system', 'kansa citi', 'know elizabeth', 'know made', 'know spread', 'kurt13warn michaelirvin88', 'la joy', 'lad power', 'lamar jackson', 'lamar reaction', 'latina becam', 'leagu send', 'left democrat', 'leg girl', 'less goof', 'level point', 'liar lie', 'lie everyth', 'lie know', 'lie patholog', 'life game', 'like life', 'like relat', 'like see', 'list name', 'list player', 'littl short', 'liverpool would', 'll judg', 'load chip', 'lol despit', 'look forward', 'look sound', 'love today', 'lrihendri realdonaldtrump', 'made progress', 'made seri', 'make challeng', 'make joke', 'make sure', 'maldini made', 'matter broadcast', 'matter puppybowlxvi', 'matthewjshow realdonaldtrump', 'may big', 'may come', 'me need', 'met latina', 'met young', 'miami ap', 'michaelirvin88 big', 'mickey mous', 'might miss', 'million peopl', 'minimik minimikebloomberg', 'minimikebloomberg superbowl', 'minut actual', 'miss game', 'missouri bigot', 'mistook us', 'modifier fitzpatrick', 'mog chief', 'moment incred', 'monday https', 'monica tx15', 'morn nfl', 'mous though', 'movement grow', 'much care', 'much feel', 'must heavy', 'mvp https', 'mvp video', 'name call', 'name peopl', 'nascaronfox broadcast', 'nation anthem', 'need big', 'need start', 'need suck', 'need tweet', 'network https', 'network respons', 'never forget', 'never see', 'never seen', 'never surpass', 'next season', 'nfl app', 'nfl happen', 'nfl https', 'nfl network', 'nfl player', 'nfl sbliv', 'nfl valuabl', 'nflgameday morn', 'nflonfox superbowl', 'nflonfox tv', 'nope ten', 'novemb 2nd', 'obes spray', 'offici clintbowy', 'on tan', 'one better', 'one week', 'onlaon whole', 'open invit', 'open set', 'owl repres', 'parscal lrihendri', 'parti involv', 'partner bc', 'paso met', 'pass car', 'pass telegram', 'patholog liar', 'patholog trump', 'patrickmahom arriv', 'peek tonight', 'peopl care', 'peopl see', 'peopl surviv', 'peopl think', 'peopl watch', 'pep guardiola', 'perform nation', 'pick monday', 'pick someon', 'pictur winner', 'pink sweati', 'play load', 'play singl', 'player 700', 'player award', 'player presid', 'pleas complain', 'pleas rt', 'pm et', 'pocahonta warren', 'point arsenal', 'point sb', 'point_down emoji', 'point_down tv', 'poor me', 'posit wanna', 'power good', 'predict correct', 'presid trump', 'presid unit', 'press nfl', 'primari voter', 'probabl never', 'progress footbal', 'puffi breath', 'puppybowlxvi https', 'queen ad', 'r_evoluti appar', 'rais husband', 'raised_hands via', 'ray_schiffer26 esmuellert_', 'reaction mvp', 'readi watch', 'real competit', 'realdonaldtrump face', 'realdonaldtrump https', 'realdonaldtrump lie', 'realdonaldtrump never', 'realdonaldtrump superbowl', 'realli get', 'realli matter', 'realli pink', 'recent left', 'red finish', 'regular 1st', 'relat global', 'relish moment', 'report pep', 'repres democrat', 'repres symbol', 'respons million', 'retweet cc', 'retweet pick', 'right movement', 'rightwards arrow', 'room sardin', 'rrxjqvf622 https', 'rt peopl', 'rt tweet', 'sacrific get', 'san francisco', 'sander general', 'sarahhuckabe kansa', 'sardin spinach', 'say gkittle46', 'sb mvp', 'sbliv 30', 'sbliv nfl', 'sbliv superbowl', 'score bonus', 'score free', 'screami dude', 'season earn', 'season footbal', 'season full', 'season regular', 'season texa', 'season trash', 'see golf', 'see https', 'see stay', 'see wear', 'seen 54', 'seen anyth', 'selector 16', 'send list', 'send love', 'seri debut', 'set free', 'shakira superbowl', 'shit disgust', 'short footbal', 'show thread', 'sinc novemb', 'singl game', 'singl list', 'slam patholog', 'smiley readi', 'snack best', 'sneak peek', 'someon comment', 'someth special', 'sound exact', 'special raised_hands', 'spinach cantgetenough', 'sport app', 'spray on', 'spread disinform', 'stadium histori', 'start begin', 'start earn', 'start one', 'state gave', 'stay onlaon', 'still gonna', 'still win', 'stun season', 'suck get', 'super bowl', 'superbowl ad', 'superbowl break', 'superbowl complain', 'superbowl face', 'superbowl foxnetwork', 'superbowl foxtv', 'superbowl giveaway', 'superbowl hope', 'superbowl https', 'superbowl interview', 'superbowl nationalanthem', 'superbowl realli', 'superbowl superbowlliv', 'superbowl today', 'superbowl watch', 'superbowl wolf', 'superbowlliv https', 'superbowlliv pleas', 'superhug might', 'sure dem', 'sure there', 'surpass amaz', 'surviv abort', 'sweati screami', 'symbol downfal', 'system heard', 'take back', 'take home', 'talk complet', 'talk work', 'tan 75', 'tape ampl', 'team black', 'team footbal', 'team monica', 'team need', 'telegram 20', 'tell favourit', 'tell right', 'ten million', 'texa still', 'texan may', 'there footbal', 'there room', 'thing game', 'thing say', 'think unfair', 'thisisanfield like', 'thread https', 'tight end', 'time factcheck', 'tm66dtbw44 https', 'today break', 'today football', 'today super', 'today weather', 'tonight minimik', 'tonight watch', 'traffick increas', 'trash progress', 'treat justic', 'tri make', 'trump ask', 'trump interview', 'trump lie', 'trump san', 'tv nflgameday', 'tv sbliv', 'tweet comment', 'tweet much', 'twitter name', 'two women', 'tx15 https', 'type https', 'type point_down', 'ucl know', 'unanim https', 'unfair treat', 'unit state', 'upcom nascaronfox', 'us two', 'valuabl player', 'variation selector', 'varieti among', 'via nfl', 'via nflonfox', 'video someth', 'vote trump', 'voter realli', 'walk partner', 'wanna ucl', 'want win', 'want wit', 'warren ericbeachgop', 'watch demi', 'watch fox', 'watch mickey', 'watch super', 'watch superbowl', 'watch three', 'way ensur', 'wear 49er', 'weather wonder', 'week 144th', 'what happen', 'whole next', 'win big', 'win card', 'win cd', 'win free', 'win got', 'win superbowl', 'wing delici', 'winner closest', 'winner pick', 'wise next', 'wit mog', 'without doubt', 'wkcdogshow 204', 'wolf closet', 'woman recent', 'women missouri', 'wonder 70', 'work befor', 'work hard', 'would level', 'would probabl', 'wow trump', 'yahoo sport', 'year father', 'year grandfath', 'year grandson', 'year owl', 'yell pass', 'yep team', 'yes puffi', 'young woman']
>>> 
