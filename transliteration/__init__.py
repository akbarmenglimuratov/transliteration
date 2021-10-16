''' 
Transliterator for Karakalpak and Uzbek language.
This transliterates from Cyrillic to Latin and vice versa
'''


__version__ = '1.0'


from .utils import translit

__all__ = (
    'translit',
)
