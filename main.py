if __name__=='__main__':
    text = "Было бы круто сдать программирование"
def sort_sentence(text):
    sorted = text.lower().split()
    sorted.sort(key = len)
    return sorted
    print(sorted)
sort_sentence(text)
