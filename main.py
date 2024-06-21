import argparse
import yaml
from core.utils import get_copywriter_model, get_assistant, get_user_main_instruction, GetAPIMessage

def main():
    parser = argparse.ArgumentParser(description="Data Fetching Operations")
    parser.add_argument("--mode", choices=["fetch_youtube_playlist", "download_subtitle", 'test'], help="Select the mode of operation.")
    parser.add_argument("--copywriter_model", help="Select a copywriter model")

    args = parser.parse_args()

    if args.mode == 'test':
        #print(get_copywriter_model('PAsS'))
        #print(get_assistant('Angel investor'))
        # print(get_system(role = 'Angel investor'))
        default_para = {
            'copywriter_model': 'PASCA',
            'language': 'English',
            'word_count': 500,
            'paragraph': 4,
            'sentence': 3,
            'format': 'markdown',
            'last': ''
        }

        message = GetAPIMessage(article_type = 'blog', role = 'Angel investor', para = default_para)
        #print('1. get_system', message.get_system())
        #print('2. get_user_main_instruction', message.get_user_main_instruction())
        print('3 . get_copywriter', get_copywriter_model('PSA'))

        # get_user_main_instruction(article_type = 'blog', para = {'language': 'EEEEE'})


if __name__ == "__main__":
    main()