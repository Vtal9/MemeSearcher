from indexer import simplifier
import indexer
import info
from . models import Images
from . models import TextDescriptions
from . models import ImageDescriptions

if indexate(dataBase):
    # SAMPLE = []
    # SAMPLE.append(info.MemeInfo("url1", "", "собака"))
    # SAMPLE.append(info.MemeInfo("url2", "хуй не хуй захуй хуй", "волк, собака"))

    index = indexer.full_index(dataBase)
    # print(index.descr_words)
    # print(index.text_words)
    return index