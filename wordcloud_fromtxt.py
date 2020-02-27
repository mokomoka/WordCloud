try:
    from wordcloud import WordCloud
    from datetime import datetime
    import csv
    import json
    import random
    import neologdn
    import re
    from os import path
    import MeCab
    import matplotlib
    matplotlib.use('Agg')
finally:
    import matplotlib.pyplot as plt


def color_func(word, font_size, position, orientation, random_state, font_path, **kwargs):
    colors = ["#1E88E5", "#FDD835", "#f44336", "#66BB6A"]  # 画像内で使われる文字の色
    return random.choice(colors)


def analyzeTweet(dfile):
    fname = r"'" + dfile + "'"
    fname = fname.replace("'", "")
    sname = datetime.now().strftime("%Y%m%d%H%M%S")  # 保存するときのファイル名

    mecab = MeCab.Tagger("-Ochasen")

    words = []

    with open(fname, 'r', encoding="utf-8") as f:
        reader = f.readline()

        while reader:
            normalized_text = neologdn.normalize(reader)
            text_without_url = re.sub(
                r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', '', normalized_text)
            node = mecab.parseToNode(text_without_url)

            while node:
                word_type = node.feature.split(",")[0]

                if word_type in ["動詞", "形容詞", "形容動詞"]:
                    # 動詞、形容詞、形容動詞は原型を使っています
                    words.append(node.feature.split(",")[6])
                elif word_type in ["名詞", "副詞"]:
                    words.append(node.surface)

                node = node.next

            reader = f.readline()

    json_file = open('config.json', 'r')
    json_obj = json.load(json_file)
    font_path = json_obj['Font_path']
    txt = " ".join(words)

    stop_words = []  # 画像内に含めないようにする単語

    wordcloud = WordCloud(color_func=color_func,
                          font_path=font_path,
                          width=1920,  # 出力画像の横幅
                          height=1080,  # 出力画像の縦幅
                          min_font_size=6,  # 最小のフォントサイズ
                          stopwords=set(stop_words),
                          collocations=False,
                          background_color="white").generate(txt)  # 背景色

    sname = sname + ".png"  # 保存形式変えたい場合は拡張子を変更
    wordcloud.to_file(path.join(path.dirname(__file__), sname))


if __name__ == '__main__':
    print('====== Enter Tweet Data file =====')
    dfile = input('>  ')

    analyzeTweet(dfile)
