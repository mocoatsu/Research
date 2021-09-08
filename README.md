# app/backend/schemas

pydantic を用いたモデルスキーマ定義
ユーザーへのレスポンス型式 をそれぞれ指定

# app/backend/models

DB に保存される型式

# app/backend/utils

ロガー・ヘルパーなどの汎用的な実装のみ

# 擬音語とパラメータの関係

- エンベロープをセットしない場合 -　ビー、ブーという音はでる。
- attack,decay,sustain を固定する場合はっきりとした音がでる
  - "attack": get_random_f(0, 0),
    "decay": get_random_f(0, 0),
    "sustain": get_random_f(1, 1),
    "release": get_random_f(0, 0.3),

# modulation Index

- 2 オペレータの場合

  - 1,18 といった値では音色に大きな差はない（論文：https://dke.maastrichtuniversity.nl/westra/PhDMaBa-teaching/GraduationStudents/Ba/LaurensAlbertsBaFINAL2005.pdf）に反する
  - 5000 ぐらいまで上げても音色に変化ある
  - サイン音として利用を考えるのであれば、1000 ぐらいでよい気がする。

  -　変調周波数とエンベロープセットの時間を入れ替えると音色が変わる
