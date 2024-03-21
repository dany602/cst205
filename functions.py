# I Daniel Bonilla hereby self-attest that Team
# Ⰸ is the appropriate team for me.
# ++++++++++++++++++++++++++++++++++++++++

def my_search(search_input):
    if my_index != 0:
            my_label.setText(f'You chose {my_list[my_index]}.')

            for image in image_info:
                if keyword.lower() in image['title'].lower() or keyword.lower() in [tag.lower() for tag in image['tags']]:
                    # print(image['id'], image['title'], image['url'])

                    image_path = f"hw3_images/{image['id']}.jpg"
                    pixmap = QPixmap(image_path)
                    
                    new_window = QLabel()
                    new_window.setPixmap(pixmap)

                    if my_index == 1: # Sepia
                        img = open(image_path)
                        sepia_img = sepia_filter(img)
                        pixmap = QPixmap(sepia_img)
                        new_window.setPixmap(pixmap)

                    elif my_index == 2: # Negative
                        img = open(image_path)
                        negative_img = negative_filter(img)
                        pixmap = QPixmap(negative_img)
                        new_window.setPixmap(pixmap)

                    elif my_index == 3: # Grayscale
                        img = open(image_path)
                        grayscale_img = grayscale_filter(img)
                        pixmap = QPixmap(grayscale_img)
                        new_window.setPixmap(pixmap)

                    elif my_index == 4: # Thumbnail
                        img = open(image_path)
                        thumbnail_img = thumbnail_filter(img)
                        pixmap = QPixmap(thumbnail_img)
                        new_window.setPixmap(pixmap)

                    new_window.show()
                    my_lbl.setText(f"{image['id']}, {image['title']}, {image['url']}")
                    my_lbl.setText("Picture is found! :)")
                    break
                else:
                    
                    image_path = f"hw3_images/hw3_images/no_results.jpg"
                    pixmap = QPixmap(image_path)
                    new_window = QLabel()
                    new_window.setPixmap(pixmap)
                    new_window.show()

                    my_lbl.setText("Picture not Found :(")

    else:
        my_lbl.setText("")
        my_label.setText('Pick a valid manipulation')


def sepia(p):
    # tint shadows
    if p[0] < 63:
        r,g,b = int(p[0] * 1.1), p[1], int(p[2] * 0.9)

    # tint midtones
    elif p[0] > 62 and p[0] < 192:
        r,g,b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)

    # tint highlights
    else:
        r = int(p[0] * 1.08)
        g,b = p[1], int(p[2] * 0.5)

    return r, g, b

def sepia_filter(image):
    img = image.copy()
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            pixel = pixels[i, j]
            r, g, b = sepia(pixel)
            pixels[i, j] = (r, g, b)

    return img

# If Negative is chosen
def negative_filter(image):
    negative_list = [(255-p[0], 255-p[1], 255-p[2]) for p in image.getdata()]
    image.putdata(negative_list)
    return image

# If grayscale is chosen
def grayscale_filter(image):
    img = image.copy()

    img = img.convert('L')
    
    return img

# If thumbnail is chosen
def thumbnail_filter(image):
    img = image.copy()
    width, height = img.size
    
    thumb_width = width // 4
    thumb_height = height // 4
    
    img = img.resize((thumb_width, thumb_height))
    
    return img
