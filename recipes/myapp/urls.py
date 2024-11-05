from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import registration, user_login, one_category, all_recipes, recipe_full, five_recipes, add_rec_confirm
from .views import logout_view, UpdateRecipe, all_categorys, one_recipe, recipes_by_category, change_rec_confirm
# from .views import AddRecipe
from .views import add_recipe, user_check, add_user_confirm

urlpatterns = [
    # path('logout/', index, name='index'),
    # path('index/', index, name='index'),
    path('', five_recipes, name='five_recipes'),#основная страница, пять случайных рецептов
    path('all_recipes/', all_recipes, name='all_recipes'),#все рецепты
    path('all_categorys/', all_categorys, name='all_categorys'),#пять случайных рецептов
    # path('add_recipe/', AddRecipe.as_view(), name='add_recipe'),#добавление рецепта
    path('user/registration/', registration, name='registration'), #регистрация, готово
    path('user/login/', user_login.as_view(), name='login'),#авторизация, готово
    path('user/logout/', logout_view, name='logout'),
    path('edit/<int:pk>/', UpdateRecipe.as_view(), name='edit_page'),#правка рецпета
    path('recipe/<int:recipe_id>/', recipe_full, name='recipe_full'),  # ссылка на отдельный рецепт
    path('category/<int:category_id>/', one_category, name='one_category'),  # отдельная категрия
    path('recipe/<int:recipe_id>/', one_recipe, name='one_recipe'),#отдельный рецепт
    path('recipe_by_cat/<int:category_id>/', recipes_by_category, name='recipes_by_category'),
    path('add_rec_confirm/', add_rec_confirm, name='add_rec_confirm'),
    path('change_rec_confirm/', change_rec_confirm, name='change_rec_confirm'),
    path('add_user_confirm/', add_user_confirm, name='add_user_confirm'),
    path('add_recipe/', add_recipe, name='add_recipe'),#добавление рецепта
    path('user_check/<int:recipe_id>/', user_check, name='user_check'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
