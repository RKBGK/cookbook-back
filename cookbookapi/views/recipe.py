from unicodedata import numeric
from cookbookapi.models.chef import Chef
from cookbookapi.models.recipe_ingredients import RecipeIngredients
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from cookbookapi.models.recipe import Recipe
from cookbookapi.models.measure import Measure
from cookbookapi.models.ingredients import Ingredient

class RecipeView(ViewSet):
    """Level up game types view"""
    
    # @permission_classes([AllowAny])
    def retrieve(self, request, pk):
        recipes = Recipe.objects.get(pk=pk)
        
        serializer = RecipeSerializer(recipes)
        print(serializer.data)    
        return Response(serializer.data)
        
    # @permission_classes([AllowAny])
    def list(self, request):
        recipes = Recipe.objects.all()            
        serializer = RecipeSerializer(recipes, many=True)
        # print(serializer.data)
        return Response(serializer.data)
  

    def update(self, request, pk):
        recipe = Recipe.objects.get(pk=pk) 
        serializer = RecipeSerializer(recipe, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        recipe.save()
        newcategories =  request.data['categories']
        recipe.categories.set(newcategories)
        elements =  request.data['element']
        print('elements ',elements )
        
        for element in elements:
            measure=Measure.objects.get(unit=(element['unit']))
            ingredient=Ingredient.objects.get(label=element['ingredient'])  
            quantity= float(element['quantity'])   
            
            recipeIngredient = RecipeIngredients(recipe=recipe, ingredient=ingredient, measure=measure,quantity=quantity)
            recipeIngredient.save()
                             
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        recipe.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)    
    
    def create(self, request):
        # print(request.data)
        # print(request.auth.user)
        chef = Chef.objects.get(user=request.auth.user)
        serializer = CreateRecipeSerializer(data=request.data)
        # print("*" * 100)
        # print(CreateRecipeSerializer(data=request.data))        
        serializer.is_valid(raise_exception=True)
        serializer.save(chef=chef)
        
        recipeid = serializer.data['id']
        recipe= Recipe.objects.get(pk=recipeid )
        categories =  request.data['categories']
        recipe.categories.add(*categories)
        
        elements =  request.data['element']
        for element in elements:
            measure=Measure.objects.get(unit=(element['measure']))
            ingredient=Ingredient.objects.get(label=element['ingredient'])
            quantity= float(element['quantity'])   
            
            recipeIngredient = RecipeIngredients(recipe=recipe, ingredient=ingredient, measure=measure,quantity=quantity)
            recipeIngredient.save()
                             
        
    
        return Response(serializer.data, status=status.HTTP_201_CREATED)  


class IngredientView(ViewSet):
    """Level up game types view"""
    
    # @permission_classes([AllowAny])
    def retrieve(self, request, pk):
        ingredients = RecipeIngredients.objects.get(pk=pk)
        serializer = IngredientSerializer(ingredients)
        print(serializer.data)    
        return Response(serializer.data)
           
class  CreateRecipeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = ('id','title','publication_date','image_url', 'description','video_url','directions','cookingtime')
        
class  CreateRecipeIngredientSerializer(serializers.ModelSerializer):
    # measureunit= MeasureSerializer(many=True, read_only=True)
    unit= serializers.CharField(source = 'measure.unit')
    
    ingredient= serializers.CharField(source = 'ingredient.label')
    class Meta:
        model = RecipeIngredients
        fields = ('recipe','ingredient','quantity','unit')

class  MeasureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measure
        fields = ('unit')
        
class  IngredientSerializer(serializers.ModelSerializer):
    # measureunit= MeasureSerializer(many=True, read_only=True)
    unit= serializers.CharField(source = 'measure.unit')
    ingredient= serializers.CharField(source = 'ingredient.label')
    class Meta:
        model = RecipeIngredients
        fields = ('ingredient','quantity','unit')
        depth = 1
        
class RecipeSerializer(serializers.ModelSerializer):
    element = IngredientSerializer(many=True, read_only=True)
    # categorylabel= serializers.CharField(source = 'category.label')

    class Meta:
        model = Recipe
        
        fields = ('id','chef','title','publication_date','image_url', 'description','video_url','directions',
                  'cookingtime','categories', 'favorite','categorized','element')
        depth = 2

