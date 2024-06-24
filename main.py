import argparse
import yaml
from core.utils import GetAPIMessage
from openai import OpenAI


def main():
    parser = argparse.ArgumentParser(description="Data Fetching Operations")
    # parser.add_argument("--mode", choices=["fetch_youtube_playlist", "download_subtitle", 'test'], help="Select the mode of operation.")


    parser.add_argument("--copywriter_model", default="PASCA", help="Select the copywriter model to use for generating content.")
    parser.add_argument("--language", default="English", help="Specify the language for the article.")
    parser.add_argument("--word_count", type=int, default=300, help="Set the total number of words for the article.")
    parser.add_argument("--paragraph", default='4-7', help="Define the number of paragraphs in the article.")
    parser.add_argument("--sentence", type=int, default=3, help="Set the number of sentences per paragraph.")
    parser.add_argument("--format", type=str, default='markdown', help="Choose the format of the article output.")




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

    message = GetAPIMessage(article_type = 'blog', role = 'Angel investor', para = para)
    #print(message.combine_messages())
    # gpt-4o
    client = OpenAI()
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages = message.combine_messages(),  max_tokens=2000)
    '''
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]
    )       
    '''
    #print(response)
    print('Text, ', response.choices[0].message.content)

if __name__ == "__main__":
    main()