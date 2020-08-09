import requests
from bs4 import BeautifulSoup as bs
from tqdm import tqdm
import concurrent.futures
import os


def download_url(video_title, video_url):

    # Creating GET request
    r = requests.get(video_url, stream=True)
    
    # Total size of downloaded video
    total_size = int(r.headers.get("content-length"))

    # Downloading video in 1MB chunks (Progress bar included)
    with open(video_title + ".mp4", "wb") as video:
        for chunk in tqdm(iterable=r.iter_content(chunk_size=1024**2), 
                          total=int(total_size/(1024**2)), 
                          ncols=100,
                          unit="MB"):
            if chunk:
                video.write(chunk)

                
def main():
    
    # Creating GET request
    url = "RSS URL Here"
    r = requests.get(url)
    
    # Scraping using BeautifulSoup4 then parsing using lxml 
    soup = bs(r.text, "lxml")

    # Removing course title prefix
    course_title = soup.find("title").text[9:] 

    # Acquiring videos titles and urls
    content = soup.find_all("item")
    titles = [title.find("title").text for title in content]
    urls = [url.find("guid").text for url in content]

    # Creating folder for course videos
    os.mkdir(course_title)
    os.chdir(course_title)

    # Downloading videos concurrently using theards for speed gains
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_url, titles, urls)

        
if __name__ == "__main__":
    main()
