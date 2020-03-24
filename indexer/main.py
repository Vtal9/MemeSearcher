import indexer
import info
import query

if __name__ == '__main__':
    SAMPLE = []
    SAMPLE.append(info.MemeInfo("url1", "собака не собака, пока она голодна твикс", "собака, твикс"))
    SAMPLE.append(info.MemeInfo("url2", "бла не бла когда он бла", "волк, собака"))

    #index = indexer.full_index(SAMPLE)
    print(query.make_query(text_phrase="бла", descr_words="волк"))
