from django.db import models
import datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
# Create your models here.

class movie_type(models.Model):
    t_name = models.CharField(max_length=200)

    def __str__(self):
        return self.t_name

class movie_language(models.Model):
    lan = models.CharField(max_length=200)

    def __str__(self):
        return self.lan

class movie_rating_type(models.Model):
    rate_type = models.CharField(max_length=200)

    def __str__(self):
        return self.rate_type

class Client(User):
    c_user = models.ForeignKey(User, related_name="+",  blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,  null=True, blank=True)
    locality = models.CharField(max_length=200, default='Canada', blank=True, null=True)
    city = models.CharField(max_length=50, default='xyz', blank=True)
    zipcode = models.CharField(max_length=50,  null=True, blank=True)
    u_contact = models.IntegerField(null=True, blank=True, )

    def __str__(slef):
        return slef.first_name + " " + slef.last_name

class movie(models.Model):
    m_name = models.CharField(max_length=200)
    m_relasedate = models.DateTimeField(auto_now=False)
    gen = [('B', 'Bollywood'), ('H', 'Hollywood')]
    movie_ge = models.CharField(max_length=2, choices=gen, default='H')
    m_type = models.ForeignKey(movie_type, related_name='types', on_delete=models.CASCADE)
    #m_lan = models.CharField(max_length=2, choices=m_Language)
    m_o_lan = models.ForeignKey(movie_language, related_name='language', on_delete=models.CASCADE)
    #m_lan = models.ForeignKey(movie_language, related_name='language', on_delete=models.CASCADE)
    dubbed = [('Y', 'Yes'), ('N', 'No')]
    m_dubbed = models.CharField(max_length=2, choices=dubbed, default='N')
    m_writer = models.CharField(max_length=200)
    m_trailer = models.CharField(max_length=200)  #video pending
    m_img = models.ImageField(null=True, blank=True, upload_to="mimages")
    m_on = models.BooleanField(default=True)
    m_price = models.FloatField()
    m_discount = models.FloatField( blank=True, null=True,)

    def __str__(movie):
        return movie.m_name

class m_rating(models.Model):
    movie_data = models.ForeignKey(movie, related_name='movie_name', on_delete= models.CASCADE)
    client = models.ForeignKey(Client, related_name='user_name', on_delete=models.CASCADE)
    rate = [('1', '*'), ('2', '**'), ('3', '***'), ('4', '****'), ('5', '*****')]
    m_rate = models.ForeignKey(movie_rating_type, related_name='language', on_delete=models.CASCADE)
    rate_date = models.DateField()

    def __str__(m_rating):
        return movie.m_name + "  " + "Ratings:" + m_rating.m_rate

class OrderItem(models.Model):
    movie_order = models.ForeignKey(movie, related_name='movie_order', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, related_name='order_user', on_delete=models.CASCADE,  blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    movie = models.ForeignKey(movie, on_delete=models.CASCADE,  blank=True, null=True)
    order_item = models.PositiveIntegerField(default=1)
    status = [('0', 'Cancelled Order'), ('1', 'Placed Order'), ('2', 'Shipped Order'), ('3', 'Delieverd Order')]
    order_status = models.CharField(max_length=20 , choices=status, default='1')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(slef):
        return slef.user_id
        #return slef.client.first_name

    def total_price(self):
        return movie.price * OrderItem.order_item

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    o_movie = models.ForeignKey(movie, on_delete=models.CASCADE)
    o_quantity = models.PositiveIntegerField(default=1)

    def __str__(slef):
        return slef.user + slef.o_movie
