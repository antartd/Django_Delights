from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(max_length=100)
    unit_price = models.FloatField(default=0.00)

    def get_absolute_url(self):
        return "/ingredients"

    def __str__(self):
        return f"""
        {self.name};
        {self.unit};
        {self.quantity};
        {self.unit_price}
        """


class MenuItem(models.Model):
    title = models.CharField(max_length=200, unique=True)
    price = models.FloatField(default=0.00)

    def get_absolute_url(self):
        return "/menu"

    def __str__(self):
        return f"{self.title};{self.price}"

    def available(self):
        return all(X.enough() for X in self.reciperequirement_set.all())


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f"{self.menu_item};{self.ingredient};{self.quantity}"

    def get_absolute_url(self):
        return "/menu"

    def enough(self):
        self.quantity <= self.ingredient.quantity


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu_item};{self.timestamp}"

    def get_absolute_url(self):
        return "/purchases"
