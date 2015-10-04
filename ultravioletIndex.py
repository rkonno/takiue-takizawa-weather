# -*- coding: utf-8 -*-

u"""
紫外線指数の値をスクレイピングにより取得し、指数値を元に紫外線に対するコメントを
付けて文章化するモジュール。
"""

def get_ultraviolet_comment(ultraviolet_value):
	u""" 紫外線指数値からいい感じのコメントでその日紫外線の強さがどうかアドバイスする文章を生成する関数
	引数にultraviolet_value(紫外線指数値)を渡すと、それに見合った外出の際の紫外線へのアドバイスを行います。
	"""
	ULTRAVIOLET_VALUE_TO_COMMENT = {
		u'弱い': u'特に心配はいらないかとおもいます',
		u'やや弱い': u'特に心配いらない紫外線指数値ではありますが、心配であれば日焼け止めを。',
		u'やや強い': u'日焼け止めクリームを使った方がよさそうです。',
		u'強い': u'帽子をかぶり、日焼け止めを使った方がよさそうです。いつもバッグに常備すると安心です。',
		u'非常に強い': u'日焼け止めクリーム必須です。日中外を歩く場合は帽子や日傘が必要かも。'
	}

	return ULTRAVIOLET_VALUE_TO_COMMENT[ultraviolet_value]

def get_today_ultraviolet(weather_index):
	u""" 取得した今日の紫外線指数を整形して文章にして渡す関数
	例：	今日の紫外線指数：やや強い
		日焼け止めクリームを使った方がよさそうです。
	"""
	# 今日の紫外線指数の値を代入
	ultraviolet_value = weather_index['results']['collection3'][0]['ultraviolet_value']
	# 値とコメントをいい感じに整形
	today_ultraviolet_main = u'今日の紫外線指数：' + ultraviolet_value + u'\n' +\
	get_ultraviolet_comment(ultraviolet_value)

	return today_ultraviolet_main

def get_tomorrow_ultraviolet(weather_index):
	u""" 取得した明日の紫外線指数を整形して文章にして渡す関数
	例：	明日の紫外線指数：強い
		帽子をかぶる、日焼け止めを使った方がよさそうです。いつもバッグに常備すると安心です。
	"""
	# 明日の紫外線指数の値を代入
	ultraviolet_value = weather_index['results']['collection3'][1]['ultraviolet_value']
	# 値とコメントをいい感じに整形
	tomorrow_ultraviolet_main = u'明日の紫外線指数：' + ultraviolet_value + u'\n' +\
	get_ultraviolet_comment(ultraviolet_value)

	return tomorrow_ultraviolet_main