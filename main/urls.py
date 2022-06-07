from django.urls import path
from .views import main_index, main_about, main_add_post, main_delete_post, main_view_post, \
    main_edit_post, main_cat, main_like
# main_shop, main_support, main_reference, main_training, main_news, main_price,

app_name = "main"

urlpatterns = [
    path('', main_index, name="index"),
    path('cat/<int:pk>/', main_cat, name="cat"),
    path('add-post/', main_add_post, name="add-post"),
    path('delete-post/<int:pk>/', main_delete_post, name="delete-post"),
    path('view/<int:pk>/', main_view_post, name="view"),
    path('edit/<int:pk>/', main_edit_post, name="edit"),
    path('about/', main_about, name="about"),
    path('post/<str:type>/<int:id>/', main_like, name="like"),
    # path('news/', main_news, name="news"),
    # path('shop/', main_shop, name="shop"),
    # path('support/', main_support, name="support"),
    # path('reference/', main_reference, name="reference"),
    # path('training/', main_training, name="training"),
    # path('price/', main_price, name="price"),

]
