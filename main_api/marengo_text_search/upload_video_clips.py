from twelvelabs import TwelveLabs
from twelvelabs.models.task import Task

def upload_video(file):
    client = TwelveLabs(api_key="API_KEY")

    task = client.task.create(
      index_id="670c03c94f6c89db01c65be5",
      file = file         #"./data/merged_video.mp4"
      # file = "C:/Users/shard/Videos/Captures/sample_video.mp4"
    )
      
    return task.video_id 
  
