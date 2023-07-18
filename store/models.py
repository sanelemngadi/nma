from django.db import models
from django.utils.text import slugify
from users.models import NMAUser

# Create your models here.

days = (
    ("mon", "Monday"),
    ("tue", "Tuesday"),
    ("wed", "Wednesday"),
    ("thur", "Thursday"),
    ("sat", "Saturday"),
    ("sun", "Sunday"),
)

times = (
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9"),
    ("ten", "10"),
    ("eleven", "11"),
    ("twelve", "12"),
)

stamps = (
    ("am", "AM"),
    ("pm", "PM")
)

class WorkingDay(models.Model):
    day = models.CharField(max_length=20, choices=days, unique=True)
    time_in = models.CharField(max_length=10, choices=times)
    time_in_stamp = models.CharField(max_length=3, choices=stamps)
    time_out = models.CharField(max_length=10, choices=times)
    time_out_stamp = models.CharField(max_length=3, choices=stamps)
  
class NMAPageSettings(models.Model):
    workind_days = models.ManyToManyField(WorkingDay)
    company_email = models.EmailField()
    company_cellnumber = models.IntegerField()
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return "NMA Printers"    

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Filter(models.Model):
    name = models.CharField('Product Filter Name', max_length=30, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField('Product Category Name', max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=130, unique=True)
    description = models.TextField()
    available = models.BooleanField(default=True)
    price = models.FloatField(default=0.0)
    ratings = models.FloatField(default=0.0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    the_filter = models.ForeignKey(Filter, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ProductImageVariant(models.Model):
    name = models.CharField(max_length=30, default="image variant")
    image = models.ImageField(upload_to="staticfiles_build/images/product_variations/")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="image_variants")

    def __str__(self):
        return self.name

# many to many relationship for product
class ProductReview(models.Model):
    heading = models.CharField("Review Heading", max_length=100)
    name = models.ForeignKey(NMAUser, on_delete=models.PROTECT)
    date_reviewed = models.DateTimeField(auto_now_add=True)
    review = models.TextField()
    reply = models.TextField(blank=True, null=True)
    replied = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="reviews")

    def __str__(self):
        return self.heading

class Cart(models.Model):
    order = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(NMAUser , on_delete=models.PROTECT)

    def __str__(self):
        return f"{str(self.user)} ordered {str(quantity)} {str(order)}"