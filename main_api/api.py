from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
from typing import Optional
from firebase_utils import FirebaseStorageSingleton
from datetime import datetime, timedelta
import nest_asyncio
nest_asyncio.apply()
from genScript import summarize_video, generate_script
from text2speech import generate_audio
from fastapi.middleware.cors import CORSMiddleware

#sample firebase usage-
'''firebase_storage = FirebaseStorageSingleton()

# Get the storage bucket
bucket = firebase_storage.get_bucket()

print(bucket)
try:
    # Upload the file
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename('scene.mp4')
    print(f"File {'scene.mp4'} uploaded to {destination_blob_name}.")
except Exception as e:
    print(f"An error occurred while uploading the file: {str(e)}")

try:
 # Generate signed URL
    expires_at = datetime.now() + timedelta(days=7)  # URL expires in 7 days
    signed_url = blob.generate_signed_url(expires_at)
    print(f"Signed URL: {signed_url}")
    
except Exception as e:
    print(f"An error occurred: {str(e)}")
'''

app = FastAPI(title="Video Generation API",debug=True)
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to specific origins if needed
    allow_credentials=False,
    allow_methods=["*"],  # Adjust this if you want to restrict methods
    allow_headers=["*"],  # Adjust this if you want to restrict headers
)

class TextQuery(BaseModel):
    text: str
    style: Optional[str] = "default"

class VideoResponse(BaseModel):
    video_url: str

# Simulated blackbox methods
'''def generate_script(text: str) -> str:
    # Placeholder for your script generation logic
    video_path = generate_script(text=text)
    return video_path'''

async def create_voiceover(script: str) -> str:
    # Placeholder for your voiceover generation logic
    await asyncio.sleep(0.5)  # Simulating processing time
    return f"voiceover_file_{hash(script)}.mp3"

async def compile_video(script: str, voiceover_file: str) -> tuple[str, float]:
    # Placeholder for your video compilation logic
    await asyncio.sleep(0.3)  # Simulating processing time
    return f"video_{hash(script)}.mp4", len(script) / 20  # Dummy duration calculation

@app.post("/generate-video", response_model=VideoResponse)
async def generate_video(query: TextQuery):
    try:
        # Generate script from input text
        path = generate_script(query.text)
        print(path)
        firebase_storage = FirebaseStorageSingleton()

        # Get the storage bucket
        bucket = firebase_storage.get_bucket()

        print(bucket)
        try:
            # Upload the file
            destination_blob_name = path.split('/')[-1]
            blob = bucket.blob(destination_blob_name)
            blob.upload_from_filename(path)
            print(f"File {path} uploaded to {destination_blob_name}.")
        except Exception as e:
            print(f"An error occurred while uploading the file: {str(e)}")

        try:
        # Generate signed URL
            expires_at = datetime.now() + timedelta(days=7)  # URL expires in 7 days
            signed_url = blob.generate_signed_url(expires_at)
            print(f"Signed URL: {signed_url}")
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        
        # Generate voiceover from script
        # voiceover_file = await create_voiceover(script)
        
        # # Compile final video
        # video_url, duration = await compile_video(script, voiceover_file)
        
        return VideoResponse(video_url=signed_url)
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
