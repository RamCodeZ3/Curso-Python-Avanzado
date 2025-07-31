from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def get_image(file_name):
    try:
        image = Image.open(file_name)
        print(image.size)
        print(image.mode)
        print(image.format)

        # image_blackwhite = image.convert('L')
        # image_blackwhite.save('BlackWhite.png')

        font = ImageFont.truetype('fonts/static/Roboto-Bold.ttf', 320)
        draw = ImageDraw.Draw(image)
        draw.text(
            (500, 1200),
            "Rick and Morty",
            (255, 255, 255),
            font
        )
        image.show()
        image.save('rick_and_morty.png')

        # Imagen thumbnail
        image.thumbnail((500, 500))
        image.show()
        image.save('imageThumbnail.png')

    except Exception as e:
        print("No se encontro la imagen" + e)


if __name__ == '__main__':
    get_image("image.png")
