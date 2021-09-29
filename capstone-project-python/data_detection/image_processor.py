import cv2


def get_player_images_left(full_img, baseX=420, playerHeight=53, width=450):
    """
    Returns a tuple of 5 images, each representing a player from the left side of the screen
    :param full image: The fullscreen image to process
    :param baseX: The base X coordinate of the first player
    :param playerHeight: The height of each player
    :param width: The width of each player
    """
    player1 = full_img[baseX:baseX + playerHeight, 0:width]
    player2 = full_img[baseX + playerHeight:baseX + 2 * playerHeight, 0:width]
    player3 = full_img[baseX + 2 * playerHeight:baseX + 3 * playerHeight, 0:width]
    player4 = full_img[baseX + 3 * playerHeight:baseX + 4 * playerHeight, 0:width]
    player5 = full_img[baseX + 4 * playerHeight:baseX + 5 * playerHeight, 0:width]

    return (player1, player2, player3, player4, player5)


def get_player_images_right(full_img, baseX=420, playerHeight=53, width=450):
    """
    Returns a tuple of 5 images, each representing a player from the right side of the screen
    :param full image: The fullscreen to process
    :param baseX: The base X coordinate of the first player
    :param playerHeight: The height of each player
    :param width: The width of each player
    """
    image_height, image_width, _ = full_img.shape
    player1 = full_img[baseX:baseX + playerHeight, image_width - width:image_width]
    player2 = full_img[baseX + playerHeight:baseX + 2 * playerHeight, image_width - width:image_width]
    player3 = full_img[baseX + 2 * playerHeight:baseX + 3 * playerHeight, image_width - width:image_width]
    player4 = full_img[baseX + 3 * playerHeight:baseX + 4 * playerHeight, image_width - width:image_width]
    player5 = full_img[baseX + 4 * playerHeight:baseX + 5 * playerHeight, image_width - width:image_width]

    return (player1, player2, player3, player4, player5)


def get_team_image_left(full_img, baseX=420, playerHeight=53, width=450):
    """
    Returns an image of all players on the left side of the screen
    :param full image: The fullscreen to process
    :param baseX: The base X coordinate of the first player
    :param playerHeight: The height of each player
    :param width: The width of each player
    """
    return full_img[baseX:baseX + 5 * playerHeight, 0:width]


def get_team_image_right(full_img, baseX=420, playerHeight=53, width=450):
    """
    Returns an image of all players on the right side of the screen
    :param full image: The fullscreen to process
    :param baseX: The base X coordinate of the first player
    :param playerHeight: The height of each player
    :param width: The width of each player
    """
    image_height, image_width, _ = full_img.shape
    return full_img[baseX:baseX + 5 * playerHeight, image_width - width:image_width]
