import random
from faker import Faker

# from django.contrib.auth.models import User
from lectures.models import Lecture

# "lectureTitle":"Mr",
# "lectureDifficulty":"net",
# "lectureDescription":"Buteo jamaicensis",
# "targetAudience":"Red-tailed hawk",
# "lectureFee":79,
# "thumbnail":"http://dummyimage.com/124x100.png/dddddd/000000",
# "isOpened":true
f = Faker("ko_KR")
for _ in range(100):
    # lectureTitle = f.text()
    # lectureDifficulty = "MIDDLE"
    # lectureDescription = f.texts()
    # targetAudience = f.text()
    # lectureFee = random.randint(0, 100)
    # thumbnail = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLemq_TmWmElWC51jQZYVLoXnUZOLUpdhbro6qO9vR&s"
    # isOpened = True
    Lecture = Lecture.objects.create()
    Lecture.save()
