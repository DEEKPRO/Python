import requests
from PIL import Image
from io import BytesIO

API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-inpainting"

API_KEY = "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"

def generate_inpainting_image(prompt, image_path, mask_path):
    headers = {"Authorization":f"Bearer{API_KEY}"}
    with open(image_path, "rb")as img_file:
        image_data = img_file.read()
    with open(mask_path, "rb") as mask_file:
        mask_data = mask_file.read()
    
    payload = {"inputs":prompt}

    files = {
        "image": ("image.png",image_data,"image/png"),
        "mask": ("mask.png",mask_data,"image/png")
    }

    try:
        response = requests.post(API_URL, headers=headers, data=payload, files=files)
        response.raise_for_status()

        if response.status_code == 200:
            inpainted_image = Image.open(BytesIO(response.content))
            return inpainted_image
        else:
            raise Exception(f"Unexpected response status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")
    
def main():
    print("Welcome to inpainting and Restoration Challenge")
    print("This activity allows you to inpaint masked regions of an image based on a text prompt.")
    print("Type 'exit' at any prompt to quit the program.")

    while True:
        prompt = input("Enter a description for the inpainting image (or type 'exit' to quit): ")
        if prompt.lower() == "exit":
            print("Goodbye!")
            break

        image_path = input("Enter the path to the original image (or type 'exit' to quit): ")
        if image_path.lower() == "exit":
            break

        mask_path = input("Enter the path to the mask image file (or type 'exit' to quit): ")
        if mask_path.lower() == "exit":
            break

        try:
            print("Generating inpainted image...")
            result_image = generate_inpainting_image(prompt, image_path, mask_path)
            result_image.show()
            save_option = input("Do you want to save the resulting image? (yes/no): ")
            if save_option.lower() == "yes":
                file_name = input("Enter the name to save the resulting image: ")
                result_image.save(f"{file_name}.png")
                print(f"Image saved to {file_name}.png")
            print("-"*80+"\n")
        except Exception as e:
            print(f"An error occurred: {e}")
main()