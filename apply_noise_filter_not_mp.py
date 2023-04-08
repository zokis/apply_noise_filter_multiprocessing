import os
import sys
import time
from glob import glob
from random import gauss
from PIL import Image


def add_noise_to_pixel(pixel, noise_factor):
    noise = tuple(int(noise_factor * gauss(0, 255)) for _ in pixel)
    return tuple(
        max(0, min(255, val + noise_val)) for val, noise_val in zip(pixel, noise)
    )


def add_noise(image_path, noise_factor, shared, total_images):
    try:
        image = Image.open(image_path)
    except IOError:
        return

    noisy_image = Image.new(image.mode, image.size)
    noisy_image.putdata([add_noise_to_pixel(p, noise_factor) for p in image.getdata()])

    file_name_without_ext, extension = os.path.splitext(os.path.basename(image_path))
    new_file_name = f"{file_name_without_ext}_noisy{extension}"
    noisy_image.save(new_file_name)

    shared["progress"] += 100 / total_images
    shared["processed"] += 1
    print(
        f"Processed {new_file_name} ({shared['processed']}/{total_images}, {shared['progress']:.2f}% complete)"
    )


def main():
    sys_argv_len = len(sys.argv)
    if sys_argv_len < 2:
        print("Usage: python apply_noise_filter_not_mp.py <image_directory> [noise_factor]")
        sys.exit(1)
    noise_factor = float(sys.argv[2]) if sys_argv_len > 2 else 0.25
    image_list = glob(os.path.join(sys.argv[1], "*"))
    total_images = len(image_list)

    start_time = time.time()
    print(f"Starting image processing of {total_images} images...")

    shared = {"processed": 0.0, "progress": 0}

    for image_path in image_list:
        add_noise(image_path, noise_factor, shared, total_images)

    elapsed_time = time.time() - start_time
    print(
        f"Processing complete! {total_images} images processed in {elapsed_time:.2f} seconds."
    )


if __name__ == "__main__":
    main()
