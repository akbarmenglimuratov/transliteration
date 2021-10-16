### transliterate
---
Transliterator for Python. Transliterates from Cyrillic to Latin and reversed.
Inlcuded languages Karakalpak and Uzbek.
(in developing..)

### Usage and examples
---
Required imports
```
from transliteration import translit
```

Text
```
text = "Өзбекстан Республикасы Президенти сайлаўына 8 күн қалды"
```
Transliteration to Karakalpak
```
print(translit(text, 'kk'))
# Output: Ózbekstan Respublikası Prezidenti saylawına 8 kún qaldı
```
List of avaiable languages (language_code)
```
['kk', 'uz']
```

Reversed transliteration from Karakalpak (kk)
```
print(translit(text, 'kk', reverse=True))
# Өзбекстан Республикасы Президенти сайлаўына 8 күн қалды
```
### Support
---
The package is under development. Open to any issues
### Author
---
Akbar Menglimuratov [akbarmenglimuratov@gmail.com](mailto:akbarmenglimuratov@gmail.com)