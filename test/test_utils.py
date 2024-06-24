import unittest
from unittest.mock import patch
from core.utils import GetAPIMessage
import yaml
#from pdb import breakponit
# python3 -m unittest
# python3 -m  coverage run --source core.utils -m unittest
# python3 -m http.server --directory ./htmlcov        
  
class TestGetAPIMessage(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.api_message = GetAPIMessage()
        self.api_message_custom = GetAPIMessage(
            para={
                'copywriter_model': 'test',
                'language': 'Spanish',
                'word_count': 300,
                'paragraph': 2,
                'sentence': 2,
                'format': 'text',
                'last': ''
            }
        )   
        with open('test/test_expected.yaml', 'r') as file:
            self.config = yaml.safe_load(file)

    def test_get_system(self):
        expected = self.config['test_get_system']
        self.assertEqual(self.api_message.get_system(), expected)

    def test_get_user_main_instruction(self):
        expected = self.config['test_get_user_main_instruction']
        self.assertEqual(self.api_message.get_user_main_instruction(), expected)

    def test_get_user_copywriter_model(self):
        expected = self.config['test_get_user_copywriter_model']
        self.assertIn(self.api_message.get_user_copywriter_model(), expected)
        expected = "The YAML file does not have the test model."
        self.assertIn(self.api_message_custom.get_user_copywriter_model(), expected)

    def test_get_user_my_reference(self):
        expected = self.config['test_get_user_my_reference']
        self.assertIn(self.api_message.get_user_my_reference(), expected)

    
    @patch.object(GetAPIMessage, 'get_system')
    @patch.object(GetAPIMessage, 'get_user_main_instruction')
    @patch.object(GetAPIMessage, 'get_user_copywriter_model')
    @patch.object(GetAPIMessage, 'get_user_my_reference')
    def test_combine_messages(self, mock_get_user_my_reference, mock_get_user_copywriter_model, mock_get_user_main_instruction, mock_get_system):
        # Define return values for the mocked methods
        mock_get_system.return_value = self.config['test_get_system']
        mock_get_user_main_instruction.return_value = self.config['test_get_user_main_instruction']
        mock_get_user_copywriter_model.return_value = self.config['test_get_user_copywriter_model']
        mock_get_user_my_reference.return_value = self.config['test_get_user_my_reference']
        # Call the method to test
        result = self.api_message.combine_messages()

        # Define the expected result
        expected_result = [
            {"role": "system", "content": mock_get_system.return_value},
            {"role": "user", "content": mock_get_user_main_instruction.return_value},
            {"role": "user", "content": mock_get_user_copywriter_model.return_value},
            {"role": "user", "content": mock_get_user_my_reference.return_value}
        ]

        # Assert the result
        self.assertEqual(result, expected_result)