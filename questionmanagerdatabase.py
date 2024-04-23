import requests
import json
import os

class QuestionManager:
    def __init__(self):
        self.questions_file = "questions.json"
        self.questions = self.load_questions()

    def load_questions(self):
        if os.path.exists(self.questions_file) and os.path.getsize(self.questions_file) > 0:
            with open(self.questions_file, "r") as file:
                return json.load(file)
        return []

    def save_questions(self):
        with open(self.questions_file, "w") as file:
            json.dump(self.questions, file, indent=4)

    def _make_request(self, url, data):
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'QuestionManager/1.0',
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def fetch_questions_by_type(self, test_type):
        data_map = {
            'math': {'asmtEventId': 99, 'test': 2, 'domain': 'H,P,Q,S'},
            'reading': {'asmtEventId': 99, 'test': 1, 'domain': 'INI,CAS,EOI,SEC'},
        }
        data = data_map.get(test_type)
        if not data:
            raise ValueError("Invalid test type provided")
        return self._make_request(
            'https://qbank-api.collegeboard.org/msreportingquestionbank-prod/questionbank/digital/get-questions', 
            data
        )

    def refresh_questions(self):
        math_questions = self.fetch_questions_by_type('math')
        reading_questions = self.fetch_questions_by_type('reading')
        self.questions = math_questions + reading_questions
        self.save_questions()

    def get_question_by_id(self, question_id):
        for question in self.questions:
            if question.get('external_id') == question_id:
                return question
        return self._make_request(
            'https://qbank-api.collegeboard.org/msreportingquestionbank-prod/questionbank/digital/get-question', 
            {'external_id': str(question_id)}
        )

    def get_all_questions(self):
        if not self.questions:
            self.refresh_questions()
        return self.questions
