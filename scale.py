#version .1
import PIL
from PIL import Image
import os,glob

def append_indicator(filename,indicator):
    return "{0}{2}.{1}".format(*filename.rsplit('.', 1) + indicator)

def strip_path(filename):
	return filename.rsplit('/',1)[1]

def clean_path(path):
	return path.split("'")[1]

def get_origin():
	origin = input("Origin directory?")
	return clean_path(origin)

def get_destination():
	destination = input("Destination directory?")
	return clean_path(destination)

#next, make extension non case sensitive
def scale_images(origin,destination):
	try:
	    for filename in glob.glob(os.path.join(origin, '*.JPG')):  
	        with open(filename, 'r') as f:
	            try:
	                for_web = ["w"]
	                new_path = append_indicator(filename,for_web)
	                new_name = strip_path(new_path)
	                #next: after input is complete, check if trailing slash is needed
	                new_destination = destination + "/" +  new_name
	                img = Image.open(filename)
	                start_width, start_height = img.size
	                new_width = int(start_width/2)
	                percent = (new_width / float(img.size[0]))
	                hsize = int((float(img.size[1]) * float(percent)))
	                img = img.resize((new_width, hsize), PIL.Image.ANTIALIAS)
	                try:
	                    #print("attempting to save scaled image: ", new_destination)
	                    img.save(new_destination)
	                    #print("saved image successfully")
	                except OSError:
	                    print("failed to scale ", img)
	            except IOError:
	                print("failed to open image")
	except OSError:
	    print("failed to open all .jpg files in ", origin)

def main():
	start = get_origin()
	end = get_destination()
	scale_images(start,end)
	print("Done!")

main()