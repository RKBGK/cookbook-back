"""View module for handling requests about game types"""
# from multiprocessing import Event
# from unicodedata import Ingredient
# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from cookbookapi.models.ingredients import Ingredient
# from rest_framework.decorators import  permission_classes
# from rest_framework.permissions import AllowAny

class IngredientView(ViewSet):
    """Level up game types view"""
    
    # @permission_classes([AllowAny])
    def retrieve(self, request, pk):
        ingredients = Ingredient.objects.get(pk=pk)
        serializer = IngredientSerializer(ingredients)
        return Response(serializer.data)
        
    # @permission_classes([AllowAny])
    def list(self, request):
        ingredients = Ingredient.objects.all()            
        serializer = IngredientSerializer(ingredients, many=True)
        print(serializer )
        return Response(serializer.data)

    def update(self, request, pk):
        ingredient = Ingredient.objects.get(pk=pk) 
        serializer = CreateIngredientSerializer(ingredient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        ingredient = Ingredient.objects.get(pk=pk)
        ingredient.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)    
    
    def create(self, request):

        print(request.data)
        serializer = CreateIngredientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  

class IngredientSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Ingredient
        fields = ('id','label')

class CreateIngredientSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Ingredient
        fields = ('label',)