"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from cookbookapi.models.measure import Measure



# from rest_framework.decorators import  permission_classes
# from rest_framework.permissions import AllowAny

class MeasureView(ViewSet):
    """Level up game types view"""  

        
    # @permission_classes([AllowAny])
    def list(self, request):
        measures= Measure.objects.all()
        serializer = MeasureSerializer(measures, many=True)
        print(serializer )
        return Response(serializer.data)
class MeasureSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Measure
        fields = ('id', 'unit')