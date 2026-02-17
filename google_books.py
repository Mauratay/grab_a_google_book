import requests

def get_public_books(query):
    base_url = "https://www.googleapis.com/books/v1/volumes"
    
    params = {
        'q': query,
        'filter': 'full',  # Only returns books with full text available
        'maxResults': 10
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()

    if 'items' not in data:
        print("No public full-text books found.")
        return

    for item in data.get('items', []):
        v_info = item.get('volumeInfo', {})
        a_info = item.get('accessInfo', {})
        
        title = v_info.get('title', 'Unknown Title')
        
        # 1. Link to read in the browser
        reader_link = a_info.get('webReaderLink')
        
        # 2. Check for PDF or EPUB download links
        # Note: downloadLink only appears if the book is DRM-free/Public Domain
        pdf_link = a_info.get('pdf', {}).get('downloadLink')
        epub_link = a_info.get('epub', {}).get('downloadLink')

        print(f"Title: {title}")
        print(f"Read Online: {reader_link}")
        
        if pdf_link:
            print(f"PDF Download: {pdf_link}")
        if epub_link:
            print(f"EPUB Download: {epub_link}")
        
        if not pdf_link and not epub_link:
            print("Note: This book is readable online but direct download is restricted.")
            
        print("-" * 30)

get_public_books("YOUR SEARCH TEXT HERE")
