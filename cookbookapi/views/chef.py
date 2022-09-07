from cookbookapi.views.recipe import RecipeSerializer
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
        chef= Chef.objects.get(user_id=pk)
        print('chef',chef.id)
        subscriptions = Subscription.objects.all().filter(follower_id=chef.id)
        serializer =  SubscriptionSerializer(subscriptions, many=True)        
        return Response(serializer.data)
    
    # http://127.0.0.1:8000/chefs/subscribed
    @action(methods=['get'], detail=False)
    def subscribed(self, request):
        """Get request to display posts of authors logged-in user is subscribed to """
        recipes = Recipe.objects.all()
        subs = Subscription.objects.all()
        user = Chef.objects.get(user_id=request.auth.user)
        print('*************************')
        print(request.auth.user)
        user_subs = subs.filter(follower=user)
        if len(user_subs) > 0:
            for user_sub in user_subs:
                recipes= recipes.filter(chef=user_sub.chef_id)
        else:
            recipes=[]
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)   
class ChefSerializer(serializers.ModelSerializer):
    """JSON serializer for users
    """
    # first_name = serializers.CharField(source = 'user.first_name')
    # last_name = serializers.CharField(source = 'user.last_name')
    class Meta:
        model = Chef

        fields = ('user', 'bio', 'image_url', 'created_on', 'active','subscribed')
        # depth = 1
        
class UserRecipeSerializer(serializers.ModelSerializer):
    """JSON serializer for users
    """
    chef= ChefSerializer(many=False)
    class Meta:
        model = Recipe
        fields = ('title','publication_date','image_url', 'description','video_url','recipe','cookingtime','chef')
        
class SubscriptionSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField(source = 'user.first_name')
    # last_name = serializers.CharField(source = 'user.last_name')
    class Meta:
        model = Subscription
        fields = ('id', 'created_on', 'deleted_on', 'chef', 'follower')
