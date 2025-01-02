from marengo_text_search.marengo_search import TwelveLabsSearch
import marengo_text_search.clip_fetch_and_synthesis
from marengo_text_search.decomposer import Decomposer

from marengo_text_search.choose_num_queries import extract_queries_within_time_limit
from marengo_text_search.upload_video_clips import upload_video
from genScript import summarize_video
from text2speech import generate_audio
from combine_audio_video import combine_audio_video
from youtube_publish import upload_video_to_youtube

# Define a sample input prompt
sample_prompt = "Focus a 90-second video about Turkish Sharpshooter Yusuf Dikec, describing his casual and unorthodox style and approach to the sport. Compare and contrast him to the more traditional competitors in this event. Make references to his backstory, including the potential that he might be a hitman."

# Call the decomposer method with the sample prompt
gemini_handler = Decomposer()
time_var, query_text_list = gemini_handler.decompose(sample_prompt)


searcher = TwelveLabsSearch()
# Call with a list of queries and a file name to save the combined results as JSON
queries_list_of_list= searcher.query(query_text_list)
# import pdb; pdb.set_trace()
results = extract_queries_within_time_limit(queries_list_of_list,time_limit=time_var)

# print(results)

video_urls = []
for idx, result in enumerate(results):
    print(result)
    video_info = TwelveLabsSearch.get_video_info(video_id=result['video_id'])
    video_url = video_info['hls']['video_url']
    
    marengo_text_search.clip_fetch_and_synthesis.download_and_crop_video(video_url, f'./data/multi_clips/output_f_{idx}.mp4', result['start'], result['end'])
    
marengo_text_search.clip_fetch_and_synthesis.merge_videos_from_directory('./data/multi_clips', './data/merged_video.mp4')
 

video_path = "./data/merged_video.mp4"
audio_path = "./speech/speech.mp3"
output_path = "./data/merged_video.mp4"
    
video_id = upload_video(output_path)
print("Video uploaded!")

response = summarize_video(video_id, sample_prompt, time_var)
print("Summarization done!")

speech_path = generate_audio(response)
print("Audio generated!")

combine_audio_video(video_path, audio_path, './data/final_video.mp4')

upload_video_to_youtube('./client_secrets.json', video_path='./data/final_video.mp4', title ='Olympics Highlights!', description="Placeholder")