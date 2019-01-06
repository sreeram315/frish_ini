from rest_framework.generics import ( ListAPIView, RetrieveAPIView, DestroyAPIView,
										 UpdateAPIView, CreateAPIView)
from rest_framework.permissions import ( AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly,
	)

from students.models import StudentInfo
from .permissions import IsOwner
from .serializers import StudentSerializer, StudentCreateSerializer, StudentDetailSerializer
from .paginators import StudentInfoLimitPagination


class StudentInfoListAPIView(ListAPIView):
	serializer_class = StudentSerializer
	pagination_class = StudentInfoLimitPagination

	def get_queryset(self):
		queryset = StudentInfo.objects.all()
		q  =  self.request.GET.get('q')
		if q:
			queryset = queryset.filter(name__icontains = q)
		return queryset


class StudentInfoDetailView(RetrieveAPIView):
	lookup_field = 'slug'
	queryset = StudentInfo.objects.all()
	serializer_class = StudentDetailSerializer
	permission_classes = [IsOwner]

class StudentInfoUpdateAPIView(UpdateAPIView):
	queryset = StudentInfo.objects.all()
	serializer_class = StudentSerializer
	permission_classes = [IsOwner]


class StudentInfoDeleteAPIView(DestroyAPIView):
	queryset = StudentInfo.objects.all()
	serializer_class = StudentSerializer

class StudentInfoCreateAPIView(CreateAPIView):
	queryset = StudentInfo.objects.all()
	serializer_class = StudentCreateSerializer

	def perform_create(self, serializer):
		serializer.save(owner = self.request.user)




