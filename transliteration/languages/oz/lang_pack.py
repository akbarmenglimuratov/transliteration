from transliteration.transliterator import Transliterator, register

class UzbekLanguagePack(Transliterator):
    language_code = 'uz'
    language_name = 'Uzbek'

    mapping = (
        "абвгдежзийкқлмнопрстуфхэҳАБВДЕЖЗИЙКЛМНОПРСТУФХЭҲ",
        "abvgdejziykqlmnoprstufxehABVDEJZIYKLMNOPRSTUFXEH",
    )

    special_letters = {
        'ч': ('ch', ),
		'ш': ('sh', ),
		'я': ('ya', ),
		'ю': ('yu', ),
		'щ': ('sh', ),
		'ё': ('yo', ),
        'ц': ('ts', ),
        'ў': ("o'", 'o`', 'o‘'),
        'ғ': ("g'", 'g`', 'g‘'),
        'ъ': ('’', "'",),
        # 'ь': ('’', "'",),

		'Ч': ('Ch', ),
		'Ш': ('Sh', ),
		'Я': ('Ya', ),
		'Ю': ('Yu', ),
		'Щ': ('Sh', ),
		'Ё': ('Yo', ),
        'Ц': ('Ts', ),
        'Ў': ("O'", 'O`', 'O‘'),
        'Ғ': ("G'", 'G`', 'G‘'),
        'Ъ': ('’', "'",),
        # 'Ь': ('’', "'",),
    }

register.register(UzbekLanguagePack)
