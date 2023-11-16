from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

class Coords(models.Model):
    """координаты"""
    latitude = models.FloatField("Широта", null=True, blank=True)
    longitude = models.FloatField("Долгота", null=True, blank=True)
    height = models.IntegerField("Высота", null=True, blank=True)

    class Meta:
        verbose_name = "Координата"
        verbose_name_plural = "Координаты"

class Level(MPTTModel):
    """сложность перевала"""
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='родитель'
    )
    slug = models.SlugField('url', max_length=50)

    def __str__(self):
        return self.name

    class MPTTMeta:
        ordering_insertion_by = ['name']
        verbose_name = 'Сложность'

class FilterPereval(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField('url', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фильтр"
        verbose_name_plural = "Фильтры"


class Pereval_added(models.Model):
    """приложение"""
    date_added = models.DateTimeField()
    status = models.CharField(
        max_length=10,
        choices=[
            ('new', 'Новый'),
            ('pending', 'Ожидает'),
            ('accepted', 'Принято'),
            ('rejected', 'Отклонено')
        ],
        default='new'
    )
    beautyTitle = models.CharField("Наименование", max_length=100, null=True, blank=True)
    title = models.CharField("Заголовок", max_length=100, null=True, blank=True)
    other_titles = models.CharField("Другое название", max_length=100, null=True, blank=True)
    connect = models.CharField("Соединение", max_length=10, default='0', null=True, blank=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    filters = models.ForeignKey(FilterPereval, verbose_name="Фильтр", on_delete=models.CASCADE)
    coord = models.ForeignKey(Coords, verbose_name="Координаты", on_delete=models.CASCADE)
    level = models.ForeignKey(Level, verbose_name="Сложность", null=True, blank=True, on_delete=models.CASCADE)
    images = models.ForeignKey(
        'gallery.Gallery',
        verbose_name="Изображения",
        blank=True, null=True,
        on_delete=models.SET_NULL
    )
    file = models.FileField("Фаил", upload_to="pablic/", blank=True, null=True)
    slug = models.SlugField('url', max_length=50, unique=True)

    def __str__(self):
        return self.beautyTitle

    def get_absolute_url(self):
        return reverse("transition-detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Новое название"
        verbose_name_plural = "Новые названия"


