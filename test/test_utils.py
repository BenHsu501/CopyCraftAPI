import unittest
from unittest.mock import patch
from core.utils import GetAPIMessage

# python3 -m unittest
# python3 -m  coverage run --source core.utils -m unittest
# python3 -m http.server --directory ./htmlcov        
  
class TestGetAPIMessage(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.api_message = GetAPIMessage()
        self.api_message_custom = GetAPIMessage(
            para={
                'copywriter_model': 'PAS',
                'language': 'Spanish',
                'word_count': 300,
                'paragraph': 2,
                'sentence': 2,
                'format': 'text',
                'last': ''
            }
        )   

    def test_get_system(self):
        expected = "I want you to act a Angel investor. As an angel investor and current CEO of multiple companies, you have transformed from a successful entrepreneur into a highly influential online thought leader and startup mentor. You are known as 'Master' among many professionals for solving problems and have advised over 500 companies and 100,000 professionals. Your expertise includes copywriting, sales, and online marketing, among other rapid money-making skills and concepts."
        self.assertEqual(self.api_message.get_system(), expected)

    def test_get_user_main_instruction(self):
        expected = "I need to write an article using the PASCA copywriting structure. The article should be in English and around 500 words. Please generate an SEO-friendly title based on 'my_reference'. The title should include relevant keywords, attract readers to click, and optimize search engine rankings. Then, extract key information from 'my_reference' to create 4 paragraphs, with each paragraph containing at least 3 Finally, summarize the key points and provide encouraging words. Try to maintain the key points of the original text and supplement them accordingly. The final output should be in markdown format. "
        self.assertEqual(self.api_message.get_user_main_instruction(), expected)

'''
    def test_get_user_copywriter_model(self):
        obj = GetAPIMessage(para={'copywriter_model': 'PASCA'})
        copywriter_message = obj.get_user_copywriter_model()
        self.assertIn("The formula's steps are as follows", copywriter_message)

    def test_get_my_reference(self):
        obj = GetAPIMessage(path='test/test_my_reference.txt')
        reference_message = obj.get_my_reference()
        self.assertEqual(reference_message, "Reference message content")

    @patch('my_module.load_yaml_config')
    def test_combine_messages(self, mock_load_yaml_config):
        mock_load_yaml_config.side_effect = [{'Angel investor': {'role': 'Angel investor', 'description': 'Description of the role'}}, {'blog': {'key': 'Main instruction message for blog article type'}}, {'PASCA': {'description': 'Description of PASCA model', 'steps': [{'step1': 'Step 1'}, {'step2': 'Step 2'}], 'example': {'key1': 'value1'}}}]
        obj = GetAPIMessage()
        combined_message = obj.combine_messages()
        expected_message = [
            {"role": "system", "content": "I want you to act a Angel investor. Description of the role."},
            {"role": "user", "content": "Main instruction message for blog article type"},
            {"role": "user", "content": "Description of PASCA model\nThe formula's steps are as follows: \nstep1: Step 1\nstep2: Step 2\nExample:\nkey1: value1"},
            {"role": "user", "content": "Reference message content"}
        ]
        self.assertEqual(combined_message, expected_message)

if __name__ == '__main__':
    unittest.main()

class TestGetAPIMessage(unittest.TestCase):
    def setUp(self):
        self.GetAPIMessage = GetAPIMessage()

    def tearDown(self) -> None:
        os.remove(self.GetAPIMessage)
        return super().tearDown()
    
    def test_get_api_message(self):
        self.assertEqual(GetAPIMessage(1), "Success")
'''