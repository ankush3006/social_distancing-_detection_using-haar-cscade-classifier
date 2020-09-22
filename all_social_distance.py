import math
import cv2
def midpoint(ptA, ptB):
	return int((ptA[0] + ptB[0]) * 0.5), int((ptA[1] + ptB[1]) * 0.5)
img = cv2.imread('q4.JPG')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
#cap = cv2.VideoCapture(1)
while True:
    #a, img = cap.read()
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))
    ww=[]
    l = []
    lf = []
    C=[]
    CN=[]
    ht=[]
    hw=[]
    i = 1
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        s = str(i)  # Face No.
        cv2.putText(img, str(int(22500 / w)), (x + int(w / 2), y + int(h / 2)), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 255, 0), 2)
        cv2.putText(img, s, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    # Putting text in the detected faces
        we=[]
        ww=[]
        i += 1
        l = []
        ht = []
        C=[]
        l.append(x)
        l.append(y)
        ht.append(w)
        ht.append(h)
        C.append(int(x+w/2))
        C.append(int(y+h/2))
        lf.append(l)
        hw.append(ht)
        CN.append(C)
        we.append(22500/w)
        we.append(0)
        ww.append(we)
        print(l)
        print(ww)
        #print(ht)
        #print(C)
    print(lf)
    print(hw)
    #print(CN)
    close_person=""
    for i in range(len(lf)):
        for j in range(i+1,len(lf)):
            print(ww[i-1])
            #ds=4500/ww[i]
            #d=math.sqrt( ((lf[j][1]-lf[i][1])**2)+((lf[j][0]-lf[i][0])**2) )
            d = math.sqrt(((CN[j][1] - CN[i][1]) ** 2) + ((CN[j][0] - CN[i][0]) ** 2))
            #facedis=22500/ww[i+1][0]
            dis=int(d)
            sd=str(dis)+"mm"
            mx=max(hw[j][1],hw[i][1])
            mn=min(hw[j][1],hw[i][1])
            #print(mx)
            #print(mn)
            #print(ds)
            #cv2.putText(img, str(int(22500/ww[i+1][0])), (lf[j][1],lf[j][0] ), cv2.FONT_HERSHEY_SIMPLEX, .5,(0, 255, 0), 2)
            print("P",i+1,"- P",j+1,"=",d)
            if d<500 and mn>0.6*mx:
                close_person+="Person "+str(i+1)+" and Person "+str(j+1)+" ; "
                cv2.line(img, (CN[i][0],CN[i][1]), (CN[j][0],CN[j][1]),(0, 0, 255),2)
                (mX, mY) = midpoint((CN[i][0],CN[i][1]), (CN[j][0],CN[j][1]))
                #textpx=int((CN[j][1]+CN[i][1])/2)
                #textpy=int((CN[j][0]+CN[i][1])/2)
                print(mX)
                print(mY)
                cv2.putText(img,sd, (mX, mY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#close_person+=" are not following social distancing "
            else:
                cv2.line(img, (CN[i][0], CN[i][1]), (CN[j][0], CN[j][1]), (0, 255, 0), 2)
                cv2.putText(img, sd, (mX, mY), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    print(close_person)
    if cv2.waitKey(20) & 0xFF == ord('c'):
        file_name_path = '1.jpg'
        cv2.imwrite(file_name_path,img)
    cv2.imshow('Window_Name',img)
#cap.release()
cv2.destroyAllWindows()