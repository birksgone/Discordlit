# convert_csv_to_json.py
import csv
import json

csv_file_path = 'emojis.csv'
json_file_path = 'emoji_data.json'

data = []

try:
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        # 1行目をヘッダーとして辞書形式で読み込む
        csv_reader = csv.DictReader(csv_file)
        
        # ヘッダー（列名）のリストを取得
        headers = csv_reader.fieldnames
        
        # 最初の3つの列名だけを保持する
        if headers and len(headers) >= 3:
            keys_to_keep = headers[:3]
            print(f"Processing the first 3 columns: {keys_to_keep}")
        else:
            print("Error: The CSV file must have at least 3 columns.")
            exit() # エラーがあればプログラムを終了

        # 各行をループ処理
        for row in csv_reader:
            # 保持したいキーだけを使って新しい辞書を作成
            new_row = {key: row[key] for key in keys_to_keep}
            data.append(new_row)

    # JSONファイルとして書き出す
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2, ensure_ascii=False)

    print(f"Successfully converted the first 3 columns of {csv_file_path} to {json_file_path}!")

except FileNotFoundError:
    print(f"Error: The file {csv_file_path} was not found in the project directory.")