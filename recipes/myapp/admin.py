from django.contrib import admin
from .models import Recipes, Recipes_category



@admin.action(description="Очистить поле наименование")
def reset_name(modeladmin, request, queryset):
    queryset.update(name='')


class RecipesAdmin(admin.ModelAdmin):
    """Список рецептов"""
    list_display = ['name', 'description', 'cooking_steps'] #вывод столбцов в админке
    ordering = ['name', 'description'] #порядок сортировки
    list_filter = ['name'] #добавление фильтрации, можно несколько полей
    search_fields = ['name'] #добавление возможности поиска
    search_help_text = 'Поиск по полю название рецепта (name)' #добавление подсказки для поля поиска
    actions = [reset_name]

class CategoryRecipesAdmin(admin.ModelAdmin):
    """Список рецептов"""
    list_display = ['category_name', 'category_description', 'image']  # вывод столбцов в админке


# Register your models here.
admin.site.register(Recipes, RecipesAdmin)
admin.site.register(Recipes_category, CategoryRecipesAdmin)
# admin.site.register(User)
# admin.site.register(Selection)

