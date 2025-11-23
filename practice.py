import request

def most_common_words_in_webpage(words,url):
    responce = request.get(url)
    return most_common_words_in_webpage(words,responce.text()

def most_common_words(words,text):
    """"
        find the most common words in web page
    """
    word_frequency = {w :text(w) for w in words}
    return sorted(words, key=word_frequency.get)[-1]