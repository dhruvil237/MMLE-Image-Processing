import os
from PIL import Image
from Method.LACC import LACC
from Method.LACE import LACE

image_dir = 'Image'
result_dir = os.path.join(image_dir, 'result')

if not os.path.exists(result_dir):
    os.makedirs(result_dir)

for file_name in os.listdir(image_dir):
    if file_name.endswith('.jpg'):
        # load input image
        input_path = os.path.join(image_dir, file_name)
        img_name = os.path.splitext(file_name)[0].replace('_input', '')
        input_image = Image.open(input_path)

        # apply LACC and LACE models
        out1 = LACC_new(input_image)
        result = LACE(out1)

        # save result
        result_path = os.path.join(result_dir, f'{img_name}_MLLE.jpg')
        result.save(result_path)