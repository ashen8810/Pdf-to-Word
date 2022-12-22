# import matplotlib.pyplot as plt
# import cv2
# import math
# import numpy as np
# import easyocr
#
#
# def midpoint(x1, y1, x2, y2):
#     x_mid = int((x1 + x2) / 2)
#     y_mid = int((y1 + y2) / 2)
#     return (x_mid, y_mid)
#
#
# def inpaint_text(img_path):
#     reader = easyocr.Reader(['en'], gpu=False)  # Hindi, telugu, and English
#
#     img = cv2.imread(img_path)
#     mask = np.zeros(img.shape[:2], dtype="uint8")
#
#     results = reader.readtext(img, detail=1, paragraph=False)  # Set detail to 0 for simple text output
#
#     for (bbox, text, prob) in results:
#         (tl, tr, br, bl) = bbox
#         x0, y0 = int(tl[0]), int(tl[1])
#         x1, y1 = int(tr[0]), int(tr[1])
#         x2, y2 = int(br[0]), int(br[1])
#         x3, y3 = int(bl[0]), int(bl[1])
#
#         x_mid0, y_mid0 = midpoint(x1, y1, x2, y2)
#         x_mid1, y_mi1 = midpoint(x0, y0, x3, y3)
#         thickness = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
#
#         # Define the line and inpaint
#         cv2.line(mask, (x_mid0, y_mid0), (x_mid1, y_mi1), 255, thickness)
#         inpainted_img = cv2.inpaint(img, mask, 7, cv2.INPAINT_NS)
#
#     return (inpainted_img)
#

# img_text_removed = inpaint_text("123.jpg")
# plt.imshow(img_text_removed)

# cv2.imwrite('text_removed_image.jpg', img_text_removed)

#
# import keras_ocr
# import cv2
# import math
# import numpy as np
#
#
# def midpoint(x1, y1, x2, y2):
#     x_mid = int((x1 + x2) / 2)
#     y_mid = int((y1 + y2) / 2)
#     return (x_mid, y_mid)
#
#
#
#
# def inpaint_text(img_path):
#     pipeline = keras_ocr.pipeline.Pipeline()
#
#     # read image
#     img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
#     print(img)
#     # generate (word, box) tuples
#     prediction_groups = pipeline.recognize([img])
#     mask = np.zeros(img.shape[:2], dtype="uint8")
#     # print(prediction_groups[0])
#
#     for box in prediction_groups[0]:
#
#         print(box)
#         x0, y0 = box[1][0]
#         x1, y1 = box[1][1]
#         x2, y2 = box[1][2]
#         x3, y3 = box[1][3]
#
#         x_mid0, y_mid0 = midpoint(x1, y1, x2, y2)
#         x_mid1, y_mi1 = midpoint(x0, y0, x3, y3)
#
#         thickness = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
#
#         cv2.line(mask, (x_mid0, y_mid0), (x_mid1, y_mi1), 255,
#                  thickness)
#         img = cv2.inpaint(img, mask, 7, cv2.INPAINT_NS)
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         cv2.imwrite('text_removed_image.jpg', inpaint_text("watermark.gif", pipeline))
#
#     return (img)
#
#
# inpaint_text("q.jpg")




#
# import cv2
# import math
# import numpy as np
# def midpoint(x1, y1, x2, y2):
#     x_mid = int((x1 + x2) / 2)
#     y_mid = int((y1 + y2) / 2)
#     return (x_mid, y_mid)
#
#
# from paddleocr import PaddleOCR
#
#
# def inpaint_text(img_path):
#     img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
#     ocr = PaddleOCR(use_angle_cls=True, lang='en')
#     img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
#
#     result = ocr.ocr(img_path, cls=True)
#     prediction_groups = [line[0] for line in result]
#
#
#     mask = np.zeros(img.shape[:2], dtype="uint8")
#     for box in prediction_groups:
#         print(box[0])
#         x0, y0 = box[0][0][0],box[0][0][1]
#         x1, y1 = box[0][1][0],box[0][1][1]
#         x2, y2 = box[0][2][0],box[0][2][1]
#         x3, y3 = box[0][3][0],box[0][3][1]
#
#
#         x_mid0, y_mid0 = midpoint(x1, y1, x2, y2)
#         x_mid1, y_mi1 = midpoint(x0, y0, x3, y3)
#
#         thickness = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
#
#         cv2.line(mask, (x_mid0, y_mid0), (x_mid1, y_mi1), 255,
#                  thickness)
#         img = cv2.inpaint(img, mask, 7, cv2.INPAINT_NS)
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         cv2.imwrite('text_removed_image.jpg',img)
#
