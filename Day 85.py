import argparse
import requests


def download_url(url, local_filename):
    if local_filename is None:
        local_filename = url.split("/")[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


parser = argparse.ArgumentParser()
parser.add_argument("url", help="Url of file to download")  # Changed "Url" to "url"
parser.add_argument("-o", "--output", help="Name of the file", default=None)

args = parser.parse_args()

print(args.url)
print(args.output, type(args.output))

download_url(args.url, args.output)