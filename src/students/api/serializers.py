from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField

#
from students.models import StudentInfo

url_detail = HyperlinkedIdentityField(
	view_name = 'students-api-detail',
	lookup_field = 'slug'
		)

class StudentSerializer(ModelSerializer):
	owner = SerializerMethodField()
	something = SerializerMethodField()
	url = url_detail
	class Meta:
		model = StudentInfo
		fields = [
					'name',
					'reg_no',
					'dob',
					'gender',
					'cgpa',
					'section',
					'address',
					'description',
					'owner',
					'contact',
					'url',
					'something',

				]
	def get_owner(self, obj):
		return obj.owner.username

	def get_something(self, obj):
		return obj.reg_no

class StudentDetailSerializer(ModelSerializer):
	owner = SerializerMethodField()
	class Meta:
		lookup_field = 'slug'
		model = StudentInfo
		fields = [
					'name',
					'reg_no',
					'dob',
					'gender',
					'cgpa',
					'section',
					'address',
					'description',
					'owner'
				]

	def get_owner(self, obj):
		return obj.owner.username

class StudentCreateSerializer(ModelSerializer):

	class Meta:
		model = StudentInfo
		fields = [
					'name',
					'reg_no',
					'cgpa',
					'section',
					'gender',
				]

data = {
	'name': 'asdin',
	'reg_no': 112913,
	'section': 'e1334',
	'cgpa'	:	10,
	'gender': 'M'
}

ser = StudentCreateSerializer(data = data, partial = True)

ser.is_valid()




