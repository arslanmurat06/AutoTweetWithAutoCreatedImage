
import shutil
import requests
import jsonImporter
from random import seed
from random import randint


def download_Image_With_Given_Number(number):
    seed(1)

    for a in range(number):
        b = randint(0, 10000000)
        image_url = "https://source.unsplash.com/user/erondu/600x600"
        filename = "DownloadedImages/"+str(b)+".jpg"

        r = requests.get(image_url, stream=True)

        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True

    # Open a local file with wb ( write binary ) permission.
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

            print('Image sucessfully Downloaded: ', filename)
        else:
            print('Image Couldn\'t be retreived')


if __name__ == '__main__':
    count = jsonImporter.import_Data_From_Json_File()
    print(count)
    download_Image_With_Given_Number(count)
