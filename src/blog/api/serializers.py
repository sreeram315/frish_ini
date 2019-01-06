from rest_framework.serializers import ModelSerializer, RelatedField, ValidationError

#
from blog.models import BlogInfo
from blog.models import CommentsInfo

class PostSerializer(ModelSerializer):
	class Meta:
		model = BlogInfo
		fields = [
					'headline',
					'age_restricted',
					#'genre',
					#'preview_points',
					'content',
					#'image',

				]

class CommentCreateSerializer(ModelSerializer):
	class Meta:
		model = CommentsInfo
		fields = '__all__'
		fields = [
				'content'
		]

	def validate_content(self, data):
		content = self.initial_data.get('content')
		if len(content) < 1: raise ValidationError('Write something!')
		return content

# def comment_create_serializer(creater = None, parent_slug = None, blog_slug = None):
# 	class CommentCreateSerializer(ModelSerializer):
# 		class Meta:
# 			model = CommentsInfo
# 			fields = [
# 						'content'
# 			]

# 		def __init__(self, *args, **kwargs):
# 			print(parent_slug)

# 		def validate(self, data):
# 			print('all_okay')

# 		def create(self, validated_data):
# 			print('okay')

