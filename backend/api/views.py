from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Board, Thread, Reply, User, University
from .serializers import UserSerializer, BoardSerializer, ThreadSerializer, ReplySerializer, PostThreadSerializer, PostReplySerializer
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from .models import User, University

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    invalid_characters = " !@#$%^&*()+-=[]{}\\|;'\",<.>/?`~"
    data = request.data

    try:
        username = data.get('username', '').strip()
        if not username:
            return Response({"error": "Username is required."}, status=status.HTTP_400_BAD_REQUEST)
        if any(char in invalid_characters for char in username):
            return Response({"error": "Username must not contain whitespaces or symbols."}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists!"}, status=status.HTTP_400_BAD_REQUEST)

        email = data.get('email', '').strip()
        if not email:
            return Response({"error": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({"error": "Email is already in use!"}, status=status.HTTP_400_BAD_REQUEST)

        password = data.get('password', '')
        if not password or len(password) < 8:
            return Response({"error": "Password must be at least 8 characters long."}, status=status.HTTP_400_BAD_REQUEST)

        university_id = data.get('university', '')
        try:
            university = University.objects.get(university_id=university_id)
        except University.DoesNotExist:
            return Response({"error": "Invalid university selection."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password),
            university=university,
        )

        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token

        return Response({
            "token": str(access_token),
            "refresh": str(refresh),
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    data = request.data
    user = authenticate(username=data.get('username'), password=data.get('password'))

    if user is not None:
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token

        return Response({
            "token": str(access_token),
            "refresh": str(refresh),
        }, status=status.HTTP_200_OK)
    
    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([AllowAny])
def university_list(request):
    universities = University.objects.all().values("university_id", "name")
    return Response(list(universities))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def feed(request):
    threads = Thread.objects.all().order_by("-updated_at")[:20]
    thread_serializer = ThreadSerializer(threads, many=True)
    return Response(thread_serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def boards_list(request):
    boards = Board.objects.all()
    serializer = BoardSerializer(boards, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def board_details(request, board_id):
    try:
        board = Board.objects.get(board_id=board_id)
    except Board.DoesNotExist:
        return Response({'error': 'Board not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = BoardSerializer(board)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def threads_list(request, board_id):
    try:
        board = Board.objects.get(board_id=board_id)
    except Board.DoesNotExist:
        return Response({'error': 'Board not found'}, status=status.HTTP_404_NOT_FOUND)

    threads = Thread.objects.filter(board=board).order_by("-updated_at")
    board_serializer = BoardSerializer(board)
    thread_serializer = ThreadSerializer(threads, many=True)

    response_data = {
        "board": board_serializer.data,
        "threads": thread_serializer.data,
    }
    return Response(response_data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def thread_detail(request, board_id, thread_id):
    try:
        board = Board.objects.get(board_id=board_id)
    except Board.DoesNotExist:
        return Response({'error': 'Board not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        thread = Thread.objects.get(id=thread_id, board=board)
    except Thread.DoesNotExist:
        return Response({'error': 'Thread not found'}, status=status.HTTP_404_NOT_FOUND)
    
    board_serializer = BoardSerializer(board)
    thread_serializer = ThreadSerializer(thread)
    response_data = {
        "board": board_serializer.data,
        "thread": thread_serializer.data,
    }

    return Response(response_data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def replies_list(request, board_id, thread_id):
    try:
        board = Board.objects.get(board_id=board_id)
    except Board.DoesNotExist:
        return Response({'error': 'Board not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        thread = Thread.objects.get(id=thread_id, board=board)
    except Thread.DoesNotExist:
        return Response({'error': 'Thread not found'}, status=status.HTTP_404_NOT_FOUND)
    replies = Reply.objects.filter(thread=thread)
    serializer = ReplySerializer(replies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_data(request, username = None):
    try: 
        if username:
            user = User.objects.get(username=username)
        else:
            user = request.user
    except User.DoesNotExist:
        return Response({'error': f'User not found: {username}'}, status=status.HTTP_404_NOT_FOUND)

    
    threads = Thread.objects.filter(author=user).order_by("-created_at")
    replies = Reply.objects.filter(author=user).order_by("-created_at")
    user_serializer = UserSerializer(user)
    thread_serializer = ThreadSerializer(threads, many=True)
    reply_serializer = ReplySerializer(replies, many=True)
    response_data = {
        "user": user_serializer.data,
        "threads": thread_serializer.data,
        "replies": reply_serializer.data
    }
    return Response(response_data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_board(request):
    data = request.data.copy()
    serializer = BoardSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_thread(request, board_id):
    try:
        board = Board.objects.get(board_id=board_id)
    except Board.DoesNotExist:
        return Response({'error': 'Board not found'}, status=status.HTTP_404_NOT_FOUND)

    data = request.data.copy()

    if len(data['title']) > 100:
        return Response({"error": "Title is too long! Please limit to 100 characters."})
    data['board'] = board.board_id
    
    print(data)
    if data['anonymous'] == "false":
        data['author'] = request.user.id
    else:
        data['author'] = None


    serializer = PostThreadSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_reply(request, board_id, thread_id):
    try:
        board = Board.objects.get(board_id=board_id)
    except Board.DoesNotExist:
        return Response({'error': 'Board not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        thread = Thread.objects.get(id=thread_id, board=board)
    except Thread.DoesNotExist:
        return Response({'error': 'Thread not found'}, status=status.HTTP_404_NOT_FOUND)

    data = request.data.copy()
    data['thread'] = thread.id

    if data['anonymous'] == "false":
        data['author'] = request.user.id
    else:
        data['author'] = None

    serializer = PostReplySerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        thread.updated_at = now()
        thread.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_profile_picture(request):
    user = request.user

    if 'profile_picture' in request.FILES:
        user.profile_picture = request.FILES['profile_picture']
        user.save()
        return Response({"message": "Profile picture uploaded successfully."}, status=status.HTTP_200_OK)
    return Response({"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_banner(request):
    user = request.user

    if 'profile_banner' in request.FILES:
        user.profile_banner = request.FILES['profile_banner']
        user.save()
        return Response({"message": "Profile banner uploaded successfully."}, status=status.HTTP_200_OK)
    return Response({"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_thread(request, board_id, thread_id):
    try:
        board = Board.objects.get(board_id=board_id)
    except Board.DoesNotExist:
        return Response({'error': 'Board not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        thread = Thread.objects.get(id=thread_id, board=board)
    except Thread.DoesNotExist:
        return Response({'error': 'Thread not found'}, status=status.HTTP_404_NOT_FOUND)
    if not request.user.is_admin and thread.author != request.user:
        return Response({'error': 'You are not authorized to delete this thread.'}, status=status.HTTP_403_FORBIDDEN)
    thread.delete()
    return Response({'message': 'Thread deleted successfully.'}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_reply(request, reply_id):
    try:
        reply = Reply.objects.get(id=reply_id)
    except Reply.DoesNotExist:
        return Response({'error': 'Reply not found'}, status=status.HTTP_404_NOT_FOUND)

    if not request.user.is_admin and reply.author != request.user:
        return Response({'error': 'You are not authorized to delete this reply.'}, status=status.HTTP_403_FORBIDDEN)

    reply.delete()
    return Response({'message': 'Reply deleted successfully.'}, status=status.HTTP_200_OK)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_account(request):
    try:
        user = request.user
        user.delete()
        return Response({"message": "Account deleted successfully."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": "Failed to delete account.", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ban_user(request, username):
    if not request.user.is_admin:
        return Response({'error': 'Unauthorized. You are not an admin.'}, status=status.HTTP_403_FORBIDDEN)

    try:
        user = get_object_or_404(User, username=username)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    user.is_banned = not user.is_banned
    user.save()

    return Response({'message': 'Toggle ban successfully done'}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_thread(request, board_id, thread_id):
    try:
        board = Board.objects.get(board_id=board_id)
    except Board.DoesNotExist:
        return Response({'error': 'Board not found'}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        thread = Thread.objects.get(id=thread_id, board=board)
    except Thread.DoesNotExist:
        return Response({'error': 'Thread not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.user.is_banned and not request.user.is_admin:
        return Response({'error': 'You are banned from editing threads.'}, status=status.HTTP_403_FORBIDDEN)

    if request.user != thread.author and not request.user.is_admin:
        return Response({'error': 'You are not authorized to edit this thread.'}, status=status.HTTP_403_FORBIDDEN)

        
    data = request.data.copy()
    
    serializer = PostThreadSerializer(thread, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def verify_token(request):
    return Response({"message": "Token is valid", "user": request.user.username}, status=status.HTTP_200_OK)
