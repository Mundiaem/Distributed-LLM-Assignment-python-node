import json
import unittest
from app import app


def decode_json(data):
    decoded_data = data.decode('utf-8')
    return json.loads(decoded_data)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.model = None

    def test_not_found(self):
        response = self.app.get('/')
        data = decode_json(response.data);
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['name'], 'Not Found')

    def test_select_model(self):
        response = self.app.post('/select_model', json={"model": "LLM1"})
        data = decode_json(response.data)
        self.assertEqual(response.status_code, 200)
        self.model = "LLM1"
        self.assertEqual(data['message'], 'Model set to LLM1')

    def test_query(self):
        question = "What is the weather today?"
        response = self.app.post('/query', json={"question": question})
        data = decode_json(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['answer'], f"Answer from {self.model} for {question}")

    def test_history(self):
        response = self.app.get('/history')
        data = decode_json(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)


if __name__ == '__main__':
    unittest.main()
