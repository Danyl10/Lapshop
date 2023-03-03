from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Laptop(models.Model):
    title = models.CharField(max_length=250)
    price = models.FloatField()
    is_sale = models.BooleanField(default=False)
    discount = models.IntegerField(blank=True, null=True)
    CPU = models.CharField(max_length=250)
    RAM = models.FloatField()
    video_card = models.CharField(max_length=250)
    nucleis = models.FloatField(null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default="", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_price(self):
        if self.is_sale:
            return round(self.price * (1 - self.discount / 100), 2)
        else:
            return self.price

    def get_rates(self):
        all_comments = Comment.objects.filter(book=self)
        rates = [c.rate for c in all_comments]
        if rates:
            return round(statistics.mean(rates), 2)
        else:
            return ''


class Comment(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    text = models.TextField(max_length=1500)
    rate = models.IntegerField()

    def __str__(self):
        return '{} :  {}'.format(self.author, self.text)


class Post(models.Model):
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    text = models.TextField(max_length=1500)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)

    def __str__(self):
        return '{} :  {}'.format(self.author, self.text)
