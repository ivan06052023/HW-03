from rest_framework import serializers
from rest_framework.serializers import ValidationError
from backend.gallery.serializers import GallerySer
from backend.profiles.serializers import UserSer
from .models import *



class CoordSer(serializers.ModelSerializer):
    """Для вывода сложности"""
    class Meta:
        model = Coords
        fields = (
            "latitude",
            "longitude",
            "height",
        )

class LevelSer(serializers.ModelSerializer):
    """Для вывода сложности"""
    class Meta:
        model = Level
        fields = (
            "name",
        )

class FilterSer(serializers.ModelSerializer):
    """Для вывода сложности"""
    class Meta:
        model = FilterPereval
        fields = (
            "name",
        )

class PerevalListSer(serializers.ModelSerializer):
    """Для вывода новых данных"""
    level = LevelSer()
    coord = CoordSer()
    filters = FilterSer()
    images = GallerySer(read_only=True)
    user = UserSer()

    class Meta:
        model = Pereval_added
        fields = (
            "date_added",
            "status",
            "beautyTitle",
            "user",
            "level",
            "coord",
            "filters",
            "images",
            "slug",
        )

class PerevalDetailSer(serializers.ModelSerializer):
    """Для вывода полных данных о перевале"""
    level = LevelSer()
    coord = CoordSer()
    filters = FilterSer()
    images = GallerySer(read_only=True)
    user = UserSer()

    class Meta:
        model = Pereval_added
        fields = (
            "date_added",
            "status",
            "beautyTitle",
            "title",
            "other_titles",
            "user",
            "level",
            "coord",
            "filters",
            "images",
            "file",
        )

class PerevalCreateSer(serializers.ModelSerializer):
    """Изменение перевала"""
    level = LevelSer()
    coord = CoordSer()
    filters = FilterSer()
    images = GallerySer(read_only=True)
    user = UserSer()

    class Meta:
        model = Pereval_added
        exclude = ('status',)


    def validate(self, attrs):
        print('validator')
        user_data = attrs.get('user')
        if not user_data:
            raise ValidationError("Данные пользователя отсутствуют")

        if self.instance:
            user = self.instance.user
        else:
            try:
                user = User.objects.get(email=user_data.get('email'))
            except User.DoesNotExist:
                user = None

        if user is not None:
            if user.first_name != user_data.get('first_name') or \
                    user.last_name != user_data.get('last_name') or user.middle_name != user_data.get('middle_name') or \
                    user.phone != user_data.get('phone') or user.email != user_data.get('email'):
                raise ValidationError("Информация не может быть изменена")

        super().validate(attrs)

        return attrs

    def create(self, validated_data):

        user_data = validated_data.pop('user')

        coord_data = validated_data.pop('coord')
        coord = CoordSer.objects.create(**coord_data)

        level_data = validated_data.pop('level')
        level = LevelSer.objects.create(**level_data)

        images_data = validated_data.pop('images')
        image = GallerySer.objects.create(**images_data)

        if Pereval_added.objects.filter(user__email=user_data.get('email')).exists():
            user = User.objects.get(email=user_data.get('email')).pk
            pereval = Pereval_added.objects.create(**validated_data, user=User.objects.get(email=user_data.get('email')),
                                             level=level, coord=coord, image=image)
        else:
            user = User.objects.create(**user_data)
            pereval = Pereval_added.objects.create(**validated_data, user=user, level=level, coord=coord, image=image)
        return pereval




