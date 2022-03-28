from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """ Question category model """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quizzes(models.Model):
    """ Quiz Model """

    category = models.ForeignKey(
        Category,
        default=1,
        on_delete=models.DO_NOTHING
    )
    title = models.CharField(
        max_length=255,
        default=_('New Quiz'),
        verbose_name=_('Quiz Title')
    )
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')
        ordering = ['id']

    def __str__(self):
        return self.title


class Updated(models.Model):
    """ Q&A update model """
    date_updated = models.DateTimeField(
        verbose_name=_('Last Updated'), auto_now=True
    )

    class Meta:
        abstract = True


class Question(Updated):
    """ Question model """
    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert')),
    )

    TYPE = (
        (0, _('Multiple Choice')),
    )

    quiz = models.ForeignKey(
        Quizzes,
        related_name='question',
        on_delete=models.DO_NOTHING
    )
    technique = models.IntegerField(
        choices=TYPE, default=0, verbose_name=_('Type of Question')
    )
    title = models.CharField(max_length=255, verbose_name=_('TItle'))
    difficulty = models.IntegerField(
        choices=SCALE, default=0, verbose_name=_('Difficulty')
    )
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Date Created')
    )
    is_active = models.BooleanField(
        default=False, verbose_name=_('Active Status')
    )

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ['id']

    def __str__(self):
        return self.title


class Answer(Updated):
    """ Answer model """

    question = models.ForeignKey(
        Question,
        related_name='answer',
        on_delete=models.DO_NOTHING
    )
    answer_text = models.CharField(
        max_length=255, verbose_name=_('Answer Text')
    )
    is_right = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')
        ordering = ['id']

    def __str__(self):
        return self.answer_text
