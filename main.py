from email.mime import audio
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os, random, shutil

path = input('Enter the destination of video to rename :')
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.mp4'])))

dir_path = input('Enter the destination of audio to rename :')
files = os.listdir(dir_path)


for index, file in enumerate(files):
    os.rename(os.path.join(dir_path, file), os.path.join(dir_path, ''.join([str(index), '.mp3'])))




n=int(input('Enter the no of videos :'))
vid=[]
audio_list=[]
outputnames=[]


count = 0
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print('File count:', count)

for jk in range(count):
    aud_1='music/' + str(jk) + '.mp3'
    audio_list.append(aud_1)

print(audio_list)


for ak in range(n):
    vid_1='video/' + str(ak) + '.mp4'
    vid.append(vid_1)

    out_1='output/' + str(ak) + '.mp4'
    outputnames.append(out_1)


print(vid) 
print("-----------------------------------------------------------")
print(outputnames) 
print("-----------------------------------------------------------")
print(audio_list) 
print("-----------------------------------------------------------")

# ---- start [to choose the vid file]
i=0
while (i<n):
    vid1=vid[i]
    print(vid1)
# ---- end

    # ---- to choose the audio file
    audio=random.choice(audio_list)
    print(audio)
    # ---- end

    # ---- to combine audio and video
    ffmpeg_extract_subclip(audio,0, 5, targetname="shorter_audio.mp3")
    audio=mp.AudioFileClip("shorter_audio.mp3")
    video=mp.VideoFileClip(vid1)
    clip = video.subclip(0, 5)
    final=clip.set_audio(audio)
    # --- end


    # --- to name output file
    out=outputnames[i]
    print(out)
    final.write_videofile(out)
    # --- end

    i+=1
    print(i)





        