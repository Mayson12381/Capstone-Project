# MARK - Constants

SAVED_MODEL_PATH = ".\ml_model\ssd_mobilenet_v2-helmet\saved_model"
LABELS_PATH = '.\ml_model\Annotations\label_map.pbtxt'
MIN_CONF_THRESH = .3
TEST_IMAGE_PATH = './helper_modules/test_images/test-screen_7.jpg'
PLAYER_X_OFFSET = 530
PLAYER_Y_OFFSET = 720
PLAYER_HEIGHT = 63
PLAYER_WIDTH = 720

WEAPON_VERTICAL_SCALE_FACTOR = 1.1
WEAPON_HORIZONTAL_SCALE_FACTOR = 1.5
GRENADE_VERTICAL_SCALE_FACTOR = 0.5
GRENADE_HORIZONTAL_SCALE_FACTOR = 0.5
DEAD_VERTICAL_SCALE_FACTOR = 0.8
DEAD_HORIZONTAL_SCALE_FACTOR = 1
WEAPONS = [
    'ak47', 'awp', 'm4a1', 'm4a4', 'galil', 'famas', 'ssg', 'sg', 'aug',
    'deagle', 'ump', 'mp9', 'mp7', 'mac', 'p90', 'g3', 'mag', 'scar'
]
GRENADES = ['he', 'flash', 'smoke', 'molotov', 'incendiary', 'decoy']
MISC = ['kevlar', 'helmet']

# MARK - Global Variables

userRef = None
model = None
is_game_data_requested = False
is_user_logged_in = False
is_team_left = False
