import requests
from twelvelabs import TwelveLabs
import time
from marengo_text_search.marengo_search import TwelveLabsSearch
import marengo_text_search.clip_fetch_and_synthesis
from marengo_text_search.decomposer import Decomposer
from marengo_text_search.choose_num_queries import extract_queries_within_time_limit
from gemini_utils import generate_text_with_gemini
from marengo_text_search.upload_video_clips import upload_video
from text2speech import generate_audio, adjust_audio_speed
from combine_audio_video import combine_audio_video
from youtube_publish import upload_video_to_youtube

import json
def summarize_video(videoId, user_prompt,time_var):
    
    
    totalwords = (150/60)*time_var
    
    res = False
    while res == False:
        res = error_handle(videoId, user_prompt)
        time.sleep(30)
    
    # Use Gemini to improve the generated commentary
    # gemini_res = generate_text_with_gemini(
    #     f"I will provide a user prompt and a given commentary. Improve the quality of details in the commentary. "
    #     f"User Prompt: {user_prompt}, Given Commentary: {res.data}"
    # )
    # import pdb; pdb.set_trace()
    
    full_prompt =f"""You are hired as a Native English Speaker and given a task to improvise of the rough script of a commentary and make it more smooth according to the given user task.
    Please respond only in JSON format with the key "output".

    Instructions
    - The generated script should have words within the domain given in the user prompt.
    - Make it more engaging and continuous.
    - Try to make the script for the time-limit given in the user prompt.
    - Don't include stage direction or visual cue.
    - The word limit of the new commentary should be {totalwords}
    
    Rough Commentary: 
    {res.data}
    
    User Prompt: 
    {user_prompt}
    """
    retries = 5
    
    result=""
    while len(result) == 0 and retries:
        retries -= 1
        sequence = generate_text_with_gemini(full_prompt)
        start_idx, end_idx = sequence.find('{'), sequence.find('}')
        if start_idx != -1 and end_idx != -1:
            valid_string = sequence[start_idx:end_idx+1]
            try:
                result = json.loads(valid_string.strip())['output']
                # import pdb; pdb.set_trace()
            except Exception as e:
                result = ''
        else:
            pass
    
    # Print and return the improved commentary
    print("ORIGINAL:",res.data)
    print("NEW:",result)
    return result
    
    
def error_handle(videoId, user_prompt):
    try:
        # Initialize the client for TwelveLabs API
        client = TwelveLabs(api_key="API_KEY")
        
        # Call the TwelveLabs API to generate text commentary based on the video
        res = client.generate.text(
            video_id=videoId,
            prompt="Generate commentary: Focus only on the players shown in the video and describe their significance in the video.",
            temperature=0.5
        )
        return res
    
    # Handle specific API-related errors or exceptions
    except Exception as e:
        print(e)
        return False
    

    
def generate_script(queryString):
    
    gemini_handler = Decomposer()
    time_var, query_text_list = gemini_handler.decompose(queryString)
    
    searcher = TwelveLabsSearch()
    # Call with a list of queries and a file name to save the combined results as JSON
    
    queries_list_of_list= searcher.query(query_text_list)
    results = extract_queries_within_time_limit(queries_list_of_list,time_limit=time_var)

    for idx, result in enumerate(results):
        print(result)
        video_info = TwelveLabsSearch.get_video_info(video_id=result['video_id'])
        video_url = video_info['hls']['video_url']
        
        marengo_text_search.clip_fetch_and_synthesis.download_and_crop_video(video_url, f'./data/multi_clips/output_f_{idx}.mp4', result['start'], result['end'])
        
    marengo_text_search.clip_fetch_and_synthesis.merge_videos_from_directory('./data/multi_clips')
    
    video_path = "./data/merged_video.mp4"
    audio_path = "./speech/speech.mp3"
    output_path = "./data/merged_video.mp4"
        
    video_id = upload_video(output_path)
    print("Video uploaded!")

    response = summarize_video(video_id, queryString,time_var)
    print("Summarization done!")

    speech_path = generate_audio(response)
    speech_path = adjust_audio_speed(speech_path, time_var)

    combine_audio_video(video_path, audio_path, './data/final_video.mp4')
        
    return "./data/final_video.mp4"

# print(summarize_video('670b6499c0f5f53791d8ea37'))

# print(generate_script("Focus a 90-second video about Turkish Sharpshooter Yusuf Dikec, describing his casual and unorthodox style and approach to the sport. Compare and contrast him to the more traditional competitors in this event. Make references to his backstory, including the potential that he might be a hitman."))
# print(summarize_video('670b6499c0f5f53791d8ea37', 'Focus a 90-second video about Turkish Sharpshooter Yusuf Dikec, describing his casual and unorthodox style and approach to the sport. Compare and contrast him to the more traditional competitors in this event. Make references to his backstory, including the potential that he might be a hitman.'))

# print(generate_script("Create a compelling 1-minute video describing why the degree of difficulty in an Olympic Gymnastics event can impact the judge's score as much as the execution of the routine."))
