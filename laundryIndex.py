# -*- coding: utf-8 -*-

u"""
天気指数の値をスクレイピングにより取得し、値を元に選択に対するコメントを
付けて文章化するモジュール。
"""

def get_laundry_comment(laundry_value):
	u""" 洗濯指数からいい感じのコメントでその日の洗濯をアドバイスする文章を生成する関数
	引数にlaundry_value(洗濯指数)を渡すと、それに見合った洗濯アドバイスを行います。
	"""
	LAUNDRY_VALUE_TO_COMMENT = {
		u'0': u'ほとんど乾きません。除湿器があればなんとか…。',
		u'10': u'部屋干しがいいです。プラス除湿器があればいいかも。',
		u'20': u'乾きづらいので、朝から干してもあまり乾かないかも。室内干しをオススメします。',
		u'30': u'雨に濡れちゃう可能性もあるので部屋干しがいいかも。乾燥機があれば使うことをオススメします。',
		u'40': u'早い時間に洗濯すれば、夕方にはなんとか乾くかも。じっくり干せば問題なし。',
		u'50': u'シャツや薄手の服、化学繊維のものは乾くかもしれない。',
		u'60': u'朝に干せば厚くない洋服であれば、乾きます。',
		u'70': u'Tシャツは乾くけど、厚手のものは乾きづらいです。',
		u'80': u'昼に洗濯しても夕方までには乾くかも。洗濯日和です。',
		u'90': u'バスタオルもバッチリ乾く洗濯日和です！',
		u'100': u'ジーンズも厚手の洋服もバッチリ乾く、絶好の洗濯日和です！'
	}

	return LAUNDRY_VALUE_TO_COMMENT[laundry_value]

def get_today_laundry(weather_index):
	u""" 取得した今日の洗濯指数を整形して文章にして渡す関数
	例：	今日の洗濯指数：30
		雨に濡れちゃう可能性もあるので部屋干しがいいかも。乾燥機があれば使うことをオススメします。
	"""
	# 今日の洗濯指数の値を代入
	laundry_value = weather_index['results']['collection1'][0]['laundry_value']
	# 値とコメントをいい感じに整形
	today_laundry_main = u'今日の洗濯指数：' + laundry_value + u'\n' +\
	get_laundry_comment(laundry_value)

	return today_laundry_main

def get_tomorrow_laundry(weather_index):
	u""" 取得した明日の洗濯指数を整形して文章にして渡す関数
	例：	明日の洗濯指数：70
		Tシャツは乾くけど、厚手のものは乾きづらいです。
	"""
	# 明日の洗濯指数の値を代入
	laundry_value = weather_index['results']['collection1'][1]['laundry_value']
	# 値とコメントをいい感じに整形
	tomorrow_laundry_main = u'明日の洗濯指数：' + laundry_value + u'\n' +\
	get_laundry_comment(laundry_value)

	return tomorrow_laundry_main