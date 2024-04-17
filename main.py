letters = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j",
           "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t",
           "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"]
word = input("Tersini almak istediginiz cümleyi yazın: ")
reversed_word = ""


def cumle_ters_cevir(metin):
    words = metin.split()
    print(words)
    empty_list = []
    for word in words:
        empty_list.append(kelimeyi_ters_cevir(word))
    return " ".join(empty_list)

def kelimeyi_ters_cevir(word):
    tersten_kelime = ""
    non_char = ""
    for i in range(len(word) - 1, -1, -1):
        if word[i] in letters:
            tersten_kelime += word[i]
        else:
            non_char += word[i]
    return f"{tersten_kelime}{non_char}"

result = cumle_ters_cevir(word)
print(f"Before :{word}\nAfter: {result}")