# -*- coding: utf-8 -*-
"""
	termina_text_colot
	~~~~~~~~~~~~~~~~~~~~~
	Permite imprimir el texto en la consola en forma de alerta 
"""
from text_color import TextColor


class AlertTextColor(TextColor):

	__ALERT_BOX_MIN_LEN__ = 40
	__CURRENT_TEXT_LEN__  = None

	__ALERT_BOX_SUCCESS__  = 'default_white_green'
	__ALERT_BOX_ERROR__    = 'default_white_red'
	__ALERT_BOX_WARNING__  = 'default_white_yellow'
	__ALERT_BOX_INFO__     = 'default_white_blue'
	__ALERT_BOX_INFO_ALT__ = 'default_white_cyan'

	@property
	def __estyle_box__(self):
		from inspect import stack
		return getattr(self,'__ALERT_BOX_'+str(stack()[3][3]).upper()+'__')

	@property
	def __func_box__(self):
		return getattr(self,self.__estyle_box__)


	def __alert_top_bottom__(self,text):
		boxlen = self.__CURRENT_TEXT_LEN__ = int(len(text))
		if boxlen < self.__ALERT_BOX_MIN_LEN__:
			boxlen = self.__ALERT_BOX_MIN_LEN__

		return " "*int(boxlen+2)

	def __alert_text_box__(self,text):
		textlen = self.__ALERT_BOX_MIN_LEN__ - self.__CURRENT_TEXT_LEN__

		if text  > 0:
			text = text +" "*textlen

		return " "+text+" "

	def __alert_box__(self,text):
		topbottom = " "+self.__func_box__(self.__alert_top_bottom__(text))
		text      = " "+self.__func_box__(self.__alert_text_box__(text))
		print ""
		print topbottom
		print text
		print topbottom
		print ""

	def success(self,text):
		self.__alert_box__(text)

	def error(self,text):
		self.__alert_box__(text)

	def warning(self,text):
		self.__alert_box__(text)

	def info(self,text):
		self.__alert_box__(text)

	def info_alt(self,text):
		self.__alert_box__(text)

	def custom(self,text,color='default',background='default',style='default'):
		pass