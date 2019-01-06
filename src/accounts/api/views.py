from rest_framework.generics import ( ListAPIView, RetrieveAPIView, DestroyAPIView,
										 UpdateAPIView, CreateAPIView)
from rest_framework.permissions import ( AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly,
	)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import AccountCreateSerializer, AccountLoginSerializer


class AccountCreateView(CreateAPIView):
	serializer_class = AccountCreateSerializer

class AccountLoginView(APIView):
	permissions_classes = [AllowAny]
	serializer_class = AccountLoginSerializer

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = AccountLoginSerializer(data = data)
		if serializer.is_valid(raise_exception = True):
			new_data  = serializer.data
			return Response(new_data, status = HTTP_200_OK)
		return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)

	




