import struct

import numpy as np
from PIL import Image


def generate_3d_from_image(image_path, file_name="hi.ply"):
    img = Image.open(image_path).convert("RGB")
    img_data = np.array(img)

    width, length = img.size
    x, y = np.meshgrid(np.arange(length), np.arange(width), indexing="ij")

    z = np.mean(img_data, axis=-1).astype(np.int32)
    colors = img_data.reshape(-1, 3).astype(np.uint8)

    vertices = np.column_stack((x.ravel(), y.ravel(), z.ravel(), colors))

    with open(file_name, "wb") as file:
        file.write(b"ply\n")
        file.write(b"format binary_little_endian 1.0\n")
        file.write(f"element vertex {vertices.shape[0]}\n".encode())
        file.write(b"property int x\n")
        file.write(b"property int y\n")
        file.write(b"property int z\n")
        file.write(b"property uchar red\n")
        file.write(b"property uchar green\n")
        file.write(b"property uchar blue\n")
        file.write(b"end_header\n")

        for vertex in vertices:
            file.write(
                struct.pack(
                    "iiiBBB",
                    vertex[0],
                    vertex[1],
                    vertex[2],
                    vertex[3],
                    vertex[4],
                    vertex[5],
                )
            )


if __name__ == "__main__":
    image_path = "./image5.png"

    generate_3d_from_image(image_path)
    print("فایل سه‌بعدی ایجاد شد.")
