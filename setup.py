try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


long_description = """
Python Terminal Text Color es una herramienta que permite ponerle color a un texto
que vallamos a imprimir por la consola.	
"""

version = __import__("terminal_text_color").__version__

classifiers = [
	'Environment :: Console',
	'Intended Audience :: Developers',
	'License :: OSI Approved :: MIT License',
	'Natural Language :: Spanish',
	'Operating System :: Unix',	
	'Programming Language :: Python :: 2.7',
	'Programming Language :: Python :: 3.2',
	'Programming Language :: Python :: 3.3',
	'Programming Language :: Python :: 3.4',
	'Intended Audience :: Developers',
	'Topic :: Software Development :: Libraries :: Python Modules',
	'Topic :: Software Development :: User Interfaces',
	'Topic :: Terminals :: Terminal Emulators/X Terminals',
	'Topic :: Utilities'
]
keywords = [
	'teminal',
	'console',
	'color',
	'style',
	'background',
	'alert',
	'elmijo'
]
install_requires = []

setup(
	name='Terminal-Text-Color',
	version=version,
	url='https://github.com/ElMijo/terminal-text-color-py',
	license='MIT',
	author='Jerry Anselmi',
	author_email='jerry.anselmi@gmail.com',
	description='Simple herramienta para darle color al texto en consola',
	long_description=long_description,
	packages=['terminal_text_color'],
	package_dir={'terminal_text_color': 'terminal_text_color'},
	include_package_data=True,
	classifiers = classifiers,
	keywords = keywords,
	platforms='any',
)