from django.db import connection, reset_queries
from .models import Course

def naive_query():
    reset_queries()
    courses = Course.objects.all()

    for c in courses:
        print(c.instructor.username)
        for l in c.lessons.all():
            print(l.title)

    print("Total Query:", len(connection.queries))


def optimized_query():
    reset_queries()
    courses = Course.objects.select_related('instructor').prefetch_related('lessons')

    for c in courses:
        print(c.instructor.username)
        for l in c.lessons.all():
            print(l.title)

    print("Total Query:", len(connection.queries))