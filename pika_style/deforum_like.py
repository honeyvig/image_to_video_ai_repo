
import cv2

img = cv2.imread("../images/input.jpg")
h, w, _ = img.shape

out = cv2.VideoWriter("../output/pika_style.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'), 6, (w, h))

for i in range(30):
    frame = cv2.resize(img, None, fx=1+i*0.002, fy=1+i*0.002)
    out.write(frame[:h, :w])

out.release()
