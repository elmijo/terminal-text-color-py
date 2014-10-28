# -*- coding: utf-8 -*-
import unittest

try:
	from terminal_text_color import *
except ImportError:
	import os,sys
	sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
	from terminal_text_color import AlertTextColor

class AlertTextColorTest(unittest.TestCase):
	"""docstring for AlertTextColorTest"""

	def setUp(self):
		self.atc = AlertTextColor()
		self.text = "Hola"
		self.longtext = "hola esto es una prueba de un texto largo, mas largo de lo normal"

	def testAlertError(self):
		self.assertIsNone(self.atc.error(self.text))

	def testAlertSuccess(self):
		self.assertIsNone(self.atc.success(self.text))

	def testAlertWarning(self):
		self.assertIsNone(self.atc.warning(self.text))

	def testAlertInfo(self):
		self.assertIsNone(self.atc.info(self.text))

	def testAlertInfoAlt(self):
		self.assertIsNone(self.atc.info_alt(self.text))

	def testAlertCustomColor(self):
		self.assertIsNone(self.atc.custom(self.text,color='cyan'))

	def testAlertCustomBackground(self):
		self.assertIsNone(self.atc.custom(self.text,background='magenta'))

	def testAlertCustomStyle(self):
		self.assertIsNone(self.atc.custom(self.text,style='bold'))

	def testAlertCustomStyleColor(self):
		self.assertIsNone(self.atc.custom(self.text,style='bold',color='cyan'))

	def testAlertCustomStyleColorBackground(self):
		self.assertIsNone(self.atc.custom(self.text,style='bold',color='cyan',background='magenta'))

	def testAlertErrorLongText(self):
		self.assertIsNone(self.atc.error(self.longtext))

	def testAlertSuccessLongText(self):
		self.assertIsNone(self.atc.success(self.longtext))

	def testAlertWarningLongText(self):
		self.assertIsNone(self.atc.warning(self.longtext))

	def testAlertInfoLongText(self):
		self.assertIsNone(self.atc.info(self.longtext))

	def testAlertInfoAltLongText(self):
		self.assertIsNone(self.atc.info_alt(self.longtext))


class AlertTextColorTestWithTitle(unittest.TestCase):
	"""docstring for AlertTextColorTest"""

	def setUp(self):
		self.atc = AlertTextColor()
		self.text = "Hola"
		self.title = "El Titulo"
		self.longtext = "hola esto es una prueba de un texto largo, mas largo de lo normal"
		self.longtitle = "hola esto es una prueba de un titulo largo, mas largo de lo normal"

	def testAlertErrorWithTitle(self):
		self.assertIsNone(self.atc.error(self.text,self.title))

	def testAlertSuccessWithTitle(self):
		self.assertIsNone(self.atc.success(self.text,self.title))

	def testAlertWarningWithTitle(self):
		self.assertIsNone(self.atc.warning(self.text,self.title))

	def testAlertInfoWithTitle(self):
		self.assertIsNone(self.atc.info(self.text,self.title))

	def testAlertInfoAltWithTitle(self):
		self.assertIsNone(self.atc.info_alt(self.text,self.title))

	def testAlertCustomColorWithTitle(self):
		self.assertIsNone(self.atc.custom(self.text,self.title,color='cyan'))

	def testAlertCustomBackgroundWithTitle(self):
		self.assertIsNone(self.atc.custom(self.text,self.title,background='magenta'))

	def testAlertCustomStyleWithTitle(self):
		self.assertIsNone(self.atc.custom(self.text,self.title,style='bold'))

	def testAlertCustomStyleColorWithTitle(self):
		self.assertIsNone(self.atc.custom(self.text,self.title,style='bold',color='cyan'))

	def testAlertCustomStyleColorBackgroundWithTitle(self):
		self.assertIsNone(self.atc.custom(self.text,self.title,style='bold',color='magenta',background='cyan'))

	def testAlertErrorLongText(self):
		self.assertIsNone(self.atc.error(self.longtext,self.title))

	def testAlertErrorLongTitle(self):
		self.assertIsNone(self.atc.error(self.text,self.longtitle))

	def testAlertSuccessLongText(self):
		self.assertIsNone(self.atc.success(self.longtext,self.title))

	def testAlertSuccessLongTitle(self):
		self.assertIsNone(self.atc.success(self.text,self.longtitle))		

	def testAlertWarningLongText(self):
		self.assertIsNone(self.atc.warning(self.longtext,self.title))

	def testAlertWarningLongTitle(self):
		self.assertIsNone(self.atc.warning(self.text,self.longtitle))	

	def testAlertInfoLongText(self):
		self.assertIsNone(self.atc.info(self.longtext,self.title))

	def testAlertInfoLongTitle(self):
		self.assertIsNone(self.atc.info(self.text,self.longtitle))	

	def testAlertInfoAltLongText(self):
		self.assertIsNone(self.atc.info_alt(self.longtext,self.title))

	def testAlertInfoAltLongTitle(self):
		self.assertIsNone(self.atc.info_alt(self.text,self.longtitle))

	def testAlertCustomColorWithlongText(self):
		self.assertIsNone(self.atc.custom(self.longtext,self.title,color='cyan'))

	def testAlertCustomColorWithLongTitle(self):
		self.assertIsNone(self.atc.custom(self.text,self.longtitle,color='cyan'))

	def testAlertCustomBackgroundWithLongText(self):
		self.assertIsNone(self.atc.custom(self.longtext,self.title,background='magenta'))

	def testAlertCustomBackgroundWithLongTitle(self):
		self.assertIsNone(self.atc.custom(self.text,self.longtitle,background='magenta'))

	def testAlertCustomStyleWithLongText(self):
		self.assertIsNone(self.atc.custom(self.longtext,self.title,style='bold'))

	def testAlertCustomStyleWithLongTitle(self):
		self.assertIsNone(self.atc.custom(self.text,self.longtitle,style='bold'))

	def testAlertCustomStyleColorWithLongText(self):
		self.assertIsNone(self.atc.custom(self.longtext,self.title,style='bold',color='cyan'))

	def testAlertCustomStyleColorWithLongTitle(self):
		self.assertIsNone(self.atc.custom(self.text,self.longtitle,style='bold',color='cyan'))

	def testAlertCustomStyleColorBackgroundWithLongText(self):
		self.assertIsNone(self.atc.custom(self.longtext,self.title,style='bold',color='magenta',background='cyan'))				

	def testAlertCustomStyleColorBackgroundWithLongTitle(self):
		self.assertIsNone(self.atc.custom(self.text,self.longtitle,style='bold',color='magenta',background='cyan'))	


if __name__ == '__main__':
    unittest.main()