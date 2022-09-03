
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from cookbookapi.models.chef import Chef

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):

    username = request.data['username']
    password = request.data['password']
    print(request.data)
    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    authenticated_user = authenticate(username=username, password=password)
    print(' authenticated_user',authenticated_user)
    #If authentication was successful, respond with their token
    
    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)

        data = {
            'valid': True,
            'user': token.user_id,
            'token': token.key
        }
        print('*' * 100)
        print(data)
        return Response(data)
    else:
        #Bad login details were provided. User cannot be logged in.
        data = { 'valid': False }
        return Response(data)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    
    '''Handles the creation of a new gamer for authentication
    Method arguments:
      request -- The full HTTP request object
    '''
    print(request.data)
    #create a new user by invoking the create_user helper method
    #on Django's built-in User model
    new_user = User.objects.create_user(
        username=request.data['username'],
        password=request.data['password'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        email=request.data['email']
    )
    
    #save extra info in the cookbookapi_chef table
    chef = Chef.objects.create(
        bio=request.data['bio'],
        image_url=request.data['image_url'],
        created_on=request.data['created_on'],
        active=request.data['active'],
        user=new_user
    )
    
    token = Token.objects.create(user=chef.user)

    data = { 
            'token': token.key,
            'user': token.user_id,
            'valid': True
            }
    print('data',data)
    return Response(data)
    