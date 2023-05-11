from pytube import YouTube

# Set the save path where the video will be saved
SAVE_PATH = "D:/youtube"

# Link of the video to be downloaded
link = "https://www.youtube.com/watch?v=Y8Tko2YC5hA"

try:
    # Create a YouTube object for the video
    yt = YouTube(link)

    # Get the highest resolution video stream
    video_stream = yt.streams.get_highest_resolution()

    # Set the filename for the downloaded video
    video_filename = "01.mp4"

    # Download the video to the specified directory
    video_stream.download(output_path=SAVE_PATH, filename=video_filename)

    print('Task Completed!')

except Exception as e:
    print("Some Error!")
    print(e)
