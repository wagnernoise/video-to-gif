import imageio
import os
import subprocess

# Path to your video
videoclip = os.path.abspath("Triaxis.mp4")


# Defining the function to transform video to gif
def gifmaker(input_path, target_format, output_video=None):
    # Setting the export path
    output_path = os.path.splitext(input_path)[0] + target_format
    print(f'Converting {input_path} to {output_path}')
    subprocess.run('ffmeg -i ' + input_path + ' -vcodec libx264 -crf 22' + output_video)

    # Read the input video and get the metadata of fps
    reader = imageio.get_reader(output_video)
    fps = reader.get_meta_data()['fps']

    # Export the video as gif with the determined fps
    writer = imageio.get_writer(output_path, fps=fps)

    for frames in reader:
        writer.append_data(frames)
        # writer.append_data(frames[:, :, 1]) - convert to gray colors
        print(f'Frame {frames}')

    print('Done :)')
    writer.close()


gifmaker(videoclip, '.gif', 'compressed.mp4')
