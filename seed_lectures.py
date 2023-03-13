from django_seed import Seed
from lectures.models import Lecture
import random

seeder = Seed.seeder()
seeder.add_entity(
    Lecture, 100
)  # replace 10 with the number of Lecture objects you want to create

seeder = Seed.seeder()
seeder.add_entity(
    Lecture,
    100,
    {
        "lectureTitle": lambda x: seeder.faker.sentence(nb_words=4),
        "lectureDescription": lambda x: seeder.faker.text(),
        "targetAudience": lambda x: seeder.faker.sentence(nb_words=4),
        "lectureDifficulty": "MIDDLE",
        "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLemq_TmWmElWC51jQZYVLoXnUZOLUpdhbro6qO9vR&s",
        "lectureFee": lambda x: random.randint(30, 90),
        "isOpened": True,
    },
)
inserted_pks = seeder.execute()
