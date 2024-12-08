import os
import time
from dotenv import load_dotenv
from i2v import generate_video_from_image
from checkstatus import check_task_status
from getvideo import download_video

# .envファイルから環境変数を読み込む
load_dotenv()


def main():
    api_key = os.getenv("API_KEY")
    # ここでURLではなくローカルファイルのパスを使うよ
    prompt_image_path = "/Users/hikarimac/Documents/python/runway/watercolor (medium),{alphonse_(white_datura)},miv4t,[[tianliang duohe fangdongye s-3199027925.png"
    prompt_text = "A group of four anime characters standing in a lush forest. The characters are wearing traditional Japanese kimonos, each with unique colors and patterns. The scene is vibrant and full of greenery, with sunlight filtering through the leaves."
    download_path = "/Users/hikarimac/Documents/python/runway/output/"

    # 画像からビデオを生成するタスクを作成
    task_id = generate_video_from_image(api_key, prompt_image_path, prompt_text)
    print(f"生成されたタスクID: {task_id}")

    # ステータスがサクセスするまで1分おきに確認
    while True:
        status = check_task_status(api_key, task_id)
        if status == "SUCCEEDED":
            print("タスクが成功しました！")
            # ビデオをダウンロード
            download_video(api_key, task_id, download_path)
            break
        elif status == "FAILED":
            print("タスクが失敗しました。")
            break
        else:
            print("タスクのステータスを確認中...")
            time.sleep(60)  # 1分待機


if __name__ == "__main__":
    main()
