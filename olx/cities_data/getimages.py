import os
import requests

images_dir = 'images'
def getimages(image_urls, date):
    os.chdir(images_dir)
    dirs = os.listdir()
    if date not in dirs:
        os.mkdir(date)
    os.chdir(date)
    image_count = 0
    for image_url in image_urls:
        print(image_url)
        img_data = requests.get(image_url).content
        image_count = image_count+1
        image_name = "image_"+str(image_count)
        try:
            with open(image_name+'.jpg', 'wb') as handler:
                handler.write(img_data)
        except FileExistsError as e:
            print(e)
            continue




if __name__ == '__main__':
    date = '4654132'
    urls = ['https://picsum.photos/1366/768']
    getimages(urls, date)

