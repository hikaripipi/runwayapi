import os
import base64
from dotenv import load_dotenv
from runwayml import RunwayML

# .envファイルから環境変数を読み込む
load_dotenv()


def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_image


def generate_video_from_image(api_key, prompt_image_path, prompt_text):
    # APIクライアントを初期化
    client = RunwayML(api_key=api_key)

    # 画像をbase64エンコードしてデータURIを作成
    encoded_image = encode_image_to_base64(prompt_image_path)
    data_uri = f"data:image/png;base64,{encoded_image}"

    # 画像からビデオを生成するタスクを作成
    task = client.image_to_video.create(
        model="gen3a_turbo",
        prompt_image=data_uri,
        prompt_text=prompt_text,
    )

    # タスクIDを返す
    return task.id


# # 関数を呼び出す
# if __name__ == "__main__":
#     api_key = os.getenv("API_KEY")
#     task_id = generate_video_from_image(
#         api_key,
#         "/Users/hikarimac/Documents/python/runway/watercolor (medium),{alphonse_(white_datura)},miv4t,[[tianliang duohe fangdongye s-3199027925.png",
#         "A group of four anime characters standing in a lush forest. The characters are wearing traditional Japanese kimonos, each with unique colors and patterns. The scene is vibrant and full of greenery, with sunlight filtering through the leaves.",
#     )
#     print(f"生成されたタスクID: {task_id}")
