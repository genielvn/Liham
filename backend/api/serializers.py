from rest_framework import serializers
from .models import Board, Thread, Reply, User, University

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['board_id', 'name', 'description', 'created_at']

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'profile_banner', 'profile_picture', 'university']

class UserSerializer(serializers.ModelSerializer):
    university = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['username', 'profile_banner', 'profile_picture', 'university', "is_banned", "is_admin"]

    def get_university(self, obj):
        return University.objects.get(university_id=obj.university.university_id).name


class ThreadSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)
    reply_count = serializers.SerializerMethodField(read_only=True)
    board_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Thread
        fields = ['id', 'title', 'board', 'board_name', 'body', 'reply_count', 'img_upload', 
                  'is_deleted', 'created_at', 'modified_at', 'updated_at', 'author']

    def create(self, validated_data):
        return super().create(validated_data)
    
    def get_reply_count(self, obj):
        return Reply.objects.filter(thread=obj).count()
    
    def get_board_name(self, obj):
        return obj.board.name
    
    def get_author(self, obj):
        return User.objects.get(id=obj.author.id).username if obj.author else "Anonymous"
    
class PostThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ['id', 'title', 'board', 'body', 'img_upload', 
                  'is_deleted', 'created_at', 'modified_at', 'updated_at', 'author']

    def create(self, validated_data):
        return super().create(validated_data)


class ReplySerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)
    thread_title = serializers.SerializerMethodField(read_only=True)
    board = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Reply
        fields = ['id', 'thread', 'body', 'img_upload', 
                  'is_deleted', 'created_at', 'modified_at', 'author', 'thread_title', 'board']

    def create(self, validated_data):
        # Perform additional validation or customization here if 
        return super().create(validated_data)
    
    def get_author(self, obj):
        return User.objects.get(id=obj.author.id).username if obj.author else "Anonymous"
    
    def get_thread_title(self, obj):
        return obj.thread.title
    
    def get_board(self, obj):
        return obj.thread.board_id
    

class PostReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'thread', 'body', 'img_upload', 
                  'is_deleted', 'created_at', 'modified_at', 'author']
        
    def create(self, validated_data):
        return super().create(validated_data)
    
