def word_search(doc_list, keyword):
    k = keyword.upper()
    k1 = keyword.upper() + '.'
    res = []
    for idx, doc in enumerate(doc_list):
        for word in doc.upper().split():
            if word == k or word == k1:
                res.append(idx)
                break
    return res


doc_list = ['The Learn Python Challenge Casino', 'They bought a car, and a horse', 'Casinoville?']
keyword = 'car'

print(word_search(doc_list, keyword))
