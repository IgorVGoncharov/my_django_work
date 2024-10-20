from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import hello, HelloView
from .views import year_post, MonthPost, post_detail
from .views import my_view
from .views import TemplIf, add_category
from .views import view_for, index, about
from .views import author_posts, add_recipe, one_recipe
from .views import user_form, many_fields_form, add_user, upload_image, recipes_category_form
from .views import registration, user_login, one_category


urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('posts/<int:year>/', year_post, name='year_post'),
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
    #path('', my_view, name='index'),
    path('if/', TemplIf.as_view(), name='temp_Lif'),
    path('for/', view_for, name='templ_for'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('author/<int:author_id>/', author_posts, name='author_posts'),
    #path('post/<int:post_id>/', post_full, name='post_full'),
    path('user/add/', user_form, name='user_form'),
    path('category/', add_category, name='add_category_recipes'),# Готово
    path('recipe/', add_recipe, name='add_recipe'),# Готово
    path('user/', add_user, name='add_user'),#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    path('upload/', upload_image, name='upload_image'),
    path('user/registration/', registration, name='registration'), #регистрация, готово
    path('user/login/', user_login.as_view(), name='login'),#авторизация, готово
    path('recipe/<int:recipe_id>/', one_recipe, name='one_recipe'),#отдельный рецепт
    path('category/<int:category_id>/', one_category, name='one_category'),#отдельная категрия


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('about/', views.about, name='about'),
#     path('recipes/', views.recipes, name='Рецепты'),
# ]