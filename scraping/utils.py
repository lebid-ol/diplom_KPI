cyrillic_letters = {
        u'а': u'a',
        u'б': u'b',
        u'в': u'v',
        u'г': u'h',
        u'ґ': u'g',
        u'д': u'd',
        u'е': u'e',
        u'ё': u'e',
        u'є': u'ye',
        u'ж': u'zh',
        u'з': u'z',
        u'и': u'y',
        u'і': u'i',
        u'ї': u'i',
        u'й': u'y',
        u'к': u'k',
        u'л': u'l',
        u'м': u'm',
        u'н': u'n',
        u'о': u'o',
        u'п': u'p',
        u'р': u'r',
        u'с': u's',
        u'т': u't',
        u'у': u'u',
        u'ф': u'f',
        u'х': u'kh',
        u'ц': u'ts',
        u'ч': u'ch',
        u'ш': u'sh',
        u'щ': u'shch',
        u'ю': u'iu',
        u'я': u'ia',
        u'ы': u'y',
        u'ъ': u'',
        u'ь': u'',
        u'э': u'e',
    }


def from_cyrillic_to_eng(text: str):
    text = text.replace(' ', '_').lower()
    tmp = ''
    for ch in text:
        tmp += cyrillic_letters.get(ch, ch)
    return tmp