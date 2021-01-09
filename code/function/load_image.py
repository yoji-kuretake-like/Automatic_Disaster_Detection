#This is the function to load the image from the directory

def load_url(folders):
  f_path = []
  for folder in folders:
    tmp_path = os.path.join(DIR_CUT_INPUTS, folder)
    inp_path = glob.glob(os.path.join(tmp_path, '*.png'))
    f_path.extend(inp_path)
  return f_path

def load_img(img_array, folders):
  all_path = load_url(folders)
  for i, each_path in enumerate(all_path):
    print('Now is {0} and {1}'.format(i, each_path))
    srcImg = Image.open(each_path)
    imgArray = np.array(srcImg)
    img_array[i] = imgArray / 255
  return (all_path, img_array)
