def mutate_string(string, position, character):
    str = list(string)
    str[position] = character
    return ''.join(str)



