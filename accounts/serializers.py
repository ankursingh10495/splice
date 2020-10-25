from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
	first_name = serializers.CharField(max_length=100, required=True)
	last_name = serializers.CharField(max_length=100, required=True)
	email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=CustomUser.objects.all())])
	user_type = serializers.CharField(max_length=10, required=True)
	username = serializers.CharField(validators=[UniqueValidator(queryset=CustomUser.objects.all())])
	password = serializers.CharField(min_length=8, write_only=True)
	mobile = serializers.IntegerField(required=True)
	phone_number = serializers.IntegerField(required=True)
	company = serializers.CharField(max_length=100)
	address_line1 = serializers.CharField(max_length=100)
	address_line2 = serializers.CharField(max_length=100)
	city = serializers.CharField(max_length=100)
	zip_code = serializers.CharField(max_length=100)
	state = serializers.CharField(max_length=100)
	country = serializers.CharField(max_length=100)

	def create(self, validated_data):
		user = CustomUser.objects.create_user(username=validated_data['username'], 
											  first_name=validated_data['first_name'], 
											  last_name=validated_data['last_name'],
											  email=validated_data['email'], 
											  user_type=validated_data['user_type'], 
											  password=validated_data['password'],
											  mobile=validated_data['mobile'],
											  phone_number=validated_data['phone_number'],
											  company=validated_data['company'],
											  address_line1=validated_data['address_line1'],
											  address_line2=validated_data['address_line2'],
											  city=validated_data['city'],
											  zip_code=validated_data['zip_code'],
											  state=validated_data['state'],
											  country=validated_data['country'],
											  is_active=True)
		print(user, 'user')

		return user

	class Meta:
		model = CustomUser
		fields = ('first_name', 'last_name', 'email', 'user_type', 'username', 'password', 'mobile',
				  'phone_number', 'company', 'address_line1', 'address_line2', 'city', 'zip_code', 'state',
				  'country')