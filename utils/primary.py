import requests
from io import BytesIO
from PIL import Image


def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None


def get_images_by_urls(urls) -> list[Image]:
    images = []

    for url in urls:
        image_data = download_image(url)
        if image_data:
            img = Image.open(BytesIO(image_data))
            images.append(img)

    return images


def save_pdf(links: list, name_pdf: str):
    images = get_images_by_urls(links)
    images[0].save(f"{name_pdf}.pdf", save_all=True, append_images=images[1::])

    # return upload_gdrive(f"{name_pdf}.pdf", f"{name_pdf}.pdf")
