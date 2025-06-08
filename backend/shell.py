from django.contrib.auth.hashers import make_password
from api.models import Board, Thread, User, University, Reply

Board.objects.create(board_id="up", name="University of The Philippines", description="Honor, Excellence, Service").save()
Board.objects.create(board_id="pup", name="Polytechnic University of The Philippines", description="Tanglaw ng Bayan").save()
Board.objects.create(board_id="tup", name="Technological University of the Philippines", description="Haligi ng Bayan").save()
Board.objects.create(board_id="pnu", name="Philippine Normal University", description="Truth. Excellence. Service.").save()
Board.objects.create(board_id="ust", name="University of Santo Tomas", description="Veritas in Caritate").save()
Board.objects.create(board_id="ue", name="University of the East", description="Tomorrow Begins in the East").save()
Board.objects.create(board_id="admu", name="Ateneo de Manila University", description="Lux in Domino").save()
Board.objects.create(board_id="dlsu", name="De La Salle College", description="Religio, Mores, Cultura").save()
Board.objects.create(board_id="feu", name="Far Eastern University", description="Love of Fatherland and God").save()
Board.objects.create(board_id="g", name="General Discussions", description="Discussions that are outside universities").save()
Board.objects.create(board_id="pol", name="Politics", description="Philippine Politcs ba talaga?").save()
Board.objects.create(board_id="ph", name="Philippines", description="Perlas ng Silanganan.").save()

University.objects.create(university_id="up", name="University of The Philippines")
uni = University.objects.create(university_id="pup", name="Polytechnic University of The Philippines")
uni.save()
University.objects.create(university_id="tup", name="Technological University of the Philippines").save()
University.objects.create(university_id="pnu", name="Philippine Normal University").save()
University.objects.create(university_id="ust", name="University of Santo Tomas").save()
University.objects.create(university_id="ue", name="University of the East").save()
University.objects.create(university_id="admu", name="Ateneo de Manila University").save()
University.objects.create(university_id="dlsu", name="De La Salle College").save()
University.objects.create(university_id="feu", name="Far Eastern University").save()

sp = User.objects.create(
    username="SmiliePop",
    university=uni,
    password=make_password("Testing"),
    is_admin=True)

sp.save()

le = User.objects.create(
    username="lezzthanthree",
    university=uni,
    password=make_password("Testing"),
    is_admin=False
)

le.save()