#These are the functions to compare using change detection method

def crop_small_patch(img_seg, patch_size):
  len_img, num_img = int(img_seg.shape[0]/patch_size), int(len_img*len_img)
  patch_imgs = np.zeros((num_img, patch_size, patch_size, 3), dtype = np.float32)
  count = 0
  for i in range(len_img):
    for j in range(len_img):
      patch_imgs[count] = img_seg[i*patch_size : (i+1)*patch_size, j*patch_size : (j+1)*patch_size, :]
      count += 1
  return patch_imgs

def comparison_small_patch(pre_patch, post_patch, threshold):
  patch_size, org_size = int(pre_patch.shape[1]), int(np.sqrt(pre_patch.shape[0]) * patch_size)
  diff_img = np.zeros((org_size, org_size, 3), dtype = np.float32)
  hlen = int(org_size//patch_size)
  tmp_array = np.zeros_like(pre_patch)
  for l in range(int(pre_patch.shape[0])):
    each_pre_patch, each_post_patch = pre_patch[l], post_patch[l]
    correct, wrong = 0, 0
    for h in range(patch_size):
      for w in range(patch_size):
        judge = each_pre_patch[h, w, :] == each_post_patch[h, w, :]
        if all(judge):
          correct += 1
        else:
          wrong += 1
    if wrong/(patch_size*patch_size) >= threshold:
      tmp_array[l] = (255, 255, 255)
    else:
      tmp_array[l] = (0, 0, 0)
  patch_imgs = np.zeros((hlen, patch_size, org_size, 3), dtype = np.float32)
  for m in range(hlen):
    patch_imgs[m] = np.hstack(tmp_array[m * hlen : (m+1)*hlen])
  final_binary = np.vstack((patch_imgs))
  return final_binary
