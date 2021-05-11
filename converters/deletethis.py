# def abcd():
#     import os
#
#     print(os.getcwd())
#     with open(f'{os.getcwd()}\\converters\\currencies\\USD.json') as file:
#         print(file.read())






































import os

name = input("Window name: ")
os.system("""ffmpeg -rtbufsize 1500M -f dshow -i audio="Stereo Mix (Realtek High Definition Audio)" -framerate 60 -pix_fmt yuv420p -profile:v baseline -y output2.mp4""")
