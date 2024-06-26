# CopyCraftAPI

## Introduction

The API Message Generator is a Python-based tool designed to manage the creation of API messages for different user roles based on YAML configurations. This tool utilizes the OpenAI API to generate content and is highly customizable through various parameters. 

## Features

- **Dynamic Role Management:** Retrieve system role descriptions and customize messages based on user roles.
- **Configurable Message Generation:** Generate main instructions and fetch details about the copywriter model using YAML configurations.
- **Reference Material Integration:** Read and include reference materials from specified files.
- **API Communication:** Combine all messages into a structured list for seamless API communication.
- **Command-Line Interface:** Use argparse for easy command-line argument parsing and script execution.

## Setup

### Prerequisites

- Python 3.7 or higher
- `pip` package manager
- OpenAI API Key

### Installation

1. Clone the repository:
    ```sh
    git clone git@github.com:BenHsu501/Automated-Blog-Post-Creation-Framework.git

    cd Automated-Blog-Post-Creation-Framework
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key as an environment variable:
    ```sh
    export OPENAI_API_KEY='your-api-key'
    ```

## Usage

### Command-Line Interface

To generate API messages, use the following command:

```sh
python main.py --path test/test_my_reference.txt --article_type blog --role 'Angel investor' --output_path output.txt
```

## Arguments
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

## Example

To generate API messages, use the following command:

```py
python main.py --path test/test_my_reference.txt --article_type blog --role 'Angel investor' --copywriter_model PASCA --language English --word_count 500 --paragraph 5 --sentence 4 --format markdown --model gpt-3.5-turbo --max_tokens 1500 --output_path output.txt
```

## Project Detail
### Code Structure
- main.py: Main script to execute the API message generation.
- CopyCraftAPI/utils.py: Contains the GetAPIMessage class for managing message creation.
- cfg/: Directory containing YAML configuration files for roles, main instructions, and copywriter models.
- test/: Directory containing test files and reference materials.

### How It Works
* Initialization: The GetAPIMessage class is initialized with user-provided parameters or default values.
* Role Description: The role description is retrieved from the YAML configuration.
* Main Instruction: The main instruction for the user is generated based on the article type and parameters.
* Copywriter Model: Details about the copywriter model are fetched and formatted.
* Reference Material: The reference material is read from the specified file.
* Message Combination: All messages are combined into a structured list for API communication.
* Content Generation: The OpenAI API generates content based on the combined messages.
* Output: The generated content is printed to the console or saved to the specified output file.
* For any questions or contributions, please feel free to open an issue or submit a pull request.

*Disclaimer: This project is for educational and experimental purposes. Use it responsibly and adhere to OpenAI's usage policies.*


