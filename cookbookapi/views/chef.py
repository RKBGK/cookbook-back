from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from cookbookapi.models import Chef, Recipe, Subscription
from rest_framework.decorators import action

class ChefView(ViewSet):
    """User view"""
    # @permission_classes([AllowAny])
    def retrieve(self, request, pk):
        chefs = Chef.objects.get(pk=pk)
        serializer = UserSerializer(chefs)
        return Response(serializer.data)
    # @permission_classes([AllowAny])
    def list(self, request):
        chefs = Chef.objects.all()
        serializer = UserSerializer(chefs, many=True)
        return Response(serializer.data)    
    
    @action(methods=['get'], detail=True)
    def chefRecipe(self, request,pk):
        rescipes = Recipe.objects.all().filter(chef_id=pk)
        serializer = UserPostSerializer(rescipes , many=True)        
        return Response(serializer.data)
    
    @action(methods=['get'], detail=True)
    def userSubscriptions(self, request,pk):
        subscriptions = Subscription.objects.all().filter(follower_id=pk)
        serializer =  SubscriptionSerializer(subscriptions, many=True)        
        return Response(serializer.data)
    
class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users
    """
    first_name = serializers.CharField(source = 'user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    class Meta:
        model = Chef

        fields = ('user', 'bio', 'image_url', 'created_on', 'active','first_name','last_name')
        # depth = 1
        
class UserPostSerializer(serializers.ModelSerializer):
    """JSON serializer for users
    """
    user = UserSerializer(many=False)
    class Meta:
        model = Chef
        fields = ('title', 'publication_date','image_url', 'content', 'approved','category','user')
        
class SubscriptionSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Subscription
        fields = ('id', 'created_on', 'deleted_on', 'author', 'follower')
