import random
from django.contrib.auth.hashers import make_password
from api.models import Board, Thread, User, University, Reply

# Create Boards
boards_data = [
    ("up", "University of The Philippines", "Honor, Excellence, Service"),
    ("pup", "Polytechnic University of The Philippines", "Tanglaw ng Bayan"),
    ("tup", "Technological University of the Philippines", "Haligi ng Bayan"),
    ("pnu", "Philippine Normal University", "Truth. Excellence. Service."),
    ("ust", "University of Santo Tomas", "Veritas in Caritate"),
    ("ue", "University of the East", "Tomorrow Begins in the East"),
    ("admu", "Ateneo de Manila University", "Lux in Domino"),
    ("dlsu", "De La Salle College", "Religio, Mores, Cultura"),
    ("feu", "Far Eastern University", "Love of Fatherland and God"),
    ("g", "General Discussions", "Discussions that are outside universities"),
    ("pol", "Politics", "Philippine Politcs ba talaga?"),
    ("ph", "Philippines", "Perlas ng Silanganan.")
]

for board_id, name, description in boards_data:
    Board.objects.create(board_id=board_id, name=name, description=description).save()

# Create Universities
universities_data = [
    ("up", "University of The Philippines"),
    ("pup", "Polytechnic University of The Philippines"),
    ("tup", "Technological University of the Philippines"),
    ("pnu", "Philippine Normal University"),
    ("ust", "University of Santo Tomas"),
    ("ue", "University of the East"),
    ("admu", "Ateneo de Manila University"),
    ("dlsu", "De La Salle College"),
    ("feu", "Far Eastern University")
]

for university_id, name in universities_data:
    University.objects.create(university_id=university_id, name=name).save()

# Create Users
uni = University.objects.get(university_id="pup")
users_data = [
    ("SmiliePop", uni, "Testing", True),
    ("lezzthanthree", uni, "Testing", False)
]

for username, university, password, is_admin in users_data:
    user = User.objects.create(
        username=username,
        university=university,
        password=make_password(password),
        is_admin=is_admin
    )
    user.save()

# Generate additional accounts, threads, and replies
users = []
usernames = ["CodeCracker", "BugHunter", "SyntaxSamurai", "NullPointer", "DebuggerDude"]
password = make_password("password123")

for username in usernames:
    user = User.objects.create(
        username=username,
        university=random.choice(University.objects.all()),
        password=password,
        is_admin=False
    )
    users.append(user)

thread_titles = [
    "Why do programmers prefer dark mode?",
    "What’s a programmer’s favorite hangout place?",
    "How do you comfort a JavaScript bug?",
    "Why did the programmer quit his job?",
    "What’s the object-oriented way to become wealthy?"
]

thread_bodies = [
    "Because light attracts bugs!",
    "Foo Bar!",
    "You console it.",
    "Because he didn’t get arrays (a raise).",
    "Inheritance!"
]

reply_bodies = [
    "This cracked me up!",
    "I can totally relate!",
    "Haha, that’s hilarious!",
    "Good one!",
    "Absolutely true!"
]

boards = Board.objects.all()
for board in boards:
    num_threads = random.randint(2, 5)
    for _ in range(num_threads):
        thread = Thread.objects.create(title=random.choice(thread_titles),board=board,author=random.choice(users),body=random.choice(thread_bodies))

        for _ in range(5):
            Reply.objects.create(thread=thread,author=random.choice(users),body=random.choice(reply_bodies))

print("Generated users, threads, and replies successfully!")
