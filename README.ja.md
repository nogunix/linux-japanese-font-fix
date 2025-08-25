# Linux Japanese Font Fix

[English](./README.md) | [日本語](./README.ja.md)

日本語以外のロケールを使用している Fedora システムで発生しがちな日本語フォントの表示不具合（いわゆる「中華フォント問題」）を解消するための、堅牢な Fontconfig 設定です。

## 背景

Fedora を日本語以外のロケール（例: 英語）で新規インストールすると、日本語の文字表示に中国語フォントが優先的に使われてしまうことがあります。
これは、デフォルトのフォント優先順位が日本語向けに最適化されていないためで、その結果、`直` や `骨` などの漢字が本来の日本語の字形では表示されなくなります。

この問題は **Fedora 38 以降**（Fedora 42 を含む）で確認されています。
原因は、Noto CJK フォントパッケージが、日本語・中国語・韓国語のグリフを単一のバリアブルフォントファイルに統合していることにあります。
日本語以外のロケール環境では、Fontconfig が日本語テキストに対して誤ったグリフを選択する可能性があります。

詳細は [Fedora Project Wiki: Noto CJK Variable Fonts](https://fedoraproject.org/wiki/Changes/Noto_CJK_Variable_Fonts) を参照してください。

## 修正前と修正後

**修正前（日本語テキストに中国語の字形が使われている例）:**

![Fedora rendering Japanese text with incorrect Chinese glyphs](./images/before.png)

**修正後（正しい日本語の字形が使われている例）:**

![Fedora rendering Japanese text with correct Japanese glyphs](./images/after.png)

## 解決方法

この設定ファイル（`50-user-jp-fonts.conf`）は、日本語の表示に高品質な Noto CJK JP フォントを強制的に使用させます。

- **Web ブラウジング向け:** 汎用フォントファミリー `sans-serif` と `serif` にそれぞれ `Noto Sans CJK JP` と `Noto Serif CJK JP` を割り当て、ブラウザで安定した日本語表示を実現します。
- **開発者向け:** コード（ラテン文字や記号）の可読性を重視して `Noto Sans Mono` を優先し、日本語コメントなどには `Noto Sans Mono CJK JP` へシームレスにフォールバックする設定を行います。

> **注意:** この設定は、`Noto Sans Mono` がデフォルトの等幅フォントである環境（Fedora では一般的）を想定しています。
> 確認するには次を実行してください:
> ```bash
> fc-match monospace
> ```
> 出力が `DejaVu Sans Mono` など異なる場合は、`50-user-jp-fonts.conf` 内の `Noto Sans Mono` を実際のフォント名に置き換えてください。

## 前提条件

対象は **Fedora 38 以降** です。
Noto CJK バリアブルフォントをインストールしておく必要があります。

**Fedora でのインストール例:**
```bash
sudo dnf install google-noto-sans-cjk-vf-fonts google-noto-serif-cjk-vf-fonts google-noto-sans-mono-fonts google-noto-sans-mono-cjk-vf-fonts
```

## インストール手順

1. リポジトリをクローンして、ディレクトリに移動します:
   ```bash
   git clone https://github.com/nogunix/linux-japanese-font-fix.git
   cd linux-japanese-font-fix
   ```

2. 設定ディレクトリがなければ作成します:
   ```bash
   mkdir -p ~/.config/fontconfig/conf.d
   ```

3. 設定ファイルをコピーします:
   ```bash
   cp 50-user-jp-fonts.conf ~/.config/fontconfig/conf.d/
   ```

4. フォントキャッシュを再構築します:
   ```bash
   fc-cache -fv ~/.config/fontconfig
   ```
   *(ディレクトリを指定すると、システム全体をスキャンするより高速に再構築できます)*

5. アプリケーションを再起動、またはログアウト・再ログインして変更を反映します。

### Copr経由でのインストール

Coprリポジトリから直接この設定をインストールできます。

1.  **Coprリポジトリを有効にする:**
    ```bash
    sudo dnf copr enable nogunix/linux-japanese-font-fix
    ```

2.  **パッケージをインストールする:**
    ```bash
    sudo dnf install linux-japanese-font-fix
    ```

3.  **フォントキャッシュを再構築する:**
    ```bash
    sudo fc-cache -fv
    ```
    *(この手順はRPMのインストール後スクリプトによって自動的に処理されますが、明確にするために含めることをお勧めします。)*

4.  アプリケーションを再起動するか、ログアウト・再ログインして変更を適用します。

## 適用確認

次のコマンドで設定が反映されているか確認できます:
```bash
fc-match 'sans:lang=ja'
fc-match 'serif:lang=ja'
fc-match 'monospace:lang=ja'
```

想定される出力例:
```
NotoSansCJK-VF.ttc: "Noto Sans CJK JP" "Regular"
NotoSerifCJK-VF.ttc: "Noto Serif CJK JP" "Regular"
NotoSansMonoCJK-VF.ttc: "Noto Sans Mono CJK JP" "Regular"
```

フォールバック順を確認するには:
```bash
fc-match -s 'monospace:lang=ja' | head -n 5
```

## アンインストール手順

1. 設定ファイルを削除します:
   ```bash
   rm -f ~/.config/fontconfig/conf.d/50-user-jp-fonts.conf
   ```

2. フォントキャッシュを再構築します:
   ```bash
   fc-cache -fv ~/.config/fontconfig
   ```

3. アプリケーションを再起動、またはログアウト・再ログインして元のフォント設定に戻します。

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。