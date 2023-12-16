# 基本イメージとしてPythonを使用
FROM python:3.9

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係のインストール
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコピー
COPY . /app

# Uvicornを使用してアプリケーションを実行
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
