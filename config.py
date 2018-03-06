# Tumblr Setup
# Replace the values with your information
# OAuth keys can be generated from https://api.tumblr.com/console/calls/user/info
consumer_key='CONSUMER_KEY' #replace with your key
consumer_secret='CONSUMER_SECRET' #replace with your secret code
oath_token='OATH_TOKEN' #replace with your oath token
oath_secret='OATH_SECRET' #replace with your oath secret code
tumblr_blog = 'TUMBLR_BLOG' # replace with your tumblr account name without .tumblr.com
tagsForTumblr = "MyTagsHere" # change to tags you want, separated with commas

#Config settings to change behavior of photo booth
monitor_w = 800    # width of the display monitor
monitor_h = 480    # height of the display monitor
file_path = '/home/pi/photobooth/pics/' # path to save images
clear_on_startup = False # True will clear previously stored photos as the program launches. False will leave all previous photos.
debounce = 0.3 # how long to debounce the button. Add more time if the button triggers too many times.
post_online = False # True to upload images. False to store locally only.
capture_count_pics = True # if true, show a photo count between taking photos. If false, do not. False is faster.
make_gifs = False   # True to make an animated gif. False to post 4 jpgs into one post.
hi_res_pics = True  # True to save high res pics from camera.
                    # If also uploading, the program will also convert each image to a smaller image before making the gif.
                    # False to first capture low res pics. False is faster.
                    # Careful, each photo costs against your daily Tumblr upload max.
camera_iso = 800    # adjust for lighting issues. Normal is 100 or 200. Sort of dark is 400. Dark is 800 max.
                    # available options: 100, 200, 320, 400, 500, 640, 800

########################
### Variables Config ###
########################
led_pin = 7 # LED
btn_pin = 18 # pin for the start button

capture_delay = 1 # delay between pics
prep_delay = 5 # number of seconds at step 1 as users prep to have photo taken
gif_delay = 100 # How much time between frames in the animated gif
restart_delay = 10 # how long to display finished message before beginning a new session
test_server = 'www.google.com'

# full frame of v1 camera is 2592x1944. Wide screen max is 2592,1555
# full frame of v2 camera is 3280x2464. Wide screen max is 3280,1968
# if you run into resource issues, try smaller, like 1920x1152.
# or increase memory http://picamera.readthedocs.io/en/release-1.12/fov.html#hardware-limits
high_res_w = 3280 # width of high res image, if taken
high_res_h = 1968 # height of high res image, if taken

camera_saturation =  0 #-100 for BW, 0 for color (between -100 and 100)
booth_trigger = "TOUCH" # BUTTON for button attached to btn_pin; TOUCH for Mousebuttondown event(tap on touchscreen)
total_pics = 4
stripL = ""         # Left strip empty "" for colour. bw for grayscale
stripR = "bw"       # Right strip empty "" for colour. bw for grayscale
printimg = True    # if true will attempt to print to CUPS.
make_montage = True # if true will make a photobooth strip montage duplicated
