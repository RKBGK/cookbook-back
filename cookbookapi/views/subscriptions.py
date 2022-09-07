"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from datetime import datetime
from cookbookapi.models.subscription import  Subscription


# from rest_framework.decorators import  permission_classes
# from rest_framework.permissions import AllowAny

class SubscriptionView(ViewSet):
    """Level up game types view"""  

        
    # @permission_classes([AllowAny])
    def list(self, request):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        print('*' * 100)
        print(serializer)
        return Response(serializer.data)

    
class SubscriptionSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Subscription
        fields = ('id', 'chef', 'follower','created_on', 'deleted_on')
