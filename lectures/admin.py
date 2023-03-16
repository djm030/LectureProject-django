from django.contrib import admin
from .models import Lecture, CalculatedLecture


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
                    "instructor",
                    "categories",
                    "grade",
                )
            },
        ),
    )


@admin.register(CalculatedLecture)
class CalculatedLectureAdmin(admin.ModelAdmin):
    pass
