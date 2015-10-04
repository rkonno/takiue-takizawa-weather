# -*- coding: utf-8 -*-

import json
import urllib
from livedoorWeather import get_outline_weather, get_livedoor_weather_results
from weather_image import get_image

u"""
夕方と夜につぶやく「あしたの天気」
get_outline_weather関数は、今日から明日にかけての天気のアウトライン
get_tomorrow_weather関数は、明日の天気の概要（天気、気温、降水確率）
"""

def get_tomorrow_weather():
	""" 明日の天気をツイートする形に文章を生成する関数
	例：	滝沢市の明日10月4日(日)の天気をお知らせ！
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
	weather_forecast = get_image(weather_live['forecasts'][1]['telop'])
	# ウェブスクレイピングした天気を取得
	weather_scraping = json.load(urllib.urlopen("https://www.kimonolabs.com/api/8zh19qmm?apikey=U5S4dcwJSMsfkd71LKNslC42ZhTyJxWB"))
	# 明日の日付を取得
	tomorrow_date = weather_scraping['results']['collection1'][0]['weather']
	# 明日の最高気温を取得
	tomorrow_maxTemp = weather_scraping['results']['collection2'][0]['temp']
	#　明日の最低気温を取得
	tomorrow_minTemp = weather_scraping['results']['collection2'][1]['temp']
	# 明日の降水確率を取得
	rainyper_0_6 = weather_scraping['results']['collection3'][1]['rainyper_0-6']
	rainyper_6_12 =  weather_scraping['results']['collection3'][1]['rainyper_6-12']
	rainyper_12_18 =  weather_scraping['results']['collection3'][1]['rainyper_12-18']
	rainyper_18_24 =  weather_scraping['results']['collection3'][1]['rainyper_18-24']
	# 滝沢市／明日の天気
	tomorrow_weather_announce = u'滝沢市の天気をお知らせ！\n' + \
	u'明日' + tomorrow_date + u'は ' + weather_forecast + u' で,\n' +\
	u'最高気温は' + tomorrow_maxTemp + u', 最低気温は' + tomorrow_minTemp + u'となる見込みです.\n' +\
	u'降水確率は…\n' + \
	u'00-06:' +  rainyper_0_6 + u'\n' + \
	u'06-12:' +  rainyper_6_12 + u'\n' + \
	u'12-18:' +  rainyper_12_18 + u'\n' + \
	u'18-24:' +  rainyper_18_24 + u'\n' + \
	u'という予報になっています.'

	return tomorrow_weather_announce