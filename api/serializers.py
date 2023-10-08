from rest_framework import serializers
from api.models import Books
from api.models import Reviews


class BookSerialzers(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    author=serializers.CharField()
    price=serializers.IntegerField()
    publication=serializers.CharField()
    qty=serializers.IntegerField()

class BookModelSerialzer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)

    class Meta:
        model=Books
        fields="__all__"


class ReviewSerializer(serializers.ModelSerializer):
    created_date=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields="__all__"
