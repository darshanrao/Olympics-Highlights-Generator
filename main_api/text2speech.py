from elevenlabs import save
from elevenlabs.client import ElevenLabs
from pydub import AudioSegment
import nest_asyncio
nest_asyncio.apply()

# Function to generate and save audio from given text and output path-
def generate_audio(text: str, voice: str = "Jessica") -> str:
    # List of available voices
    available_voices = ["Rachel", "Will", "Jessica"]
    
    # Check if the voice passed is valid
    if voice not in available_voices:
        raise ValueError(f"Invalid voice selection. Choose from {available_voices}.")
    
    # Initialize the ElevenLabs client
    client = ElevenLabs(
        api_key="sk_07dbd7a750ca397e42d63c1de71ca7b60687e455be19c83c",  # Defaults to ELEVEN_API_KEY
    )

    # Call to generate audio with the input text
    audio = client.generate(
        text=text,
        voice=voice,  # Dynamically use the selected voice
        model="eleven_multilingual_v2"
    )

    save_path = f'speech/speech.mp3'
    save(audio, save_path)

    return save_path


# Example usage with dynamic input and output path-
'''input_text = "Hello! I’m Anupam Atul Patil, currently pursuing my Master’s in Computer Science at USC..."
output_file_path = "output_tts.mp3"

print(generate_audio(input_text))'''



# Function to change the speed of an audio file and save the adjusted file
def adjust_audio_speed(input_file_path, target_duration):
    """
    Adjust the speed of an audio file to fit a desired duration.

    :param input_file_path: Path to the input MP3 file.
    :param target_duration: Desired duration in seconds.
    :return: Path to the saved output file.
    """
    # Load the MP3 file
    audio = AudioSegment.from_file(input_file_path)

    # Get the current duration of the audio file (in milliseconds)
    current_duration_ms = len(audio)

    target_duration*=1000
    # Calculate the speed factor
    speed_factor = current_duration_ms / target_duration

    # Function to change the speed
    def change_speed(sound, speed_factor):
        sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
            "frame_rate": int(sound.frame_rate * speed_factor)
        })
        return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

    # Adjust the speed
    adjusted_audio = change_speed(audio, speed_factor)

    output_file_path = f"speech/adjusted_{hash(input_file_path)}.mp3"

    # Export the adjusted audio to a new file
    adjusted_audio.export(output_file_path, format="mp3")

    return output_file_path

# Example usage:
'''output_path = adjust_audio_speed("speech/tts_6621438197872185942.mp3", 6)
print(f"Adjusted audio saved to: {output_path}")'''

