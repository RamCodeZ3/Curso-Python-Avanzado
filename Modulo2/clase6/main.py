from PIL import Image
import os


def compress_images(image_folder):
    try:
        for file in os.listdir(image_folder):
            file_name, file_extension = os.path.splitext(image_folder + file)
            print(file_name)

            if file_extension == '.png':
                file_compress = Image.open(image_folder + file)
                file_compress.save(
                    image_folder + file_name + "_Comprimido.png",
                    optimize=True,
                    quality=70
                )

    except FileNotFoundError as e:
        print("No se pudo comprimir la imagen: " + f"{e}")


if __name__ == '__main__':
    compress_images('C:/rick/')
