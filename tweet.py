#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tweetモジュール

do_Tweetを呼び出せばかんたんにtweetできるモジュール
"""

from requests_oauthlib import OAuth1Session

def do_Tweet(content):
	CK = 'your_CK' # Consumer Key
	CS = 'your_CS' # Consumer Secret
	AT = 'your_AT' # Access Token
	AS = 'your_AS' # Accesss Token Secer

	# ツイート投稿用のURL
	url = "https://api.twitter.com/1.1/statuses/update.json"

	# ツイート本文
	tweet = {"status": content}

	# OAuth認証で POST method で投稿
	twitter = OAuth1Session(CK, CS, AT, AS)
	req = twitter.post(url, params = tweet)

	# レスポンスを確認
	if req.status_code == 200:
	    print ("OK")
	else:
	    print ("Error: %d" % req.status_code)