from django.urls import path
from sample_app import views


app_name = 'sample_app'
urlpatterns = [
    path('post/create/', views.create_post, name='create_post'),  # 作成
    path('post/edit/<int:post_id>/', views.edit_post, name='edit_post'),  # 修正
    path('post/', views.read_post, name='read_post'),   # 一覧表示
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),   # 削除
    path('post/login/', views.login, name='login'),   # ログイン
    path('post/logincheck/<str:parameter>', views.login_check, name='login_check'),   # ログインチェック
]