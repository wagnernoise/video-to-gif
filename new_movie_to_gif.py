# importing libraries
import cv2
from moviepy.editor import *
from pygifsicle import optimize

# subprocess.run('ffmeg -i ' + gif_video + ' -vcodec libx264 -crf 22' + output) #TRY TO COMPRESS USING FFMEG. THIS SHOULD BE
# DONE AFTER THE GIF CREATION

video_path = "path_to_video.mp4"
gif_path = 'gif_path.gif'

clip = (VideoFileClip(video_path)
        .subclip()
        .resize(0.3))
clip.write_gif(gif_path)

# Open the created gif. It's not a necessary step but it's cool :)
# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('gif_path')

# Check if camera opened successfully
if (cap.isOpened() == False):
        print("Error opening video file")

# Read until video is completed
while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:

                # Display the resulting frame
                cv2.imshow('Frame', frame)

                # Press Q on keyboard to exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                        break

        # Break the loop
        else:
                break

# When everything done, release
# the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

# Optimize the gif size
optimize(gif_path)
