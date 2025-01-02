from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx
import numpy as np
from PIL import Image, ImageEnhance

def apply_standard_filters(video_path, choice) ->str:
    # Load the video file
    video = VideoFileClip(video_path)
    
    # Apply the selected filter
    if choice == 1:
        # Black & White filter
        filtered_video = video.fx(vfx.blackwhite)
    elif choice == 2:
        # Sepia filter
        def sepia(image):
            # Convert image to sepia
            sepia_filter = np.array([[0.393, 0.769, 0.189],
                                     [0.349, 0.686, 0.168],
                                     [0.272, 0.534, 0.131]])
            return Image.fromarray((np.dot(np.array(image), sepia_filter.T)).clip(0, 255).astype(np.uint8))

        filtered_video = video.fl_image(sepia)
    elif choice == 3:
        # Vignette filter
        def vignette(image):
            # Create a vignette effect by darkening the corners
            height, width = image.shape[:2]
            X, Y = np.ogrid[:height, :width]
            center_x, center_y = width // 2, height // 2
            radius = np.sqrt((X - center_y)**2 + (Y - center_x)**2) / np.sqrt(center_x**2 + center_y**2)
            mask = 1 - np.clip(radius, 0, 1)
            vignette_image = image * mask[..., np.newaxis]
            return vignette_image.astype(np.uint8)
        
        filtered_video = video.fl_image(vignette)

    else:
        print("Invalid choice. No filter applied.")
        return
    
    # Generate output file name
    output_path = f"./media/{hash(video_path)}_filtered.mp4"
    # output_path = video_path.replace(".mp4", f"{hash(video_path)}_filtered.mp4")
    
    # Save the edited video
    filtered_video.write_videofile(output_path, codec="libx264")
    
    print(f"Filter applied and video saved as {output_path}")

    return output_path

# Example usage
#apply_standard_filters("scene.mp4", 1)
