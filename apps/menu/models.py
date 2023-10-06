from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', blank=False, null=False)
    slug = models.SlugField(unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name

    @property
    def upper_items(self):
        return MenuItem.objects.filter(menu=self, parent=None)

        
class MenuItem(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', blank=False, null=False)
    # To use named url write 'named_url:url_name'
    url = models.CharField(max_length=255, null=True, blank=True, verbose_name='URL')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children', verbose_name='Родитель')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Меню', related_name='menu_items')

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'

    def __str__(self):
        return self.name
