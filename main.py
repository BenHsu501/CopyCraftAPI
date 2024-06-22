import argparse
import yaml
from core.utils import GetAPIMessage

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
        # print('1. get_system', message.get_system())
        print('2. get_user_main_instruction', message.get_user_main_instruction())
        # print('3 . get_copywriter', message.get_copywriter_model())
        # print('4 . get_my_reference', message.get_my_reference())
        # print('5. combine_messages', message.combine_messages())

if __name__ == "__main__":
    main()