# Ususama （烏枢沙摩）

## このプロジェクトについて

トイレ個室の空き状況を確認できるようにする、マルチメディア研究サークルの1プロジェクトです。

主担当は[伊藤](https://github.com/jujunjun110)と[いっちー](https://github.com/icchii0618)です。

## 問題意識

2016年ごろから、社員数の増加に伴い、混雑時にトイレの個室が埋まっておりなかなか利用できないケースが増えました。

このプロジェクトでは、トイレ個室の空き状況をセンサーで可視化し、自席などから確認できるようにすることにより、
トイレへの無駄足を避け、より**業務の生産性を高める**ことを目的にしています。

## 使っている機器
- [Raspberry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi)
- [近接センサー](https://www.pololu.com/product/2579)
- [Wifiドングル](https://www.amazon.co.jp/dp/B004AP8QKM)

## プライバシーについて
このプロジェクトで利用しているセンサーは**近接センサー**といい、「センサーから一定の距離に物があるかないか」を測定するもので、これによってドアの開閉を個室の空き状況として利用しています。

近接センサーによって、**個人の特定や、人の動作の特定をすることはできない**のでご安心ください。

また、メインマシンとして利用しているRaspberyPiという小型コンピューターにも、カメラ・マイクといったセンサーは付いていないので、**システム全体としてプライバシー情報を取得することは事実上不可能**です。

## プロジェクト名の由来

密教における明王の一尊であり、火神・**厠の神**として信仰される**烏枢沙摩明王**（うすさまみょうおう）から。（[詳細](https://ja.wikipedia.org/wiki/%E7%83%8F%E6%9E%A2%E6%B2%99%E6%91%A9%E6%98%8E%E7%8E%8B)）

