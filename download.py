from modelscope import snapshot_download

# 下载 Qwen2.5-1.5B-Instruct 模型到本地目录
model_dir = snapshot_download('qwen/Qwen2.5-1.5B-Instruct', cache_dir='./models')
print(f"模型已下载至: {model_dir}")