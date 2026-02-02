from PIL import Image

ASCII_CHARS = "@#W$9876543210?!abc;:+=-,._ "
def image_to_ascii(self, image_path, width=180):
        image = Image.open(image_path).convert("L")

        aspect_ratio = image.height / image.width
        height = int(width * aspect_ratio * 0.52)

        image = image.resize((width, height), Image.BICUBIC)
        pixels = image.getdata()

        result = []
        scale = len(ASCII_CHARS) - 1

        for i, pixel in enumerate(pixels):
            char = ASCII_CHARS[int(pixel / 255 * scale)]
            result.append(char)
            if (i + 1) % width == 0:
                result.append("\n")

        return "".join(result)
