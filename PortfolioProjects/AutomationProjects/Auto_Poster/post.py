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

def post_to_instagram(image_url, caption):
    media_url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media"
    media_payload = {
        'image_url': image_url,
        'caption': caption,
        'access_token': ACCESS_TOKEN
    }
    media_response = requests.post(media_url, data=media_payload)
    media_id = media_response.json().get('id')
    if not media_id:
        print("Media creation failed:", media_response.text)
        return 
    publish_url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media_publish"
    publish_payload = {
        'creation_id': media_id,
        'access_token': ACCESS_TOKEN
    }
    publish_response = requests.post(publish_url, data=publish_payload)
    if publish_response.status_code == 200:
        print("Post published successfully!")
    else:
        print("Failed to publish post:", publish_response.text)
        
if __name__ == "__main__":
    local_image_path = "path/to/your/image.jpg"  
    image_url = upload_image_to_cloudinary(local_image_path)
    print("Uploaded image URL:", image_url)
    post_to_instagram(image_url, CAPTION)
    