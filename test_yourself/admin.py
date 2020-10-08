from django.contrib import admin
from .models import UserProfile
from .models import  Category,MCQQuestion, Answer,Subcat

# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('category', )

class SubcatAdmin(admin.ModelAdmin):
    search_fields = ('subcat', )


class MCQuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'category','subcat',)
    list_filter = ('category','subcat',)
    fields = ('content', 'category','subcat',
               'explanation')

    search_fields = ('content', 'explanation')


    inlines = [AnswerInline]


admin.site.register(UserProfile)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcat, SubcatAdmin)
admin.site.register(MCQQuestion, MCQuestionAdmin)
