from rest_framework.generics import ListAPIView

from shortenurl.models import UrlInfo
from .serializers import PostSerializer

class PostListAPIView(ListAPIView):
	queryset		 = UrlInfo.objects.all()
	serializer_class = PostSerializer