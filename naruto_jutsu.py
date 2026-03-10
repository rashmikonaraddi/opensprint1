import cv2
import mediapipe as mp
import pygame

# initialize sound
pygame.mixer.init()
sound = pygame.mixer.Sound(r"C:\Users\rashm\Downloads\shadow_clone_jutsu.mp3")

# mediapipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

played = False

while True:

    ret, frame = cap.read()
    if not ret:
        break

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    h, w, _ = frame.shape

    if results.multi_hand_landmarks:

        for hand in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            cv2.putText(frame,
                        "Shadow Clone Jutsu!",
                        (50,50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0,255,255),
                        3)
            clone1 = frame.copy()
            clone2 = frame.copy()
            small1 = cv2.resize(clone1, (200,150))
            small2 = cv2.resize(clone2, (200,150))
            if h > 450 and w > 440:
                frame[300:450, 20:220] = small1
                frame[300:450, 240:440] = small2

            if not played:
                sound.play()
                played = True

    else:
        played = False

    cv2.imshow("Naruto Jutsu Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()