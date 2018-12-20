メディカルAI専門コース オンライン講義資料
=========================================


News
^^^^
2018/12/17: 講義資料Ver 1.0を公開

本講義資料について
^^^^^^^^^^^^^^^^^^

本ページは **日本メディカルAI学会公認資格：メディカルAI専門コースのオンライン講義資料（以下本資料）** です．
本講料を読むことで，医療で人工知能技術を使う際に最低限必要な知識や実践方法を学ぶことができます．本資料は全てGoogle Colaboratoryというサービスを用いて執筆されており，各章はJupyter notebook (iPython notebook)の形式（.ipynb）で以下のリポジトリにて配布されています（notebooksディレクトリ以下に全ての.ipynbファイルが入っています）： `japan-medical-ai/medical-ai-course-materials <https://github.com/japan-medical-ai/medical-ai-course-materials>`_

想定受講者
^^^^^^^^^^

受講想定者として大学生，大学院生，医療従事者を想定しています．
また，Python，Google Colaboratoryの基本的な使い方を知っていることを想定しています．
Python，Google Colaboratoryについては様々な参考資料や解説サイトがあります．例えば，以下のような資料も参考にしてください．

* `Python学習サイト集 <https://qiita.com/kita33/items/8891c7c04b664e7669bf>`_
* `ゼロからはじめるPython第26回 (Colaboratorの使い方について） <https://news.mynavi.jp/article/zeropython-26/>`_
* `Google colaboratory FAQ <https://research.google.com/colaboratory/faq.html>`_

Pythonについては変数（数値・文字列，リスト，タプル，辞書），制御構文（for，if），関数，クラスを理解している必要があります．

内容について
^^^^^^^^^^^^

* 線形代数，統計，確率の基礎，機械学習，DeepLearning（深層学習）の基礎や実践を学んでいきます．
* 実践では，Google Colaboratory上で動くJupyter Notebookを使って，ブラウザ上で実際にプログラムを書き，実行結果を確認しながら進めていきます．
* 本資料は全部で8章からなり，各章を終えるのにそれぞれ既に知識がある人であれば1時間程度，新しく学ぶ人であれば6時間程度を想定しています．すでに知っている部分がある方は本資料を確認程度でスキップして進めていくこともできます．
* 受講者には本講義に基づいた問題を解いてもらい，基準を満たした人が合格となります．問題は受講した人だけに提供されます．合格基準は非公開です．

"Open in Colab"ボタンについて
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

各章のページの冒頭には，以下のような"Open in Colab"と書かれたボタンが設置されています．これをクリックすると，Google Colaboratory上で資料が開き，途中のコードを実際に実行しながら読み進めることができます．4章以降は基本的にGoogle Colaboratory上でコードを実行しながら読み進めていくことを前提に書かれています．すべての講義資料はGoogle Colaboratoryが動作している環境（Ubuntu 18.04）を前提としています．それ以外の環境で動作させることは想定していません．

.. image:: https://colab.research.google.com/assets/colab-badge.svg

（このボタンをクリックしてもGoogle Colabは開きません．各章のページへ移動してからお試しください．）

利用
^^^^
本資料はコースの受講者以外も誰でも自由に無料で使うことができます．


資料もくじ
^^^^^^^^^^

.. toctree::
    :maxdepth: 1
    :numbered:
    
    notebooks/Basic_Math_for_ML
    notebooks/Introduction_to_ML_libs
    notebooks/Introduction_to_Neural_Network
    notebooks/Introduction_to_Chainer
    notebooks/Image_Segmentation
    notebooks/Blood_Cell_Detection
    notebooks/DNA_Sequence_Data_Analysis
    notebooks/Sequential_Data_Analysis_with_Deep_Learning

推奨ブラウザ環境
^^^^^^^^^^^^^^^^^

* 主要なブラウザはサポートしています．特に内部で使用しているGoogle Colaboratory はPC 版のChromeとFirefoxでは完全に動作するよう検証されています．


本資料の作成者
^^^^^^^^^^^^^^
本資料は株式会社Preferred Networksの岡野原 大輔，齋藤 俊太，菅原 洋平，その他多くの有志，そして株式会社キカガクの吉崎 亮介が中心となって作成しました．

問い合わせ先
^^^^^^^^^^^^^^
本資料についての質問、不具合の報告などについては以下の `フォーラム <https://groups.google.com/forum/#!forum/japan-medical-ai>`_ で受け付けています．


索引と検索
==========

* :ref:`genindex`
* :ref:`search`
