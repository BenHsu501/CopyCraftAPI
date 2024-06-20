import argparse
import yaml
from core.utils import get_copywriter_model, get_assistant, get_user_main_instruction

def main():
    parser = argparse.ArgumentParser(description="Data Fetching Operations")
    parser.add_argument("--mode", choices=["fetch_youtube_playlist", "download_subtitle", 'test'], help="Select the mode of operation.")
    parser.add_argument("--copywriter_model", help="Select a copywriter model")

    args = parser.parse_args()

    if args.mode == 'test':
        #print(get_copywriter_model('PAsS'))
        #print(get_assistant('Angel investor'))
        # print(get_system(role = 'Angel investor'))
        get_user_main_instruction(article_type = 'blog', para = {'language': 'EEEEE'})


if __name__ == "__main__":
    main()