import cv2
import mediapipe as mp
import numpy as np
import time
import threading
import winsound

# ==========================================
# DRIVER DROWSINESS DETECTION SYSTEM
# ==========================================

# MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Eye landmarks
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# Variables
alarm_on = False
eyes_closed_start = None

# ==========================================
# Alarm Function
# ==========================================
def play_alarm():
    global alarm_on
    while alarm_on:
        winsound.Beep(2500, 1000)  # Frequency, Duration

# ==========================================
# Eye Aspect Ratio Function
# ==========================================
def eye_aspect_ratio(eye_points):
    p1, p2, p3, p4, p5, p6 = eye_points

    vertical1 = np.linalg.norm(np.array(p2) - np.array(p6))
    vertical2 = np.linalg.norm(np.array(p3) - np.array(p5))
    horizontal = np.linalg.norm(np.array(p1) - np.array(p4))

    ear = (vertical1 + vertical2) / (2.0 * horizontal)
    return ear

# ==========================================
# Start Webcam
# ==========================================
cap = cv2.VideoCapture(0)

print("Driver Drowsiness Detection Started")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    h, w, _ = frame.shape

    if results.multi_face_landmarks:

        for face_landmarks in results.multi_face_landmarks:

            left_eye_points = []
            right_eye_points = []

            # Left Eye
            for idx in LEFT_EYE:
                x = int(face_landmarks.landmark[idx].x * w)
                y = int(face_landmarks.landmark[idx].y * h)

                left_eye_points.append((x, y))
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

            # Right Eye
            for idx in RIGHT_EYE:
                x = int(face_landmarks.landmark[idx].x * w)
                y = int(face_landmarks.landmark[idx].y * h)

                right_eye_points.append((x, y))
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

            # EAR Calculation
            left_ear = eye_aspect_ratio(left_eye_points)
            right_ear = eye_aspect_ratio(right_eye_points)

            avg_ear = (left_ear + right_ear) / 2

            cv2.putText(
                frame,
                f"EAR: {avg_ear:.2f}",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 0, 0),
                2
            )

            # Eyes Closed
            if avg_ear < 0.22:

                if eyes_closed_start is None:
                    eyes_closed_start = time.time()

                closed_duration = time.time() - eyes_closed_start

                cv2.putText(
                    frame,
                    f"Eyes Closed: {closed_duration:.1f}s",
                    (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 255),
                    2
                )

                if closed_duration >= 3:

                    cv2.putText(
                        frame,
                        "DROWSINESS ALERT!",
                        (120, 180),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.2,
                        (0, 0, 255),
                        3
                    )

                    if not alarm_on:
                        alarm_on = True
                        threading.Thread(
                            target=play_alarm,
                            daemon=True
                        ).start()

            else:

                eyes_closed_start = None
                alarm_on = False

                cv2.putText(
                    frame,
                    "AWAKE",
                    (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

    cv2.imshow("Driver Drowsiness Detection", frame)

    key = cv2.waitKey(1)

    if key == 27:  # Press ESC to Exit
        break

cap.release()
cv2.destroyAllWindows()