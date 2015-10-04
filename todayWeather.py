# -*- coding: utf-8 -*-

import json
import urllib
from livedoorWeather import get_outline_weather, get_livedoor_weather_results
from weather_image import get_image

u"""
朝につぶやく「きょうの天気」
get_outline_weather関数は、本日の天気のアウトライン
get_today_weather関数は、本日の天気の概要（天気、気温、降水確率）
"""

def get_today_weather():
	""" 今日の天気をツイートする形に文章を生成する関数
	例：	滝沢市の今日10月3日(土)の天気をお知らせ！
		曇り☁のち雨☔
		MAX:23℃[+3], MIN:14℃[-3]
		降水確率は…
		06-12:---
		12-18:---
		18-24:60％
		という予報になっています。
	"""
	# livedoorWeatherのresultsを取得
	weather_live = get_livedoor_weather_results()
	# 天気概要（例：曇りのち晴れ）に＋イメージ（絵文字）を付加したものを取得
	weather_forecast = get_image(weather_live['forecasts'][0]['telop'])
	# ウェブスクレイピングした天気を取得
	weather_scraping = json.load(urllib.urlopen("https://www.kimonolabs.com/api/a8nvvyiu?apikey=U5S4dcwJSMsfkd71LKNslC42ZhTyJxWB"))
	# 今日の日付を取得
	today_date = weather_scraping['results']['collection1'][0]['weather']
	# 今日の最高気温を取得
	today_maxTemp = weather_scraping['results']['collection2'][0]['temp']
	#　今日の最低気温を取得
	today_minTemp = weather_scraping['results']['collection2'][1]['temp']
	# 今日の降水確率を取得
	rainyper_6_12 =  weather_scraping['results']['collection3'][1]['rainyper_6-12']
	rainyper_12_18 =  weather_scraping['results']['collection3'][1]['rainyper_12-18']
	rainyper_18_24 =  weather_scraping['results']['collection3'][1]['rainyper_18-24']
	# 滝沢市／今日の天気
	today_weather_announce = u'滝沢市の天気をお知らせ！\n' + \
	u'本日' + today_date + u'は ' + weather_forecast + u' で,\n' +\
	u'最高気温は' + today_maxTemp + u', 最低気温は' + today_minTemp + u'となる見込みです.\n' +\
	u'降水確率は…\n' + \
	u'06-12:' +  rainyper_6_12 + u'\n' + \
	u'12-18:' +  rainyper_12_18 + u'\n' + \
	u'18-24:' +  rainyper_18_24 + u'\n' + \
	u'という予報になっています.'

	return today_weather_announce
