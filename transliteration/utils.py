import os
from .transliterator import register

try:
	from importlib import import_module
except ImportError:
	import_module = __import__

def project_dir(base):
	return os.path.abspath(
		os.path.join(
			os.path.dirname(__file__),
			os.path.join(*base) if isinstance(base, (tuple, list)) else base
		).replace('\\', '/')
	)

def import_modules():
	language_dir = ('languages',)
	language_pack_module_name = 'lang_pack'
	
	for app_path in os.listdir(project_dir(language_dir)):
		full_app_path = list(language_dir)
		full_app_path.append(app_path)
		if os.path.isdir(project_dir(full_app_path)):
			try:
				import_module(
					'transliteration.{}.{}.{}'.format(
						'.'.join(language_dir),
						app_path,
						language_pack_module_name
					)
				)
			except ImportError:
				pass

def translit(value, language_code=None, reverse=False):
	
	import_modules()

	if language_code is None:
		raise LanguageCodeError(
			'Missing ``language_code`` argument'
		)
	
	cls = register.get(language_code)

	if cls is None:
		raise LanguagePackError(
			'Language pack not found with given ``language_code``.'
		)
	pack = cls()
	return pack.translit(value, reverse)
