# -*- coding: utf-8 -*-

u"""
傘指数の値をスクレイピングにより取得し、値を元に傘に対するコメントを
付けて文章化するモジュール。
"""

def get_umbrella_comment(umbrella_value):
	u""" 傘指数からいい感じのコメントでその日傘が必要かどうかアドバイスする文章を生成する関数
	引数にumbrella_value(傘指数)を渡すと、それに見合った外出の際の傘の必要性をアドバイスを行います。
	"""
	UMBRELLA_VALUE_TO_COMMENT = {
		u'0': u'傘は必要ありません！',
		u'10': u'傘を持って行かなくても大丈夫です！',
		u'20': u'傘を使うことは恐らくなさそうなので、持って行かなくても大丈夫です。',
		u'30': u'降ってもそこまで濡れないと思うので傘は必要なさそう。',
		u'40': u'折りたたみ傘がカバンに入っていると安心かも。',
		u'50': u'折りたたみ傘を持って出かけよう！',
		u'60': u'傘を持って出かけた方が安心です。',
		u'70': u'傘を持って出かけましょう。',
		u'80': u'雨が降りそうです。傘を持って出かけましょう。',
		u'90': u'小さめの傘だと心もとないかも。大きい傘を持って出かけましょう！',
		u'100': u'傘を持って出かけよう！'
	}

	return UMBRELLA_VALUE_TO_COMMENT[umbrella_value]

def get_today_umbrella(weather_index):
	u""" 取得した今日の傘指数を整形して文章にして渡す関数
	例：	今日の傘指数：70
		傘を持って出かけましょう。
	"""
	# 今日の傘指数の値を代入
	umbrella_value = weather_index['results']['collection2'][0]['umbrella_value']
	# 値とコメントをいい感じに整形
	today_umbrella_main = u'今日の傘指数：' + umbrella_value + u'\n' +\
	get_umbrella_comment(umbrella_value)

	return today_umbrella_main

def get_tomorrow_umbrella(weather_index):
	u""" 取得した明日の傘指数を整形して文章にして渡す関数
	例：　明日の傘指数：30
		降ってもそこまで濡れないと思うので傘は必要なさそう。
	"""
	# 明日の傘指数の値を代入
	umbrella_value = weather_index['results']['collection2'][1]['umbrella_value']
	# 値とコメントをいい感じに整形
	tomorrow_umbrella_main = u'明日の傘指数：' + umbrella_value + u'\n' +\
	get_umbrella_comment(umbrella_value)

	return tomorrow_umbrella_main