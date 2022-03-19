import cv2
cap = cv2.VideoCapture('‪F:\GOOD Test\sucai\1.mp4')
j=1
i=1
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps =cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter('F:/Processed Videos/' + str(j) + '.mp4', fourcc,fps, size)
while (True):
    ret, frame = cap.read()
i = i + 1
out.write(frame)
if (i % 1200== 0):
    j = j + 1
out = cv2.VideoWriter('F:/Processed Videos/' + str(j) + '.mp4', fourcc, fps, size)
cv2.imshow('frame', frame)

cap.release()
out.release()
cv2.destroyAllWindows()