from moviepy.editor import VideoFileClip
from pydub import AudioSegment

# Extract audio from mp4 using moviepy
video = VideoFileClip("input.mp4")
audio_path = "mp3_output.mp3"
video.audio.write_audiofile(audio_path)

# Convert mp3 to aiff using pydub
sound = AudioSegment.from_file(audio_path, format="mp3")
output_path = "aiff_sound.aiff"
sound.export(output_path, format="aiff")

print(f"Audio successfully extracted and saved as {output_path}")
