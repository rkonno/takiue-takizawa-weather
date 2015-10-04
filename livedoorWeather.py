# -*- coding: utf-8 -*-

import requests
from datetime import datetime
from weather_image import get_image
from transformation_tone import get_soft_tone

def get_livedoor_weather(id):
	""" Livedoor Weather Web Serviceの天気を取得する関数
	- 取得して return で結果を返す
	"""
	# 地域コードを指定
	location_city_id = {'city': id} # 岩手県内陸
	# JSONデータ取得先
	url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
	# 地域コードを指定して天気情報をリクエスト
	response = requests.get(url, params=location_city_id)
	# JSONデコードにしてreturn
	return response.json()


def description_formating(weather_outline):
	""" 取得した天気情報の概要（descriptionのtext）情報を整形する関数
	- そのままdescription,textを出力すると200文字近い。
	- Twiterの制限文字数は140文字なため、そのままだとツイートできない。
	- そこで、余分な情報をスライス等して140文字以内にまとめる。
	"""
	# アウトラインを一度改行コードでsplitして消して、文字列型に変換してtempに入れている
	temporarily = ''.join(weather_outline.split('\n'))
	# 岩手県以前の文章は不要なため、岩手県のindexを取得
	start_index = temporarily.find(u'岩手県')
	# <天気変化等の留意点>は不要なので < のindexを取得
	end_index = temporarily.find(u'<')
	# 文字列を必要な範囲で指定してスライスしリターン
	return temporarily[start_index : end_index]


def get_outline_weather():
	""" 現在からの天気の見通しであるアウトラインを生成する関数
	例：　現在の岩手県滝沢市は、曇りや晴れで、雨や雷雨となっている所があります。
		3日夜は、気圧の谷の影響によって、曇りで雨や雷雨となる所があると思います。
		4日は、高気圧に覆われて晴れますが、気圧の谷や寒気の影響によって、
		朝晩は曇りで雨の降る所がある見込みです。
	"""
	weather_outline = description_formating(weather_live['description']['text'])
	soft_weather_outline = get_soft_tone(weather_outline)
	return soft_weather_outline


def get_livedoor_weather_results():
	# livedoorの天気を投げる
	return weather_live


# livedoorの天気を取得する(岩手県内陸)
weather_live = get_livedoor_weather('030010')