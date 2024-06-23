import cv2
import numpy as np

video_name = 'scrolling_text.mp4'
frame_width = 100
frame_height = 100
frame_rate = 144

text = input('Введите строку: ')
speed = float(input('Введите скорость (пикселей в секунду): '))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(video_name, fourcc, frame_rate, (frame_width, frame_height))

font = cv2.FONT_ITALIC
font_thickness = 3

font_scale = frame_height / 50  
text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
text_height = text_size[1]
text_y = (frame_height + text_height) // 2

text_x_start = frame_width
text_x_end = -text_size[0]

distance = text_x_start - text_x_end
duration = distance / speed+0.5

num_frames = int(frame_rate * duration)
dx = speed / frame_rate

for i in range(num_frames):
    frame = np.full((frame_height, frame_width, 3), (128, 0, 128), dtype=np.uint8)
    text_x = int(text_x_start - i * dx)
    cv2.putText(frame, text, (text_x, text_y), cv2.FONT_ITALIC, font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)
    video.write(frame)

video.release()
cv2.destroyAllWindows()
