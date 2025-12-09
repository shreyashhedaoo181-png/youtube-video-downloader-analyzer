from pytube import YouTube
import json
import os

def download_video(url, output_folder="downloads"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    yt = YouTube(url)

    print("Downloading:", yt.title)
    video = yt.streams.get_highest_resolution()
    video_path = video.download(output_folder)

    info = {
        "title": yt.title,
        "author": yt.author,
        "length_sec": yt.length,
        "views": yt.views,
        "rating": yt.rating,
        "description": yt.description,
        "download_path": video_path
    }

    with open(f"{output_folder}/video_info.json", "w", encoding="utf-8") as f:
        json.dump(info, f, indent=4)

    print("Download complete!")
    return info
