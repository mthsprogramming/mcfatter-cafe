from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce import models as tinymce_models


# Models for the cafe app


class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    used_for = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class BlogPostImage(models.Model):
    image = models.ImageField(upload_to='media/images/cafe/blog')

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return self.image.name





class BlogPost(models.Model):
    post_title = models.CharField(max_length=50)
    post_text = tinymce_models.HTMLField(max_length=10000)
    pub_date = models.DateTimeField('date published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    images = models.ManyToManyField(BlogPostImage, blank=True)

    def __str__(self):
        return self.post_title

    def was_published_recently(self):
        now = timezone.localtime(timezone.now())
        return now - datetime.timedelta(days=7) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class CafeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name="cafeprofile")
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField('birth_date', blank=True, null=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    def recent_order(self):
        return Order.objects.filter(user=self.pk)[:1].get()

    @receiver(post_save, sender=User)
    def ensure_cafeprofile_exists(sender, **kwargs):
        if kwargs.get('created', False):
            CafeProfile.objects.get_or_create(user=kwargs.get('instance'))


class MealType(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    location_name = models.CharField(max_length=50, db_index=True)

    def has_special_today(self):
        for special in Specials.objects.filter(location=1):
            if special.is_special_today():
                return True

        return False

    def get_special(self):
        for special in Specials.objects.filter(location=1):
            if special.is_special_today():
                return special

    def __str__(self):
        return self.location_name

class Specials(models.Model):
    special = models.CharField(max_length=50)
    soup = models.CharField(max_length=50)
    date = models.DateField()
    location = models.ForeignKey(Menu, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name_plural = "specials"

    def is_special_today(self):
        return self.date == timezone.localtime(timezone.now()).date()

    def __str__(self):
        return "{} {}, {} - Special: {}, Soup: {}".format(self.date.month,self.date.day,self.date.year,self.special,self.soup)

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, default=1)
    type = models.ForeignKey(MealType, on_delete=models.CASCADE, default=1)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(max_length=1000)

    # Nutritional fields
    calories = models.IntegerField(default=0)
    fat = models.IntegerField(default=0, blank=True, null=True)
    sat_fat = models.IntegerField(default=0, blank=True, null=True)
    trans_fat = models.IntegerField(default=0, blank=True, null=True)
    protein = models.IntegerField(default=0, blank=True, null=True)
    carbs = models.IntegerField(default=0, blank=True, null=True)
    dietary_fiber = models.IntegerField(default=0, blank=True, null=True)
    sugar = models.IntegerField(default=0, blank=True, null=True)
    sodium = models.IntegerField(default=0, blank=True, null=True)
    cholesterol = models.IntegerField(default=0, blank=True, null=True)
    potassium = models.IntegerField(default=0, blank=True, null=True)

    image = models.ImageField(upload_to='media/images/cafe/menu', blank=True, null=True)
    available = models.BooleanField(default=True)
    extra_options = models.CharField(max_length=100, blank=True, null=True)
    multiple_sizes = models.BooleanField(default=False)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def is_entree(self):
        return self.type.name == 'Entree'

    def is_side(self):
        return self.type.name == 'Side'

    def is_special_today(self):
        return self.name.lower() == Specials.objects.get(date=timezone.localtime(timezone.now()).date()).special.lower() or self.name.lower() == Specials.objects.get(date=timezone.localtime(timezone.now()).date()).soup.lower()

    def __str__(self):
        return self.name


class Order(models.Model):
    time_placed = models.TimeField('time placed')
    is_ready = models.BooleanField(default=False)
    order_for = models.CharField(max_length=50)
    pickup_time = models.DateTimeField('pickup time', blank=True, null=True)
    user = models.ForeignKey(CafeProfile, on_delete=models.CASCADE, blank=True, null=True)
    items = models.TextField(max_length=5000)
    total = models.DecimalField(max_digits=4, decimal_places=2)
    instructions = models.TextField(max_length=5000, blank=True, null=True)

    def __str__(self):
        return self.items


class Ticket(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    ticket_text = models.TextField(max_length=5000)
    user = models.ForeignKey(CafeProfile, on_delete=models.CASCADE, blank=True, null=True)
    complete = models.BooleanField(default=False)
    date = models.DateTimeField('time received')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.subject

    def is_complete(self):
        return self.complete

    is_complete.admin_order_field = 'subject'
    is_complete.boolean = True
    is_complete.short_description = 'Is ticket complete?'