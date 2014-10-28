# -*- coding: utf-8 -*-
'''
    termina_text_colot
    ~~~~~~~~~~~~~~~~~~~~~
    Permite imprimir el texto en la consola en forma de alerta 
'''
from .text_color import TextColor


class AlertTextColor(TextColor):
    '''
        Permite imprimir un texto en consola en forma de alerta, paraa ello posee 6 metodos:
        :success:
        :error:
        :warning:
        :info:
        :info_alt:
        :custom:
    '''
    __ALERT_BOX_MIN_LEN__  = 40
    __CURRENT_TEXT_LEN__   = None

    __ALERT_BOX_SUCCESS__  = 'default_white_green'
    __ALERT_BOX_ERROR__    = 'default_white_red'
    __ALERT_BOX_WARNING__  = 'default_white_yellow'
    __ALERT_BOX_INFO__     = 'default_white_blue'
    __ALERT_BOX_INFO_ALT__ = 'default_white_cyan'
    __ALERT_BOX_CUSTOM__   = 'default'
    __ALERT_BOX_TITLE__    = 'default'

    @property
    def __style_box__(self):
        from inspect import stack
        return getattr(self,'__ALERT_BOX_'+str(stack()[3][3]).upper()+'__')

    @property
    def __func_box__(self):
        return getattr(self,self.__style_box__)

    @property
    def __style_title_box__(self):
        from inspect import stack
        return getattr(self,'__ALERT_BOX_'+str(stack()[3][3]).upper()+'__').replace('default','bold',1)

    @property
    def __func_title_box__(self):
        return getattr(self,self.__style_title_box__)

    def __text_content_len__(self,text,title):
        return len(title) if title and len(title) > len(text) else len(text)+2 if title else len(text)

    def __alert_top_bottom__(self,text,title):
        boxlen = self.__CURRENT_TEXT_LEN__ = self.__text_content_len__(text,title)
        if boxlen < self.__ALERT_BOX_MIN_LEN__:
            boxlen = self.__ALERT_BOX_MIN_LEN__

        return " "*int(boxlen+2)

    def __alert_text_box__(self,text,title):

        if self.__CURRENT_TEXT_LEN__ > len(text) and self.__ALERT_BOX_MIN_LEN__ > self.__CURRENT_TEXT_LEN__:
            textlen = self.__ALERT_BOX_MIN_LEN__ - len(text)

        elif self.__CURRENT_TEXT_LEN__ < self.__ALERT_BOX_MIN_LEN__:
            textlen = self.__ALERT_BOX_MIN_LEN__ - len(text)

        else:
            textlen = self.__CURRENT_TEXT_LEN__ - len(text)

        text = " "*2 + text + " "*(textlen-2) if title else text +" "*textlen

        return " "+text+" "     

    def __alert_title_box__(self,title):

        if self.__CURRENT_TEXT_LEN__ > len(title):
            title = title+ " "*(self.__CURRENT_TEXT_LEN__ - len(title))
        else:
            title = title+ " "*(self.__ALERT_BOX_MIN_LEN__ - len(title))

        return " "+title+" "

    def __alert_box__(self,text,title):
        topbottom = self.__func_box__(self.__alert_top_bottom__(text,title))
        text      = self.__func_box__(self.__alert_text_box__(text,title))
        title     = self.__func_title_box__(self.__alert_title_box__(title)) if title else None
        print("")
        print(topbottom)
        if title: 
            print(title)
        print(text)
        print(topbottom)
        print("")

    def success(self,text,title=None):
        self.__alert_box__(text,title)

    def error(self,text,title=None):
        self.__alert_box__(text,title)

    def warning(self,text,title=None):
        self.__alert_box__(text,title)

    def info(self,text,title=None):
        self.__alert_box__(text,title)

    def info_alt(self,text,title=None):
        self.__alert_box__(text,title)

    def custom(self,text,title=None,color='default',background='default',style='default'):
    
        color = color if self.__is_valid_color__(color) else 'default'
        background = background if self.__is_valid_color__(background) else 'default'
        style = style if self.__is_valid_style__(style) else 'default'

        if color == background == style == 'default':

            self.__ALERT_BOX_CUSTOM__ = 'default'

        elif color == background == 'default':
            
            self.__ALERT_BOX_CUSTOM__ = style

        elif background == 'default':

            self.__ALERT_BOX_CUSTOM__ = style+'_'+color

        else:

            self.__ALERT_BOX_CUSTOM__ = style+'_'+color+'_'+background


        self.__alert_box__(text,title)