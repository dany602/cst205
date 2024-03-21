# I Daniel Bonilla hereby self-attest that Team
# Ⰸ is the appropriate team for me.
# ++++++++++++++++++++++++++++++++++++++++
# import cv2

def my_search(search_input):
    if my_index != 0:
            self.my_label.setText(f'You chose {self.my_list[my_index]}.')

            for image in image_info:
                if keyword.lower() in image['title'].lower() or keyword.lower() in [tag.lower() for tag in image['tags']]:
                    # print(image['id'], image['title'], image['url'])

                    image_path = f"hw3_images/{image['id']}.jpg"
                    pixmap = QPixmap(image_path)
                    
                    self.new_window = QLabel()
                    self.new_window.setPixmap(pixmap)

                    if my_index == 1: # Sepia
                        img = Image.open(image_path)
                        sepia_img = sepia_filter(img)
                        pixmap = QPixmap.fromImage(ImageQt.ImageQt(sepia_img))
                        self.new_window.setPixmap(pixmap)

                    elif my_index == 2: # Negative
                        img = Image.open(image_path)
                        negative_img = negative_filter(img)
                        pixmap = QPixmap.fromImage(ImageQt.ImageQt(negative_img))
                        self.new_window.setPixmap(pixmap)

                    elif my_index == 3: # Grayscale
                        img = Image.open(image_path)
                        grayscale_img = grayscale_filter(img)
                        pixmap = QPixmap.fromImage(ImageQt.ImageQt(grayscale_img))
                        self.new_window.setPixmap(pixmap)

                    elif my_index == 4: # Thumbnail
                        img = Image.open(image_path)
                        thumbnail_img = thumbnail_filter(img)
                        pixmap = QPixmap.fromImage(ImageQt.ImageQt(thumbnail_img))
                        self.new_window.setPixmap(pixmap)

                    self.new_window.show()
                    self.my_lbl.setText(f"{image['id']}, {image['title']}, {image['url']}")
                    self.my_lbl.setText("Picture is found! :)")
                    break
                else:
                    
                    image_path = f"hw3_images/hw3_images/no_results.jpg"
                    pixmap = QPixmap(image_path)
                    self.new_window = QLabel()
                    self.new_window.setPixmap(pixmap)
                    self.new_window.show()

                    self.my_lbl.setText("Picture not Found :(")

    else:
        self.my_lbl.setText("")
        self.my_label.setText('Pick a valid manipulation')


# def apply_sepia(image_path):
#     # Implement sepia effect
#     pass

# def apply_negative(image_path):
#     # Implement negative effect
#     # import cv2
#     image = cv2.imread(image_path)
#     if image is None:
#         print("Error: Unable to load image.")
#         return None
#     negative_image = 
#     cv2.imshow("Negative Image", negative_image)
#     pass

# def apply_grayscale(image_path):
#     # Implement negative effect
#     pass

# def apply_thumbnail(image_path):
#     # Implement negative effect
#     pass

# def apply_none(image_path):
#     # Implement negative effect
#     pass