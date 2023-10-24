def search4vowels(phrase):
    '''Выводит гласные, найденные во введенном слове.'''
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return vowels.intersection(set(phrase))

def search4letters(phrase, letters:str='aeiou'):
    '''Возвращает множество букв из letters, найденных в указанной фразе.'''
    return set(letters).intersection(set(phrase))
