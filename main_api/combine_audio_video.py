import moviepy.editor as mp
import os

def combine_audio_video(video_path, audio_path, output_path):
    # Load the video clip
    video_clip = mp.VideoFileClip(video_path)
    
    # Load the audio clip
    audio_clip = mp.AudioFileClip(audio_path)
    
    # Set the audio of the video clip
    video_clip = video_clip.set_audio(audio_clip)
    
    # Write the final video file
    video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
