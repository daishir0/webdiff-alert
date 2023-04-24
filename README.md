# webdiff-alert

## Overview

`webdiff-alert` is a Python tool that monitors a list of URLs for changes in their content. When a change is detected, the tool prints the text difference between the old and new versions of the webpage and saves the new version as an HTML file. The tool runs continuously, checking the list of URLs every minute.

## Installation

1.  Install Python 3.x if not already installed.
2.  Clone the `webdiff-alert` repository.
3.  Install the required Python packages using the following command:

```
pip install -r requirements.txt
```

## Usage

1.  Add the URLs you want to monitor to the `urls.txt` file, one URL per line.
2.  Run the `webdiff-alert` script using the following command:

```
python webdiff_alert.py
```

## Notes

-   The tool uses single-threading to process URLs sequentially. As the number of URLs increases, the processing time will be longer.

## License

This project is licensed under the MIT License.

* * *

# webdiff-alert（日本語）

## 概要

`webdiff-alert`は、URLリストのコンテンツの変更を監視するPythonツールです。変更が検出されると、ツールは古いバージョンと新しいバージョンのウェブページのテキスト差分を出力し、新しいバージョンをHTMLファイルとして保存します。ツールは継続的に実行され、URLリストを1分ごとにチェックします。

## インストール方法

1.  まだインストールされていない場合は、Python 3.xをインストールしてください。
2.  `webdiff-alert`リポジトリをクローンします。
3.  以下のコマンドを使用して、必要なPythonパッケージをインストールします。

```
pip install -r requirements.txt
```

## 使い方

1.  監視するURLを`urls.txt`ファイルに追加します。1行に1つのURLを記載してください。
2.  以下のコマンドで`webdiff-alert`スクリプトを実行します。

```
python webdiff_alert.py
```

## 注意事項

-   ツールはシングルスレッドを使用してURLを順次処理します。URLの数が増えると、処理時間が長くなります。

## ライセンス

このプロジェクトは、MITライセンスでライセンスされています。
