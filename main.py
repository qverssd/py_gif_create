from PIL import Image, ImageDraw
import imageio
import os

def create_images(num_images, size=(100, 100)):
    images = []
    for i in range(num_images):
        img = Image.new('RGB', size, color=(i*10, i*20, i*30))
        draw = ImageDraw.Draw(img)
        draw.text((size[0]//4, size[1]//4), f"Frame {i + 1}", fill=(255, 255, 255))
        img_path = f"frame_{i}.png"
        img.save(img_path)
        images.append(img_path)
    return images

def create_gif(image_list, gif_name, duration=0.5):
    frames = []
    for image_path in image_list:
        frames.append(imageio.imread(image_path))
    imageio.mimsave(gif_name, frames, duration=duration)

if __name__ == "__main__":
    num_images = 10
    images = create_images(num_images)
    create_gif(images, 'output.gif')

    for img in images:
        os.remove(img)