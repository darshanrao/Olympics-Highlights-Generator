import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

def merge_videos_from_directory(directory_path, output_file="merged_videos.mp4"):
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

# Example usage:
# directory_path = "path_to_your_directory"  # Replace with your directory path
# merge_videos_from_directory(directory_path, output_file="final_merged.mp4")



def extract_subclip(video_path, start_time, end_time, output_file="subclip.mp4"):
    # Load the video
    clip = VideoFileClip(video_path)

    # Extract the subclip
    subclip = clip.subclip(start_time, end_time)

    # Write the subclip to the output file
    subclip.write_videofile(output_file, codec="libx264")

    # Close the clips to release resources
    clip.close()
    subclip.close()

    print(f"Subclip saved as {output_file}")

# Example usage:
# video_path = "video1.mp4"  # Replace with your video path
# start_time = 5.0  # In seconds
# end_time = 15.0  # In seconds
# output_file = "extracted_subclip.mp4"  # Optional output filename

# extract_subclip(video_path, start_time, end_time, output_file)
