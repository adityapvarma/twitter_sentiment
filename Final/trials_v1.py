#Basic auth and tweet collection

import tweepy
import sys

non_bmp_map=dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


api_key="YIHxNkdYNGzrNdj0TPfFbnFmR"
api_seckey="BY2p6WVm0L5j4TV55l3Hj7tpexjIz6xeSjh676psFAYXRmuNqI"

acc_tok="974952819223445505-Hdiytd67IFrwtzUoZSKkJdFJbfjGUev"
acc_toksec="skAIgktED0hfVnVUsvhJyEAS5xDSX20HOocFFb0VUNT16"

#auth=tweepy.AppAuthHandler(api_key,api_seckey)
auth=tweepy.OAuthHandler(api_key,api_seckey)
auth.set_access_token(acc_tok,acc_toksec)

api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Verified")
except:
    print("Some error")



test=[]

for i in tweepy.Cursor(api.search,q='NFL',lang=["en"]).items(20):
    print(i.text.translate(non_bmp_map))
    test.append(i)
