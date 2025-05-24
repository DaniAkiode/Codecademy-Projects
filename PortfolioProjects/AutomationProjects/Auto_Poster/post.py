import os 
import cloudinary
import cloudinary.uploader
import requests
from dotenv import load_dotenv

load_dotenv()

# Cloudinary configuration

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

# Instagram API Information

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
IG_USER_ID = os.getenv("IG_USER_ID")
CAPTION = os.getenv("CAPTION")

def upload_image_to_cloudinary(local_path):
    result = cloudinary.uploader.upload(local_path)
    return result['secure_url']

def post_to_instagram():
    pass

if __name__ == "__main__":
    local_image_path = "path/to/your/image.jpg"  
    image_url = upload_image_to_cloudinary(local_image_path)
    print("Uploaded image URL:", image_url)
    post_to_instagram(image_url, CAPTION)
    