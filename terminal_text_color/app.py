# -*- coding: utf-8 -*-
from text_color import TextColor

# from terminal_text_color.text_color import TextColor

tc = TextColor()

print tc.default('probando...')
print tc.bold('probando...')
print tc.opaque('probando...')
print tc.italic('probando...')
print tc.underline('probando...')
print tc.crossedout('probando...')

print tc.default_grey('probando...')
print tc.default_red('probando...')
print tc.default_green('probando...')
print tc.default_yellow('probando...')
print tc.default_blue('probando...')
print tc.default_magenta('probando...')
print tc.default_cyan('probando...')
print tc.default_white('probando...')

print tc.default_grey_grey('probando...')
print tc.default_grey_red('probando...')
print tc.default_grey_green('probando...')
print tc.default_grey_yellow('probando...')
print tc.default_grey_blue('probando...')
print tc.default_grey_magenta('probando...')
print tc.default_grey_cyan('probando...')
print tc.default_grey_while('probando...')

print tc.default_red_grey('probando...')
print tc.default_red_red('probando...')
print tc.default_red_green('probando...')
print tc.default_red_yellow('probando...')
print tc.default_red_blue('probando...')
print tc.default_red_magenta('probando...')
print tc.default_red_cyan('probando...')
print tc.default_red_while('probando...')

print tc.default_green_grey('probando...')
print tc.default_green_red('probando...')
print tc.default_green_green('probando...')
print tc.default_green_yellow('probando...')
print tc.default_green_blue('probando...')
print tc.default_green_magenta('probando...')
print tc.default_green_cyan('probando...')
print tc.default_green_while('probando...')

# import sys

# def print_format_table():
#     """
#     prints table of formatted text format options
#     """
#     for style in xrange(8):
#         for fg in xrange(30,38):
#             s1 = ''
#             for bg in xrange(40,48):
#                 format = ';'.join([str(style), str(fg), str(bg)])
#                 s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
#                 print [s1]
#                 sys.exit(0)
#             print s1
#         print '\n'

# # print_format_table()

# print '\x1b[0;33;40m estoy bien \x1b[0m'
# print '\x1b[1;33;40m estoy bien \x1b[0m'
# print '\x1b[2;33;40m estoy bien \x1b[0m'
# print '\x1b[4;33;40m estoy bien \x1b[0m'
# print '\x1b[9;33;40m estoy bien \x1b[0m'
# print '\x1b[39;49mprobando\x1b[0m\x1b[35;49mprobando \x1b[0m'

# estilos en la fuente..
# 0 normal
# 1 bold
# 2 opaca
# 3 italic
# 4 subrallado
# 9 tachado

# background
# 40 grey
# 41 red
# 42 green
# 43 yelow
# 44 blue
# 45 magenta
# 46 cyan
# 47 white

# color
# 30 grey
# 31 red
# 32 green
# 33 yelow
# 34 blue
# 35 magenta
# 36 cyan
# 37 white

# formato

# \x1b[(estilo;color;background)m texto \x1b[0m