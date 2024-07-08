from typing import List, Dict
import yaml
import pkg_resources

'''
def load_yaml_config(path: str) -> dict:
    with open(path, 'r') as file:
        return yaml.safe_load(file)
'''

def load_yaml_config(resource_path):
    """
    Load a YAML configuration file from the package resources.
    """
    try:
        resource_package = __name__
        resource_path = 'cfg/' + resource_path
        file_path = pkg_resources.resource_filename(resource_package, resource_path)
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise FileNotFoundError(f"Unable to find or open the file: {resource_path}") from e

class GetAPIMessage:
    """
    Manages the creation of API messages for different user roles based on YAML configurations.
    Methods:
        get_system: Retrieves the system role description from YAML configuration.
        get_user_main_instruction: Generates the main instruction for the user from YAML configuration.
        get_user_copywriter_model: Fetches details about the copywriter model from YAML configuration.
        get_user_my_reference: Reads and returns the reference material from a file.
        combine_messages: Combines all messages into a structured list for API communication.

    """
    def __init__(self, path:str = 'test/test_my_reference.txt', article_type:str = 'blog', role = 'Angel investor', para:dict = None):
        """
        Initializes the GetAPIMessage object with default parameters and updates them with any user-provided parameters.

        Args:
            path (str): Path to the file containing reference material.
            article_type (str): The type of article, e.g., 'blog'.
            role (str): The role of the user, e.g., 'Angel investor'.
            para (dict, optional): Parameters to override default message settings.

        Example:
            message_creator = GetAPIMessage(article_type='blog', role='Angel investor', para={'language': 'Spanish'})
        """
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
        self.para = default_para
        self.article_type = article_type
        self.role = role

    def get_system(self) -> str:
        role = self.role
        config = load_yaml_config('system/role.yaml')
        system_info = 'I want you to act a ' + config[role]['role'] + '. ' + config[role]['description']

        return system_info
    
    def get_user_main_instruction(self) -> str:
        article_type = self.article_type
        para = self.para
  
        config = load_yaml_config('user/main_instruction.yaml')
        prompts = config[article_type]
        message = ' '.join(prompts[key] + ' ' + str(para[key]) for key in prompts.keys())

        return message
    
    def get_user_copywriter_model(self) -> str:
        #breakpoint()
        para = self.para
        model = para['copywriter_model']
        config = load_yaml_config('user/copywriter_model.yaml')

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
    def get_user_my_reference(self) -> str:
        path = self.path
        with open(path, 'r') as file:
          message = file.read()
        return "Here is my reference material:\n" + message
        
    def combine_messages(self) -> List[Dict]:
        system_message = self.get_system()
        main_instruction = self.get_user_main_instruction()
        copywriter_message = self.get_user_copywriter_model()
        reference_message = self.get_user_my_reference()

        combined_message = [
          {"role": "system", "content": system_message},
          {"role": "user", "content": main_instruction},
          {"role": "user", "content": copywriter_message},
          {"role": "user", "content": reference_message}
        ]

        return combined_message
    
  