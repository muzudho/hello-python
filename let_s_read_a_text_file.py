#
# python let_s_read_a_text_file.py
#
# ファイルに保存した文章を読み込もう
#
import traceback


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':
        try:
                # ファイル名の一部が入力されます
                file_path = input("""\
以前ファイルに保存した文章を読み込む練習をします。

例えば、既に logs フォルダーの中に burger100yen.log といった名前のファイルを作っていますか？
フォルダー名とファイル名を１つにつなげたものを、［ファイルへのパス］と呼びます。
この場合のファイルへのパスは logs/burger100yen.log になります。

それでは、以前に保存したファイルへのパスを打鍵して、エンター・キーを打鍵してみてください。
? """)


                # とりあえず、テキストをファイルから読み出すための簡単な書き方
                with open(file_path, 'r', encoding='utf8') as f:
                        text = f.read()


                print(f"""\
{text}
という文章を、［{file_path}］から読み取りました。
おわり。
""")


        except Exception as err:
                print(f"""\
おお、残念！　例外が投げられてしまった！  
{err=}  {type(err)=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
