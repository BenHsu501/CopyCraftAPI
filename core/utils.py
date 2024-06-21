# 
# https://community.make.com/t/what-is-the-difference-between-system-user-and-assistant-roles-in-chatgpt/36160/4
from openai import OpenAI
from typing import Union, List, Dict
import yaml

def load_yaml_config(path: str) -> dict:
    with open(path, 'r') as file:
        return yaml.safe_load(file)

class GetAPIMessage:
    def __init__(self, path:str = 'test/test_my_reference.txt', article_type:str = 'blog', role = 'Angel investor', para:dict = None, ):
        # Define default parameters
        default_para = {
            'copywriter_model': 'PASCA',
            'language': 'English',
            'word_count': 500,
            'paragraph': 4,
            'sentence': 3,
            'format': 'markdown',
            'last': ''
        }
        if para is not None:
            default_para.update(para)
        #
        self.path = path
        self.para = para
        self.article_type = article_type
        self.role = role

    def get_system(self) -> str:
        role = self.role
        config = load_yaml_config('cfg/system/role.yaml')
        system_info = 'I want you to act a ' + config[role]['role'] + '. ' + config[role]['description']

        return system_info
    
    def get_user_main_instruction(self) -> str:
        article_type = self.article_type
        para = self.para
  
        config = load_yaml_config('cfg/user/main_instruction.yaml')
        prompts = config[article_type]
        message = ' '.join(prompts[key] + str(para[key]) for key in prompts.keys())

        return message
    
    def get_user_copywriter_model(self) -> str:
        para = self.para
        model = para['copywriter_model']
        config = load_yaml_config('cfg/user/copywriter_model.yaml')

        if not model in config.keys():
            return f"The YAML file does not have the {model} model."
        
        model_info = config[model]
        description = model_info['description']
        steps = model_info['steps']
        example = model_info['example']

        steps_message = "\n".join([f"{list(step.keys())[0]}: {list(step.values())[0]}" for step in steps])
        example_message = "\n".join([f"{key}: {value}" for key, value in example.items()])
        message = description + '\n' + 'The formula\'s steps are as follows: \n' + steps_message + '\nExample:\n' + example_message
          
        return message
    def get_my_reference(self):
        path = self.path
        with open(path, 'r') as file:
          message = file.read()
        return message
        
    def combine_messages(self):
        system_message = self.get_system()
        main_instruction = self.get_user_main_instruction()
        copywriter_message = self.get_user_copywriter_model()
        reference_message = self.get_my_reference()

        combined_message = [
          {"role": "system", "content": system_message},
          {"role": "user", "content": main_instruction},
          {"role": "user", "content": copywriter_message},
          {"role": "user", "content": reference_message}
        ]

        return combined_message