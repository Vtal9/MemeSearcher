import simplifier

BIGRAM_WEIGHT = 3
PHRASE_WEIGHT = 10
DESCRIPTION_WEIGHT = 12

DB_INDEX_TEXT_SAMPLE = {'сапака': {'url1': [0, 2]}, 'ни': {'url1': [1], 'url2': [1]}, 'пака': {'url1': [3]}, 'ана': {'url1': [4]}, 'калатна': {'url1': [5]}, 'тфикс': {'url1': [6]}, 'хуи': {'url2': [0, 2, 4]}, 'сахуи': {'url2': [3]}}
DB_INDEX_DESCR_SAMPLE = {"сапака": {"url1", "url2"}, "фалк": {"url2"}, "тфикс": {"url1"}}

def db_result(word, is_descr=False):
    if is_descr: # get info from description db
        return DB_INDEX_DESCR_SAMPLE[word]
    else:
        return {}#{word: DB_INDEX_TEXT_SAMPLE[word]}

def __intersection(*args):
    intersect = set(args[0])
    for arg in args:
        intersect &= set(arg)
    return list(intersect)


def _one_word_query(word, word_index, urls_weight={}):
    for url in word_index[word].keys():
        if url in urls_weight:
            urls_weight[url] += len(word_index[word][url])
        else:
            urls_weight[url] = len(word_index[word][url])
    return urls_weight


def _bigram_query(word1, word2, word_index, urls_weight={}):
    common_urls = __intersection(word_index[word1].keys(), word_index[word2].keys())

    for url in common_urls:
        poss1 = word_index[word1][url]
        poss2 = [pos - 1 for pos in word_index[word2][url]]

        if len(__intersection(poss1, poss2)) != 0:
            if url in urls_weight.keys():
                urls_weight[url] += BIGRAM_WEIGHT
            else:
                urls_weight[url] = BIGRAM_WEIGHT + 2 # + 2

    return urls_weight


def _phrase_query(phrase, word_index, urls_weight={}):
    words = phrase.split(' ')
    common_urls = __intersection(*words)

    for url in common_urls:
        words_pos = []
        for i, word in enumerate(words):
            words_pos.append(poss - i for poss in word_index[word][url])

        if len(__intersection(*words_pos)) != 0:
            if url in urls_weight.keys():
                urls_weight[url] += PHRASE_WEIGHT * len(words)
            else:
                urls_weight[url] = PHRASE_WEIGHT * len(words) + len(words)

    return urls_weight


def make_query_text_part(text):
    stext = simplifier.simplify_string(text)

    word_text_index = {}

    words = stext.split(' ')
    words_set = set(words)
    for word in words_set: # optimisation
        word_text_index.update(db_result(word, is_descr=False))

    if len(word_text_index) == 0:
        return None

    urls_weight = {}

    for word in words_set:
        urls_weight.update(_one_word_query(word, word_text_index, urls_weight))

    if len(words) > 2:
        i = 0
        while i + 1 < len(words):
            urls_weight.update(_bigram_query(words[i], words[i + 1], word_text_index, urls_weight))
            i += 1
        urls_weight.update(_phrase_query(stext, word_text_index, urls_weight))

    return urls_weight


def make_query_descr_part(descr):
    sdescr = simplifier.simplify_string(descr)
    words = sdescr.split(' ')

    common_urls = db_result(words[0], is_descr=True)

    if len(words) > 1:
        for word in words:
            common_urls.intersection(db_result(word, is_descr=True))

    return common_urls


def make_query(text_phrase="", descr_words=""):
    message = ""
    if text_phrase == "":
        common_urls_from_descr = make_query_descr_part(descr_words)
        ranked_result = list(common_urls_from_descr)
        message = "text is empty"
    else:
        urls_weight_from_text = make_query_text_part(text_phrase)

        if urls_weight_from_text == None:
            message = "no text words found in the database"
            if descr_words == "":
                urls_weight_from_text = []
            else:
                common_urls_from_descr = make_query_descr_part(descr_words)
                ranked_result = list(common_urls_from_descr)
        else:
            if descr_words != "":
                common_urls_from_descr = make_query_descr_part(descr_words)
                for url in common_urls_from_descr:
                    if url in urls_weight_from_text.keys():
                        urls_weight_from_text[url] += DESCRIPTION_WEIGHT

            ranked_result = sorted(urls_weight_from_text, key=urls_weight_from_text.get, reverse=True)

    return ranked_result, message
