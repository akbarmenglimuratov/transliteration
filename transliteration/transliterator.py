

class Transliterator:
	''' Base language pack

	The attributes below should be defined
	``language_code``: Language code. Example: 'uz', 'kk'
	``language_name``: Language name. Example: 'Uzbek', 'Karakalpak'
	``mapping``: Mapping. A tuple, consisting of two strings
		(source and target). Example value: (u'абс', u'abs').
	----------------------------------------------
	``special_letters``: A dictionary mapping for letters that can't be 
		represented by a single latin letter
	'''
	language_code = None
	language_name = None
	mapping = ()
	special_letters = None

	def __init__(self):
		assert self.language_code is not None
		assert self.language_name is not None
		assert self.mapping is not None
		super().__init__()

		# Creating translation table from mapping set
		self.letters_table = dict(
			zip(*self.mapping)
		)

		self.special_letters_table = {}
		if self.special_letters:
			self.special_letters_table.update(self.special_letters)
		
		self.special_letters_table.update(self.letters_table)
		self.all_in_one = self.special_letters_table

	def translit(self, text, reverse=False):
		if reverse:
			for key, value in self.all_in_one.items():
				for v in value:
					text = text.replace(v, key)
			return text

		for key, value in self.all_in_one.items():
			text = text.replace(key, value[0] if isinstance(value, tuple) else value)

		return text


class LanguagePackRegisterer:
	_registered = {}
	
	def __init__(self):
		pass
	
	@property
	def registered(self):
		return self._registered

	def register(self, class_pack):

		if class_pack.language_code in self._registered:
			return False
		else:
			self._registered[class_pack.language_code] = class_pack
			return True
	
	def get(self, language_code, default=None):
		return self._registered.get(language_code, default)

register = LanguagePackRegisterer()
