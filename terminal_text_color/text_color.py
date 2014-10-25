# -*- coding: utf-8 -*-
"""
	termina_text_colot
	~~~~~~~~~~~~~~~~~~~~~
	Permite agregar color a un texto que se desea imprimir en la consola 
"""
class TextColor():
	"""
		TextColor es una clase que contiene todo lo relativo a los colores
		que pueden verse por consola
	"""

	__COLOR_LIST__    = ['GREY','RED','GREEN','YELLOW','BLUE','MAGENTA','CYAN','WHITE']

	__COLOR_ENDC__    = '\x1b[0m'
	__COLOR_INIT__    = '\x1b[%s;%s;%sm'

	__TEXT_STYLE_DEFAULT__    = 0
	__TEXT_STYLE_BOLD__       = 1
	__TEXT_STYLE_OPAQUE__     = 2
	__TEXT_STYLE_ITALIC__     = 3
	__TEXT_STYLE_UNDERLINE__  = 4
	__TEXT_STYLE_CROSSEDOUT__ = 9

	__TEXT_COLOR_DEFAULT__ = 39
	__TEXT_COLOR_GREY__    = 30
	__TEXT_COLOR_RED__     = 31
	__TEXT_COLOR_GREEN__   = 32
	__TEXT_COLOR_YELLOW__  = 33
	__TEXT_COLOR_BLUE__    = 34
	__TEXT_COLOR_MAGENTA__ = 35
	__TEXT_COLOR_CYAN__    = 36
	__TEXT_COLOR_WHITE__   = 37

	__BACKGROUND_COLOR_DEFAULT__ = 49
	__BACKGROUND_COLOR_GREY__    = 40
	__BACKGROUND_COLOR_RED__     = 41
	__BACKGROUND_COLOR_GREEN__   = 42
	__BACKGROUND_COLOR_YELLOW__  = 43
	__BACKGROUND_COLOR_BLUE__    = 44
	__BACKGROUND_COLOR_MAGENTA__ = 45
	__BACKGROUND_COLOR_CYAN__    = 46
	__BACKGROUND_COLOR_WHITE__   = 47

	def __compiler__(self,text,color=39,background=49,style=0):
		"""
			Compila el texto agregandole el color, fondo y estilo deseado
		"""
		return self.__COLOR_INIT__ % (style,color,background)+text+self.__COLOR_ENDC__

	def default(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__)

	def bold(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__)

	def opaque(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__)

	def italic(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__)

	def underline(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__)

	def crossedout(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__)



	def default_grey(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREY__)

	def default_red(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_RED__)

	def default_green(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREEN__)

	def default_yellow(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_YELLOW__)

	def default_blue(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_BLUE__)

	def default_magenta(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_MAGENTA__)

	def default_cyan(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_CYAN__)

	def default_white(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_WHITE__)


	def default_grey_grey(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_GREY__)

	def default_grey_red(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_RED__)

	def default_grey_green(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_GREEN__)

	def default_grey_yellow(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_YELLOW__)

	def default_grey_blue(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_BLUE__)

	def default_grey_magenta(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_MAGENTA__)

	def default_grey_cyan(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_CYAN__)										

	def default_grey_while(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_WHITE__)


	def default_red(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_RED__)

	def default_green(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREEN__)

	def default_yellow(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_YELLOW__)

	def default_blue(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_BLUE__)

	def default_magenta(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_MAGENTA__)

	def default_cyan(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_CYAN__)

	def default_white(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_WHITE__)




														

	def bold(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__)

	def opaque(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__)

	def italic(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__)

	def underline(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__)

	def crossedout(self,text):
		return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__)



	# def gris(self,text):
	# 	return self.grey(text)

	# def grey(self,text):
	# 	return self.__compiler__(text,self.__COLOR_GREY__)

	# def rojo(self,text):
	# 	return self.red(text)

	# def red(self,text):
	# 	return self.__compiler__(text,self.__COLOR_RED__)

	# def verde(self,text):
	# 	return self.green(text)

	# def green(self,text):
	# 	return self.__compiler__(text,self.__COLOR_GREEN__)

	# def amarillo(self,text):
	# 	return self.yellow(text)

	# def yellow(self,text):
	# 	return self.__compiler__(text,self.__COLOR_YELLOW__)

	# def azul(self,text):
	# 	return self.blue(text)

	# def blue(self,text):
	# 	return self.__compiler__(text,self.__COLOR_BLUE__)

	# def magenta(self,text):
	# 	return self.__compiler__(text,self.__COLOR_MAGENTA__)

	# def cian(self,text):
	# 	return self.cyan(text)

	# def cyan(self,text):
	# 	return self.__compiler__(text,self.__COLOR_CYAN__)

	# def blanco(self,text):
	# 	return self.white(text)

	# def white(self,text):
	# 	return self.__compiler__(text,self.__COLOR_WHITE__)

	# def negrita(self,text):
	# 	return self.bold(text)

	# def bold(self,text):
	# 	return self.__compiler__(text,self.__COLOR_BOLD__)

	# def default(self,text):
	# 	return self.__compiler__(text,self.__COLOR_DEFAULT__)