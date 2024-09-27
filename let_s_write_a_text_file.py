#
# python let_s_write_a_text_file.py
#
# 文章をファイルに保存しよう
#
import traceback
import time


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':
        try:
                # 現在時刻を取得
                start = time.time()

                # ファイル名の一部が入力されます
                file_name_stem = input("""\
文章を保存する練習をします。

文章は、ファイルに保存されます。
そこで、今からファイルの名前を考えてください。
名前に使える文字はとりあえず A～Z、 a～z、 0～9 と _ （下線）としましょう。
文字数は、慣れないうちは１０ 文字前後ぐらいを目安にするといいでしょう。

例： burger100yen

では、名前を打鍵して、エンター・キーを打鍵してみてください。
? """)

                # フォルダー名の logs と、パス区切りの / 、拡張子の .log を追加して、ファイル・パスとします
                file_path = f"logs/{file_name_stem}.log"

                text = input("""\
次に、保存したい文章を入力してください。

例： おいしい

? """)

                # とりあえず、テキストファイルを保存するための簡単な書き方
                with open(file_path, 'a', encoding='utf8') as f:
                        f.write(f"{text}\n")    # 末尾に改行を付けて保存


                print(f"""\
［{file_path}］に、［{text}］という文章が保存されているはずです。
確認してみてください。
おわり。
""")


        except Exception as err:
                print(f"""\
おお、残念！　例外が投げられてしまった！  
{err=}  {type(err)=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
