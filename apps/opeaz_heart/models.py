from django.db import models


class Groupement(models.Model):
    name = models.CharField(
        max_length=255,
    )


class Pharmacy(models.Model):
    name = models.CharField(
        max_length=255,
    )
    groupement = models.ForeignKey(
        'Groupement',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )


class Laboratory(models.Model):
    name = models.CharField(
        max_length=255,
    )
    code = models.CharField(
        max_length=50,
        unique=True,
    )


class Document(models.Model):
    laboratory = models.ForeignKey(
        'Laboratory',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=255,
    )
    file = models.FileField(
        upload_to='documents/',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class Flyer(models.Model):
    laboratory = models.ForeignKey(
        'Laboratory',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=255,
    )
    image = models.ImageField(
        upload_to='flyers/',
    )
    start_at = models.DateField()
    end_at = models.DateField()


class CommercialCondition(models.Model):
    laboratory = models.ForeignKey(
        'Laboratory',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=255,
    )
    text = models.TextField()
    year = models.PositiveSmallIntegerField()
