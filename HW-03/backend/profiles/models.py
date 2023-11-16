from django.contrib.auth.models import User
from django.db import models # reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from PIL import Image
import os

def get_path_upload_avatar(instance,file):
    """путь к аватару пользователя"""
    time = timezone.now().strftime("%Y-%m-%d")
    end_extention = file.split('.')[-1]
    head = file.split('.')[0]
    if len(head) >10:
        head = head[:10]
    file_name =  head + '_' + time + '.' + end_extention
    return os.path.join('profile_pics','user_{0},{1}').format(instance.user.id, file_name)

class Profile(models.Model):
    """модель пользователя"""
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    avatar = models.ImageField("Аватар", upload_to="profiles/", null=True, blank=True)
    email_two = models.EmailField("Почта 2", primary_key=True, default=1)
    phone = models.CharField("Телефон", max_length=25)
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    middle_name = models.CharField("Отчество", max_length=50, null=True, blank=True)
    slug = models.SlugField("url", max_length=50, default='')

    def __str__(self):
        return self.first_name

    @property
    def get_avatar_url(self):
        if self.avatar:
            return '/media/{}'.format(self.avatar)
        else:
            return '/static/img/no_photo.jpg'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.avatar:
            print("avatar detected")
            img = Image.open(self.avatar.path)
            if img.height > 150 or img.width > 150:
                output_size = (150, 150)
                img.thumbnail(output_size)
                img.save(self.avatar.path)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Используем сигналы"""
    """Создание профиля пользователя при регистрации"""
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    instance.profile.save()