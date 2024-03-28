import requests
import os

def download_image(url, filename):
    """
    Downloads an image from the given URL and saves it to disk with the specified filename.
    
    Args:
        url (str): The URL of the image to download.
        filename (str): The name of the file to save the image as.
        
    Returns:
        None
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Get the content of the image
        image_data = response.content
        
        # Open a file for writing binary data
        with open(filename, 'wb') as file:
            file.write(image_data)
        
        print(f"Image downloaded and saved as {filename}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading the image: {e}")

# Example usage
image_url = input("Enter the URL of the image to download: ")
image_filename = input("Enter the filename to save the image as: ")

download_image(image_url, image_filename)