from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class StudentInfoLimitPagination(LimitOffsetPagination):
	default_limit = 7
	max_limit = 10