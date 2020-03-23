import simplifier
import indexer
import info

if __name__ == '__main__':
    SAMPLE = []
    SAMPLE.append(info.MemeInfo("url1", "ЛБЫФ,ЫФВ хуй", "собака"))
    SAMPLE.append(info.MemeInfo("url2", "хуй не хуй захуй хуй", "волк, собака"))

    index = indexer.full_index(SAMPLE)
    print(index.descr_words)
    print(index.text_words)