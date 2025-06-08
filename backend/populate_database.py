from django.db import migrations
from django.contrib.auth.hashers import make_password

def populate_initial_data(apps, schema_editor):
    Board = apps.get_model("api", "Board")
    University = apps.get_model("api", "University")
    User = apps.get_model("api", "User")

    # Create Boards
    boards = [
        {"board_id": "up", "name": "University of The Philippines", "description": "Honor, Excellence, Service"},
        {"board_id": "pup", "name": "Polytechnic University of The Philippines", "description": "Tanglaw ng Bayan"},
        {"board_id": "tup", "name": "Technological University of the Philippines", "description": "Haligi ng Bayan"},
        {"board_id": "pnu", "name": "Philippine Normal University", "description": "Truth. Excellence. Service."},
        {"board_id": "ust", "name": "University of Santo Tomas", "description": "Veritas in Caritate"},
        {"board_id": "ue", "name": "University of the East", "description": "Tomorrow Begins in the East"},
        {"board_id": "admu", "name": "Ateneo de Manila University", "description": "Lux in Domino"},
        {"board_id": "dlsu", "name": "De La Salle College", "description": "Religio, Mores, Cultura"},
        {"board_id": "feu", "name": "Far Eastern University", "description": "Love of Fatherland and God"},
        {"board_id": "g", "name": "General Discussions", "description": "Discussions that are outside universities"},
        {"board_id": "pol", "name": "Politics", "description": "Philippine Politcs ba talaga?"},
        {"board_id": "ph", "name": "Philippines", "description": "Perlas ng Silanganan."},
    ]
    for board in boards:
        Board.objects.create(**board)

    # Create Universities
    universities = [
        {"university_id": "up", "name": "University of The Philippines"},
        {"university_id": "pup", "name": "Polytechnic University of The Philippines"},
        {"university_id": "tup", "name": "Technological University of the Philippines"},
        {"university_id": "pnu", "name": "Philippine Normal University"},
        {"university_id": "ust", "name": "University of Santo Tomas"},
        {"university_id": "ue", "name": "University of the East"},
        {"university_id": "admu", "name": "Ateneo de Manila University"},
        {"university_id": "dlsu", "name": "De La Salle College"},
        {"university_id": "feu", "name": "Far Eastern University"},
    ]
    for uni in universities:
        University.objects.create(**uni)

    # Create Users
    pup_university = University.objects.get(university_id="pup")
    sp = User.objects.create(
        username="sp",
        university=pup_university,
        password=make_password("Testing"),
        is_admin=True,
    )
    le = User.objects.create(
        username="le",
        university=pup_university,
        password=make_password("Testing"),
        is_admin=False,
    )
    sp.save()
    le.save()

class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),  # Replace with your actual initial migration
    ]

    operations = [
        migrations.RunPython(populate_initial_data),
    ]
