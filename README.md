# 🌟 Lambda Python テンプレート

AWS Lambda用のPythonプロジェクトテンプレートです。Python初心者でも使いやすいように基本的な機能を備えています。

## 📚 フォルダ構造の説明

```
lambda-python-template/
├── .github/              # GitHub関連の設定
│   ├── workflows/        # GitHub Actions（自動テスト等）の設定
│   └── PULL_REQUEST_TEMPLATE.md  # PRの雛形
├── src/                  # ソースコード
│   ├── handlers/         # Lambda関数のメイン処理
│   └── utils/           # 共通の便利機能
├── tests/               # テストコード
├── Makefile            # 開発用コマンドをまとめたファイル
├── setup.cfg           # Python関連ツールの設定ファイル
├── pyproject.toml      # Python関連ツールの設定ファイル
├── requirements.txt    # 本番環境用のパッケージリスト
└── requirements-dev.txt  # 開発環境用のパッケージリスト
```

## 🚀 はじめ方

### 1. 環境構築

```
# 1. 仮想環境を作成
python -m venv venv

# 2. 仮想環境を有効化
# Windowsの場合:
venv/Scripts/activate
# Mac/Linuxの場合:
source venv/bin/activate

# 3. 必要なパッケージをインストール
make install
# もしくは以下のコマンドを実行:
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 2. 開発の始め方

1. `src/handlers/main.py` にLambda関数のメイン処理を書きます
2. `src/utils/` に共通の機能を書きます
3. `tests/` にテストコードを書きます

### 3. よく使うコマンド（Makefileの使い方）

Makefileは開発でよく使うコマンドをまとめたものです。

```
# テストを実行
make test

# コードの形式をチェック
make lint

# コードの形式を自動修正
make format

# 一時ファイルを削除
make clean
```

### 4. 設定ファイルの説明

#### setup.cfg
- Pythonの各種ツール（flake8, coverage等）の設定ファイル
- 普段は変更する必要はありません

#### pyproject.toml
- Black（コードフォーマッター）やMyPy（型チェック）の設定ファイル
- 普段は変更する必要はありません

### 5. テストの書き方

```python
# tests/test_handler.py の例
def test_lambda_handler():
    """
    lambda_handler関数のテスト例
    """
    # テストの準備
    event = {}
    context = None
    
    # 関数の実行
    response = lambda_handler(event, context)
    
    # 結果の確認
    assert response['statusCode'] == 200
```

### 6. デプロイ方法

#### ローカルテスト（Docker使用）
```bash
# Dockerイメージのビルド
docker-compose build

# Dockerでの実行
docker-compose up
```

#### AWS環境への反映
1. AWSコンソールからLambda関数を作成
2. `src/handlers/main.py` をLambdaコンソールにアップロード
3. または、AWS CLIやTerraformを使用して自動デプロイ

## 🔧 トラブルシューティング

### よくあるエラーと解決方法

1. **"make: command not found"** が表示される場合
   - Windowsの場合: [Make for Windows](http://gnuwin32.sourceforge.net/packages/make.htm) をインストール
   - Macの場合: `xcode-select --install` を実行

2. **ImportError** が表示される場合
   - 仮想環境が有効になっているか確認
   - `pip install -r requirements.txt` を再実行

3. **テストが失敗する場合**
   - `make lint` でコードの形式をチェック
   - エラーメッセージを確認して該当箇所を修正

## 📝 その他の便利な機能

### 1. 型チェック
```bash
# 型の問題をチェック
mypy src tests
```

### 2. コードカバレッジの確認
```bash
# テストカバレッジレポートを生成
pytest --cov=src tests/
```

### 3. コードの自動整形
```bash
# Blackでコードを自動整形
black src tests
```


## ❓ 質問・サポート

- 変更したい内容はIssueを作成してください
- または、プロジェクトの管理者の柳本に直接連絡してください

