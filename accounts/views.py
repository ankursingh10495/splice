from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import UserSerializer
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.


def index_page(request):
	pass

	return render(request, 'index.html')


class UserCreate(APIView):
	def post(self, request, format='json'):
		serializer = UserSerializer(data=request.data)
		try:
			if serializer.is_valid():
				user = serializer.save()
				if user:
					token = Token.objects.create(user=user)
					json = serializer.data
					json['token'] = token.key

					return Response(serializer.data, status=status.HTTP_201_CREATED)
				else:
					return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			print(e)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def login(request):
    if request.method == 'POST':
        email = request.POST.get('login_email', '')
        password = request.POST.get('login_password', '')
        user_type = request.POST.get('login_user_type', '')

        check_user = CustomUser.objects.filter(email=email, user_type=user_type)
        if check_user:
        	username = check_user[0].username
        	user = authenticate(username=username, password=password)
        	print(user)
        	if user is not None:
        		auth.login(request, user)
        		get_user = CustomUser.objects.filter(username=username).values('id')
        		request.session['user_id'] = get_user[0]['id']
        		return HttpResponse('Logged in')
        	else:
        		return HttpResponse('failed')
        else:
        	return HttpResponse('Invalid User')



@login_required()
def dashboard(request):
	user_id = request.session['user_id']

	check_user = CustomUser.objects.filter(id=int(user_id))
	user_type = check_user[0].user_type

	return render(request, 'dashboard.html', {'user_type': user_type})