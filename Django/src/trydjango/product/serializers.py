from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'pk',
            'title',
            'description',
            'price',
            'summary',
            'featured',
            ]
        # read_only_fields = ['title']
    def validate_title(self,value):
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("this title already exist")
        return value