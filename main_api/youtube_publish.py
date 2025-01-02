import httplib2
import os
import random
import time

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow

# Define constants and configurations
httplib2.RETRIES = 1
MAX_RETRIES = 10
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError)
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]
VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")
YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"

def upload_video_to_youtube(client_secrets_file, video_path, title, description,
                            category_id='22', keywords='', privacy_status='public'):
    """
    Uploads a video to YouTube.

    Parameters:
    - client_secrets_file: Path to the client_secrets.json file.
    - video_path: Path to the video file.
    - title: Title of the video.
    - description: Description of the video.
    - category_id: YouTube category ID (default '22' for People & Blogs).
    - keywords: Comma-separated list of keywords.
    - privacy_status: Video privacy status ('public', 'private', 'unlisted').

    Returns:
    - None
    """

    # Authenticate and construct service
    youtube = get_authenticated_service(client_secrets_file)

    # Prepare video metadata
    tags = keywords.split(',') if keywords else None
    body = dict(
        snippet=dict(
            title=title,
            description=description,
            tags=tags,
            categoryId=category_id
        ),
        status=dict(
            privacyStatus=privacy_status
        )
    )

    # Create MediaFileUpload object
    media_body = MediaFileUpload(video_path, chunksize=-1, resumable=True)

    # Initiate the upload
    insert_request = youtube.videos().insert(
        part=','.join(body.keys()),
        body=body,
        media_body=media_body
    )

    # Execute the upload
    resumable_upload(insert_request)

def get_authenticated_service(client_secrets_file):
    flow = flow_from_clientsecrets(
        client_secrets_file,
        scope=YOUTUBE_UPLOAD_SCOPE
    )
    storage = Storage(f"{os.path.splitext(client_secrets_file)[0]}-oauth2.json")
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage)
    return build("youtube", "v3", credentials=credentials)

def resumable_upload(request):
    response = None
    error = None
    retry = 0
    while response is None:
        try:
            print("Uploading file...")
            status, response = request.next_chunk()
            if response is not None:
                if 'id' in response:
                    print(f"Video id '{response['id']}' was successfully uploaded.")
                else:
                    print(f"The upload failed with an unexpected response: {response}")
                    return
        except HttpError as e:
            if e.resp.status in RETRIABLE_STATUS_CODES:
                error = f"A retriable HTTP error {e.resp.status} occurred:\n{e.content}"
            else:
                print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")
                return
        except RETRIABLE_EXCEPTIONS as e:
            error = f"A retriable error occurred: {e}"

        if error is not None:
            print(error)
            retry += 1
            if retry > MAX_RETRIES:
                print("No longer attempting to retry.")
                return
            sleep_seconds = random.uniform(0, 2 ** retry)
            print(f"Sleeping {sleep_seconds} seconds and retrying...")
            time.sleep(sleep_seconds)
            error = None


# upload_video_to_youtube('./client_secrets.json', video_path='./data/final_video.mp4', title ='Olympics Highlights!', description="Placeholder")