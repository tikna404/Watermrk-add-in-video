from moviepy.editor import *

clip = VideoFileClip("demo.mp4").subclip(0,30)

txt_clip = TextClip("enjoy world!",fontsize=30,color="yellow")
txt_clip = txt_clip.set_position('center').set_duration(30)


video = CompositeVideoClip([clip,txt_clip])

video.write_videofile("enjoy.mp4")