from rest_framework.serializers import (
										ModelSerializer, RelatedField, ValidationError, 
										EmailField, CharField
									)
from django.contrib.auth import get_user_model

User  = get_user_model()



class AccountCreateSerializer(ModelSerializer):
	email_1 = EmailField(label = 'Email address', required = True)
	email_2 = EmailField(label = 'Confirm email', required = True)
	class Meta:
		model = User
		fields = '__all__'
		fields = [
				'username',
				'email_1',
				'email_2',
				'password'
		]

		extra_kwargs = {
					"password":{
								"write_only": True
					}
		}

	def validate_email_1(self, value):
		email = value
		print(email)
		obj = User.objects.filter(email = email)
		print(obj)
		if obj.exists():
			raise ValidationError("Email already in use")
		return value


	def validate_email_2(self, value):
		email_2 = value
		email_1 = self.initial_data.get("email_1")
		if email_1!=email_2:
			raise ValidationError("Emails do the match")
		return value
		



	def create(self, validated_data):
		email = validated_data["email_1"]
		password = validated_data["password"]
		username = validated_data["username"]

		print("""

			""")
		if User.objects.filter(email = email).exists():
			print('DONT DO THID')
		else:
			print(User.objects.filter(email = email))

		print(email)

		print("""

			""")

		user_obj = User(
							username = username,
							email    = email
					)
		user_obj.set_password(password)
		user_obj.save()
		return validated_data

	# def validate_content(self, data):
	# 	content = self.initial_data.get('content')
	# 	if len(content) < 1: raise ValidationError('Write something!')
	# 	return content



class AccountLoginSerializer(ModelSerializer):
	username 	= CharField( label = 'Username')
	token 		= CharField( allow_blank = True, read_only = True)
	class Meta:
		model =  User
		fields = [
				'username',
				'password',
				'token'
			]

		extra_kwargs = {
			"password":{
						"write_only": True
			}
		}

	def validate(self, data):



		data['token'] = "take this token re!"
		return data
