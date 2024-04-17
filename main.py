# word = input("Tersini almak istediginiz cümleyi yazın: ")
word = "ali seni cok seviyorum."
reversed_word = ""

def cumle_ters_cevir(metin):
    words = metin.split()
    empty_list = []
    for word in words:
        empty_list.append(kelimeyi_ters_cevir(word))
    return " ".join(empty_list)



def kelimeyi_ters_cevir(kelime):
    tersten_kelime = ""
    for i in range(len(kelime)-1, -1, -1):
        tersten_kelime += kelime[i]
    return tersten_kelime

result = cumle_ters_cevir(word)
print(f"Before :{word}\nAfter: {result}")
