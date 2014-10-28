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

    __COLOR_LIST__    = ['default','grey','red','green','yellow','blue','magenta','cyan','white']
    __STYLE_LIST__    = ['default','bold','opaque','italic','underline','crossedout']

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

    def __is_valid_color__(self,color):
        """
            Valida si el nombre del clor es soportaado por la clase
        """
        return str(color).lower() in self.__COLOR_LIST__

    def __is_valid_style__(self,style):
        """
            Valida si el estilo es soportado por lla claase
        """
        return str(style).lower() in self.__STYLE_LIST__

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

    def bold_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_GREY__)

    def bold_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_RED__)

    def bold_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_GREEN__)

    def bold_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_YELLOW__)

    def bold_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_BLUE__)

    def bold_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_MAGENTA__)

    def bold_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_CYAN__)

    def bold_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_WHITE__)

    def opaque_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_GREY__)

    def opaque_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_RED__)

    def opaque_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_GREEN__)

    def opaque_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_YELLOW__)

    def opaque_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_BLUE__)

    def opaque_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_MAGENTA__)

    def opaque_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_CYAN__)

    def opaque_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_WHITE__)

    def italic_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_GREY__)

    def italic_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_RED__)

    def italic_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_GREEN__)

    def italic_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_YELLOW__)

    def italic_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_BLUE__)

    def italic_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_MAGENTA__)

    def italic_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_CYAN__)

    def italic_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_WHITE__)     

    def underline_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_GREY__)

    def underline_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_RED__)

    def underline_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_GREEN__)

    def underline_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_YELLOW__)

    def underline_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_BLUE__)

    def underline_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_MAGENTA__)

    def underline_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_CYAN__)

    def underline_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_WHITE__)
    def crossedout_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_GREY__)

    def crossedout_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_RED__)

    def crossedout_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_GREEN__)

    def crossedout_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_YELLOW__)

    def crossedout_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_BLUE__)

    def crossedout_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_MAGENTA__)

    def crossedout_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_CYAN__)

    def crossedout_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_WHITE__)

    def default_default_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_GREY__)

    def default_default_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_RED__)

    def default_default_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_GREEN__)

    def default_default_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def default_default_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_BLUE__)

    def default_default_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def default_default_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_CYAN__)

    def default_default_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_WHITE__)

    def bold_default_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_GREY__)

    def bold_default_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_RED__)

    def bold_default_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_GREEN__)

    def bold_default_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def bold_default_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_BLUE__)

    def bold_default_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def bold_default_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_CYAN__)

    def bold_default_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_WHITE__)

    def opaque_default_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_GREY__)

    def opaque_default_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_RED__)

    def opaque_default_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_GREEN__)

    def opaque_default_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def opaque_default_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_BLUE__)

    def opaque_default_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def opaque_default_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_CYAN__)

    def opaque_default_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_WHITE__)

    def italic_default_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_GREY__)

    def italic_default_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_RED__)

    def italic_default_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_GREEN__)

    def italic_default_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def italic_default_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_BLUE__)

    def italic_default_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def italic_default_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_CYAN__)

    def italic_default_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_WHITE__)        

    def underline_default_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_GREY__)

    def underline_default_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_RED__)

    def underline_default_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_GREEN__)

    def underline_default_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def underline_default_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_BLUE__)

    def underline_default_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def underline_default_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_CYAN__)

    def underline_default_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_WHITE__)

    def crossedout_default_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_GREY__)

    def crossedout_default_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_RED__)

    def crossedout_default_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_GREEN__)

    def crossedout_default_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def crossedout_default_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_BLUE__)

    def crossedout_default_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def crossedout_default_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_CYAN__)

    def crossedout_default_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_DEFAULT__,background=self.__BACKGROUND_COLOR_WHITE__)

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

    def default_grey_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_WHITE__)

    def default_red_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_GREY__)

    def default_red_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_GREEN__)

    def default_red_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def default_red_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_BLUE__)

    def default_red_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def default_red_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_CYAN__)

    def default_red_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_WHITE__)

    def default_green_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_GREY__)

    def default_green_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_RED__)

    def default_green_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def default_green_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_BLUE__)

    def default_green_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def default_green_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_CYAN__)

    def default_green_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_WHITE__)

    def default_yellow_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_GREY__)

    def default_yellow_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_RED__)

    def default_yellow_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_GREEN__)

    def default_yellow_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_BLUE__)

    def default_yellow_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def default_yellow_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_CYAN__)

    def default_yellow_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_WHITE__)

    def default_blue_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_GREY__)

    def default_blue_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_RED__)

    def default_blue_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_GREEN__)

    def default_blue_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def default_blue_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def default_blue_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_CYAN__)

    def default_blue_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_WHITE__)
        
    def default_magenta_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_GREY__)

    def default_magenta_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_RED__)

    def default_magenta_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_GREEN__)

    def default_magenta_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def default_magenta_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_BLUE__)

    def default_magenta_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_CYAN__)

    def default_magenta_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_WHITE__)

    def default_cyan_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_GREY__)

    def default_cyan_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_RED__)

    def default_cyan_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_GREEN__)

    def default_cyan_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def default_cyan_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_BLUE__)

    def default_cyan_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def default_cyan_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_WHITE__)

    def default_white_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_GREY__)

    def default_white_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_RED__)

    def default_white_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_GREEN__)

    def default_white_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def default_white_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_BLUE__)

    def default_white_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def default_white_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_DEFAULT__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_CYAN__)

    def bold_grey_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_RED__)

    def bold_grey_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_GREEN__)

    def bold_grey_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def bold_grey_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_BLUE__)

    def bold_grey_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def bold_grey_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_CYAN__)

    def bold_grey_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_WHITE__)

    def bold_red_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_GREY__)

    def bold_red_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_GREEN__)

    def bold_red_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def bold_red_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_BLUE__)

    def bold_red_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def bold_red_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_CYAN__)

    def bold_red_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_WHITE__)

    def bold_green_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_GREY__)

    def bold_green_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_RED__)

    def bold_green_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def bold_green_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_BLUE__)

    def bold_green_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def bold_green_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_CYAN__)

    def bold_green_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_WHITE__)

    def bold_yellow_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_GREY__)

    def bold_yellow_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_RED__)

    def bold_yellow_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_GREEN__)

    def bold_yellow_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_BLUE__)

    def bold_yellow_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def bold_yellow_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_CYAN__)

    def bold_yellow_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_WHITE__)

    def bold_blue_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_GREY__)

    def bold_blue_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_RED__)

    def bold_blue_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_GREEN__)

    def bold_blue_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def bold_blue_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def bold_blue_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_CYAN__)

    def bold_blue_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_WHITE__)

    def bold_magenta_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_GREY__)

    def bold_magenta_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_RED__)

    def bold_magenta_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_GREEN__)

    def bold_magenta_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def bold_magenta_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_BLUE__)

    def bold_magenta_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_CYAN__)

    def bold_magenta_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_WHITE__)

    def bold_cyan_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_GREY__)

    def bold_cyan_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_RED__)

    def bold_cyan_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_GREEN__)

    def bold_cyan_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def bold_cyan_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_BLUE__)

    def bold_cyan_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def bold_cyan_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_WHITE__)

    def bold_white_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_GREY__)

    def bold_white_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_RED__)

    def bold_white_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_GREEN__)

    def bold_white_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def bold_white_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_BLUE__)

    def bold_white_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def bold_white_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_BOLD__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_CYAN__)

    def opaque_grey_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_RED__)

    def opaque_grey_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_GREEN__)

    def opaque_grey_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def opaque_grey_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_BLUE__)

    def opaque_grey_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def opaque_grey_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_CYAN__)

    def opaque_grey_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_WHITE__)

    def opaque_red_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_GREY__)

    def opaque_red_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_GREEN__)

    def opaque_red_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def opaque_red_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_BLUE__)

    def opaque_red_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def opaque_red_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_CYAN__)

    def opaque_red_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_WHITE__)

    def opaque_green_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_GREY__)

    def opaque_green_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_RED__)

    def opaque_green_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def opaque_green_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_BLUE__)

    def opaque_green_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def opaque_green_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_CYAN__)

    def opaque_green_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_WHITE__)

    def opaque_yellow_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_GREY__)

    def opaque_yellow_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_RED__)

    def opaque_yellow_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_GREEN__)

    def opaque_yellow_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_BLUE__)

    def opaque_yellow_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def opaque_yellow_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_CYAN__)

    def opaque_yellow_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_WHITE__)

    def opaque_blue_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_GREY__)

    def opaque_blue_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_RED__)

    def opaque_blue_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_GREEN__)

    def opaque_blue_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def opaque_blue_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def opaque_blue_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_CYAN__)

    def opaque_blue_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_WHITE__)
                
    def opaque_magenta_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_GREY__)

    def opaque_magenta_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_RED__)

    def opaque_magenta_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_GREEN__)

    def opaque_magenta_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def opaque_magenta_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_BLUE__)

    def opaque_magenta_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_CYAN__)

    def opaque_magenta_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_WHITE__)

    def opaque_cyan_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_GREY__)

    def opaque_cyan_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_RED__)

    def opaque_cyan_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_GREEN__)

    def opaque_cyan_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def opaque_cyan_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_BLUE__)

    def opaque_cyan_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def opaque_cyan_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_WHITE__)

    def opaque_white_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_GREY__)

    def opaque_white_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_RED__)

    def opaque_white_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_GREEN__)

    def opaque_white_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def opaque_white_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_BLUE__)

    def opaque_white_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def opaque_white_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_OPAQUE__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_CYAN__)

    def italic_grey_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_RED__)

    def italic_grey_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_GREEN__)

    def italic_grey_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def italic_grey_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_BLUE__)

    def italic_grey_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def italic_grey_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_CYAN__)

    def italic_grey_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_WHITE__)

    def italic_red_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_GREY__)

    def italic_red_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_GREEN__)

    def italic_red_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def italic_red_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_BLUE__)

    def italic_red_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def italic_red_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_CYAN__)

    def italic_red_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_WHITE__)

    def italic_green_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_GREY__)

    def italic_green_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_RED__)

    def italic_green_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def italic_green_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_BLUE__)

    def italic_green_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def italic_green_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_CYAN__)

    def italic_green_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_WHITE__)

    def italic_yellow_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_GREY__)

    def italic_yellow_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_RED__)

    def italic_yellow_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_GREEN__)

    def italic_yellow_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_BLUE__)

    def italic_yellow_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def italic_yellow_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_CYAN__)

    def italic_yellow_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_WHITE__)

    def italic_blue_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_GREY__)

    def italic_blue_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_RED__)

    def italic_blue_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_GREEN__)

    def italic_blue_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def italic_blue_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def italic_blue_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_CYAN__)

    def italic_blue_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_WHITE__)

    def italic_magenta_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_GREY__)

    def italic_magenta_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_RED__)

    def italic_magenta_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_GREEN__)

    def italic_magenta_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def italic_magenta_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_BLUE__)

    def italic_magenta_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_CYAN__)

    def italic_magenta_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_WHITE__)

    def italic_cyan_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_GREY__)

    def italic_cyan_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_RED__)

    def italic_cyan_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_GREEN__)

    def italic_cyan_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def italic_cyan_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_BLUE__)

    def italic_cyan_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def italic_cyan_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_WHITE__)

    def italic_white_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_GREY__)

    def italic_white_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_RED__)

    def italic_white_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_GREEN__)

    def italic_white_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def italic_white_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_BLUE__)

    def italic_white_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def italic_white_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_ITALIC__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_CYAN__)

    def underline_grey_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_RED__)

    def underline_grey_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_GREEN__)

    def underline_grey_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def underline_grey_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_BLUE__)

    def underline_grey_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def underline_grey_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_CYAN__)

    def underline_grey_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_WHITE__)

    def underline_red_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_GREY__)

    def underline_red_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_GREEN__)

    def underline_red_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def underline_red_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_BLUE__)

    def underline_red_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def underline_red_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_CYAN__)

    def underline_red_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_WHITE__)

    def underline_green_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_GREY__)

    def underline_green_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_RED__)

    def underline_green_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def underline_green_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_BLUE__)

    def underline_green_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def underline_green_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_CYAN__)

    def underline_green_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_WHITE__)

    def underline_yellow_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_GREY__)

    def underline_yellow_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_RED__)

    def underline_yellow_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_GREEN__)

    def underline_yellow_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_BLUE__)

    def underline_yellow_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def underline_yellow_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_CYAN__)

    def underline_yellow_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_WHITE__)

    def underline_blue_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_GREY__)

    def underline_blue_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_RED__)

    def underline_blue_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_GREEN__)

    def underline_blue_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def underline_blue_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def underline_blue_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_CYAN__)

    def underline_blue_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_WHITE__)

    def underline_magenta_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_GREY__)

    def underline_magenta_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_RED__)

    def underline_magenta_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_GREEN__)

    def underline_magenta_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def underline_magenta_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_BLUE__)

    def underline_magenta_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_CYAN__)

    def underline_magenta_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_WHITE__)

    def underline_cyan_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_GREY__)

    def underline_cyan_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_RED__)

    def underline_cyan_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_GREEN__)

    def underline_cyan_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def underline_cyan_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_BLUE__)

    def underline_cyan_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def underline_cyan_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_WHITE__)

    def underline_white_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_GREY__)

    def underline_white_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_RED__)

    def underline_white_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_GREEN__)

    def underline_white_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def underline_white_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_BLUE__)

    def underline_white_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def underline_white_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_UNDERLINE__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_CYAN__)

    def crossedout_grey_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_RED__)

    def crossedout_grey_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_GREEN__)

    def crossedout_grey_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def crossedout_grey_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_BLUE__)

    def crossedout_grey_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def crossedout_grey_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_CYAN__)

    def crossedout_grey_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_GREY__,background=self.__BACKGROUND_COLOR_WHITE__)

    def crossedout_red_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_GREY__)

    def crossedout_red_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_GREEN__)

    def crossedout_red_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def crossedout_red_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_BLUE__)

    def crossedout_red_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def crossedout_red_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_CYAN__)

    def crossedout_red_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_RED__,background=self.__BACKGROUND_COLOR_WHITE__)

    def crossedout_green_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_GREY__)

    def crossedout_green_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_RED__)

    def crossedout_green_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def crossedout_green_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_BLUE__)

    def crossedout_green_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def crossedout_green_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_CYAN__)

    def crossedout_green_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_GREEN__,background=self.__BACKGROUND_COLOR_WHITE__)

    def crossedout_yellow_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_GREY__)

    def crossedout_yellow_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_RED__)

    def crossedout_yellow_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_GREEN__)

    def crossedout_yellow_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_BLUE__)

    def crossedout_yellow_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def crossedout_yellow_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_CYAN__)

    def crossedout_yellow_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_YELLOW__,background=self.__BACKGROUND_COLOR_WHITE__)

    def crossedout_blue_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_GREY__)

    def crossedout_blue_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_RED__)

    def crossedout_blue_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_GREEN__)

    def crossedout_blue_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def crossedout_blue_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def crossedout_blue_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_CYAN__)

    def crossedout_blue_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_BLUE__,background=self.__BACKGROUND_COLOR_WHITE__)

    def crossedout_magenta_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_GREY__)

    def crossedout_magenta_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_RED__)

    def crossedout_magenta_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_GREEN__)

    def crossedout_magenta_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def crossedout_magenta_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_BLUE__)

    def crossedout_magenta_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_CYAN__)

    def crossedout_magenta_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_MAGENTA__,background=self.__BACKGROUND_COLOR_WHITE__)

    def crossedout_cyan_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_GREY__)

    def crossedout_cyan_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_RED__)

    def crossedout_cyan_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_GREEN__)

    def crossedout_cyan_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def crossedout_cyan_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_BLUE__)

    def crossedout_cyan_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def crossedout_cyan_white(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_CYAN__,background=self.__BACKGROUND_COLOR_WHITE__)

    def crossedout_white_grey(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_GREY__)

    def crossedout_white_red(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_RED__)

    def crossedout_white_green(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_GREEN__)

    def crossedout_white_yellow(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_YELLOW__)

    def crossedout_white_blue(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_BLUE__)

    def crossedout_white_magenta(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_MAGENTA__)

    def crossedout_white_cyan(self,text):
        return self.__compiler__(text,style=self.__TEXT_STYLE_CROSSEDOUT__,color=self.__TEXT_COLOR_WHITE__,background=self.__BACKGROUND_COLOR_CYAN__)   