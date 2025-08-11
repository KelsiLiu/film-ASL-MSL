pip install opencv-python scenedetect
# 导入核心算法模块
from shot_detection import calculate_asl_msl

# 分析视频文件
asl, msl = calculate_asl_msl("your_video.mp4")

# 输出结果
print(f"平均切变长度 (ASL): {asl:.2f} 秒")
print(f"最大切变长度 (MSL): {msl:.2f} 秒")
calculate_asl_msl(
    video_path,       # 视频文件路径(必需)
    threshold=30.0,   # 切变检测敏感度(默认30)
    min_shot_len=15   # 最小切变长度(帧数，默认15)
检测到 142 个切变点
平均切变长度 (ASL): 2.37 秒
最大切变长度 (MSL): 8.92 秒
