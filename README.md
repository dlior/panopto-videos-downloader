# Panopto Videos Downloader

Panopto Vidoes Downloader is a Python script for downloading Technion course videos from Panopto 

# Getting Started

## Installation

Clone the repo
```bash
$ git clone https://github.com/dlior/panopto-videos-downloader.git
$ cd panopto-videos-downloader
$ pip install -r requirements.txt
```

## Using Panopto Vidoes Downloader

1. In Google Chrome subscribe to RSS

    ![](Assets/RSS.png)

2. Copy the URL and paste it in the url variable in the script then save file

```python
url = "https://{RSS URL Here}"
```

3. Open terminal and run the script:
```bash
$ python main.py
```

## Example
![](Assets/progress_bar.png)


## Disclaimer

The tool above is for research purpose only not for human consumption, I am not responsible for any use of this program, please read [Panopto Terms of Service](https://www.panopto.com/terms-of-service/) before using this.



