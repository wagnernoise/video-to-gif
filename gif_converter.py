import imageio
import os

#Path to your video
videoclip = os.path.abspath('PATH TO YOUR VIDEO')

#Defining the function to transform video to gif
def gifmaker(input_path, target_format):
    #Setting the export path
    output_path = os.path.splitext(input_path)[0] + target_format
    print(f'Converting {input_path} to {output_path}')

    #Read the input video and get the metadata of fps
    reader = imageio.get_reader(input_path)
    fps = reader.get_meta_data()['fps']

    #Export the video as gif with the determined fps
    writer = imageio.get_writer(output_path, fps = fps)

    for frames in reader:
        writer.append_data(frames)
        #writer.append_data(frames[:, :, 1]) - convert to gray colors
        print(f'Frame {frames}')

    print('Done :)')
    writer.close()

gifmaker(videoclip, '.gif')
