from django.contrib import admin

from .models import RecipeRequirement, MenuItem, Ingredient, Purchase

admin.site.register(RecipeRequirement)
admin.site.register(Ingredient)
admin.site.register(Purchase)
admin.site.register(MenuItem)
