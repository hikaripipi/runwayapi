import os
from dotenv import load_dotenv
from datetime import datetime

# .envファイルから環境変数を読み込む
load_dotenv()


def download_video(api_key, task_id, download_dir):
    import requests
    from runwayml import RunwayML

    # APIクライアントを初期化
    client = RunwayML(api_key=api_key)

    # タスクの結果を取得
    task_result = client.tasks.retrieve(task_id)

    # 動画のURLを取得
    video_url = task_result.output[0]  # 出力の最初のURLを取得

    # ダウンロード日時を取得
    download_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    # ファイル名をフォーマット
    file_name = f"{download_time}_{task_id}.mp4"
    download_path = os.path.join(download_dir, file_name)

    # 動画をダウンロード
    response = requests.get(video_url)
    with open(download_path, "wb") as file:
        file.write(response.content)

    print(f"{file_name} がダウンロードされました！")


# if __name__ == "__main__":
#     api_key = os.getenv("API_KEY")
#     task_id = "00eb86cc-dfc7-4be3-9b13-865da32ca8b5"  # ここにタスクIDを入れてね
#     download_path = "/Users/hikarimac/Documents/python/runway/output/output_video.mp4"  # ダウンロード先のパスを指定してね

#     download_video(api_key, task_id, download_path)
