# -*- coding: utf-8 -*-

u"""
ビール指数の値をスクレイピングにより取得し、指数値を元にビールがうまい日等とコメントを
付けて文章化するモジュール。
"""

def get_beer_comment(beer_value):
	u""" ビール指数値からいい感じのコメントでその日ビールがおいしいかアドバイスする文章を生成する関数
	引数にbeer_value(ビール指数値)を渡すと、ビールがうまい等とアドバイスを行います。
	"""
	BEER_VALUE_TO_COMMENT = {
		u'10': u'今日は暖かい部屋で、温かい熱燗でも飲んでまったりしましょう。',
		u'20': u'おつまみがあるとよりビールがすすみますよ！',
		u'30': u'いつもと違うビールを買って帰りませんか？',
		u'40': u'TVでも見ながらビールでもどうですか？',
		u'50': u'ビールがおいしい日です。飲みすぎないように！',
		u'60': u'ビールが飲みたくなるビール日和です。帰りに買って帰りませんか？',
		u'70': u'こんな日はビールがおいしいはずです。家にない？コンビニで買って帰りましょう！',
		u'80': u'暑い！今日はビールを飲んで、疲れを吹き飛ばしましょう。',
		u'90': u'今日は暑かったですね！冷えたビールを飲んで生き返りましょう！！',
		u'100': u'キンッキンに冷やしたビールを飲みましょう！冷凍庫で冷やして飲む際には忘れずに1時間以内に取り出してくださいね！'
	}

	return BEER_VALUE_TO_COMMENT[beer_value]

def get_today_beer(weather_index):
	u""" 取得した今日のビール指数を整形して文章にして渡す関数
	例：	今日のビール指数：60
		ビールが飲みたくなるビール日和です。帰りに買って帰りませんか？
	"""
	# 今日のビール指数の値を代入
	beer_value = weather_index['results']['collection5'][0]['beer_value']
	# 値とコメントをいい感じに整形
	today_beer_main = u'今日のビール指数：' + beer_value + u'\n' +\
	get_beer_comment(beer_value)

	return today_beer_main

def get_tomorrow_beer(weather_index):
	u""" 取得した明日のビール指数を整形して文章にして渡す関数
	例：　明日のビール指数：70
		こんな日はビールがおいしいはずです。家にない？コンビニで買って帰りましょう！
	"""
	# 明日のビール指数の値を代入
	beer_value = weather_index['results']['collection5'][1]['beer_value']
	# 値とコメントをいい感じに整形
	tomorrow_beer_main = u'明日のビール指数：' + beer_value + u'\n' +\
	get_beer_comment(beer_value)

	return tomorrow_beer_main