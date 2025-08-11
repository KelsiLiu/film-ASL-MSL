import os
import csv
import sys
from scenedetect import SceneManager, ContentDetector, VideoManager


def find_scenes(video_path, output_folder,threshold=27.5):
    # video name
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    # Output CSV paths
    output_scenes_csv = os.path.join(output_folder, "output_{}.csv".format(video_name))
    
    # Open our video, create a scene manager, and add a detector.
    video_manager = VideoManager([video_path])
    scene_manager = SceneManager()
    scene_manager = SceneManager()
    scene_manager.add_detector(
        ContentDetector(threshold=threshold))
    # Set downscale factor and start the video manager
    video_manager.set_downscale_factor()
    video_manager.start()
    # Detect all scenes in video from current position to end.
    scene_manager.detect_scenes(frame_source=video_manager)
    # `get_scene_list` returns a list of start/end timecode pairs
    scene_list = scene_manager.get_scene_list()
    # 视频频率
    framerate = video_manager.duration.framerate
    # 视频时长
    total_duration = video_manager.duration.frame_num / framerate
    # 镜头数
    num_shots = len(scene_list)
    # 各镜头帧数
    shot_lengths = [scene[1].get_frames() - scene[0].get_frames() for scene in scene_list]
    # 最短镜头帧数
    min_shot_length = min(shot_lengths)
    # 最短镜头时长
    min_shot_time_length = min_shot_length / framerate
    # 最长镜头帧数
    max_shot_length = max(shot_lengths)
    # 最长镜头时长
    max_shot_time_length = max_shot_length / framerate
    # 平均镜头帧数
    average_shot_length = sum(shot_lengths) / len(shot_lengths) if len(shot_lengths) > 0 else 0
    # 平均镜头时长
    average_shot_time_length = average_shot_length / framerate
    # 中值镜头帧数
    median_shot_length = sorted(shot_lengths)[len(shot_lengths) // 2]
    # 中值镜头时长
    median_shot_time_length = median_shot_length / framerate

    video_manager.release()
    # Save scene details to CSV
    with open(output_scenes_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames_scenes = ["电影名",  "总时长", "镜头数","最短镜头时长", 
                              "最长镜头时长", "平均镜头时长",  "中值镜头时长"]
        writer_scenes = csv.DictWriter(csvfile, fieldnames=fieldnames_scenes)

        writer_scenes.writeheader()

        writer_scenes.writerow({"电影名": video_name,
                                "总时长": round(total_duration, 2),
                                "镜头数": num_shots,
                                "最短镜头时长": round(min_shot_time_length,2),
                                "最长镜头时长": round(max_shot_time_length,2),
                                "平均镜头时长": round(average_shot_time_length,2),
                                "中值镜头时长": round(median_shot_time_length,2)})
    return 


if __name__ == "__main__":
    # Check if a video file path and output folder path are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <video_path> <output_folder>")
        sys.exit(1)

    # Get the video file path and output folder path from the command-line arguments
    video_path = sys.argv[1]
    output_folder = sys.argv[2]
    # video_path = "test.mp4"
    # output_folder = r"C:\Users\lenovo\Desktop\代码\视频时长"
    find_scenes(video_path, output_folder, threshold=27.75)
    print("success")
    