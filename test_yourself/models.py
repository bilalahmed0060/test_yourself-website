from django.db import models
from django.contrib.auth.models import User
import re
from django.utils.translation import ugettext as _
from model_utils.managers import InheritanceManager
import os

# Create your models here.

class UserProfile(models.Model):
    user   = models.OneToOneField(User,on_delete=models.CASCADE)
    ProfilePhoto = models.ImageField(upload_to='UserProfiles')

    def __str__(self):
        return self.user.email

    def extension(self):
        name, extension = os.path.splitext(self.ProfilePhoto.name)
        return extension



class catagories:
    id : int
    name : str
    img : str
    about: str



class CategoryManager(models.Manager):

    def new_category(self, category):
        new_category = self.create(category=re.sub('\s+', '-', category)
                                   .lower())

        new_category.save()
        return new_category


class Category(models.Model):

    category = models.CharField(
        verbose_name=_("Category"),
        max_length=250, blank=True,
        unique=True, null=True)
    catagory_image = models.ImageField(upload_to='Catagories')
    catagory_explanation = models.TextField(max_length=2000,
                                            blank=True,
                                            help_text=_("Explanation to be shown "
                                                        "For the Catagory "),
                                            verbose_name=_('Catagory Explanation'))


    objects = CategoryManager()

    class Meta:
        verbose_name =_("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.category

class SubcatManager(models.Manager):

    def new_subcat(self, subcat):
        new_subcat = self.create(subcat=re.sub('\s+', '-', subcat)
                                   .lower())

        new_subcat.save()
        return new_subcat
class Subcat(models.Model):
    catag = models.ForeignKey(Category,
                              verbose_name=_("Catagory"),
                              blank=True,
                              null=True, on_delete= models.CASCADE)
    subcat = models.CharField(
        verbose_name=_("Sub category"),
        max_length=250, blank=True,
        unique=True, null=True)


    objects = SubcatManager()

    class Meta:
        verbose_name = _("Sub category")
        verbose_name_plural = _("Sub categories")

    def __str__(self):
        return self.subcat





class Question(models.Model):
    """
    Base class for all question types.
    Shared properties placed here.
    """


    category = models.ForeignKey(Category,
                                 verbose_name=_("Category"),
                                 blank=True,
                                 null=True, on_delete=models.CASCADE)
    subcat = models.ForeignKey(Subcat,
                              verbose_name=('Sub category'),
                               null=True, on_delete=models.CASCADE)


    content = models.CharField(max_length=1000,
                               blank=False,
                               help_text=_("Enter the question text that "
                                           "you want displayed"),
                               verbose_name=_('Question'))

    explanation = models.TextField(max_length=2000,
                                   blank=True,
                                   help_text=_("Explanation to be shown "
                                               "after the question has "
                                               "been answered."),
                                   verbose_name=_('Explanation'))

    objects = InheritanceManager()

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['category']

    def __str__(self):
        return self.content


class MCQQuestion(Question):


    def check_if_correct(self, guess):
        answer = Answer.objects.get(id=guess)

        if answer.correct is True:
            return True
        else:
            return False


    def get_answers_list(self):
        return [(answer.id, answer.content) for answer in self.order_answers(Answer.objects.filter(question=self))]

    def answer_choice_to_string(self, guess):
        return Answer.objects.get(id=guess).content

    class Meta:
        verbose_name = "Multiple Choice Question"
        verbose_name_plural = "Multiple Choice Questions"


class Answer(models.Model):
    question = models.ForeignKey(MCQQuestion, verbose_name='Question', on_delete=models.CASCADE)

    content = models.CharField(max_length=1000,
                               blank=False,
                               help_text="Enter the answer text that \
                                            you want displayed",
                               verbose_name="Content")

    correct = models.BooleanField(blank=False,
                                  default=False,
                                  help_text="Is this a correct answer?",
                                  verbose_name="Correct")

    def __str__(self):
        return self.content


    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"



