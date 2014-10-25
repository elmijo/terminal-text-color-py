from setuptools import setup, find_packages

long_description = """
Python Terminal Text Color es una herramienta que permite ponerle color a un texto
que vallamos a imprimir por la consola.	
""""

version = __import__("terminal_text_color").VERSION



classifiers = [
	'Programming Language :: Python',
	'Programming Language :: Python :: 3',
	'Natural Language :: Spanish',
	'Intended Audience :: Developers',
	'License :: MIT License',
	'Operating System :: OS Independent',
	'Topic :: Software Development :: Libraries :: Python Modules',
]

install_requires = []

setup(
	name='Python Terminal Text Color',
	version=version,
	url='https://github.com/ElMijo/terminal-text-color-py',
	license='MIT',
	author='Jerry Anselmi'
	author_email='jerry.anselmi@gmail.com',
	description='Simple herramienta para darle color al texto en consola',
	long_description=long_description,
	packages=['terminal_text_color'],
	package_dir={'terminal_text_color': 'terminal_text_color'},
	include_package_data=True,
	classifiers = classifiers,

)