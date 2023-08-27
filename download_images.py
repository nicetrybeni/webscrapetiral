from google_images_search import GoogleImagesSearch

# Replace these values with your API key and Custom Search Engine ID
GCS_DEVELOPER_KEY = 'AIzaSyBojg2p776TaRhthVcJqNwxgY5tJrBySC0'
GCS_CX = '956a87f4f9604465c'

# Search for images
search_term = 'R15 Yamaha Sports Bike'
num_images = 500

gis = GoogleImagesSearch(GCS_DEVELOPER_KEY, GCS_CX)
search_params = {
    'q': search_term,
    'num': num_images,
    'safe': 'high'
}
gis.search(search_params)

# Download images
for image in gis.results():
    image.download('images')
    print(f'Downloaded: {image.url}')
