def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
 #   words = phrase.split(' ').capitalize()
    words = [word.capitalize() for word in phrase.split(' ')]
    return ' '.join(words)