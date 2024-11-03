from rest_framework import serializers
from .models import Quiz, Question, Answer

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'question_text']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'answer_text', 'is_correct']

# class UserQuizAttemptSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserQuizAttempt
#         fields = ['id', 'user', 'quiz', 'score', 'attempt_date']