# CopyCraftAPI
[中文閱讀](docs/README_ZH.md)
## Introduction

CopyCraftAPI is an acronym for Copywriting, Crafting, and API, aiming to simplify the process of automatically generating articles. This project helps generate efficient OpenAI API messages to create articles. You can customize the messages through parameters and YAML files to get the best results.

## Features

- **Generate Efficient API Structure**: The project sets up several efficient article generation templates.
- **Custom Configuration through YAML**: Easily set up message roles and users through YAML files in the `CopyCraftAPI/cfg/` directory.
- **Command-Line Interface**: Use argparse for simple command-line parameter parsing and script execution.

## Setup

### Prerequisites

- Python 3.7 or higher
- `pip` package manager
- `openai`

### Installation

1. Install via git:
    ```sh
    pip install git+https://github.com/BenHsu501/CopyCraftAPI.git
    ```

2. Set your OpenAI API key as an environment variable:
    ```sh
    export OPENAI_API_KEY='your-api-key'
    ```

3. Load the package:
    ```py
    from CopyCraftAPI.utils import GetAPIMessage
    ```

## Usage

### Command-Line Interface

```sh
python main.py --path test/test_my_reference.txt --article_type blog --role 'Angel investor' --output_path output.txt
```
### Arguments
- --path: Path to the file containing reference material. Default is test/test_my_reference.txt.
- --output_path: Path to save the generated article. Default is None.
- --article_type: Type of the article, e.g., 'blog'. Default is blog.
- --copywriter_model: Select the copywriter model to use for generating content. Default is PASCA.
- --language: Specify the language for the article. Default is English.
- --word_count: Set the total number of words for the article. Default is 300.
- --paragraph: Define the number of paragraphs in the article. Default is 4-7.
- --sentence: Set the number of sentences per paragraph. Default is 3.
- --format: Choose the format of the article output. Default is markdown.
- --model: Set the model for the chatGPT API. Default is gpt-3.5-turbo.
- --max_tokens: Set the max tokens for the chatGPT API. Default is 2000.

### Python Interface
Generate API usage message:
```py
from CopyCraftAPI.utils import GetAPIMessage
message = GetAPIMessage(path='your_reference_txt', article_type='blog', role='Angel investor')
message = message.combine_messages()
```

Call OpenAI API:
```py
client = OpenAI()
response = client.chat.completions.create(model="gpt-3.5-turbo", messages=message, max_tokens=2000)
response_content = response.choices[0].message.content
### Generate result
print(response_content)
```

## Project Details

### Code Structure
- main.py: Main script to execute API message generation.
- CopyCraftAPI/utils.py: Contains the GetAPIMessage class for managing message creation.
- CopyCraftAPI/cfg/: Directory containing YAML configuration files for roles, main instructions, and copywriter models.
- test/: Directory containing test files and reference materials.

### YAML Configuration Details
- OpenAI API has three roles: system, user, and assistant.
    -  System: High-level instructions, serving as the tone and background.
    - User: User-guided statements.
    - Assistant: Response settings, not needed for article generation in this project.
- **cfg/system/role.yaml:** Provides roles, writing articles in the tone of the specified role.
- **cfg/user/copywriter_model.yaml:** Various copywriting structures, can be added as needed.
- **cfg/user/main_instruction.yaml:** Details of article generation, can add formats like Twitter or others.

### Next plan
Add tiktoken to limit the number of max tokens.

For any questions or contributions, please feel free to open an issue or submit a pull request.
