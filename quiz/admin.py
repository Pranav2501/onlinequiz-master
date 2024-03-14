from django.contrib import admin

# Register your models here.
from .models import Instructions, Listening, Question,Result,Course,Passage,Email,LongPassage,Exam

admin.site.register(Question)
admin.site.register(Result)
admin.site.register(Course)
admin.site.register(Email)
admin.site.register(Passage)
admin.site.register(LongPassage)
admin.site.register(Instructions)
admin.site.register(Listening)
admin.site.register(Exam)


