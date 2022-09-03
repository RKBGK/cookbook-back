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
        serializer = ChefSerializer(chefs)
        return Response(serializer.data)
    # @permission_classes([AllowAny])
    def list(self, request):
        chefs = Chef.objects.all()
        serializer = ChefSerializer(chefs, many=True)
        return Response(serializer.data)    
    
    # http://127.0.0.1:8000/chefs/1/chefRecipe
    @action(methods=['get'], detail=True)
    def chefRecipe(self, request,pk):
        recipes = Recipe.objects.all().filter(chef_id=pk)
        serializer = UserRecipeSerializer(recipes , many=True)        
        return Response(serializer.data)
    
    # http://127.0.0.1:8000/chefs/1/chefSubscriptions
    # Subscriptions of follower 1
    @action(methods=['get'], detail=True)
    def chefSubscriptions(self, request,pk):
        subscriptions = Subscription.objects.all().filter(follower_id=pk)
        serializer =  SubscriptionSerializer(subscriptions, many=True)        
        return Response(serializer.data)
    
class ChefSerializer(serializers.ModelSerializer):
    """JSON serializer for users
    """
    first_name = serializers.CharField(source = 'user.first_name')
    last_name = serializers.CharField(source = 'user.last_name')
    class Meta:
        model = Chef

        fields = ('user', 'bio', 'image_url', 'created_on', 'active','first_name','last_name')
        # depth = 1
        
class UserRecipeSerializer(serializers.ModelSerializer):
    """JSON serializer for users
    """
    chef= ChefSerializer(many=False)
    class Meta:
        model = Recipe
        fields = ('title','publication_date','image_url', 'description','video_url','recipe','cookingtime','chef')
        
class SubscriptionSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Subscription
        fields = ('id', 'created_on', 'deleted_on', 'chef', 'follower')
