import os
from dotenv import load_dotenv
from runwayml import RunwayML

# .envファイルから環境変数を読み込む
load_dotenv()


def check_task_status(api_key, task_id):
    # APIクライアントを初期化
    client = RunwayML(api_key=api_key)

    # タスクの状態を取得
    task_status = client.tasks.retrieve(task_id)

    # タスクIDとステータスを抽出して表示
    task_id = task_status.id
    status = task_status.status
    print(f"タスクID: {task_id}, ステータス: {status}")

    # 状態を返す
    return status


# if __name__ == "__main__":
#     api_key = os.getenv("API_KEY")
#     task_id = "00eb86cc-dfc7-4be3-9b13-865da32ca8b5"  # 生成されたタスクIDを使用
#     status = check_task_status(api_key, task_id)
#     print(f"タスクの状態: {status}")
