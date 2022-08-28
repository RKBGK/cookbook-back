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
        serializer = CategorySerializer(recipes)
        return Response(serializer.data)
        
    # @permission_classes([AllowAny])
    def list(self, request):
        recipes = Recipe.objects.all()            
        serializer = CategorySerializer(recipes, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        recipe = Recipe.objects.get(pk=pk) 
        serializer = CategorySerializer(recipe, data=request.data)
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
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Recipe
        fields = ('id','chef','title','publication_date','image_url', 'description','video_url','recipe','cookingtime','category', 'favorite')

