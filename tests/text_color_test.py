# -*- coding: utf-8 -*-
import unittest

try:
	from terminal_text_color import *
except ImportError:
	import os,sys
	sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
	from terminal_text_color import TextColor

class TexColorTestStyle(unittest.TestCase):
    def testStyleDefault(self):
    	tc = TextColor()
    	texto = "Hola"
    	textoesperado = '\x1b[0;39;49m'+texto+'\x1b[0m'
        self.assertEqual(tc.default(texto), textoesperado)

    def testStyleBold(self):
    	tc = TextColor()
    	texto = "Hola"
    	textoesperado = '\x1b[1;39;49m'+texto+'\x1b[0m'
        self.assertEqual(tc.bold(texto), textoesperado)

    def testStyleOpaque(self):
    	tc = TextColor()
    	texto = "Hola"
    	textoesperado = '\x1b[2;39;49m'+texto+'\x1b[0m'
        self.assertEqual(tc.opaque(texto), textoesperado)

    def testStyleItalic(self):
    	tc = TextColor()
    	texto = "Hola"
    	textoesperado = '\x1b[3;39;49m'+texto+'\x1b[0m'
        self.assertEqual(tc.italic(texto), textoesperado)

    def testStyleUnderline(self):
    	tc = TextColor()
    	texto = "Hola"
    	textoesperado = '\x1b[4;39;49m'+texto+'\x1b[0m'
        self.assertEqual(tc.underline(texto), textoesperado)

    def testStyleCrossedout(self):
    	tc = TextColor()
    	texto = "Hola"
    	textoesperado = '\x1b[9;39;49m'+texto+'\x1b[0m'
        self.assertEqual(tc.crossedout(texto), textoesperado)                                


class TextColorTestColor(unittest.TestCase):
	"""docstring for TextColorTestColor"""

	def testColorGrey (self):
		tc = TextColor()
		texto = "Hola"
		textoesperado = "\x1b[0;30;49m"+texto+"\x1b[0m"
		self.assertEqual(tc.default_grey(texto), textoesperado)

	def testColorRed (self):
		tc = TextColor()
		texto = "Hola"
		textoesperado = "\x1b[0;31;49m"+texto+"\x1b[0m"
		self.assertEqual(tc.default_red(texto), textoesperado)

	def testColorGreen (self):
		tc = TextColor()
		texto = "Hola"
		textoesperado = "\x1b[0;32;49m"+texto+"\x1b[0m"
		self.assertEqual(tc.default_green(texto), textoesperado)

	def testColorYellow (self):
		tc = TextColor()
		texto = "Hola"
		textoesperado = "\x1b[0;33;49m"+texto+"\x1b[0m"
		self.assertEqual(tc.default_yellow(texto), textoesperado)

	def testColorBlue (self):
		tc = TextColor()
		texto = "Hola"
		textoesperado = "\x1b[0;34;49m"+texto+"\x1b[0m"
		self.assertEqual(tc.default_blue(texto), textoesperado)

	def testColorMagenta (self):
		tc = TextColor()
		texto = "Hola"
		textoesperado = "\x1b[0;35;49m"+texto+"\x1b[0m"
		self.assertEqual(tc.default_magenta(texto), textoesperado)

	def testColorCyan (self):
		tc = TextColor()
		texto = "Hola"
		textoesperado = "\x1b[0;36;49m"+texto+"\x1b[0m"
		self.assertEqual(tc.default_cyan(texto), textoesperado)

	def testColorWhite (self):
		tc = TextColor()
		texto = "Hola"
		textoesperado = "\x1b[0;37;49m"+texto+"\x1b[0m"
		self.assertEqual(tc.default_white(texto), textoesperado)


class TextColorTestBackground(unittest.TestCase):
	"""docstring for TextColorTestColor"""

	def testBackgroundGrey (self):
		tc = TextColor()
		texto = "Hola"
		textoesperado = "\x1b[0;39;40m"+texto+"\x1b[0m"
		self.assertEqual(tc.default_default_grey(texto), textoesperado)

	def testBackgroundRed (self):
		tc = TextColor()
		texto = "Hola"
		textoesperado = "\x1b[0;39;41m"+texto+"\x1b[0m"
		self.assertEqual(tc.default_default_red(texto), textoesperado)

	def testBackgroundGreen (self):
		tc = TextColor()
		texto = "Hola"
		textoesperado = "\x1b[0;39;42m"+texto+"\x1b[0m"
		self.assertEqual(tc.default_default_green(texto), textoesperado)

	def testBackgroundYellow (self):
		tc = TextColor()
		texto = "Hola"
		textoesperado = "\x1b[0;39;43m"+texto+"\x1b[0m"
		self.assertEqual(tc.default_default_yellow(texto), textoesperado)

	def testBackgroundBlue (self):
		tc = TextColor()
		texto = "Hola"
		textoesperado = "\x1b[0;39;44m"+texto+"\x1b[0m"
		self.assertEqual(tc.default_default_blue(texto), textoesperado)

	def testBackgroundMagenta (self):
		tc = TextColor()
		texto = "Hola"
		textoesperado = "\x1b[0;39;45m"+texto+"\x1b[0m"
		self.assertEqual(tc.default_default_magenta(texto), textoesperado)

	def testBackgroundCyan (self):
		tc = TextColor()
		texto = "Hola"
		textoesperado = "\x1b[0;39;46m"+texto+"\x1b[0m"
		self.assertEqual(tc.default_default_cyan(texto), textoesperado)

	def testBackgroundWhite (self):
		tc = TextColor()
		texto = "Hola"
		textoesperado = "\x1b[0;39;47m"+texto+"\x1b[0m"
		self.assertEqual(tc.default_default_white(texto), textoesperado)		

if __name__ == '__main__':
    unittest.main()