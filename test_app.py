import unittest
from app import app

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_status_endpoint(self):
        # Envia uma requisição GET para o endpoint /api/status
        response = self.client.get('/api/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "API is running!"})

    def test_data_endpoint(self):
        # Envia uma requisição POST para o endpoint /api/data com um JSON de exemplo
        data = {"key": "value"}
        response = self.client.post('/api/data', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"received_data": data})

if __name__ == '__main__':
    unittest.main()
