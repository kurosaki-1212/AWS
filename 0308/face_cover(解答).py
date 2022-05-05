import boto3
import json
import sys
from PIL import Image

if len(sys.argv) != 3:
    print('python', sys.argv[0], 'image1 image2')
    exit()

rekognition = boto3.client('rekognition')

with open(sys.argv[1], 'rb') as file:
    result = rekognition.detect_faces(
        Image={'Bytes': file.read()})
    print(json.dumps(result, indent=4))

image_in = Image.open(sys.argv[1])

# カバーする画像をオープンしてcovermarkという変数名で使えるようにする
covermark = Image.open(sys.argv[2])

w, h = image_in.size
# 出力する画像をコピーしてimage_outとしておく
image_out = image_in
for face in result['FaceDetails']:
    box = face['BoundingBox']
    left = int(box['Left']*w)
    top = int(box['Top']*h)
    # right = left+int(box['Width']*w)
    # bottom = top+int(box['Height']*h)

    # 画像を顔の上に重ねる
    image_out.paste(covermark,(left, top))

image_out.save('cover_'+sys.argv[1])
image_out.show()
