from rest_framework import serializers
from .models import *


class PhotoSer(serializers.ModelSerializer):
    """Для вывода изображения"""
    class Meta:
        model = Photo
        fields = (
            "image",
        )


class GallerySer(serializers.ModelSerializer):
    """Для вывода галереи"""
    photos = PhotoSer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = (
            "photos",
        )


