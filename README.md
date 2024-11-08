
---

# Flutter Quiz App Backend

A simple backend for a Flutter Quiz App, built with Django REST Framework. This API manages quizzes, questions, and user scores.

## Features

- API for quizzes, questions, and scores

## Getting Started

1. **Clone the repo**:
   ```bash
   git clone https://github.com/yourusername/flutter-quiz-app-backend.git
   cd flutter-quiz-app-backend
   ```

2. **Set up the environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: `env\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the server**:
   ```bash
   python manage.py runserver
   ```

Your API is now live at `http://127.0.0.1:8000/api/`.

## License

Licensed under the MIT License.

---