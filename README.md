Python Terminal Text Color
==========================

[![Build Status](https://travis-ci.org/ElMijo/terminal-text-color-py.svg?branch=master)](https://travis-ci.org/ElMijo/terminal-text-color-py) [![Coverage Status](https://coveralls.io/repos/ElMijo/terminal-text-color-py/badge.png?branch=master)](https://coveralls.io/r/ElMijo/terminal-text-color-py?branch=master) [![Documentation Status](https://readthedocs.org/projects/terminal-text-color-py/badge/?version=latest)](https://readthedocs.org/projects/terminal-text-color-py/?badge=latest)

Este es una herramienta muy simple que permite darle color a nuestros textos al momento de trabajar en consola. La paleta de colores utilizados en esta versión son de SGR (Select  Graphic Rendition), los mismos estan basados en colores que pueden ser renderizados en forma normal o en alta intensidad. Para esta versión no damos sopote ha  los colores de altaa intensidad ya que los mismos solo son vistos en aixterm.

## Estilos soportados (style)

 - Default : *Estilo por defecto de tu consola*
 - Bold : *Estilo negrita*
 - Opaque : *Estilo opaco, una pequeña variación del color de la fueente*
 - Italic : *Estilo cursivo, para que surta efecto la consoola debe tener __Italic : on__*
 - Underline : *Estilo subrallado*
 - Crossedout : *Estilo tachado*


## Colores soportados (background and color)

 - Default : *Color por defecto de la consola en la fuente o fondo*
 - Grey : *Gris o negro segun la consola, y aplicable para la fuente o fondo*
 - Red : *Rojo aplicable para la fuente o fondo*
 - Green : *Verde aplicable para la fuente o fondo*
 - Yellow : *Amarillo aplicable para la fuente o fondo*
 - Blue : *Azul aplicable para la fuente o fondo*
 - Magenta : *Magenta aplicable para la fuente o fondo*
 - Cyan : *Cian aplicable para la fuente o fondo*
 - White : *Blanco aplicable para la fuente o fondo*

## Manual de uso rapido

### Incluir el paquete

 ```python
 from terminal_text_color import TextColor
 ```
### Inicializar la clase

 ```python
 tc = TextColor()
 ```
### Invocar los metodos de color deseada

Hay tres formas de invocar los metodos

#### Metodos solo estilo

```python
tc.{{style}}(text)
```

Ejemplos:
Estos metodos colocan el color de la fuente y fondo por defecto (*default*)

```python
print tc.default("Mi texto con estilo")
print tc.bold("Mi texto con estilo")
print tc.opaque("Mi texto con estilo")
print tc.italic("Mi texto con estilo")
print tc.underline("Mi texto con estilo")
print tc.crossedout("Mi texto con estilo")
```

#### Metodos estilos y colores de fuente

```python
tc.{{style}}_{{color}}(text)
```

Ejemplos:
Estos metodos colocan el fondo por defecto (*default*), aqui puedes hacer diferentes convinaciones
entre estilos y colores segun se deseen

```python
print tc.default_red("Mi texto con estilo y color")
print tc.default_yellow("Mi texto con estilo y color")

print tc.bold_cyan("Mi texto con estilo y color")
print tc.bold_yellow("Mi texto con estilo y color")

print tc.opaque_blue("Mi texto con estilo y color")
print tc.opaque_yellow("Mi texto con estilo y color")

print tc.italic_white("Mi texto con estilo y color")
print tc.italic_magenta("Mi texto con estilo y color")

print tc.underline_white("Mi texto con estilo y color")
print tc.underline_grey("Mi texto con estilo y color")

print tc.crossedout_green("Mi texto con estilo y color")
print tc.crossedout_red("Mi texto con estilo y color")
```

#### Metodos estilos y colores de fuente y fondos 

```python
tc.{{style}}_{{color}}_{{background}}(text)
```

Ejemplos:
Con estos metodos podemos hacer las combinaiones que queramos entre estilo (*style*), colores (*color*) y fondos (*background*),
 segun las necesidaades del caso


```python
print tc.default_red_white("Mi texto con estilo, color y fondo")
print tc.default_yellow_blue("Mi texto con estilo, color y fondo")

print tc.bold_default_cyan("Mi texto con estilo, color y fondo")
print tc.bold_defaul_yellow("Mi texto con estilo, color y fondo")

print tc.opaque_blue_grey("Mi texto con estilo, color y fondo")
print tc.opaque_yellow_magenta("Mi texto con estilo, color y fondo")

print tc.italic_white_blue("Mi texto con estilo, color y fondo")
print tc.italic_default_magenta("Mi texto con estilo, color y fondo")

print tc.underline_white_blue("Mi texto con estilo, color y fondo")
print tc.underline_grey_yellow("Mi texto con estilo, color y fondo")

print tc.crossedout_green_white("Mi texto con estilo, color y fondo")
print tc.crossedout_red_blue("Mi texto con estilo, color y fondo")
```

#### Ejemplo Completo

```python
from terminal_text_color import TextColor

tc = TextColor()

print tc.default("Mi texto con estilo")
print tc.bold("Mi texto con estilo")
print tc.opaque("Mi texto con estilo")
print tc.italic("Mi texto con estilo")
print tc.underline("Mi texto con estilo")
print tc.crossedout("Mi texto con estilo")
print tc.default_red("Mi texto con estilo y color")
print tc.default_yellow("Mi texto con estilo y color")
print tc.bold_cyan("Mi texto con estilo y color")
print tc.bold_yellow("Mi texto con estilo y color")
print tc.opaque_blue("Mi texto con estilo y color")
print tc.opaque_yellow("Mi texto con estilo y color")
print tc.italic_white("Mi texto con estilo y color")
print tc.italic_magenta("Mi texto con estilo y color")
print tc.underline_white("Mi texto con estilo y color")
print tc.underline_grey("Mi texto con estilo y color")
print tc.crossedout_green("Mi texto con estilo y color")
print tc.crossedout_red("Mi texto con estilo y color")
print tc.default_red_white("Mi texto con estilo, color y fondo")
print tc.default_yellow_blue("Mi texto con estilo, color y fondo")
print tc.bold_default_cyan("Mi texto con estilo, color y fondo")
print tc.bold_defaul_yellow("Mi texto con estilo, color y fondo")
print tc.opaque_blue_grey("Mi texto con estilo, color y fondo")
print tc.opaque_yellow_magenta("Mi texto con estilo, color y fondo")
print tc.italic_white_blue("Mi texto con estilo, color y fondo")
print tc.italic_default_magenta("Mi texto con estilo, color y fondo")
print tc.underline_white_blue("Mi texto con estilo, color y fondo")
print tc.underline_grey_yellow("Mi texto con estilo, color y fondo")
print tc.crossedout_green_white("Mi texto con estilo, color y fondo")
print tc.crossedout_red_blue("Mi texto con estilo, color y fondo")
```
![Terminal Text Color 1](https://farm4.staticflickr.com/3946/15073526364_6a196c446b_z.jpg)

Alert Text Color
================

Una clase muy util que permite imprimir un texto en consola como una alerta, esta basada en la clase TextColor

## Manual de uso rapido

### Incluir el paquete

 ```python
from terminal_text_color import AlertTextColor
 ```
### Inicializar la clase

 ```python
atc = AlertTextColor()
 ```
### Invocar los metodos base

```python
atc.{{metodo}}(text,title=None)
```

Esta clase nos provee de medodos de uso rapido:

 - success
 - error
 - warning
 - info
 - info_alt

```python
atc.success("Mensaje de alerta para el usuario")
atc.success("Probando mensaje","Titulo de la Alerta")

atc.error("Mensaje de alerta para el usuario")
atc.error("Probando mensaje",title="Titulo de la Alerta")

atc.warning("Mensaje de alerta para el usuario")
atc.warning("Probando mensaje",title="Titulo de la Alerta")

atc.info("Mensaje de alerta para el usuario")
atc.info("Probando mensaje",title="Titulo de la Alerta")

atc.info_alt("Mensaje de alerta para el usuario")
atc.info_alt("Probando mensaje",title="Titulo de la Alerta")
```

#### Invocar el metodo custom

```python
atc.custom(text,title=None,color='default',background='default',style='default')
```

Este metodo nos permite personalizar nuestra alerta

```python
atc.custom("Mensaje de alerta para el usuario")
atc.custom("Probando mensaje","Titulo de la Alerta")
atc.custom("Probando mensaje",title="Titulo de la Alerta",color="red")
atc.custom("Probando mensaje",title="Titulo de la Alerta",background="white")
atc.custom("Probando mensaje",title="Titulo de la Alerta",style="bold")
atc.custom("Probando mensaje",title="Titulo de la Alerta",background="white",color="red")
atc.custom("Probando mensaje",title="Titulo de la Alerta",color="red",style="bold",background="white")
atc.custom("Probando mensaje",title="Titulo de la Alerta","red","white","bold")
```

#### Ejemplo Completo

```python
from terminal_text_color import AlertTextColor

atc = AlertTextColor()

atc.success("Mensaje de alerta para el usuario")
atc.success("Probando mensaje","Titulo de la Alerta")

atc.error("Mensaje de alerta para el usuario")
atc.error("Probando mensaje",title="Titulo de la Alerta")

atc.warning("Mensaje de alerta para el usuario")
atc.warning("Probando mensaje",title="Titulo de la Alerta")

atc.info("Mensaje de alerta para el usuario")
atc.info("Probando mensaje",title="Titulo de la Alerta")

atc.info_alt("Mensaje de alerta para el usuario")
atc.info_alt("Probando mensaje",title="Titulo de la Alerta")

atc.custom("Mensaje de alerta para el usuario")
atc.custom("Probando mensaje","Titulo de la Alerta")
atc.custom("Probando mensaje",title="Titulo de la Alerta",color="red")
atc.custom("Probando mensaje",title="Titulo de la Alerta",background="white")
atc.custom("Probando mensaje",title="Titulo de la Alerta",style="bold")
atc.custom("Probando mensaje",title="Titulo de la Alerta",background="white",color="red")
atc.custom("Probando mensaje",title="Titulo de la Alerta",color="red",style="bold",background="white")
```

![Terminal Text Color 2](https://farm8.staticflickr.com/7492/15508081138_09aaafe32a_z.jpg)