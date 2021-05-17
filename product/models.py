from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    image = models.ImageField(upload_to='product/',null=True,blank=True,verbose_name='Изображение')
    weight = models.IntegerField(verbose_name='Вес, в граммах',null=True,)
    length = models.IntegerField(verbose_name='Длина, в сантиметрах',null=True)
    width = models.IntegerField(verbose_name='Ширина, в сантиметрах',null=True)
    height = models.IntegerField(verbose_name='Высота, в сантиметрах',null=True)

    def __str__(self):
        return self.name