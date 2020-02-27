# Word Cloud

## 概要

Twitter API を利用して、ツイートの検索結果からワードクラウドを生成します。  
（とはいえ、ツイート取得とワードクラウド生成のプログラムは分けているので、ツイートじゃなくてもテキストファイルさえあればそれを基に生成できます。）

こんなやつ ↓  
<img src="https://user-images.githubusercontent.com/27045715/75446511-e6388e80-59aa-11ea-9d35-42d17222f539.png" width="300px">

## 使い方

1. config_sample.json を config.json にリネームします。
2. config.json に、Twitter API のキーやトークン、ワードクラウド生成に使用するフォントのパスを入力します。
3. `python tweepy_savefulltxt.py` を実行します。
   - "Enter Search KeyWord"と出てきたら、検索する文字列を入力
   - "Enter Tweet Data file"と出てきたら、検索結果を保存するファイル名を入力
4. wordcloud_fromtxt.py をいい感じにいじります。
   - 画像内に含まないようにする単語を stop_words に入れておきます。コード内では私が使ったものに特化しているので、人によって調整が必要です。
   - 文字色や出力サイズなども適宜変更
5. `python wordcloud_fromtxt.py` を実行します。
   - "Enter Tweet Data file"と出てきたら、3 で出力した検索結果を保存したファイル名を入力
6. ワードクラウドの画像が生成されます。
   - デフォルトのファイル名はタイムスタンプです。
   - デフォルトだと色がランダムに選ばれるので、何度か同じファイルで生成すると印象が変わったりします。

## 参考

- [Python Twitter からツイートを取得してテキスト分析(wordcloud で見える化)](https://qiita.com/kngsym2018/items/3719f8da1f129793257c)

## 備考

- 現状、画像サイズの設定が怪しいです。
- URL とか RT の除外ができていないので、生成されるワードクラウドにノイズが混ざりがちです…><
  - RT は検索ワードに "-RT"を入れれば除外できますが、コード上で除外することはしていません。
