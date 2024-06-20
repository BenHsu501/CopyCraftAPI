# 
# https://community.make.com/t/what-is-the-difference-between-system-user-and-assistant-roles-in-chatgpt/36160/4
from openai import OpenAI
from typing import Union, List, Dict
import yaml

def load_yaml_config(path: str) -> dict:
    with open(path, 'r') as file:
        return yaml.safe_load(file)


class GetAPIMessage:
    def __init__(self, path='cfg/', language='English', word_count=720, 
                  copywriter_model='PASCA', system_article='blog', assistant=''):
        self.path = path
        self.para = {
            'language': language,
            'word_count': word_count,
            'copywriter_model': copywriter_model,
            'system_article': system_article,
            'assistant': assistant
        }
    def get_system(role:str) -> str:
        config = load_yaml_config('cfg/system/role.yaml')
        system_info = 'I want you to act a ' + config[role]['role'] + '. ' + config[role]['description']

        print(system_info)
        return system_info

def get_copywriter_model(model: str) -> Union[List[Dict], str]:
    config = load_yaml_config('cfg/copywriter_model.yaml')

    if not model in config.keys():
        return f"The YAML file does not have the {model} model."
    
    model_info = config[model]
    description = model_info['description']
    steps = model_info['steps']
    example = model_info['example']

    steps_message = "\n".join([f"{list(step.keys())[0]}: {list(step.values())[0]}" for step in steps])
    example_message = "\n".join([f"{key}: {value}" for key, value in example.items()])

    message = [
      {"role": "user", "content": {"type": "text", "text": description}},
      {"role": "user", "content": {"type": "text", "text": steps_message}},
      {"role": "user", "content": {"type": "text", "text": example_message}},
    ]
    return message

def get_assistant(assistant: str) -> List[Dict]:
    config = load_yaml_config('cfg/assistant.yaml')
    #print(config)
    assistant_info = config[assistant]
    message = [{"role": "assistant", "content": {"type": "text", "text": assistant_info}},]
    
    return message
def get_user_main_instruction(
    article_type='blog',
    para={
        'copywriter_model': 'PASCA',
        'language': 'English',
        'word_count': 500,
        'paragraph': 4,
        'sentence': 3,
        'format': 'markdown',
        'final': 'final'
    }
) -> str:
    1
def get_user_main_instruction(article_type = 'blog', para = None ) -> str:
    # Define default parameters
    default_para = {
        'copywriter_model': 'PASCA',
        'language': 'English',
        'word_count': 500,
        'paragraph': 4,
        'sentence': 3,
        'format': 'markdown',
        'final': 'final'
    }
    
    # If `para` is provided, update the default dictionary with the provided parameters
    if para is not None:
        default_para.update(para)

    print(default_para)
    config = load_yaml_config('cfg/user/main_instruction.yaml')
    prompts = config[article_type]
    message = ''.join(prompts[key] + details[key] for key in prompts.keys() if key in details)

    #print(system_info)
    #return system_info
   

'''

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {"role": "system", "content": "你是一名天使投資人. 現任多家公司總裁. 從一位成功的企業家，化身成極具影響力的網路意見領袖和創業導師，為許多人排憂解惑，成為許多人口中的「師傅」，至今已輔導超過500家公司、和100,000多位專業人士。你精通文案撰寫、銷售、網路行銷等非常多快速賺錢的技能與觀念"},
        {"type": "text", "text":"你需要使用文案技巧根據下面文章重新撰寫 750 字的文章，文章需要包含標題，這個標題要是非常吸引人，並將750字的內容分為子標題，會包含多個主標題"},

        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=20,
)

print(response.choices[0])


response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": {"type": "text", "text": "System initializing..."}},
        {"role": "user", "content": {"type": "text", "text": "Hello, how can I improve my garden?"}},
        {"role": "assistant", "content": {"type": "text", "text": "You can start by assessing the sunlight and soil quality."}},
        {"role": "user", "content": {"type": "text", "text": "What plants thrive in partial sunlight?"}},
        {"role": "assistant", "content": {"type": "text", "text": "Ferns and hostas are great for partial sunlight."}}
    ],
    max_tokens=150
)

'''