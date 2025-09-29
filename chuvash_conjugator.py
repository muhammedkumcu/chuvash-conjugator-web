# -*- coding: utf-8 -*-
VOWELS = {'а', 'ӑ', 'ы', 'у', 'э', 'ӗ', 'и', 'ӳ'}  # Ünlüler
CONSONANTS = {'й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ф', 'в', 'п', 'р', 'л', 'д', 'ж', 'ч', 'с', 'м', 'т', 'б', 'ю', 'я'}  # Ünsüzler

BACK_VOWELS = {'а', 'ӑ', 'ы', 'у'}  # Kalın ünlüler
FRONT_VOWELS = {'э', 'ӗ', 'и', 'ӳ'}  # İnce ünlüler

def get_vowel_harmony(word):
    """Kelimenin ünlü uyumunu belirler."""
    for char in reversed(word):
        if char in BACK_VOWELS:
            return 'back'
        elif char in FRONT_VOWELS:
            return 'front'
    return 'back'

def get_last_letter_type(word):
    """Son harfin ünlü/ünsüz olduğunu belirler."""
    if not word:
        return 'consonant'
    return 'vowel' if word[-1] in VOWELS else 'consonant'

def has_single_consonant_before_ăĕ(word):
    """ӑ/ӗ'den önce tek ünsüz var mı kontrol eder (iki heceli kelime için)."""
    if len(word) >= 2 and word[-1] in {'ӑ', 'ӗ'}:
        if word[-2] in CONSONANTS:
            vowel_count = sum(1 for char in word if char in VOWELS)
            return vowel_count >= 2
    return False

def get_syllable_count(word):
    """Kelimedeki hece sayısını hesaplar"""
    return sum(1 for char in word if char in VOWELS)

# 1. TEKİL ŞAHIS İYELİK EKİ
def add_first_singular_possessive(word):
    if not word:
        return word
    
    harmony = get_vowel_harmony(word)
    last_char = word[-1]
    
    # Kural 3: у/ӳ ile biten
    if last_char in {'у', 'ӳ'}:
        if harmony == 'back':
            return word[:-1] + 'ӑвӑм'
        else:
            return word[:-1] + 'ӗвӗм'
    
    # Kural 4: ӑ/ӗ ile biten ve öncesinde tek ünsüz (İKİZLEŞME - ă/ĕ DÜŞMEZ!)
    if has_single_consonant_before_ăĕ(word):
        consonant = word[-2]
        stem = word[:-2] + consonant * 2
        return stem + word[-1] + 'м'
    
    # Kural 1: Ünsüzle biten
    if get_last_letter_type(word) == 'consonant':
        return word + ('ӑм' if harmony == 'back' else 'ӗм')
    
    # Kural 2: Ünlüyle biten (a, e, ă, ĕ, ы, и, ӳ)
    return word + 'м'

# 2. TEKİL ŞAHIS İYELİK EKİ  
def add_second_singular_possessive(word):
    if not word:
        return word
    
    harmony = get_vowel_harmony(word)
    last_char = word[-1]
    suffix = 'у' if harmony == 'back' else 'ӳ'
    
    # Kural 1: a/э ile biten (a ve э sesleri düşer)
    if last_char in {'а', 'э'}:
        return word[:-1] + suffix
    
    # Kural 2: ӑ/ӗ ile biten ve öncesinde tek ünsüz (İKİZLEŞME - ă/ĕ DÜŞER!)
    if has_single_consonant_before_ăĕ(word):
        consonant = word[-2]
        stem = word[:-2] + consonant * 2
        return stem + suffix
    
    return word + suffix

# 3. TEKİL ŞAHIS İYELİK EKİ
def add_third_singular_possessive(word):
    if not word:
        return word
    
    harmony = get_vowel_harmony(word)
    last_char = word[-1]
    
    # Kural 4: т/д ile biten
    if last_char in {'т', 'д'}:
        return word[:-1] + 'чӗ'
    
    # Kural 3: у/ӳ ile biten
    if last_char in {'у', 'ӳ'}:
        if harmony == 'back':
            return word[:-1] + 'ӑвӗ'
        else:
            return word[:-1] + 'ӗвӗ'
    
    # Kural 2: и ile biten
    if last_char == 'и':
        return word + 'йӗ'
    
    # Kural 1: a/э/ă/ĕ ile biten (a/э/ă/ĕ sesleri düşer)
    if last_char in {'а', 'э', 'ӑ', 'ӗ'}:
        # ӑ/ӗ ile biten ve öncesinde tek ünsüz (İKİZLEŞME - ă/ĕ DÜŞER!)
        if last_char in {'ӑ', 'ӗ'} and has_single_consonant_before_ăĕ(word):
            consonant = word[-2]
            stem = word[:-2] + consonant * 2
            return stem + 'ӗ'
        else:
            return word[:-1] + 'ӗ'
    
    # Diğer ünlülerle biten (ы/у/ӳ): direkt +ӗ
    return word + 'ӗ'

# 1. ÇOĞUL ŞAHIS İYELİK EKİ
def add_first_plural_possessive(word):
    """1. çoğul şahıs (bizim)"""
    if not word:
        return word
    
    harmony = get_vowel_harmony(word)
    last_char = word[-1]
    
    # у/ӳ ile biten
    if last_char in {'у', 'ӳ'}:
        if harmony == 'back':
            return word[:-1] + 'ӑвӑмӑр'
        else:
            return word[:-1] + 'ӗвӗмӗр'
    
    # ӑ/ӗ ile biten ve öncesinde tek ünsüz (İKİZLEŞME)
    if has_single_consonant_before_ăĕ(word):
        consonant = word[-2]
        stem = word[:-2] + consonant * 2
        return (stem + word[-1] + 'мӑр') if harmony == 'back' else (stem + word[-1] + 'мӗр')
    
    # Ünsüzle biten
    if get_last_letter_type(word) == 'consonant':
        return word + ('ӑмӑр' if harmony == 'back' else 'ӗмӗр')
    
    # Ünlüyle biten (a, e, ă, ĕ, ы, и, ӳ)
    return word + ('мӑр' if harmony == 'back' else 'мӗр')

# 2. ÇOĞUL ŞAHIS İYELİK EKİ
def add_second_plural_possessive(word):
    """2. çoğul şahıs (sizin)"""
    if not word:
        return word
    
    harmony = get_vowel_harmony(word)
    last_char = word[-1]
    
    # у/ӳ ile biten
    if last_char in {'у', 'ӳ'}:
        if harmony == 'back':
            return word[:-1] + 'ӑвӑр'
        else:
            return word[:-1] + 'ӗвӗр'
    
    # ӑ/ӗ ile biten ve öncesinde tek ünsüz (İKİZLEŞME)
    if has_single_consonant_before_ăĕ(word):
        consonant = word[-2]
        stem = word[:-2] + consonant * 2
        return stem + ('ӑр' if harmony == 'back' else 'ӗр')
    
    # Ünsüzle biten
    if get_last_letter_type(word) == 'consonant':
        return word + ('ӑр' if harmony == 'back' else 'ӗр')
    
    # Ünlüyle biten
    return word + ('р' if harmony == 'back' else 'р')

# 3. ÇOĞUL ŞAHIS İYELİK EKİ
def add_third_plural_possessive(word):
    """3. çoğul şahıs (onların) - 3. tekil ile aynı kurallar"""
    return add_third_singular_possessive(word)

# ÇOKLUK EKİ
def add_plural_suffix(word):
    """Çokluk eki +сем ekler"""
    return word + 'сем'

# ANA ÇEKİMLEME FONKSİYONU
def conjugate_chuvash(word, person, plural=False):
    """
    Ana çekimleme fonksiyonu
    
    Args:
        word: Çekimlenecek kelime
        person: İyelik şahısı ('1sg', '2sg', '3sg', '1pl', '2pl', '3pl')
        plural: Çoğul mu? (True/False)
    """
    if not word:
        return word
    
    # Önce iyelik eki ekle
    if person == '1sg':
        result = add_first_singular_possessive(word)
    elif person == '2sg':
        result = add_second_singular_possessive(word)
    elif person == '3sg':
        result = add_third_singular_possessive(word)
    elif person == '1pl':
        result = add_first_plural_possessive(word)
    elif person == '2pl':
        result = add_second_plural_possessive(word)
    elif person == '3pl':
        result = add_third_plural_possessive(word)
    else:
        result = word
    
    # Sonra çokluk eki ekle (eğer isteniyorsa)
    if plural:
        result = add_plural_suffix(result)
    
    return result
