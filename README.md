# Google Books Public Domain Search

A simple Python utility that interacts with the Google Books API to find books with **full text availability**. It retrieves essential reading links, prioritizing direct downloads (PDF/EPUB) for public domain titles.

## Features

* **Full-Text Filter:** Automatically filters search results to only include volumes where the full text is available.
* **Direct Download Links:** Extracts direct download links for **PDF** and **EPUB** formats if the book is DRM-free/Public Domain.
* **Web Reader:** Provides the direct link to read the book in the browser via Google Books.
* **Lightweight:** clear and simple code using the `requests` library.

## Prerequisites

You need **Python 3.x** installed on your system.

You also need the `requests` library. If you don't have it, install it via pip:

```bash
pip install requests

```

## Usage

1. Clone this repository or download the script.
2. Open the script file (e.g., `books_search.py`).
3. Scroll to the bottom of the file and locate the function call:
```python
get_public_books("YOUR SEARCH TEXT HERE")

```


4. Replace `"YOUR SEARCH TEXT HERE"` with your desired search query (e.g., `"Pride and Prejudice"` or `"Python Programming"`).
5. Run the script:
```bash
python books_search.py

```



## Example Output

```text
Title: Pride and Prejudice
Read Online: [http://play.google.com/books/reader?id=](http://play.google.com/books/reader?id=)...
PDF Download: [http://books.google.com/books/download/Pride_and_Prejudice.pdf](http://books.google.com/books/download/Pride_and_Prejudice.pdf)?...
EPUB Download: [http://books.google.com/books/download/Pride_and_Prejudice.epub](http://books.google.com/books/download/Pride_and_Prejudice.epub)?...
------------------------------
Title: The Works of Jane Austen
Read Online: [http://play.google.com/books/reader?id=](http://play.google.com/books/reader?id=)...
Note: This book is readable online but direct download is restricted.
------------------------------

```

## Note on API Limits

This script uses the public Google Books API. No API key is strictly required for low-volume usage, but heavy usage may require generating an API key from the [Google Cloud Console]() and adding it to the request parameters.

## Contributing

Feel free to fork this repository and submit pull requests to add features like Command Line Arguments (CLI) or results exporting!
