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
    ("pol", "Politics", "Philippine Politics ba talaga?"),
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
users_data = [
    ("SmiliePop", "pup", "Testing", True),
    ("lezzthanthree", "pup", "Testing", False),
    ("CodeCracker", "up", "password123", False),
    ("BugHunter", "tup", "password123", False),
    ("SyntaxSamurai", "ust", "password123", False),
    ("NullPointer", "admu", "password123", False),
    ("DebuggerDude", "feu", "password123", False)
]

users = []
for username, uni_id, password, is_admin in users_data:
    user = User.objects.create(
        username=username,
        university=University.objects.get(university_id=uni_id),
        password=make_password(password),
        is_admin=is_admin
    )
    users.append(user)

# Generate Threads and Replies Specific to University Boards
thread_templates = {
    "up": ["How to ace UPCAT?", "UP Lantern Parade Tips"],
    "pup": ["PUP: Tanglaw ng Bayan or Tanglag ng Bayan?", "Best tambayan spots in PUP"],
    "tup": ["Top engineering challenges in TUP", "Is TUP really Haligi ng Bayan?"],
    "pnu": ["PNU education tips", "Favorite PNU traditions"],
    "ust": ["UST Paskuhan: What to expect", "Surviving quadricentennial exams"],
    "ue": ["UE sports fest highlights", "Life in Recto: Myth or reality?"],
    "admu": ["Why Ateneo Blue Eagles soar high", "Best orgs in Ateneo"],
    "dlsu": ["Green Archers’ secret strategies", "Balancing academics and Lasallian traditions"],
    "feu": ["FEU's love for the environment", "Best tambayan spots in FEU"],
    "g": ["General knowledge trivia", "Funny moments in student life"],
    "pol": ["Philippine politics: A discussion", "Why every vote matters"],
    "ph": ["Best tourist spots in the Philippines", "How to promote local culture"]
}

reply_templates = [
    "This is so true!",
    "I can’t agree more.",
    "Thanks for the insights!",
    "This made my day!",
    "Interesting perspective."
]

image_templates = [
    None,
    None,
    None,
    None,
    None,
    "/images/up.jpg",
    "/images/pup.jpg",
    "/images/tup.jpg",
    "/images/pnu.jpg",
    "/images/ust.jpg",
    "/images/ue.jpg",
    "/images/admu.jpg",
    "/images/dlsu.jpg",
    "/images/cat.JPG",
]

for board in Board.objects.all():
    threads = thread_templates.get(board.board_id, ["Random topic for this board"])
    for title in threads:
        thread = Thread.objects.create(title=title,board=board,author=random.choice(users),body=f"Discussing {title.lower()} for {board.name}.", img_upload=random.choice(image_templates))
        for _ in range(5):
            Reply.objects.create(thread=thread,author=random.choice(users),body=random.choice(reply_templates), img_upload=random.choice(image_templates))

print("University-specific threads and replies generated successfully!")
