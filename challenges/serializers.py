from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Month

class MonthSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    idea = serializers.CharField(max_length=200)
    position = serializers.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    isGoodIdea = serializers.BooleanField(default=False)
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)
        
    def create(self, validate_data):
        # Remove read-only fields from validate_data
        validate_data.pop('id', None)
        validate_data.pop('created_on', None)
        validate_data.pop('updated_on', None)
        return Month.objects.create(**validate_data)

# class MonthSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Month
#         fields = ['id', 'name', 'idea', 'position', 'isGoodIdea', 'created_on', 'updated_on']
#         read_only_fields = ['id', 'created_on', 'updated_on']

# class MonthSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Month
#         fields = '__all__'