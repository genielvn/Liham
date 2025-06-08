from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('b/', views.boards_list, name='boards-list'),
    path('f/', views.feed, name='feed'),
    path('b/create/', views.create_board, name='create-board'),  # POST to create a thread
    path('b/<str:board_id>/', views.threads_list, name='threads-list'),
    path('b/<str:board_id>/details', views.board_details, name='board-details'),
    path('b/<str:board_id>/<int:thread_id>/', views.thread_detail, name='thread-detail'),
    path('b/<str:board_id>/<int:thread_id>/delete/', views.delete_thread, name='delete_thread'),
    path('b/<str:board_id>/create/', views.create_thread, name='create-thread'),  # POST to create a thread
    path('b/<str:board_id>/<int:thread_id>/replies/', views.replies_list, name='replies-list'),
    path('b/<str:board_id>/<int:thread_id>/edit/', views.edit_thread, name='edit-thread'),
    path('u/', views.user_data, name='user-data'),
    path('u/<str:username>/', views.user_data, name='user-data'),
    path('u/<str:username>/ban/', views.ban_user, name='ban_user'),
    path('s/upload-profile-picture/', views.upload_profile_picture, name='upload-profile-picture'),
    path('s/upload-banner/', views.upload_banner, name='upload-banner'),
    path("s/delete-account/", views.delete_account, name="delete_account"),
    path('b/<str:board_id>/<int:thread_id>/reply/', views.create_reply, name='create-reply'),  # POST to create a reply
    path('auth/login/', views.login, name="login"),
    path('auth/signup/', views.signup, name="signup"),
    path('auth/verify/', views.verify_token, name='verify'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('replies/<int:reply_id>/delete/', views.delete_reply, name='delete_reply'),
    path('universities/', views.university_list, name='university-list'),
]