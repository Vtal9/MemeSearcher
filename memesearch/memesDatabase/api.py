from . models import Images
from . models import TextDescriptions
from . models import ImageDescriptions
from rest_framework import viewsets, permissions
from .serializers import ImagesSerializer
from .serializers import TextDescriptionsSerializer
from .serializers import ImagesDescriptionsSerializer
from django.db.models import Q
from .indexer import indexer, info, query



def searchText(query):
		textIndex = buildTextIndex(queryText)
		words = textIndex.keys()
		queryset = Image.objects.filter(any())


def searchImage(query):
		imageIndex = buildImageIndex(queryImage)
		words = imageIndex.keys()


def splitQuery(str):
    res = []
    for i in str.split(", "):
        for j in i.split(" "):
            res.append(j)
    return res


def droptTables():
	TextDescriptions.objects.all().delete()
	ImageDescriptions.objects.all().delete()


def reIndexate(SAMPLE):

	queryset = Images.objects.all()

	SAMPLE = []

	for i in queryset:
		SAMPLE.append(info.MemeInfo(i.image, i.vector, "")) #wrong

		index = indexer.full_index(SAMPLE)

	droptTables()

	for i in index.text_words.keys():
		if(i != ''):
			new_word = TextDescriptions.objects.create(word=i, index=index.text_words[i])
			new_word.save()

	for i in index.descr_words.keys():
		if(i != ''):
			new_word = ImageDescriptions.objects.create(word=i, index=index.text_words[i])
			new_word.save()




class ImagesViewSet(viewsets.ModelViewSet):
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = ImagesSerializer
	def get_queryset(self):
		if self.request.method == 'GET':
			#приходит запрос в виде двух строк - слова через пробел, мб запятые, с ключевыми словами
			queryText = self.request.GET.get('qText')
			queryImage = self.request.GET.get('qImage')
			

			TextWords = []
			ImageWords = []
			# разбиваем запросы на отдельные слова.
			if queryText is not None:
				TextWords = splitQuery(queryText)
			if queryImage is not None:
				ImageWords = splitQuery(queryImage)

			# ищем все картинки в описании которых совпало хотя бы одно слово. получаем список объектов модели
			querysetText = TextDescriptions.objects.filter(Q(index__in=TextWords))
			querysetImage = ImageDescriptions.objects.filter(Q(index__in=ImageWords))


			# отдаем ражировщику эти списки
			if(queryText is None):
				queryText = ""
			if (queryImage is None):
				queryImage = ""

			# получаем список из URL
			# ([urls],"error")
			# result = query.make_query(text_phrase=queryText, descr_words=queryImage)

			# записываем их в  response

			# if (result[1] == ""):
			result = [["url1", "url2", "url3"]]
			print([{'url':i} for i in result[0]])
			queryset = Images.objects.all()



			# # queryset = Images.objects.filter(Q(vector__in=words))
			return queryset
		if self.request.method == 'POST':
			print("POST")


class TextDesriptionsViewSet(viewsets.ModelViewSet):
	queryset = TextDescriptions.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = TextDescriptionsSerializer

class ImageDescriptionsViewSet(viewsets.ModelViewSet):
	queryset = ImageDescriptions.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = ImagesDescriptionsSerializer