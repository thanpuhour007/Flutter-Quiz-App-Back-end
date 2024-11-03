from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Quiz(models.Model):
    title = models.CharField(max_length=200, verbose_name="Quiz Title", help_text="The title of the quiz")

    class Meta:
        db_table = 'Quiz'
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"
        ordering = ['title']

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions', verbose_name="Quiz")
    question_text = models.CharField(max_length=255, verbose_name="Question Text", help_text="The text of the question")

    class Meta:
        db_table = 'Question'
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ['quiz', 'question_text']

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', verbose_name="Question")
    answer_text = models.CharField(max_length=255, verbose_name="Answer Text", help_text="The text of the answer")
    is_correct = models.BooleanField(default=False, verbose_name="Is Correct", help_text="Check if this answer is correct")

    class Meta:
        db_table = 'Answer'
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        ordering = ['question', 'answer_text']

    def __str__(self):
        return self.answer_text


# class UserQuizAttempt(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_attempts', verbose_name="User")
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='attempts', verbose_name="Quiz")
#     score = models.IntegerField(default=0, validators=[MinValueValidator(0)], verbose_name="Score", help_text="The score the user achieved")
#     attempt_date = models.DateTimeField(auto_now_add=True, verbose_name="Attempt Date", help_text="The date and time of the attempt")
#
#     class Meta:
#         db_table = 'UserQuizAttempt'
#         verbose_name = "User Quiz Attempt"
#         verbose_name_plural = "User Quiz Attempts"
#         ordering = ['-attempt_date']
#
#     def __str__(self):
#         return f"{self.user.username}'s attempt on {self.quiz.title}"