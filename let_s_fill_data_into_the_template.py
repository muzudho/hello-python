#
# python let_s_fill_data_into_the_template.py
#
# テンプレートにデータを流し込もう
#
import traceback


DATA_TXT_FILE_PATH = 'resources/data.txt'
TEMPLATE_TXT_FILE_PATH = 'resources/template.txt'


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':
        try:
                # ファイル名の一部が入力されます
                file_path = input(f"""\
予め、データを書き込んだ {DATA_TXT_FILE_PATH} ファイルを用意しています。

また、データを書き出す書式を書いた {TEMPLATE_TXT_FILE_PATH} ファイルを用意しています。
これはテンプレートと呼びます。

これから、テンプレートにデータを流し込むのを練習をします。

それでは、エンター・キーを打鍵してみてください。
? """)


                # テンプレート・ファイルを先に読込
                with open(TEMPLATE_TXT_FILE_PATH, 'r', encoding='utf8') as f:
                        # NOTE テキストファイルの末尾に改行が入っていると、表示時に改行されます。改行されたくない場合は、ファイルの末尾に改行を入れないようにしてください
                        template = f.read()

                # データ・ファイルを１行ずつに分解したリストにして読込
                with open(DATA_TXT_FILE_PATH, 'r', encoding='utf8') as f:
                        # 📖 [python でファイルを read してリストにする時に、改行コードを入れない](https://qiita.com/suzuki-hoge/items/8eac60f7b68044eea6c1)
                        line_list = f.read().splitlines()

                # データを１行ずつ見ていく
                for line in line_list:
                        # データは半角空白区切り
                        tokens = line.split(' ')

                        person = tokens[0]
                        place = tokens[1]

                        filled_text = template.replace('{{person}}', person).replace('{{place}}', place)
                        print(filled_text)


                print("おわり。")


        except Exception as err:
                print(f"""\
おお、残念！　例外が投げられてしまった！
{type(err)=}  {err=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
