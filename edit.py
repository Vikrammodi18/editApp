import cv2
import numpy as np
img = cv2.imread("model.jpg")
copyModel = np.copy(img)

def crop(copyModel):
    
    # print(copyModel.shape)1
    x1,y1,x2,y2 = 0,0,0,0
    def cropping(events,x,y,param,flag):
        nonlocal x1,y1,x2,y2

        if events == cv2.EVENT_LBUTTONDOWN:
            
            x1,y1 = x,y
   
        elif events == cv2.EVENT_LBUTTONUP: 
           
            x2,y2 = x,y
            x1, x2 = min(x1, x2), max(x1, x2)
            y1, y2 = min(y1, y2), max(y1, y2)
            cv2.rectangle(copyModel,(x1,y1),(x2,y2),(120,55,12),1)
            cv2.imshow("copyModel",copyModel)
            croped = np.zeros([abs(y2-y1),abs(x2-x1),3],np.uint8)

            for i in range(3):
                croped[:,:,i] = copyModel[y1:y2,x1:x2:,i]
            cv2.imshow("cropedImg",croped)
            


    copyModel = cv2.resize(copyModel,None,fx=0.3,fy=0.2)
    cv2.imshow("copyModel",copyModel)
    cv2.setMouseCallback("copyModel",cropping)
    cv2.waitKey(0)


def hsvChange(copyModel):
    copyModel = cv2.resize(copyModel,None,fx=0.3,fy=0.2)
    def onChange(x):
        pass
    hsvImg = cv2.cvtColor(copyModel,cv2.COLOR_BGR2HSV)
    
    H = hsvImg[:,:,0]
    S = hsvImg[:,:,1]
    V = hsvImg[:,:,2]
    # S = S+30
    

    
    cv2.namedWindow("track")
    cv2.resizeWindow("track",400,120)
    cv2.createTrackbar("HUE","track",50,360,onChange)
    cv2.createTrackbar("SATURATION","track",50,180,onChange)
    cv2.createTrackbar("VALUE","track",50,180,onChange)
    

    while(True):
        h_pos = cv2.getTrackbarPos("HUE","track")
        s_pos = cv2.getTrackbarPos("SATURATION","track")
        v_pos = cv2.getTrackbarPos("VALUE","track")
        # print(h_pos,s_pos,v_pos)
        inhancedH = cv2.add(H,h_pos-50)
        inhancedS = cv2.add(S,s_pos-50)
        inhancedV = cv2.add(V,v_pos-50)
        inhancedHSV = cv2.merge((inhancedH,inhancedS,inhancedV))
        inhancedImg = cv2.cvtColor(inhancedHSV,cv2.COLOR_HSV2BGR)
        cv2.imshow("output",inhancedImg)
        
        
        if cv2.waitKey(30) == ord('q'):
            break

def BGRchange(copyModel):

    copyModel = cv2.resize(copyModel,None,fx=0.3,fy=0.2)
    def onChange(x):
        pass
    B = copyModel[:,:,0]
    G = copyModel[:,:,1]
    R = copyModel[:,:,2]
    cv2.namedWindow('track')
    cv2.createTrackbar("Blue","track",100,255,onChange)
    cv2.createTrackbar("Green","track",100,255,onChange)
    cv2.createTrackbar("Red","track",100,255,onChange)
    while(True):
        b_pos = cv2.getTrackbarPos("Blue","track")
        g_pos = cv2.getTrackbarPos("Green","track")
        r_pos = cv2.getTrackbarPos("Red","track")
        b = cv2.add(B,(b_pos-100))
        g = cv2.add(G,(g_pos-100))
        r = cv2.add(R,(r_pos-100))
        inhancedImg = cv2.merge((b,g,r))
        cv2.imshow("editedImg",inhancedImg)
        if cv2.waitKey(30) == ord('q'):
            break



while(True):
    choice = int(input("Press \n1.crop\n2.brightess\n3.Change color\n"))
    if choice == 1:
        crop(copyModel)
        cv2.destroyAllWindows()
    elif choice == 2:
        hsvChange(copyModel)
        cv2.destroyAllWindows()
    elif choice == 3:
        BGRchange(copyModel)
        cv2.destroyAllWindows()
    
    stop = int(input("do you want to stop(0/1)"))
    if stop == 1:
        break



