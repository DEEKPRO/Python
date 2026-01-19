import requests
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO

API_KEY = "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"

def generate_image_from_text(prompt):

    API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-3-medium-diffusers"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image
    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
    
def post_process_image(image):
    enhancer = ImageEnhance.Brightness(image)
    bright_image = enhancer.enhance(1.2)
    enhancer = ImageEnhance.Contrast(bright_image)
    contrast_image = enhancer.enhance(1.3)

    soft_focus_image = contrast_image.filter(ImageFilter.GaussianBlur(radius=2))

    return soft_focus_image
def light(image):
    light_enhance = ImageEnhance.Brightness(image)
    light_image = light_enhance.enhance(4.2)
    light_enhance = ImageEnhance.Contrast(light_image)
    contrast_image = light_enhance.enhance(2.3)

    soft_focus_image = contrast_image.filter(ImageFilter.GaussianBlur(radius=1))
    return soft_focus_image

def dark(image):
    dark_enhance = ImageEnhance.Brightness(image)
    dark_image = dark_enhance.enhance(0.2)
    dark_enhance = ImageEnhance.Contrast(dark_image)
    dark_contrast = dark_enhance.enhance(6.3)

    soft_focus_image = dark_contrast.filter(ImageFilter.GaussianBlur(radius=0.5))
    return soft_focus_image

def main():
    print("Welcome to the Post-Processing Magic Workshop!")
    print("This program generates an image fro text and applies post-processing effects.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter a description for the image (or 'exit to quit'): \n")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        try:
            print("\nGenerating Image...")
            image = generate_image_from_text(user_input)
            print("Appliying post-processing effects... \n")
            processed_image = post_process_image(image)
            processed_image.show()
            light_image = light(image)
            dark_image = dark(image)
            light_image.show()
            dark_image.show()

            save_option = input("Do u want to save the processed image? (yes/no):")
            if save_option == 'yes':
                file_name = input("Enter a name for the image (without extention): ").strip()
                processed_image.save(f"{file_name}.png")
                light_image.save(f"{file_name}_light.png")
                dark_image.save(f"{file_name}_dark.png")
                print(f"Image saved as {file_name}.png\n")
            print("-"*80+"\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")

main()