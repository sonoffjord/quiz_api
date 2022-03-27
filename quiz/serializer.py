from rest_framework import serializers

from . import models


class QuizSerializer(serializers.ModelSerializer):
    """ Quiz Serializer """

    class Meta:
        model = models.Quizzes
        fields = ['title', ]


class AnswerSerializer(serializers.ModelSerializer):
    """ Answer Serializer """

    class Meta:
        model = models.Answer
        fields = ['id', 'answer_text', 'is_right']


class RandomQuestionSerializer(serializers.ModelSerializer):
    """ Random Question Serializer """

    quiz = QuizSerializer(read_only=True)
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = models.Question
        fields = ['quiz', 'title', 'answer']


class QuestionSerializer(serializers.ModelSerializer):
    """ Question Serializer """

    quiz = QuizSerializer(read_only=True)
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = models.Question
        fields = ['quiz', 'title', 'answer']
