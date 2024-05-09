import cv2 
import numpy as np 
import mediapipe as mp 
from keras.models import load_model 
import time
from firebase_admin import db

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

PushUpModelUD = load_model("Realtime\Pushup\PushUp_CounterModel_UD_5Layer.h5")
PushUpModelRW = load_model("Realtime\Pushup\PU_RW_model55.h5")

total_reps=0
total_Wreps=0
total_time=0
total_cal=0

class Levels:
    def __init__(self, Reps: int, Sets: int):
        self.Reps = Reps
        self.Sets = Sets
      
    def Perform_Workout(self, reps,setNum):
        if reps == self.Reps:
            msg= f"End of set {setNum+1} Take a break for 15 sec." 

        elif  setNum == self.Sets :
            msg = f"You completed the workout"
            
        else:
            msg = f"Reps {reps} From {self.Reps} in Set {setNum+1}"   
        return msg    


def Process_Frame(user_level):

    MODEL_PREDICTION_THRESHOLD = 0.65
    global total_reps, total_Wreps, total_time
    pRW ="Wrong"
    pred = "down"
    reps = 0
    Wreps=0
    setNum=0
    set_complet = False
    WK_complet = False
    Pause_detection= False
    Break_start = 0
    BreakTime = 15 
    BeginTime= 5
    Start = False
    prev_pose = None

    levels = [
        Levels(8,3),        # Beginner level: 8 reps, 3 sets
        Levels(12, 3),       # Intermediate level: 12 reps, 3 sets
        Levels(15, 3)        # Pro level: 15 reps, 3 sets
    ]

    cap = cv2.VideoCapture(0) 
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:

        start_time = time.time()
        Workout_time = 0

        while cap.isOpened():
            ret, image = cap.read()

            if not ret:
                break

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            image = cv2.resize(image,  (1250, 670))   
            
            if not Start:
                stopwatch = int(time.time() - start_time)
                cv2.rectangle(image,(410,200), (810,270),(153, 255, 255), -1)
                cv2.putText(image, f"Start in: {BeginTime - stopwatch} sec",  (475,245), 
                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2,cv2.LINE_AA)
                if stopwatch == BeginTime:
                    Start = True   

            try:
            
                if results.pose_landmarks and Pause_detection == False and Start == True:
        
                    lst = []
                    for i in results.pose_landmarks.landmark:
                        lst.append(i.x - results.pose_landmarks.landmark[0].x)
                        lst.append(i.y - results.pose_landmarks.landmark[0].y)

                    lst = np.array(lst).reshape(1, -1)
                    p = PushUpModelUD.predict(lst)
                    pRW = PushUpModelRW.predict(lst)


                    if p[0][0] > MODEL_PREDICTION_THRESHOLD:
                        pred = "up"
                    else:
                        pred = "down"

                        
                    if pRW[0][1]> MODEL_PREDICTION_THRESHOLD:
                        predRW ="Right"
                    else:
                        predRW = "Wrong"
                    

                    if p[0][np.argmax(p)] > MODEL_PREDICTION_THRESHOLD:
                        if prev_pose == "down" and pred == "up":
                           if predRW == "Right":
                              reps += 1 
                              total_reps+=1
                           else: 
                              Wreps += 1 
                              total_Wreps+=1
                        prev_pose = pred
                        
                        
                    if predRW == "Wrong": 
                       mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                                mp_drawing.DrawingSpec(color=(244, 117, 66), thickness=2, circle_radius=1), 
                                                mp_drawing.DrawingSpec(color=(34,34,178), thickness=2, circle_radius=1))
                    
                    else:
                       mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                                mp_drawing.DrawingSpec(color=(244, 117, 66), thickness=2, circle_radius=1), 
                                                mp_drawing.DrawingSpec(color=(113,179,60), thickness=2, circle_radius=1))   

                    # Choose a level
                    # 0 is Beginner level
                    # 1 is Intermediate level
                    # 2 is pro level 
                    
                    select_level = levels[user_level]
                    PerformanceMsg = select_level.Perform_Workout(reps, setNum)

                    if reps == select_level.Reps and pred == "down":
                        set_complet = True
                        setNum += 1
                        reps = 0 
                        Pause_detection = True            
                        if setNum != select_level.Sets:                        
                            Break_start = time.time()
                        else:
                            WK_complet = True 
                            WK_completMsg = select_level.Perform_Workout(reps, setNum)
    
                else: 
                
                    if set_complet:
                        stopwatch = int(time.time() - Break_start)
                        cv2.rectangle(image,(380,210), (850,270),(250, 206, 135), -1)
                        cv2.putText(image, f"Break Time: {BreakTime - stopwatch} sec",  (450,250), 
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2,cv2.LINE_AA)

                        if stopwatch == BreakTime:
                            Pause_detection = False
                            set_complet = False

                    if WK_complet:
                       cv2.rectangle(image,(340,200), (880,280),(155, 193, 139), -1)
                       cv2.putText(image, WK_completMsg,  (370,250), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2,cv2.LINE_AA)

                       cv2.imshow("window", image)
                       cv2.waitKey(5000) 
                       cap.release()
                       cv2.destroyAllWindows()

                Workout_time = int(time.time() - start_time)  
                total_time=Workout_time                       

        

                cv2.rectangle(image,(20,75), (500,120),(158, 171, 41), -1)
                cv2.putText(image, PerformanceMsg , (25, 105), 
                            cv2.FONT_HERSHEY_COMPLEX,0.7, (255, 255, 255), 1, cv2.LINE_AA)


                cv2.rectangle(image, (0, 0), (670, 50), (245, 117, 16), -1)

                
                cv2.putText(image, "WR Prediction", (15, 20), 
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image,str(predRW), (50, 40), 
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                

                cv2.putText(image, "Stage", (170, 20), 
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(pred) , (170, 40), 
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                

                cv2.putText(image, "Wrong Reps", (260, 20), 
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(Wreps), (290, 40), 
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                
                
                cv2.putText(image, "Reps", (390, 20), 
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(reps) , (400, 40), 
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                

                cv2.putText(image, "Set", (460, 20), 
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(setNum+1) , (470, 40), 
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                
                cv2.putText(image, "Workout Time", (520, 20), 
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, f"{Workout_time} seconds" , (530, 40), 
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)



            except Exception as e:
                print(f"Error: {e}")

            cv2.imshow("window", image)

            if cv2.waitKey(1) == 27 or cv2.getWindowProperty("window", cv2.WND_PROP_VISIBLE) < 1:
                break

    cap.release()
    cv2.destroyAllWindows()

    def cal_burpees_cal(cal_per_min, duration_min):
        global total_cal
        total_cal = cal_per_min * duration_min
        return total_cal

    ref = db.reference('/workout/wo-2/')
    data = ref.get()
    duration_min = Workout_time/60 
    cal_per_min = data["cal_per_min"]
    cal_burned = cal_burpees_cal(cal_per_min, duration_min)
    ref = db.reference('/workout/wo-2/report/re-2/cal')
    ref.set({
        'calorie': cal_burned
    })