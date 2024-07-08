import argparse
from CopyCraftAPI.utils import GetAPIMessage
from openai import OpenAI

def main():
    #breakpoint()
    parser = argparse.ArgumentParser(description="Data Fetching Operations")
    parser.add_argument("--path", type=str, default='test/test_my_reference.txt', help="Generate sources for articles")
    parser.add_argument("--output_path", type=str, default=None, help="output the generated article")
    parser.add_argument("--article_type", type=str, default='blog', help="output the generated article")
    
    #
    parser.add_argument("--copywriter_model", default="PASCA", help="Select the copywriter model to use for generating content.")
    parser.add_argument("--language", default="English", help="Specify the language for the article.")
    parser.add_argument("--word_count", type=int, default=300, help="Set the total number of words for the article.")
    parser.add_argument("--paragraph", default='4-7', help="Define the number of paragraphs in the article.")
    parser.add_argument("--sentence", type=int, default=3, help="Set the number of sentences per paragraph.")
    parser.add_argument("--format", type=str, default='markdown', help="Choose the format of the article output.")
    #
    parser.add_argument("--model", type=str, default="gpt-3.5-turbo", help="Set the model for the chatGPT API.")
    parser.add_argument("--max_tokens", type=int, default=2000, help="set the max tokens for the chatGPT API.")
    args = parser.parse_args()

    para = {
        'copywriter_model': args.copywriter_model,
        'language': args.language,
        'word_count': args.word_count,
        'paragraph': args.paragraph,
        'sentence': args.sentence,
        'format': args.format,
        'last': ''
    }
    

    message = GetAPIMessage(path = args.path, article_type = 'blog', role = 'Angel investor', para = para)
    # gpt-4o

    client = OpenAI()
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages = message.combine_messages(),  max_tokens=2000)
    response_content = response.choices[0].message.content
    print(response_content)
    if args.output_path:
        with open(args.output_path, "w") as file:
            file.write(response_content)
        print("Response saved to:", args.output_path)

if __name__ == "__main__":
    main()