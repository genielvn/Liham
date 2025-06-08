from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=100)
    university_id = models.CharField(max_length=10, primary_key=True)

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'

    def __str__(self):
        return self.name

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='profile/')
    profile_banner = models.ImageField(null=True, blank=True, upload_to='banner/')
    is_admin = models.BooleanField(default=False) 
    is_banned = models.BooleanField(default=False) 

    class Meta:
        verbose_name = 'User'

    def __str__(self):
        return self.username
    
class Board(models.Model):
    board_id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(default="A board.", max_length=100, blank=True) # Can be a motto of the university or a simple description of the board.
    created_at = models.DateTimeField(auto_now_add=True)

    # TODO: Add sorting using class Meta

    class Meta:
        verbose_name = 'Board'

    def __str__(self):
        return self.name

class Thread(models.Model):
    title = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True, blank=True)
    img_upload = models.ImageField(null=True, blank=True, upload_to='images/')
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # TODO: Add sorting using class Meta

    class Meta:
        verbose_name = 'Thread' # no need for verbose_name_plural (automatic + 's')

    def __str__(self):
        return f'[T] {self.author.username}: {self.title}'

class Reply(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=False, blank=False)
    img_upload = models.ImageField(null=True, blank=True, upload_to='images/')
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # TODO: Add sorting using class Meta

    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'

    def __str__(self):
        return f'[R] {self.author.username} to {self.thread.id}: {self.body}'
    
