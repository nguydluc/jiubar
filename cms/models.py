from django.db import models

# Create your models here.
from django.db import models

from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"


class Contact(models.Model):
    phone = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField()
    facebook_link = models.URLField(null=True)
    instagram_link = models.URLField()

    def save(self, *args, **kwargs):
        # Check if there's an existing Contact instance
        if Contact.objects.exists():
            # If so, update it instead of creating a new one
            contact = Contact.objects.first()
            contact.phone = self.phone
            contact.address = self.address
            contact.email = self.email
            contact.facebook_link = self.facebook_link
            contact.instagram_link = self.instagram_link
            contact.save()
        else:
            # If not, proceed with normal save
            super(Contact, self).save(*args, **kwargs)


from django.db import models


class TimeSet(models.Model):
    opening = models.CharField(max_length=5)
    closing = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.opening} - {self.closing}"


class OperationHour(models.Model):
    day = models.CharField(max_length=20)
    timesets = models.ManyToManyField(TimeSet)

    def __str__(self):
        return self.day

    class Meta:
        verbose_name = "Operation Hour"
        verbose_name_plural = "Operation Hours"


"""
class Gallery(models.Model):
    image = models.ImageField(upload_to="img/")
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description[:50]

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Gallery"
"""


class Gallery(models.Model):
    image = models.ImageField(upload_to="img/")
    description = models.CharField(max_length=255)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.description[:50]

    def save(self, *args, **kwargs):
        # Call the original save method
        super().save(*args, **kwargs)

        if settings.DEFAULT_FILE_STORAGE == "storages.backends.s3boto3.S3Boto3Storage":
            self.image_url = self.image.url
            self.save(update_fields=["image_url"])

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Gallery"
