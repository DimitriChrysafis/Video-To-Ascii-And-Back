import cv2
import PIL.Image

ASCII_CHARS = "@%#*+=-:. "

def main(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    import os
    os.makedirs("asciitxt", exist_ok=True)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image_pil = PIL.Image.fromarray(image)

        image_pil = resize(image_pil)
        greyscale_image = to_greyscale(image_pil)
        ascii_str = pixel_to_ascii(greyscale_image)

        ascii_img = ""
        img_width = greyscale_image.width
        ascii_str_len = len(ascii_str)
        for i in range(0, ascii_str_len, img_width):
            ascii_img += ascii_str[i:i + img_width] + "\n"

        frame_txt_path = os.path.join("asciitxt", f"frame_{frame_count:04d}.txt")
        with open(frame_txt_path, "w") as f:
            f.write(ascii_img)

    cap.release()
    cv2.destroyAllWindows()

def resize(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def to_greyscale(image):
    greyscale_image = image.convert("L")
    return greyscale_image

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        scaled_value = int((pixel_value / 255) * (len(ASCII_CHARS) - 1))
        ascii_str += ASCII_CHARS[scaled_value]
    return ascii_str

if __name__ == "__main__":
    video_path = "YOUR PATH"
    main(video_path)
