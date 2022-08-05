from rest_framework import serializers
from base.models import item

class item_serializers(serializers.ModelSerializer) :
    class Meta :
        model = item
        fields = '__all__'
        
