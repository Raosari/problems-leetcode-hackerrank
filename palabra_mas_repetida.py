def MostRepeated(string):
    words = string.lower().split()
    frequency = {}
    for element in words:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    max_frequency = max(frequency.values())
    most_repeated_words = [word for word, freq in frequency.items() if freq == max_frequency]
    return f"palabras mas repetidas {most_repeated_words}, {max_frequency} repeticiones"

a = MostRepeated("Hola mi nombre es rao, es genial")
print(a)

