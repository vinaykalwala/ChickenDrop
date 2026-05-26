from django.db import models


class ContactEnquiry(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('read', 'Read'),
    )

    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='new'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Enquiry"
        verbose_name_plural = "Contact Enquiries"

    def __str__(self):
        return f"{self.full_name} - {self.subject}"

class Offer(models.Model):

    title = models.CharField(
        max_length=200
    )


    image = models.ImageField(
        upload_to='offers/'
    )

    discount = models.CharField(
        max_length=100,
        help_text='Example: 50% OFF'
    )

    description = models.TextField()

    start_date = models.DateField()

    end_date = models.DateField()

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ['-created_at']

    def __str__(self):

        return self.title


class LatestUpdate(models.Model):

    title = models.CharField(
        max_length=255
    )

   

    image = models.ImageField(
        upload_to='updates/',
        blank=True,
        null=True
    )

    short_description = models.TextField()

    description = models.TextField()

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ['-created_at']

    def __str__(self):

        return self.title