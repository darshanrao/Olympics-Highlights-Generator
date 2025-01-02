import subprocess
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

def download_and_crop_video(video_url, output_path, start_time, end_time):
    try:
        print(f"Loading video from {video_url}...")
        
        # Load the video directly from the URL using MoviePy
        clip = VideoFileClip(video_url)
        
        print(f"Cropping video from {start_time} to {end_time} seconds...")
        
        # Extract the subclip
        subclip = clip.subclip(start_time, end_time)
        
        # Write the subclip to the output file
        subclip.write_videofile(output_path, codec="libx264")
        
        print(f"Video cropped successfully and saved to {output_path}")
        
    except Exception as e:
        print("Error processing video:", str(e))
        
    finally:
        # Close the clips to release resources
        if 'clip' in locals():
            clip.close()
        if 'subclip' in locals():
            subclip.close()
            

def merge_videos_from_directory(directory_path, output_file="./data/merged_video.mp4"):
    # Get all MP4 files in the directory
    video_files = [f for f in os.listdir(directory_path) if f.endswith('.mp4')]
    video_files.sort()  # Sort to maintain a consistent order (optional)

    if not video_files:
        print("No MP4 files found in the directory.")
        return

    print(f"Found {len(video_files)} MP4 files. Merging...")

    # Load the video clips
    clips = [VideoFileClip(os.path.join(directory_path, f)) for f in video_files]

    # Merge all video clips
    final_clip = concatenate_videoclips(clips, method="compose")

    # Write the final merged video to the output file
    final_clip.write_videofile(output_file, codec="libx264")

    # Close all clips to release resources
    for clip in clips:
        clip.close()

    print(f"All videos have been merged into {output_file}")

# Example usage
# if __name__ == "__main__":
#     from marengo_search import TwelveLabsSearch

#     video_id = "66f1b1e84e302ab9f2e7ef20"
#     video_info = TwelveLabsSearch.get_video_info(video_id=video_id)

#     video_url = video_info['hls']['video_url']
#     output_file = "cropped_video.mp4"
#     start_time = 0.0  # In seconds
#     end_time = 15.0   # In seconds

    
#     download_and_crop_video(video_url, output_file, start_time, end_time)
