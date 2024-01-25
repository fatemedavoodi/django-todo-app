from rest_framework import serializers
from ...models import Task




class TaskSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        alidated_data['user'] = self.context.get('request').user
        return super().create(validated_data) 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["user" ,"title"]
  
  
