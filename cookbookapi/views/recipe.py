from cookbookapi.models.recipe_ingredients import RecipeIngredients
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from cookbookapi.models.recipe import Recipe
# from rest_framework.decorators import  permission_classes
# from rest_framework.permissions import AllowAny

class RecipeView(ViewSet):
    """Level up game types view"""
    
    # @permission_classes([AllowAny])
    def retrieve(self, request, pk):
        recipes = Recipe.objects.get(pk=pk)
        ingredients= RecipeIngredients.objects.get_or_create(recipe=pk)
        serializer = RecipeSerializer(recipes)
        return Response(serializer.data)
        
    # @permission_classes([AllowAny])
    def list(self, request):
        recipes = Recipe.objects.all()            
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        recipe = Recipe.objects.get(pk=pk) 
        serializer = RecipeSerializer(recipe, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        recipe.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        recipe.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)    
    
    def create(self, request):

        print(request.data)
        serializer = RecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  

class RecipeSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    # first_name = serializers.CharField(source = 'chef.user.first_name')
    # last_name = serializers.CharField(source = 'chef.user.last_name')

    class Meta:
        model = Recipe
        
        fields = ('id','chef','title','publication_date','image_url', 'description','video_url','recipe','cookingtime','category', 'favorite','categorized')
        # depth = 2
        
class  CreateRecipeSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Recipe
        fields = ('id','chef','title','publication_date','image_url', 'description','video_url','recipe')

