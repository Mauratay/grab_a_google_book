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
