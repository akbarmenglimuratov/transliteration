from transliteration.transliterator import Transliterator, register

class KarakalpakLanguagePack(Transliterator):
    language_code = 'kk'
    language_name = 'Karakalpak'

    mapping = (
        'абдефгҳхижкқлмнопрстувўйзцъАБДЕФГҲХИЖКҚЛМНОПРСТУВЎЙЗЦЪ',
        'abdefghxijkqlmnoprstuvwyzcyABDEFGHXIJKQLMNOPRSTUVWYZCY'
    )

    special_letters = {
        'ч': ('ch', ),
		'ш': ('sh', ),
		'я': ('ya', ),
		'ю': ('yu', ),
		'щ': ('sh', ),
		'ё': ('yo', ),
		'ь': '',

		'Ч': ('Ch', ),
		'Ш': ('Sh', ),
		'Я': ('Ya', ),
		'Ю': ('Yu', ),
		'Щ': ('Sh', ),
		'Ё': ('Yo', ),
		'Ь': '',
		
		'ә': ('á', "a'", 'a`', 'a‘'),
		'ғ': ('ǵ', "g'", 'g`', 'g‘'),
		'ы': ('ı', "i'", 'i`', 'i‘'),
		'ң': ('ń', "n'", 'n`', 'n‘'),
		'ө': ('ó', "o'", 'o`', 'o‘'),
		'ү': ('ú', "u'", 'u`', 'u‘'),
		'Ә': ('Á', "A'", 'A`', 'A‘'),
		'Ғ': ('Ǵ', "G'", 'G`', 'G‘'),
		'Ы': ('Í', "I'", 'I`', 'I‘'),
		'Ң': ('Ń', "N'", 'N`', 'N‘'),
		'Ө': ('Ó', "O'", 'O`', 'O‘'),
		'Ү': ('Ú', "u'", 'U`', 'U‘'),
    }

register.register(KarakalpakLanguagePack)
