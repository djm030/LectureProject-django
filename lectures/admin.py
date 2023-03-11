from django.contrib import admin
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
                    "user",
                    "categories",
                )
            },
        ),
    )


@admin.register(calculatedLecture)
class calculatedLectureAdmin(admin.ModelAdmin):
    pass
