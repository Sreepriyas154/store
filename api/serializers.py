from rest_framework import serializers
from api.models import Books
from api.models import Reviews
from django.contrib.auth.models import User


class BookSerialzers(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    author=serializers.CharField()
    price=serializers.IntegerField()
    publication=serializers.CharField()
    qty=serializers.IntegerField()


    def create(self, validated_data):
        return Books.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name=validated_data.get("name")
        instance.author = validated_data.get("author")
        instance.price = validated_data.get("price")
        instance.publication=validated_data.get("publication")
        instance.qty = validated_data.get("qty")
        instance.save()
        return instance



    # def validate(self, data):
    #     price=data.get("price")
    #     qty=data.get("qty")
    #     if qty not in range(1,500):                                object level validation
    #         raise serializers.ValidationError("invalied error")
    #     if price not in range(50,1000):
    #         raise serializers.ValidationError("invalid price")
    #     return data





class BookSerialzer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)

    class Meta:
        model=Books
        fields="__all__"

        def validate_price(self, value):
            if value not in range(50, 1000):
                raise serializers.ValidationError("invalid error")  # field level validtaion
            return value

        def validate_qty(self, value):
            if value not in range(50, 1000):
                raise serializers.ValidationError("invalid error")  # field level validtaion
            return value


class ReviewSerializer(serializers.ModelSerializer):
    created_date=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields="__all__"


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","email","password"]

    def create(self, validated_data):
        user= User.objects.create_user(User,**validated_data)
        return user



