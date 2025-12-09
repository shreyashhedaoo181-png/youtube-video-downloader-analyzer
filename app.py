from downloader import download_video
from analyzer import analyze_video_info

print("\n📥 YouTube Video Downloader + Analyzer\n")

url = input("Enter YouTube video URL: ")

info = download_video(url)

analysis = analyze_video_info()

print("\n🎯 Video Analysis:")
print("Title:", analysis["title"])
print("Author:", analysis["author"])
print("Views:", analysis["views"])
print("Top Words in Description:", analysis["top_words_in_description"])
