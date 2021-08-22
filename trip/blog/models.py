from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


CATEGORY_CHOICE = ( 
    ('mountains', 'MOUNTAINS'),
    ('lakesAndRivers', 'LAKES AND RIVERS'),
    ('Gorges', 'GORGES'),
    ('waterfalls', 'WATERFALLS'),
    ('hotSpings', 'HOT SPRINGS'),
    ('equestrian', 'EQUESTIAN'),
    ('cultural', 'CULTURAL'),
    ('season', 'SEASON'),
    ('extreme', 'EXTREME'),
)


point_min = 1
point_max = 10


class Tours(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    price = models.PositiveSmallIntegerField()
    date1 = models.DateField(verbose_name='Start day', null=True, blank=True)
    date2 = models.DateField(verbose_name='End day', null=True, blank=True)
    category = models.CharField(max_length=16, choices=CATEGORY_CHOICE)
    point = models.FloatField(validators=[MinValueValidator(point_min), MaxValueValidator(point_max)])
    img = models.ImageField(upload_to='uploads/', verbose_name='image')
    date_pub = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/tours/{self.id}'

    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'

        ordering = ['-date_pub']

class Review(models.Model):
    full_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    text = models.CharField(max_length=250)
    date_pub = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-date_pub']


