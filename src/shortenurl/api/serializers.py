from rest_framework.serializers import ModelSerializer

#
from shortenurl.models import UrlInfo

class PostSerializer(ModelSerializer):
	class Meta:
		model = UrlInfo
		fields = [
					'name',
					'original_link',

				]

'''
data = {
	'name' : 'Poolane',
	'original_link': 'https://en.wikipedia.org/wiki/Zero_(2018_film)'
}

obj = PostSerializer(data = data)

if obj.is_valid():
	obj.save()
else:
	print(obj.errors)
'''