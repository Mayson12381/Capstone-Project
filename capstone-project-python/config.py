# MARK - Constants

SAVED_MODEL_PATH = ".\SSD_Test\ssd_mobilenet_v2-helmet\saved_model"
LABELS_PATH = '.\SSD_Test\Annotations\label_map.pbtxt'
MIN_CONF_THRESH = .3
TEST_IMAGE_PATH = './test-screen_7.jpg'
PLAYER_X_OFFSET = 530
PLAYER_Y_OFFSET = 720
PLAYER_HEIGTH = 63

# MARK - Global Variables

userRef = None
model = None
is_game_data_requested = False
is_user_logged_in = False
