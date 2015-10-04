# -*- coding: utf-8 -*-

"""
です→だよ！ のように天気予報を堅苦しくなく
文字列変換し、口調を柔らかくするためのモジュール。
"""

from string import maketrans, translate
import re

trans_tone_dict = {
		u'岩手県': u'現在の岩手県滝沢市',
		u'より、': u'よって、',
		u'います': u'いるよ。',
		u'概ね': u'おおむね',
		u'ため': u'から',
		u'でしょう': u'と思います',
}

def multiple_replace(text, adict):
	""" 一度に複数のパターンを置換する関数
	- text中からディクショナリのキーに合致する文字列を探し、対応の値で置換して返す
	- キーでは、正規表現を置換前文字列とできる
	"""

	rx = re.compile('|'.join(adict))
	def dedictkey(text):
		""" マッチした文字列の元であるkeyを返す
		"""
		for key in adict.keys():
			if re.search(key, text):
				return key

	def one_xlat(match):
		return adict[dedictkey(match.group(0))]

	return rx.sub(one_xlat, text)

def get_soft_tone(content):
	return multiple_replace(content, trans_tone_dict)