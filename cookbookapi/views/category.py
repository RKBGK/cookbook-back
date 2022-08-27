from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from cookbookapi.models.category import Category
# from rest_framework.decorators import  permission_classes
# from rest_framework.permissions import AllowAny

class CategoryView(ViewSet):
    """Level up game types view"""
    
    # @permission_classes([AllowAny])
    def retrieve(self, request, pk):
        categories = Category.objects.get(pk=pk)
        serializer = CategorySerializer(categories)
        return Response(serializer.data)
        
    # @permission_classes([AllowAny])
    def list(self, request):
        categories = Category.objects.all()            
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        category = Category.objects.get(pk=pk) 
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        category.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
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
        model = Category
        fields = ('id','label')
