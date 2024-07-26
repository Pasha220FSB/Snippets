from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views


from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name='snippets-add'),
    path('snippets/list', views.snippets_page, name='snippets-list'),
    path('snippets/<int:snippet_id>', views.snippet_detail, name='snippet-detail'),
    path('snippets/delete/<int:snippet_id>', views.delete_snippet, name='delete-snippet'),
    path('snippets/update/<int:snippet_id>', views.update_snippet, name='update-snippet'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register', views.creat_user, name='register'),
    path('snippets/my_list', views.my_snippets_page, name='my-snippets-list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
