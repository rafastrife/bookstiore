from django.db import models


# Create your models here.

class ModelBase(models.Model):
    id = models.AutoField(
        db_column='id',
        null=False,
        primary_key=True
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )
    created_at = models.DateTimeField(
        db_column='dt_created_at',
        null=False,
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified_at',
        null=True,
        auto_now=True
    )

    class Meta:
        abstract = True


class Category(ModelBase):
    description = models.CharField(
        db_column='tx_description',
        null=False,
        max_length=104
    )

    class Meta:
        db_table = 'category'
        managed = True


class Book(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=104
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.DO_NOTHING,
        db_column='id_category',
        null=False,
        db_index=False
    )
    description = models.TextField(
        db_column='tx_description',
        null=False
    )

    class Meta:
        db_table = 'book'
        managed = True
        indexes = [
            models.Index(fields=['category'])
        ]
