#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2

cap = cv2.VideoCapture(0)

#line1
coor1=(0,250)
coor2=(700,250)
color1=(0,255,0)
thickness=2

#line2
coor3=(310,0)
coor4=(310,500)

#circle
center_coordinates=(310,250)
radius=120
color2=(0,0,255)

#rectangle
start=(10,470)
end=(240,410)
color3=(255,255,255)

#text
text='Felix Filipi'
coor5=(10,450)
font=cv2.FONT_HERSHEY_SIMPLEX
fontScale=1.5
color4=(255,0,0)

if cap.isOpened(): # init first frame
    rval, frame = cap.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = cap.read()
    key = cv2.waitKey(0) #press any button (except ESC to read cap)
    if key == 27: # exit on ESC
        break
    else:
        #cv2.line(img,(x1,y1),(x2,y2),color,thickness)
        cv2.line(frame, coor1, coor2, color1, thickness)
        cv2.line(frame, coor3, coor4, color1, thickness)
        cv2.circle(frame, center_coordinates, radius, color2, thickness)
        cv2.rectangle(frame, start, end, color3, -1)
        cv2.putText(frame,'Felix Filipi',coor5,font,fontScale,color4,thickness,cv2.LINE_AA)

cap.release()
cv2.destroyAllWindows()   

