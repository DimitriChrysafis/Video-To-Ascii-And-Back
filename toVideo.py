from PIL import Image, ImageDraw
import os
import cv2

def main():
    txt_folder = "YOUR PATH"
    output_video_path = "output_video.mp4"

    txt_files = [f for f in os.listdir(txt_folder) if f.endswith(".txt")]
    txt_files.sort()

    frame = read_frame(os.path.join(txt_folder, txt_files[0]))
    frame_width, frame_height = frame.size

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_video_path, fourcc, 30, (frame_width, frame_height))

    for txt_file in txt_files:
        frame = read_frame(os.path.join(txt_folder, txt_file))
        frame.save("temp_frame.png")
        img = cv2.imread("temp_frame.png")
        out.write(img)

    out.release()
    os.remove("temp_frame.png")

def read_frame(txt_path):
    with open(txt_path, "r") as f:
        lines = f.readlines()

    frame_width = len(lines[0])
    frame_height = len(lines)

    img = Image.new("RGB", (frame_width, frame_height), "black")
    draw = ImageDraw.Draw(img)

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                draw.point((x, y), fill="white")

    return img

if __name__ == "__main__":
    main()