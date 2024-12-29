import os
import subprocess

# 设置文件夹路径，这里可以替换为你自己的文件夹路径
folder_path = "/Users/lijinming/iCloud云盘（归档）/Desktop/学业/具身智能/project/coa_cvpr/static/videos"

# 获取文件夹内所有MP4文件
for filename in os.listdir(folder_path):
    if filename.endswith(".mp4"):
        # 构造完整文件路径
        input_file = os.path.join(folder_path, filename)
        os.makedirs("/Users/lijinming/iCloud云盘（归档）/Desktop/学业/具身智能/project/coa_cvpr/static/videos2", exist_ok=True)
        output_file = os.path.join("/Users/lijinming/iCloud云盘（归档）/Desktop/学业/具身智能/project/coa_cvpr/static/videos2",  filename)
        if os.path.exists(output_file):
            print(f"文件已存在: {output_file}")
            continue

        # 使用FFmpeg进行压缩
        ffmpeg_command = [
            "ffmpeg",
            "-i", input_file,  # 输入文件
            "-vcodec", "libx264",  # 使用H.264编码器
            "-crf", "28",  # 设置CRF值为28（压缩程度）
            "-preset", "fast",  # 设置编码速度
            output_file  # 输出文件路径
        ]

        # 执行FFmpeg命令
        subprocess.run(ffmpeg_command)

        print(f"压缩完成: {input_file} -> {output_file}")
