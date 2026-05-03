from django.db import models


class Category(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='menu_items')

    def __str__(self):
        return self.title


class Booking(models.Model):
    first_name = models.CharField(max_length=255)
    reservation_date = models.DateField()
    reservation_slot = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['reservation_date', 'reservation_slot']
        constraints = [
            models.UniqueConstraint(
                fields=['reservation_date', 'reservation_slot'],
                name='unique_reservation_slot_per_date'
            )
        ]

    def __str__(self):
        return f'{self.first_name} - {self.reservation_date} at {self.reservation_slot}:00'
