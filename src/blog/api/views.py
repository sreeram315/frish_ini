from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import ( AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly,
	)
from rest_framework.serializers import ValidationError

from blog.models import BlogInfo, CommentsInfo
from .serializers import PostSerializer, CommentCreateSerializer

class PostListAPIView(ListAPIView):
	queryset		 = BlogInfo.objects.all()
	serializer_class = PostSerializer

class CommentCreateView(CreateAPIView):
	queryset = CommentsInfo.objects.all()
	serializer_class = CommentCreateSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		parent_slug = self.request.GET.get('parent_slug')
		blog_slug = self.request.GET.get('blog_slug')
		creater = self.request.user
		
		# parent
		if parent_slug:
			
			parent 		= CommentsInfo.objects.filter(slug = parent_slug)
			if parent.exists() and parent.count() == 1:
				parent = parent.first()
		# blog
			blog 		= 	CommentsInfo.objects.get(slug = parent_slug).blog
		elif blog_slug:
			blog 	=	BlogInfo.objects.filter(slug = blog_slug)
			if blog.exists() and blog.count() == 1:
				blog = blog.first()
			else:
				raise ValidationError('Unique blog/blog not found')
			parent = None
		else:
			raise ValidationError('Please provide either blog slug or the parent slug')

		serializer.save(	creater = creater,
							parent  = parent,
							blog   = blog
						)



	
