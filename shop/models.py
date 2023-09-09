from django.db import models


class Category(models.Model):
    # name of the category
    name = models.CharField(max_length=200)
    # slug field of the category
    # each slug field will be uniques
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        # order categories by name
        ordering = ('name',)
        # to improve database query performance
        indexes: [
            models.Index(fields=['name']),
        ]

        verbose_name = 'category'
        verbose_name_plural = 'categories'
    # when printing an object of this class...
    # return its name

    def __str__(self):
        return self.name


class Product(models.Model):

    # category.products.all()
    # product.category.name

    # many-to-one relationship
    # a category can have multiple products...
    # while each product is associated with one category

    # the category the product is associated with.
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    # name of the product
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    # this image field is optional
    image = models.ImageField('products/%Y/%m/%d', blank=True)
    # description field can be blank - optional
    description = models.TextField(blank=True)
    # price of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # boolean field to check if product is available or not.
    available = models.BooleanField(default=True)
    # date the product was created in the database
    created = models.DateTimeField(auto_now_add=True)
    # date product was updated in the database
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        indexes = [
            # every model specification has an id field...
            # by default
            # so as to improve database query performance.
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created'])
        ]

    def __init__(self):
        return self.name
