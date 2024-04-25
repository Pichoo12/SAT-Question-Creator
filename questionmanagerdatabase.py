import requests
import json
import os
class QuestionManager:
    def __init__(self):
        self.questions_file = "questions.json"
        self.questions = []

        if os.path.exists(self.questions_file) and os.path.getsize(self.questions_file) > 0:
            with open(self.questions_file, "r") as qfile:
                self.questions = json.load(qfile)

    def saveQuestions(self):
        # Save the current state of questions to the file
        with open(self.questions_file, "w") as qfile:
            json.dump(self.questions, qfile, indent=4)

    def fetchQuestions(self, json_data):
        headers = {
            'authority': 'qbank-api.collegeboard.org',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://satsuitequestionbank.collegeboard.org',
            'referer': 'https://satsuitequestionbank.collegeboard.org/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.217 Safari/537.36',
        }

        response = requests.post(
            'https://qbank-api.collegeboard.org/msreportingquestionbank-prod/questionbank/digital/get-questions',
            headers=headers,
            json=json_data,
        )
        return response.json()

    def getAllReadingQuestions(self):
        return self.fetchQuestions({
            'asmtEventId': 99,
            'test': 1,
            'domain': 'INI,CAS,EOI,SEC',
        })

    def getAllMathQuestions(self):
        return self.fetchQuestions({
            'asmtEventId': 99,
            'test': 2,
            'domain': 'H,P,Q,S',
        })

    def getQuestionIds(self):
        questions = self.getQuestions()
        ids = []
        for q in questions:
            if "external_id" in q:
                ids.append(q['external_id'])
        return ids

    def getQuestion(self, id):
        headers = {
            'authority': 'qbank-api.collegeboard.org',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://satsuitequestionbank.collegeboard.org',
            'referer': 'https://satsuitequestionbank.collegeboard.org/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.217 Safari/537.36',
        }
        json_data = {
            'external_id': str(id),
        }

        response = requests.post(
            'https://qbank-api.collegeboard.org/msreportingquestionbank-prod/questionbank/digital/get-question',
            headers=headers,
            json=json_data,
        )
        return response.json()

    def getQuestions(self):
        if len(self.questions) == 0:
            print("Fetching new questions...")
            math_questions = self.getAllMathQuestions()
            reading_questions = self.getAllReadingQuestions()
            self.questions = math_questions + reading_questions
            self.saveQuestions()
        else:
            print("Using cached questions.")
            pass
        return self.questions