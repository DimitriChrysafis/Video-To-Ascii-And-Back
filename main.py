import os
import subprocess
import cv2


def main():
    video_to_ascii()

    ascii_to_video()

    play_video()


def video_to_ascii():
    video_path = "YOUR PATH"
    os.system(f"python ascii.py {video_path}")


def ascii_to_video():
    subprocess.run(["python", "toVideo.py"])


def play_video():
    output_video_path = "output_video.mp4"
    cap = cv2.VideoCapture(output_video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("ASCII Video", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
