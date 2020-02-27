try:
    from wordcloud import WordCloud
    from datetime import datetime
    import csv
    import json
    import random
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
            node = mecab.parseToNode(reader)

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

    stop_words = ['https', 'co', 'th',
                  u'くれる', u'10周年', u'周年', u'記念', u'タグ',
                  u'もの', u'こと', u'なる', u'する', u'いる', u'ある', u'てる', u'よう', u'れる', u'くい', u'せる', u'ない', u'無い', u'られる', u'それ', u'そう', u'くん', u'さん', u'あと', u'これ', u'どう', u'たち']  # 画像内に含めないようにする単語

    wordcloud = WordCloud(color_func=color_func,
                          font_path=font_path,
                          width=1920,
                          height=1080,
                          min_font_size=6,
                          stopwords=set(stop_words),
                          collocations=False,
                          background_color="white").generate(txt)

    plt.figure(figsize=(19.20, 10.80), dpi=100)
    plt.imshow(wordcloud, interpolation="nearest", aspect="equal")
    plt.axis("off")

    sname = sname + ".png"
    plt.savefig(sname, bbox_inches='tight')


if __name__ == '__main__':
    print('====== Enter Tweet Data file =====')
    dfile = input('>  ')

    analyzeTweet(dfile)
