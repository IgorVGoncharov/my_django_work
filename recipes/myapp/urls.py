from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import registration, user_login, all_recipes, recipe_full, five_recipes, add_rec_confirm
from .views import logout_view, UpdateRecipe, all_categorys, recipes_by_category, change_rec_confirm
from .views import add_recipe, user_check, add_user_confirm

urlpatterns = [
    path('', five_recipes, name='five_recipes'),
    path('all_recipes/', all_recipes, name='all_recipes'),
    path('all_categorys/', all_categorys, name='all_categorys'),
    path('user/registration/', registration, name='registration'),
    path('user/login/', user_login.as_view(), name='login'),
    path('user/logout/', logout_view, name='logout'),
    path('edit/<int:pk>/', UpdateRecipe.as_view(), name='edit_page'),
    path('recipe/<int:recipe_id>/', recipe_full, name='recipe_full'),
    path('recipe_by_cat/<int:category_id>/', recipes_by_category, name='recipes_by_category'),
    path('add_rec_confirm/', add_rec_confirm, name='add_rec_confirm'),
    path('change_rec_confirm/', change_rec_confirm, name='change_rec_confirm'),
    path('add_user_confirm/', add_user_confirm, name='add_user_confirm'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('user_check/<int:recipe_id>/', user_check, name='user_check'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
