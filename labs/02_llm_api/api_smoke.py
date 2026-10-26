import os
from dotenv import load_dotenv
from openai import OpenAI

# 从 .env 读取配置（.env 已被 .gitignore 忽略，不会进 git）
load_dotenv()

workspace_id = os.getenv("DASHSCOPE_WORKSPACE_ID")
api_key = os.getenv("DASHSCOPE_API_KEY")

# 注意：你的 WORKSPACE_ID 已经是完整域名，直接拼 /compatible-mode/v1 即可
base_url = f"https://{workspace_id}/compatible-mode/v1"

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)

completion = client.chat.completions.create(
    # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    model="qwen3.5-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁？"},
    ],
)
print(completion.model_dump_json())
