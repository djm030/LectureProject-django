from django.contrib import admin
from .models import Lecture, CalculatedLecture
from videos.models import Video


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


class VideoInline(admin.StackedInline):
    model = Video
    fields = [
        "title",
        "description",
        "videoFile",
        "videoLength",
    ]


@admin.register(CalculatedLecture)
class CalculatedLectureAdmin(admin.ModelAdmin):
    fields = [
        "lecture",
    ]
    inlines = [
        VideoInline,
    ]


admin.site.register(Video)
