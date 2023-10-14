from pathlib import Path
from moviepy.editor import VideoFileClip

class Converter:
    def __init__(self):
        self.files_list = []
        self.dir_op = ""
 
    def convert(self, path_video, output_file, extension="mp3"):
        # try:
        #     video = VideoFileClip(str(path_video))  # Convert path to string
        #     video.fps = 30
        #     audio_clip = video.audio

        #     audio_clip.write_audiofile(output_file, codec=extension)
        # except Exception as e: 
        #     print(f"[-] Error Converting files: {e}")

        video = VideoFileClip(str(path_video))  # Convert path to string
        audio_clip = video.audio
        audio_clip.write_audiofile(output_file, codec=extension)



    def get_files_list(self) -> list:
        dir_location = Path(self.dir_op)
        path_list = []
        for video_location in dir_location.glob("*.mp4"):
            if video_location.is_file():
                path_list.append(video_location)
        return path_list

    def write_files(self):
        video_paths = self.get_files_list()
        output_directory = Path(self.dir_op) / "output"
        output_directory.mkdir(parents=True, exist_ok=True)
        
        for video in video_paths:
            output_file = output_directory / (video.stem + ".mp3")
            # print(output_file)
            self.convert(video, output_file)

def main():
    ci = Converter()
    ci.dir_op = "/mnt/c/Users/suyog/Desktop/music/test"
    ci.write_files()

if __name__ == "__main__":
    main()