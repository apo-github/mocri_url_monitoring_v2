# mocri url monitoring ver.2

## mocri の画面を監視し，URL を取得するものです．

### 必要なもの

    1. python環境とその他必要なパッケージ．
    2. mpv player (コマンドからyoutubeを再生するために使用します)．
    3. 音を流すための別アカウント

### 導入方法 How to install

    1. ソースをダウンロード．
    2. 必要なものパッケージをpipインストールし，プログラムが動作するようにしておく．
    3. プログラムを実行するPCにmpv playerを導入する．
    4. 音を流すための，別アカウントを用意する．
    5. key.txtにログイン情報を書いておく

### 使用方法 How to use

    1 .pc上で，mocri_url_monitering_v2.py を実行する．
    2 .後は置いておくだけです．(別のスマホ端末などからyoutubeのURLを送信すると再生してくれます)．

### コマンド add commad option

    - yt URL：URLで指定されたyoutubeを再生します．
    - yt stop：youtubeの再生を止めるコマンドです．チャットから送信すると音楽を停止します．
    - @ 任意テキスト：botから定型文を返します．

### 動かない場合

    以下を確認してみてください．
    - 必要なパッケージがinstallされていない可能性があります．import error等を確認して下さい．
    - python 3.11.1で動作確認済みです．
