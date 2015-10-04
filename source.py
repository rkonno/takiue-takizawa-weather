# -*- coding: utf-8 -*-
import json
import urllib
from datetime import datetime
from tweet import do_Tweet
from todayWeather import get_today_weather
from tomorrowWeather import get_tomorrow_weather
from livedoorWeather import get_outline_weather
from laundryIndex import get_today_laundry, get_tomorrow_laundry
from umbrellaIndex import get_today_umbrella, get_tomorrow_umbrella
from ultravioletIndex import get_today_ultraviolet, get_tomorrow_ultraviolet
from starIndex import get_today_star, get_tomorrow_star
from beerIndex import get_today_beer, get_tomorrow_beer

weather_index = json.load(urllib.urlopen("https://www.kimonolabs.com/api/b9rljpwg?apikey=U5S4dcwJSMsfkd71LKNslC42ZhTyJxWB"))

"""
【何時に何を呟くか　CRON実行　→ 05 7,9,12,18,21 * * * 】
07時	:	今日の天気 get_today_weather を実行,
		今日のアウトライン get_outline_weather を実行,
		傘指数 get_today_umbrella を実行,
		紫外線指数 get_today_ultraviolet　を実行

09時:	洗濯指数　	get_today_laundry　を実行

12時:	今日の今からの天気　get_outline_weather を実行,
		これからの今日の降水確率	

18時:	明日の天気 get_tomorrow_weather を実行,
		星空指数 	get_today_star を実行,
		ビール指数 get_today_beer　を実行

21時:	明日の天気 get_tomorrow_weather を実行,
		いまから明日にかけてのアウトライン get_outline_weather を実行,
		星空指数 get_today_star を実行
"""

# 現在時刻を取得
now_hour = datetime.now().hour
if now_hour == 7:
	# 7時に…

	# 今日の天気を呟く
	todayWeather = get_today_weather()
	print todayWeather
	do_Tweet(todayWeather)

	# 今日のアウトラインを呟く
	todayOutline = get_outline_weather()
	print todayOutline
	do_Tweet(todayOutline)

	# 今日の傘指数を呟く
	todayUmbrella = get_today_umbrella(weather_index)
	print todayUmbrella
	do_Tweet(todayUmbrella)

	# 今日の紫外線指数を呟く
	todayUltraviolet = get_today_ultraviolet(weather_index)
	print todayUltraviolet
	do_Tweet(todayUltraviolet)

elif now_hour == 9:
	# 9時に…

	#今日の洗濯指数を呟く
	todayLaundry = get_today_laundry(weather_index)
	print todayLaundry
	do_Tweet(todayLaundry)

elif now_hour == 12:
	# 12時に…

	# 今日のこれからのアウトラインを呟く
	todayOutline = get_outline_weather()
	print todayOutline
	do_Tweet(todayOutline)

elif now_hour == 18:
	# 18時に…

	# 明日の天気を呟く
	tomorrowWeather = get_tomorrow_weather()
	print tomorrowWeather
	do_Tweet(tomorrowWeather)

	# 星空指数を呟く
	todayStar = get_today_star(weather_index)
	print todayStar
	do_Tweet(todayStar)

	# ビール指数を呟く
	todayBeer = get_today_beer(weather_index)
	print todayBeer
	do_Tweet(todayBeer)

elif now_hour == 21:
	# 21時に…

	# 明日の天気を呟く
	tomorrowWeather = get_tomorrow_weather()
	print tomorrowWeather
	do_Tweet(tomorrowWeather)

	# 今日明日にかけてのアウトラインを呟く
	todayOutline = get_outline_weather()
	print todayOutline
	do_Tweet(todayOutline)

	# 星空指数を呟く
	todayStar = get_today_star(weather_index)
	print todayStar
	do_Tweet(todayStar)
else:
	print u"エラー：どこにも当てはまらない時間のため何も呟かない"
