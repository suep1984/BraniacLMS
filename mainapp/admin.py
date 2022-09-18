from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from mainapp import models as mainapp_models
from authapp import models as authapp_models


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["title", "preambule", "body"]


@admin.register(mainapp_models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "get_course_name", "num", "title", "deleted"]
    ordering = ["-course__name", "-num"]
    list_per_page = 10
    list_filter = ["course", "created", "deleted"]
    actions = ["mark_deleted"]

    def get_course_name(self, obj):
        return obj.course.name

    get_course_name.short_description = _("Course")

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")


@admin.register(authapp_models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "age", "email"]
    ordering = ["username"]
