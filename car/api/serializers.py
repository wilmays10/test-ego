from rest_framework import serializers

from car.models import Group, Version, Price


class GroupSerializer(serializers.ModelSerializer):

    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return obj.get_category_display()

    class Meta:
        model = Group
        fields = ['id', 'name', 'category']

class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = ['year', 'price']

class VersionSerializer(serializers.ModelSerializer):
    price_set = PriceSerializer(many=True, read_only=True)
    group = serializers.CharField(source='group.name')
    photo = serializers.CharField(source='photo.url')

    class Meta:
        model = Version
        fields = ['id', 'name', 'photo', 'group', 'price_set']
