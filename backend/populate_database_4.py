import random
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

# Create sample threads
threads_data = [
    ("up", "Thesis Tips", "Any advice on writing a CS thesis?"),
    ("up", "Best CS Professors", "Who are the best CS professors in UP?"),
    ("up", "CS Electives", "Which CS electives are the most useful?"),
    ("pup", "Professors to Avoid", "Who are the most challenging professors in PUP?"),
    ("pup", "Best Cafeterias", "Where can I find good food on campus?"),
    ("pup", "Dorm Life", "How is dorm life at PUP?"),
    ("tup", "Best Programming Languages", "Which languages are most useful for TUP students?"),
    ("tup", "Machine Shop Guide", "Tips for first-year students using the machine shop."),
    ("tup", "Engineering Clubs", "Which engineering clubs are worth joining?"),
    ("ust", "Dorm Recommendations", "Affordable dorms near UST?"),
    ("ust", "Library Resources", "How to maximize UST’s library resources?"),
    ("ust", "UST Culture Shock", "What surprised you the most about UST?"),
    ("ue", "Exam Week Survival", "How do you prepare for exams?"),
    ("ue", "UE Student Organizations", "What are the most active student organizations?"),
    ("ue", "Best UE Professors", "Who are the most recommended professors?"),
    ("admu", "Internship Opportunities", "Best places for internships in CS?"),
    ("admu", "Jesuit Education", "How does Jesuit education shape Ateneo students?"),
    ("admu", "Study Spots in Ateneo", "Where's the best place to study on campus?"),
    ("feu", "Scholarships in FEU", "Are there any scholarships available?"),
    ("feu", "FEU vs Other Universities", "How does FEU compare to other schools?"),
    ("feu", "FEU Sports", "What are the top sports teams in FEU?"),
    ("dlsu", "Group Study Spots", "Best places to study in DLSU?"),
    ("dlsu", "DLSU Organizations", "Which student organizations are worth joining?"),
    ("dlsu", "DLSU Student Life", "What is student life like at DLSU?"),
    ("pnu", "Teaching Strategies", "What are effective teaching strategies for education students?"),
    ("pnu", "Best Education Professors", "Who are the best professors in PNU?"),
    ("pnu", "Practice Teaching Tips", "Tips for student teachers preparing for practicum."),
    ("g", "Online Learning", "How has online learning affected your studies?"),
    ("g", "Best Study Apps", "What study apps do you use?"),
    ("g", "Mental Health Support", "How do students cope with academic stress?")
]

threads = []
for board_id, title, body in threads_data:
    thread = Thread.objects.create(
        title=title,
        board=Board.objects.get(board_id=board_id),
        author=random.choice(User.objects.all()),
        body=body
    )
    threads.append(thread)

# Create sample replies
replies_data = [
    ("Thesis Tips", ["Start early and choose a topic you're passionate about!", "Make sure to follow your professor's guidelines.", "Use LaTeX for better formatting."]),
    ("Best CS Professors", ["Prof. Reyes is really good at explaining algorithms.", "Try to get Prof. Santos for database systems.", "Prof. Lim gives challenging but fair exams."]),
    ("CS Electives", ["AI and Data Science are really useful.", "Cybersecurity is a great choice for job opportunities.", "Web development is practical and widely applicable."]),
    ("Professors to Avoid", ["It's not about avoiding, but adapting to their teaching style.", "Some professors are strict but fair.", "Join student forums to get more insights."]),
    ("Best Cafeterias", ["The main cafeteria has the cheapest meals.", "Try the food stalls outside the campus.", "The engineering building has good lunch options."]),
    ("Dorm Life", ["Make sure to set ground rules with your roommates.", "Keep your valuables safe.", "Dorm life teaches you independence."]),
    ("Best Programming Languages", ["Python and JavaScript are solid choices!", "C++ is great for system programming.", "Learn SQL for database management."]),
    ("Machine Shop Guide", ["Always wear safety gear.", "Ask senior students for tips.", "Double-check measurements before cutting materials."]),
    ("Engineering Clubs", ["IEEE and ASME are great for networking.", "Join the robotics club if you love automation.", "Student organizations help you gain practical experience."]),
    ("Dorm Recommendations", ["Try España Grand Residences, it's affordable and near UST.", "Look for dorms with good internet connection.", "Consider sharing a room to cut costs."]),
    ("Library Resources", ["Use the online library catalog.", "Reserve books ahead of time.", "Join study groups for better insights."]),
    ("UST Culture Shock", ["The campus is bigger than expected.", "There's a strong sense of tradition.", "People are very friendly and welcoming."]),
    ("Internship Opportunities", ["Try applying at Globe or Accenture, they take interns.", "Network with alumni for recommendations.", "Look for remote internships if location is an issue."]),
    ("Jesuit Education", ["It emphasizes holistic education.", "There is a strong emphasis on community service.", "Ateneo fosters critical thinking skills."]),
    ("Study Spots in Ateneo", ["The Rizal Library is the best place to focus.", "Some coffee shops near campus have good ambiance.", "Try reserving study rooms for group sessions."]),
    ("Online Learning", ["It has been challenging but also convenient.", "Recorded lectures help with revision.", "Group projects are harder to coordinate online."])
]

for thread_title, body_list in replies_data:
    thread = Thread.objects.get(title=thread_title)
    for body in body_list:
        Reply.objects.create(
            thread=thread,
            author=random.choice(User.objects.all()),
            body=body
        )

image_templates = {
    "up": None,
    "pup": "/images/pup.jpg",
    "tup": "/images/tup.jpg",
    "pnu": "/images/pnu.jpg",
    "ust": "/images/ust.jpg",
    "ue": "/images/ue.jpg",
    "admu": "/images/admu.jpg",
    "dlsu": "/images/dlsu.jpg",
    "g": "/images/cat.JPG",  
    "pol": None, 
    "ph": None, 
}

for thread in Thread.objects.all():
    board_id = thread.board.board_id
    image_path = image_templates.get(board_id)
    if image_path and random.choice([True, False]): 
        thread.img_upload = image_path
    else:
        thread.img_upload = None 
    thread.save()

for reply in Reply.objects.all():
    board_id = reply.thread.board.board_id
    image_path = image_templates.get(board_id)
    if image_path and random.choice([True, False]):
        reply.img_upload = image_path
    else:
        reply.img_upload = None
    reply.save()