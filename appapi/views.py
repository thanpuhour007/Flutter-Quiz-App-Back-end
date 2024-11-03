from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Quiz, Question, Answer
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        quiz = self.get_object()
        questions = Question.objects.filter(quiz=quiz)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(detail=True, methods=['get'])
    def answers(self, request, pk=None):
        question = self.get_object()
        answers = Answer.objects.filter(question=question)
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

# class UserQuizAttemptViewSet(viewsets.ModelViewSet):
#     queryset = UserQuizAttempt.objects.all()
#     serializer_class = UserQuizAttemptSerializer
#     # permission_classes = [IsAuthenticated]
#
#     @action(detail=False, methods=['post'])
#     def submit_answer(self, request):
#         # user = request.user
#         # if not user.is_authenticated:
#         #     return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
#
#         quiz_id = request.data.get('quiz_id')
#         question_id = request.data.get('question_id')
#         answer_id = request.data.get('answer_id')
#         try:
#             answer = Answer.objects.get(id=answer_id)
#         except Answer.DoesNotExist:
#             return Response({'error': 'Answer does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#         is_correct = answer.is_correct
#
#         attempt, created = UserQuizAttempt.objects.get_or_create(quiz_id=quiz_id)
#         if is_correct:
#             attempt.score += 1
#         attempt.save()
#
#         return Response({'is_correct': is_correct}, status=status.HTTP_200_OK)