# CopyCraftAPI
[Read this in English](/README.md)


## 介紹

CopyCraftAPI 是 Copywriting、Crafting 與 API 的簡稱，目標是簡化自動生成文章的步驟。此專案會協助生成高效的 OpenAI API message 來生成文章，你將能透過參數與 yaml 檔客製化 message，得到最佳結果。

## 特點
- **生成高效的API結構**：專案設定數個有效率的文章生成模板
- **透過yaml客製化配置**：透過 cfg/ 內的 yaml，可輕鬆設置 message 的 role 與 user
- **命令行介面**：使用 argparse 進行簡單的命令行參數解析和腳本執行

## 設置

### 先決條件

- Python 3.7 或更高版本
- `pip` 包管理器
- ```openai```

### 安裝

1. git install
    ```sh
    pip install git+https://github.com/BenHsu501/CopyCraftAPI.git
    ```

2. 將您的 OpenAI API 金鑰設置為環境變量：
    ```sh
    export OPENAI_API_KEY='your-api-key'
    ```

3. 載入套件：
    ```py
    import CopyCraftAPI.utils as CopyCraftAPI
    ```

## 使用

### 命令行介面
```sh
python main.py --path test/test_my_reference.txt --article_type blog --role 'Angel investor' --output_path output.txt
```

### 參數
- --path: 包含參考資料的文件路徑。默認為 test/test_my_reference.txt。
- --output_path: 保存生成文章的路徑。默認為 None。
- --article_type: 文章類型，例如 'blog'。默認為 blog。
- --copywriter_model: 選擇用於生成內容的文案模型。默認為 PASCA。
- --language: 指定文章的語言。默認為 English。
- --word_count: 設置文章的總字數。默認為 300。
- --paragraph: 定義文章的段落數。默認為 4-7。
- --sentence: 設置每段的句子數。默認為 3。
- --format: 選擇文章輸出的格式。默認為 markdown。
- --model: 設置 chatGPT API 的模型。默認為 gpt-3.5-turbo。
- --max_tokens: 設置 chatGPT API 的最大 tokens。默認為 2000。

### Python 介面
生成 API 使用訊息：
```py
import CopyCraftAPI.utils as CopyCraftAPI
message = GetAPIMessage(path = 'your_reference_txt', article_type = 'blog', role = 'Angel investor')
message = message.combine_messages()
```

呼叫 OpenAI 套件:
```py
client = OpenAI()
response = client.chat.completions.create(model="gpt-3.5-turbo", messages = message,  max_tokens=2000)
response_content = response.choices[0].message.content
### 生成結果
print(response_content)
```


## 專案細節
### 代碼結構
- main.py: 執行 API message 生成的主腳本。
- CopyCraftAPI/utils.py: 包含管理 message 建立的 GetAPIMessage class。
- cfg/: 包含角色、主要指令和文案模型的 YAML 配置文件的目錄。
- test/: 包含測試文件和參考資料的目錄。

### yaml 設置細節
- OpenAI API 有三種角色，system、user 與 assistant
    - system 為 high-level instructions, 作為語氣、人物背景的基底
    - user 為使用者引導的語句
    - assistant 為對話回應設定，本專案生成文章，不需要此角色
- **cfg/system/role.yam** 提供人物，以該人物的口吻撰寫文章
- **cfg/user/copywriter_model.yam** 多種文案結構，可自行加入
- **cfg/user/main_instruction.yam** 文章生成的細節，可以新增 tewitter 或其他格式。


*如有任何問題或貢獻，請隨時提交問題或拉取請求。*
