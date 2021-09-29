import cv2


def getPlayerImagesLeftSeperated(image, baseX=420, playerHeight=53, width=450):
    player1 = image[baseX:baseX + playerHeight, 0:width]
    player2 = image[baseX + playerHeight:baseX + 2 * playerHeight, 0:width]
    player3 = image[baseX + 2 * playerHeight:baseX + 3 * playerHeight, 0:width]
    player4 = image[baseX + 3 * playerHeight:baseX + 4 * playerHeight, 0:width]
    player5 = image[baseX + 4 * playerHeight:baseX + 5 * playerHeight, 0:width]

    return (player1, player2, player3, player4, player5)


def getPlayerImagesRightSeperated(image, baseX=420, playerHeight=53, width=450):
    image_height, image_width, _ = image.shape
    player1 = image[baseX:baseX + playerHeight, image_width - width:image_width]
    player2 = image[baseX + playerHeight:baseX + 2 * playerHeight, image_width - width:image_width]
    player3 = image[baseX + 2 * playerHeight:baseX + 3 * playerHeight, image_width - width:image_width]
    player4 = image[baseX + 3 * playerHeight:baseX + 4 * playerHeight, image_width - width:image_width]
    player5 = image[baseX + 4 * playerHeight:baseX + 5 * playerHeight, image_width - width:image_width]

    return (player1, player2, player3, player4, player5)


def getPlayerImagesLeftFull(image, baseX=420, playerHeight=53, width=450):
    return image[baseX:baseX + 5 * playerHeight, 0:width]


def getPlayerImagesRightFull(image, baseX=420, playerHeight=53, width=450):
    image_height, image_width, _ = image.shape
    return image[baseX:baseX + 5 * playerHeight, image_width - width:image_width]
