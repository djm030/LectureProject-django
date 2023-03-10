from django.contrib import admin
<<<<<<< HEAD
from .models import Lecture

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    pass
=======
from .models import Lecture, calculatedLecture


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = (
        "lectureTitle",
        "lectureDescription",
    )
    fieldsets = (
        (
            "Profle",
            {
                "fields": (
                    "lectureTitle",
                    "lectureDifficulty",
                    "lectureDescription",
                    "targetAudience",
                    "lectureFee",
                    "thumbnail",
                    "lecturePeriod",
                    "isOpened",
                    "lectureDuration",
                    "lectureTotal",
                    "likes",
                )
            },
        ),
    )


@admin.register(calculatedLecture)
class calculatedLectureAdmin(admin.ModelAdmin):
    pass
>>>>>>> 8635767911e5135e624b04e9ca1cd276aa801718
