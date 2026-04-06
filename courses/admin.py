from django.contrib import admin
from .models import User, Category, Course, Lesson, Enrollment, Progress

# =====================
# INLINE LESSON
# =====================
class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1


# =====================
# USER ADMIN
# =====================
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    list_filter = ('role', 'is_staff')
    search_fields = ('username', 'email')


# =====================
# CATEGORY ADMIN
# =====================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)
    list_filter = ('parent',)


# =====================
# COURSE ADMIN
# =====================
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'category', 'created_at')
    list_filter = ('category', 'instructor')
    search_fields = ('title', 'description')
    inlines = [LessonInline]


# =====================
# LESSON ADMIN
# =====================
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    list_filter = ('course',)
    ordering = ('order',)


# =====================
# ENROLLMENT ADMIN
# =====================
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')
    list_filter = ('course',)
    search_fields = ('student__username',)


# =====================
# PROGRESS ADMIN
# =====================
@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('get_student', 'lesson', 'completed')

    def get_student(self, obj):
        return obj.enrollment.student

    get_student.short_description = 'Student'