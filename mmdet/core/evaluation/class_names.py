# Copyright (c) OpenMMLab. All rights reserved.
import mmcv
from enum import Enum

class DatasetEnum(Enum):
    VOC = 'voc'
    IMAGENET_DET = 'imagenet_det'
    IMAGENET_VID = 'imagenet_vid'
    COCO = 'coco'
    SUN='sun'
    LVIS = 'lvis'
    WIDER_FACE = 'wider_face'
    CITYSCAPES = 'cityscapes'
    OID_CHALLENGE = 'oid_challenge'
    OID_V6 = 'oid_v6'

def wider_face_classes():
    return ['face']


def voc_classes():
    return [
        'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat',
        'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person',
        'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor'
    ]


def imagenet_det_classes():
    return [
        'accordion', 'airplane', 'ant', 'antelope', 'apple', 'armadillo',
        'artichoke', 'axe', 'baby_bed', 'backpack', 'bagel', 'balance_beam',
        'banana', 'band_aid', 'banjo', 'baseball', 'basketball', 'bathing_cap',
        'beaker', 'bear', 'bee', 'bell_pepper', 'bench', 'bicycle', 'binder',
        'bird', 'bookshelf', 'bow_tie', 'bow', 'bowl', 'brassiere', 'burrito',
        'bus', 'butterfly', 'camel', 'can_opener', 'car', 'cart', 'cattle',
        'cello', 'centipede', 'chain_saw', 'chair', 'chime', 'cocktail_shaker',
        'coffee_maker', 'computer_keyboard', 'computer_mouse', 'corkscrew',
        'cream', 'croquet_ball', 'crutch', 'cucumber', 'cup_or_mug', 'diaper',
        'digital_clock', 'dishwasher', 'dog', 'domestic_cat', 'dragonfly',
        'drum', 'dumbbell', 'electric_fan', 'elephant', 'face_powder', 'fig',
        'filing_cabinet', 'flower_pot', 'flute', 'fox', 'french_horn', 'frog',
        'frying_pan', 'giant_panda', 'goldfish', 'golf_ball', 'golfcart',
        'guacamole', 'guitar', 'hair_dryer', 'hair_spray', 'hamburger',
        'hammer', 'hamster', 'harmonica', 'harp', 'hat_with_a_wide_brim',
        'head_cabbage', 'helmet', 'hippopotamus', 'horizontal_bar', 'horse',
        'hotdog', 'iPod', 'isopod', 'jellyfish', 'koala_bear', 'ladle',
        'ladybug', 'lamp', 'laptop', 'lemon', 'lion', 'lipstick', 'lizard',
        'lobster', 'maillot', 'maraca', 'microphone', 'microwave', 'milk_can',
        'miniskirt', 'monkey', 'motorcycle', 'mushroom', 'nail', 'neck_brace',
        'oboe', 'orange', 'otter', 'pencil_box', 'pencil_sharpener', 'perfume',
        'person', 'piano', 'pineapple', 'ping-pong_ball', 'pitcher', 'pizza',
        'plastic_bag', 'plate_rack', 'pomegranate', 'popsicle', 'porcupine',
        'power_drill', 'pretzel', 'printer', 'puck', 'punching_bag', 'purse',
        'rabbit', 'racket', 'ray', 'red_panda', 'refrigerator',
        'remote_control', 'rubber_eraser', 'rugby_ball', 'ruler',
        'salt_or_pepper_shaker', 'saxophone', 'scorpion', 'screwdriver',
        'seal', 'sheep', 'ski', 'skunk', 'snail', 'snake', 'snowmobile',
        'snowplow', 'soap_dispenser', 'soccer_ball', 'sofa', 'spatula',
        'squirrel', 'starfish', 'stethoscope', 'stove', 'strainer',
        'strawberry', 'stretcher', 'sunglasses', 'swimming_trunks', 'swine',
        'syringe', 'table', 'tape_player', 'tennis_ball', 'tick', 'tie',
        'tiger', 'toaster', 'traffic_light', 'train', 'trombone', 'trumpet',
        'turtle', 'tv_or_monitor', 'unicycle', 'vacuum', 'violin',
        'volleyball', 'waffle_iron', 'washer', 'water_bottle', 'watercraft',
        'whale', 'wine_bottle', 'zebra'
    ]


def imagenet_vid_classes():
    return [
        'airplane', 'antelope', 'bear', 'bicycle', 'bird', 'bus', 'car',
        'cattle', 'dog', 'domestic_cat', 'elephant', 'fox', 'giant_panda',
        'hamster', 'horse', 'lion', 'lizard', 'monkey', 'motorcycle', 'rabbit',
        'red_panda', 'sheep', 'snake', 'squirrel', 'tiger', 'train', 'turtle',
        'watercraft', 'whale', 'zebra'
    ]


def coco_classes():
    return [
        'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train',
        'truck', 'boat', 'traffic_light', 'fire_hydrant', 'stop_sign',
        'parking_meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep',
        'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella',
        'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard',
        'sports_ball', 'kite', 'baseball_bat', 'baseball_glove', 'skateboard',
        'surfboard', 'tennis_racket', 'bottle', 'wine_glass', 'cup', 'fork',
        'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange',
        'broccoli', 'carrot', 'hot_dog', 'pizza', 'donut', 'cake', 'chair',
        'couch', 'potted_plant', 'bed', 'dining_table', 'toilet', 'tv',
        'laptop', 'mouse', 'remote', 'keyboard', 'cell_phone', 'microwave',
        'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase',
        'scissors', 'teddy_bear', 'hair_drier', 'toothbrush'
    ]

def sun_classes():
    return [
        'type2', 'type3', 'type3s', 'type4', 'type5'
    ]
def cityscapes_classes():
    return [
        'person', 'rider', 'car', 'truck', 'bus', 'train', 'motorcycle',
        'bicycle'
    ]


def oid_challenge_classes():
    return [
        'Footwear', 'Jeans', 'House', 'Tree', 'Woman', 'Man', 'Land vehicle',
        'Person', 'Wheel', 'Bus', 'Human face', 'Bird', 'Dress', 'Girl',
        'Vehicle', 'Building', 'Cat', 'Car', 'Belt', 'Elephant', 'Dessert',
        'Butterfly', 'Train', 'Guitar', 'Poster', 'Book', 'Boy', 'Bee',
        'Flower', 'Window', 'Hat', 'Human head', 'Dog', 'Human arm', 'Drink',
        'Human mouth', 'Human hair', 'Human nose', 'Human hand', 'Table',
        'Marine invertebrates', 'Fish', 'Sculpture', 'Rose', 'Street light',
        'Glasses', 'Fountain', 'Skyscraper', 'Swimwear', 'Brassiere', 'Drum',
        'Duck', 'Countertop', 'Furniture', 'Ball', 'Human leg', 'Boat',
        'Balloon', 'Bicycle helmet', 'Goggles', 'Door', 'Human eye', 'Shirt',
        'Toy', 'Teddy bear', 'Pasta', 'Tomato', 'Human ear',
        'Vehicle registration plate', 'Microphone', 'Musical keyboard',
        'Tower', 'Houseplant', 'Flowerpot', 'Fruit', 'Vegetable',
        'Musical instrument', 'Suit', 'Motorcycle', 'Bagel', 'French fries',
        'Hamburger', 'Chair', 'Salt and pepper shakers', 'Snail', 'Airplane',
        'Horse', 'Laptop', 'Computer keyboard', 'Football helmet', 'Cocktail',
        'Juice', 'Tie', 'Computer monitor', 'Human beard', 'Bottle',
        'Saxophone', 'Lemon', 'Mouse', 'Sock', 'Cowboy hat', 'Sun hat',
        'Football', 'Porch', 'Sunglasses', 'Lobster', 'Crab', 'Picture frame',
        'Van', 'Crocodile', 'Surfboard', 'Shorts', 'Helicopter', 'Helmet',
        'Sports uniform', 'Taxi', 'Swan', 'Goose', 'Coat', 'Jacket', 'Handbag',
        'Flag', 'Skateboard', 'Television', 'Tire', 'Spoon', 'Palm tree',
        'Stairs', 'Salad', 'Castle', 'Oven', 'Microwave oven', 'Wine',
        'Ceiling fan', 'Mechanical fan', 'Cattle', 'Truck', 'Box', 'Ambulance',
        'Desk', 'Wine glass', 'Reptile', 'Tank', 'Traffic light', 'Billboard',
        'Tent', 'Insect', 'Spider', 'Treadmill', 'Cupboard', 'Shelf',
        'Seat belt', 'Human foot', 'Bicycle', 'Bicycle wheel', 'Couch',
        'Bookcase', 'Fedora', 'Backpack', 'Bench', 'Oyster',
        'Moths and butterflies', 'Lavender', 'Waffle', 'Fork', 'Animal',
        'Accordion', 'Mobile phone', 'Plate', 'Coffee cup', 'Saucer',
        'Platter', 'Dagger', 'Knife', 'Bull', 'Tortoise', 'Sea turtle', 'Deer',
        'Weapon', 'Apple', 'Ski', 'Taco', 'Traffic sign', 'Beer', 'Necklace',
        'Sunflower', 'Piano', 'Organ', 'Harpsichord', 'Bed', 'Cabinetry',
        'Nightstand', 'Curtain', 'Chest of drawers', 'Drawer', 'Parrot',
        'Sandal', 'High heels', 'Tableware', 'Cart', 'Mushroom', 'Kite',
        'Missile', 'Seafood', 'Camera', 'Paper towel', 'Toilet paper',
        'Sombrero', 'Radish', 'Lighthouse', 'Segway', 'Pig', 'Watercraft',
        'Golf cart', 'studio couch', 'Dolphin', 'Whale', 'Earrings', 'Otter',
        'Sea lion', 'Whiteboard', 'Monkey', 'Gondola', 'Zebra',
        'Baseball glove', 'Scarf', 'Adhesive tape', 'Trousers', 'Scoreboard',
        'Lily', 'Carnivore', 'Power plugs and sockets', 'Office building',
        'Sandwich', 'Swimming pool', 'Headphones', 'Tin can', 'Crown', 'Doll',
        'Cake', 'Frog', 'Beetle', 'Ant', 'Gas stove', 'Canoe', 'Falcon',
        'Blue jay', 'Egg', 'Fire hydrant', 'Raccoon', 'Muffin', 'Wall clock',
        'Coffee', 'Mug', 'Tea', 'Bear', 'Waste container', 'Home appliance',
        'Candle', 'Lion', 'Mirror', 'Starfish', 'Marine mammal', 'Wheelchair',
        'Umbrella', 'Alpaca', 'Violin', 'Cello', 'Brown bear', 'Canary', 'Bat',
        'Ruler', 'Plastic bag', 'Penguin', 'Watermelon', 'Harbor seal', 'Pen',
        'Pumpkin', 'Harp', 'Kitchen appliance', 'Roller skates', 'Bust',
        'Coffee table', 'Tennis ball', 'Tennis racket', 'Ladder', 'Boot',
        'Bowl', 'Stop sign', 'Volleyball', 'Eagle', 'Paddle', 'Chicken',
        'Skull', 'Lamp', 'Beehive', 'Maple', 'Sink', 'Goldfish', 'Tripod',
        'Coconut', 'Bidet', 'Tap', 'Bathroom cabinet', 'Toilet',
        'Filing cabinet', 'Pretzel', 'Table tennis racket', 'Bronze sculpture',
        'Rocket', 'Mouse', 'Hamster', 'Lizard', 'Lifejacket', 'Goat',
        'Washing machine', 'Trumpet', 'Horn', 'Trombone', 'Sheep',
        'Tablet computer', 'Pillow', 'Kitchen & dining room table',
        'Parachute', 'Raven', 'Glove', 'Loveseat', 'Christmas tree',
        'Shellfish', 'Rifle', 'Shotgun', 'Sushi', 'Sparrow', 'Bread',
        'Toaster', 'Watch', 'Asparagus', 'Artichoke', 'Suitcase', 'Antelope',
        'Broccoli', 'Ice cream', 'Racket', 'Banana', 'Cookie', 'Cucumber',
        'Dragonfly', 'Lynx', 'Caterpillar', 'Light bulb', 'Office supplies',
        'Miniskirt', 'Skirt', 'Fireplace', 'Potato', 'Light switch',
        'Croissant', 'Cabbage', 'Ladybug', 'Handgun', 'Luggage and bags',
        'Window blind', 'Snowboard', 'Baseball bat', 'Digital clock',
        'Serving tray', 'Infant bed', 'Sofa bed', 'Guacamole', 'Fox', 'Pizza',
        'Snowplow', 'Jet ski', 'Refrigerator', 'Lantern', 'Convenience store',
        'Sword', 'Rugby ball', 'Owl', 'Ostrich', 'Pancake', 'Strawberry',
        'Carrot', 'Tart', 'Dice', 'Turkey', 'Rabbit', 'Invertebrate', 'Vase',
        'Stool', 'Swim cap', 'Shower', 'Clock', 'Jellyfish', 'Aircraft',
        'Chopsticks', 'Orange', 'Snake', 'Sewing machine', 'Kangaroo', 'Mixer',
        'Food processor', 'Shrimp', 'Towel', 'Porcupine', 'Jaguar', 'Cannon',
        'Limousine', 'Mule', 'Squirrel', 'Kitchen knife', 'Tiara', 'Tiger',
        'Bow and arrow', 'Candy', 'Rhinoceros', 'Shark', 'Cricket ball',
        'Doughnut', 'Plumbing fixture', 'Camel', 'Polar bear', 'Coin',
        'Printer', 'Blender', 'Giraffe', 'Billiard table', 'Kettle',
        'Dinosaur', 'Pineapple', 'Zucchini', 'Jug', 'Barge', 'Teapot',
        'Golf ball', 'Binoculars', 'Scissors', 'Hot dog', 'Door handle',
        'Seahorse', 'Bathtub', 'Leopard', 'Centipede', 'Grapefruit', 'Snowman',
        'Cheetah', 'Alarm clock', 'Grape', 'Wrench', 'Wok', 'Bell pepper',
        'Cake stand', 'Barrel', 'Woodpecker', 'Flute', 'Corded phone',
        'Willow', 'Punching bag', 'Pomegranate', 'Telephone', 'Pear',
        'Common fig', 'Bench', 'Wood-burning stove', 'Burrito', 'Nail',
        'Turtle', 'Submarine sandwich', 'Drinking straw', 'Peach', 'Popcorn',
        'Frying pan', 'Picnic basket', 'Honeycomb', 'Envelope', 'Mango',
        'Cutting board', 'Pitcher', 'Stationary bicycle', 'Dumbbell',
        'Personal care', 'Dog bed', 'Snowmobile', 'Oboe', 'Briefcase',
        'Squash', 'Tick', 'Slow cooker', 'Coffeemaker', 'Measuring cup',
        'Crutch', 'Stretcher', 'Screwdriver', 'Flashlight', 'Spatula',
        'Pressure cooker', 'Ring binder', 'Beaker', 'Torch', 'Winter melon'
    ]

def lvis_classes():
    return [
        'aerosol_can', 'air_conditioner', 'airplane', 'alarm_clock', 'alcohol',
        'alligator', 'almond', 'ambulance', 'amplifier', 'anklet', 'antenna',
        'apple', 'applesauce', 'apricot', 'apron', 'aquarium',
        'arctic_(type_of_shoe)', 'armband', 'armchair', 'armoire', 'armor',
        'artichoke', 'trash_can', 'ashtray', 'asparagus', 'atomizer',
        'avocado', 'award', 'awning', 'ax', 'baboon', 'baby_buggy',
        'basketball_backboard', 'backpack', 'handbag', 'suitcase', 'bagel',
        'bagpipe', 'baguet', 'bait', 'ball', 'ballet_skirt', 'balloon',
        'bamboo', 'banana', 'Band_Aid', 'bandage', 'bandanna', 'banjo',
        'banner', 'barbell', 'barge', 'barrel', 'barrette', 'barrow',
        'baseball_base', 'baseball', 'baseball_bat', 'baseball_cap',
        'baseball_glove', 'basket', 'basketball', 'bass_horn', 'bat_(animal)',
        'bath_mat', 'bath_towel', 'bathrobe', 'bathtub', 'batter_(food)',
        'battery', 'beachball', 'bead', 'bean_curd', 'beanbag', 'beanie',
        'bear', 'bed', 'bedpan', 'bedspread', 'cow', 'beef_(food)', 'beeper',
        'beer_bottle', 'beer_can', 'beetle', 'bell', 'bell_pepper', 'belt',
        'belt_buckle', 'bench', 'beret', 'bib', 'Bible', 'bicycle', 'visor',
        'billboard', 'binder', 'binoculars', 'bird', 'birdfeeder', 'birdbath',
        'birdcage', 'birdhouse', 'birthday_cake', 'birthday_card',
        'pirate_flag', 'black_sheep', 'blackberry', 'blackboard', 'blanket',
        'blazer', 'blender', 'blimp', 'blinker', 'blouse', 'blueberry',
        'gameboard', 'boat', 'bob', 'bobbin', 'bobby_pin', 'boiled_egg',
        'bolo_tie', 'deadbolt', 'bolt', 'bonnet', 'book', 'bookcase',
        'booklet', 'bookmark', 'boom_microphone', 'boot', 'bottle',
        'bottle_opener', 'bouquet', 'bow_(weapon)', 'bow_(decorative_ribbons)',
        'bow-tie', 'bowl', 'pipe_bowl', 'bowler_hat', 'bowling_ball', 'box',
        'boxing_glove', 'suspenders', 'bracelet', 'brass_plaque', 'brassiere',
        'bread-bin', 'bread', 'breechcloth', 'bridal_gown', 'briefcase',
        'broccoli', 'broach', 'broom', 'brownie', 'brussels_sprouts',
        'bubble_gum', 'bucket', 'horse_buggy', 'bull', 'bulldog', 'bulldozer',
        'bullet_train', 'bulletin_board', 'bulletproof_vest', 'bullhorn',
        'bun', 'bunk_bed', 'buoy', 'burrito', 'bus_(vehicle)', 'business_card',
        'butter', 'butterfly', 'button', 'cab_(taxi)', 'cabana', 'cabin_car',
        'cabinet', 'locker', 'cake', 'calculator', 'calendar', 'calf',
        'camcorder', 'camel', 'camera', 'camera_lens', 'camper_(vehicle)',
        'can', 'can_opener', 'candle', 'candle_holder', 'candy_bar',
        'candy_cane', 'walking_cane', 'canister', 'canoe', 'cantaloup',
        'canteen', 'cap_(headwear)', 'bottle_cap', 'cape', 'cappuccino',
        'car_(automobile)', 'railcar_(part_of_a_train)', 'elevator_car',
        'car_battery', 'identity_card', 'card', 'cardigan', 'cargo_ship',
        'carnation', 'horse_carriage', 'carrot', 'tote_bag', 'cart', 'carton',
        'cash_register', 'casserole', 'cassette', 'cast', 'cat', 'cauliflower',
        'cayenne_(spice)', 'CD_player', 'celery', 'cellular_telephone',
        'chain_mail', 'chair', 'chaise_longue', 'chalice', 'chandelier',
        'chap', 'checkbook', 'checkerboard', 'cherry', 'chessboard',
        'chicken_(animal)', 'chickpea', 'chili_(vegetable)', 'chime',
        'chinaware', 'crisp_(potato_chip)', 'poker_chip', 'chocolate_bar',
        'chocolate_cake', 'chocolate_milk', 'chocolate_mousse', 'choker',
        'chopping_board', 'chopstick', 'Christmas_tree', 'slide', 'cider',
        'cigar_box', 'cigarette', 'cigarette_case', 'cistern', 'clarinet',
        'clasp', 'cleansing_agent', 'cleat_(for_securing_rope)', 'clementine',
        'clip', 'clipboard', 'clippers_(for_plants)', 'cloak', 'clock',
        'clock_tower', 'clothes_hamper', 'clothespin', 'clutch_bag', 'coaster',
        'coat', 'coat_hanger', 'coatrack', 'cock', 'cockroach',
        'cocoa_(beverage)', 'coconut', 'coffee_maker', 'coffee_table',
        'coffeepot', 'coil', 'coin', 'colander', 'coleslaw',
        'coloring_material', 'combination_lock', 'pacifier', 'comic_book',
        'compass', 'computer_keyboard', 'condiment', 'cone', 'control',
        'convertible_(automobile)', 'sofa_bed', 'cooker', 'cookie',
        'cooking_utensil', 'cooler_(for_food)', 'cork_(bottle_plug)',
        'corkboard', 'corkscrew', 'edible_corn', 'cornbread', 'cornet',
        'cornice', 'cornmeal', 'corset', 'costume', 'cougar', 'coverall',
        'cowbell', 'cowboy_hat', 'crab_(animal)', 'crabmeat', 'cracker',
        'crape', 'crate', 'crayon', 'cream_pitcher', 'crescent_roll', 'crib',
        'crock_pot', 'crossbar', 'crouton', 'crow', 'crowbar', 'crown',
        'crucifix', 'cruise_ship', 'police_cruiser', 'crumb', 'crutch',
        'cub_(animal)', 'cube', 'cucumber', 'cufflink', 'cup', 'trophy_cup',
        'cupboard', 'cupcake', 'hair_curler', 'curling_iron', 'curtain',
        'cushion', 'cylinder', 'cymbal', 'dagger', 'dalmatian', 'dartboard',
        'date_(fruit)', 'deck_chair', 'deer', 'dental_floss', 'desk',
        'detergent', 'diaper', 'diary', 'die', 'dinghy', 'dining_table', 'tux',
        'dish', 'dish_antenna', 'dishrag', 'dishtowel', 'dishwasher',
        'dishwasher_detergent', 'dispenser', 'diving_board', 'Dixie_cup',
        'dog', 'dog_collar', 'doll', 'dollar', 'dollhouse', 'dolphin',
        'domestic_ass', 'doorknob', 'doormat', 'doughnut', 'dove', 'dragonfly',
        'drawer', 'underdrawers', 'dress', 'dress_hat', 'dress_suit',
        'dresser', 'drill', 'drone', 'dropper', 'drum_(musical_instrument)',
        'drumstick', 'duck', 'duckling', 'duct_tape', 'duffel_bag', 'dumbbell',
        'dumpster', 'dustpan', 'eagle', 'earphone', 'earplug', 'earring',
        'easel', 'eclair', 'eel', 'egg', 'egg_roll', 'egg_yolk', 'eggbeater',
        'eggplant', 'electric_chair', 'refrigerator', 'elephant', 'elk',
        'envelope', 'eraser', 'escargot', 'eyepatch', 'falcon', 'fan',
        'faucet', 'fedora', 'ferret', 'Ferris_wheel', 'ferry', 'fig_(fruit)',
        'fighter_jet', 'figurine', 'file_cabinet', 'file_(tool)', 'fire_alarm',
        'fire_engine', 'fire_extinguisher', 'fire_hose', 'fireplace',
        'fireplug', 'first-aid_kit', 'fish', 'fish_(food)', 'fishbowl',
        'fishing_rod', 'flag', 'flagpole', 'flamingo', 'flannel', 'flap',
        'flash', 'flashlight', 'fleece', 'flip-flop_(sandal)',
        'flipper_(footwear)', 'flower_arrangement', 'flute_glass', 'foal',
        'folding_chair', 'food_processor', 'football_(American)',
        'football_helmet', 'footstool', 'fork', 'forklift', 'freight_car',
        'French_toast', 'freshener', 'frisbee', 'frog', 'fruit_juice',
        'frying_pan', 'fudge', 'funnel', 'futon', 'gag', 'garbage',
        'garbage_truck', 'garden_hose', 'gargle', 'gargoyle', 'garlic',
        'gasmask', 'gazelle', 'gelatin', 'gemstone', 'generator',
        'giant_panda', 'gift_wrap', 'ginger', 'giraffe', 'cincture',
        'glass_(drink_container)', 'globe', 'glove', 'goat', 'goggles',
        'goldfish', 'golf_club', 'golfcart', 'gondola_(boat)', 'goose',
        'gorilla', 'gourd', 'grape', 'grater', 'gravestone', 'gravy_boat',
        'green_bean', 'green_onion', 'griddle', 'grill', 'grits', 'grizzly',
        'grocery_bag', 'guitar', 'gull', 'gun', 'hairbrush', 'hairnet',
        'hairpin', 'halter_top', 'ham', 'hamburger', 'hammer', 'hammock',
        'hamper', 'hamster', 'hair_dryer', 'hand_glass', 'hand_towel',
        'handcart', 'handcuff', 'handkerchief', 'handle', 'handsaw',
        'hardback_book', 'harmonium', 'hat', 'hatbox', 'veil', 'headband',
        'headboard', 'headlight', 'headscarf', 'headset',
        'headstall_(for_horses)', 'heart', 'heater', 'helicopter', 'helmet',
        'heron', 'highchair', 'hinge', 'hippopotamus', 'hockey_stick', 'hog',
        'home_plate_(baseball)', 'honey', 'fume_hood', 'hook', 'hookah',
        'hornet', 'horse', 'hose', 'hot-air_balloon', 'hotplate', 'hot_sauce',
        'hourglass', 'houseboat', 'hummingbird', 'hummus', 'polar_bear',
        'icecream', 'popsicle', 'ice_maker', 'ice_pack', 'ice_skate',
        'igniter', 'inhaler', 'iPod', 'iron_(for_clothing)', 'ironing_board',
        'jacket', 'jam', 'jar', 'jean', 'jeep', 'jelly_bean', 'jersey',
        'jet_plane', 'jewel', 'jewelry', 'joystick', 'jumpsuit', 'kayak',
        'keg', 'kennel', 'kettle', 'key', 'keycard', 'kilt', 'kimono',
        'kitchen_sink', 'kitchen_table', 'kite', 'kitten', 'kiwi_fruit',
        'knee_pad', 'knife', 'knitting_needle', 'knob', 'knocker_(on_a_door)',
        'koala', 'lab_coat', 'ladder', 'ladle', 'ladybug', 'lamb_(animal)',
        'lamb-chop', 'lamp', 'lamppost', 'lampshade', 'lantern', 'lanyard',
        'laptop_computer', 'lasagna', 'latch', 'lawn_mower', 'leather',
        'legging_(clothing)', 'Lego', 'legume', 'lemon', 'lemonade', 'lettuce',
        'license_plate', 'life_buoy', 'life_jacket', 'lightbulb',
        'lightning_rod', 'lime', 'limousine', 'lion', 'lip_balm', 'liquor',
        'lizard', 'log', 'lollipop', 'speaker_(stereo_equipment)', 'loveseat',
        'machine_gun', 'magazine', 'magnet', 'mail_slot', 'mailbox_(at_home)',
        'mallard', 'mallet', 'mammoth', 'manatee', 'mandarin_orange', 'manger',
        'manhole', 'map', 'marker', 'martini', 'mascot', 'mashed_potato',
        'masher', 'mask', 'mast', 'mat_(gym_equipment)', 'matchbox',
        'mattress', 'measuring_cup', 'measuring_stick', 'meatball', 'medicine',
        'melon', 'microphone', 'microscope', 'microwave_oven', 'milestone',
        'milk', 'milk_can', 'milkshake', 'minivan', 'mint_candy', 'mirror',
        'mitten', 'mixer_(kitchen_tool)', 'money',
        'monitor_(computer_equipment) computer_monitor', 'monkey', 'motor',
        'motor_scooter', 'motor_vehicle', 'motorcycle', 'mound_(baseball)',
        'mouse_(computer_equipment)', 'mousepad', 'muffin', 'mug', 'mushroom',
        'music_stool', 'musical_instrument', 'nailfile', 'napkin',
        'neckerchief', 'necklace', 'necktie', 'needle', 'nest', 'newspaper',
        'newsstand', 'nightshirt', 'nosebag_(for_animals)',
        'noseband_(for_animals)', 'notebook', 'notepad', 'nut', 'nutcracker',
        'oar', 'octopus_(food)', 'octopus_(animal)', 'oil_lamp', 'olive_oil',
        'omelet', 'onion', 'orange_(fruit)', 'orange_juice', 'ostrich',
        'ottoman', 'oven', 'overalls_(clothing)', 'owl', 'packet', 'inkpad',
        'pad', 'paddle', 'padlock', 'paintbrush', 'painting', 'pajamas',
        'palette', 'pan_(for_cooking)', 'pan_(metal_container)', 'pancake',
        'pantyhose', 'papaya', 'paper_plate', 'paper_towel', 'paperback_book',
        'paperweight', 'parachute', 'parakeet', 'parasail_(sports)', 'parasol',
        'parchment', 'parka', 'parking_meter', 'parrot',
        'passenger_car_(part_of_a_train)', 'passenger_ship', 'passport',
        'pastry', 'patty_(food)', 'pea_(food)', 'peach', 'peanut_butter',
        'pear', 'peeler_(tool_for_fruit_and_vegetables)', 'wooden_leg',
        'pegboard', 'pelican', 'pen', 'pencil', 'pencil_box',
        'pencil_sharpener', 'pendulum', 'penguin', 'pennant', 'penny_(coin)',
        'pepper', 'pepper_mill', 'perfume', 'persimmon', 'person', 'pet',
        'pew_(church_bench)', 'phonebook', 'phonograph_record', 'piano',
        'pickle', 'pickup_truck', 'pie', 'pigeon', 'piggy_bank', 'pillow',
        'pin_(non_jewelry)', 'pineapple', 'pinecone', 'ping-pong_ball',
        'pinwheel', 'tobacco_pipe', 'pipe', 'pistol', 'pita_(bread)',
        'pitcher_(vessel_for_liquid)', 'pitchfork', 'pizza', 'place_mat',
        'plate', 'platter', 'playpen', 'pliers', 'plow_(farm_equipment)',
        'plume', 'pocket_watch', 'pocketknife', 'poker_(fire_stirring_tool)',
        'pole', 'polo_shirt', 'poncho', 'pony', 'pool_table', 'pop_(soda)',
        'postbox_(public)', 'postcard', 'poster', 'pot', 'flowerpot', 'potato',
        'potholder', 'pottery', 'pouch', 'power_shovel', 'prawn', 'pretzel',
        'printer', 'projectile_(weapon)', 'projector', 'propeller', 'prune',
        'pudding', 'puffer_(fish)', 'puffin', 'pug-dog', 'pumpkin', 'puncher',
        'puppet', 'puppy', 'quesadilla', 'quiche', 'quilt', 'rabbit',
        'race_car', 'racket', 'radar', 'radiator', 'radio_receiver', 'radish',
        'raft', 'rag_doll', 'raincoat', 'ram_(animal)', 'raspberry', 'rat',
        'razorblade', 'reamer_(juicer)', 'rearview_mirror', 'receipt',
        'recliner', 'record_player', 'reflector', 'remote_control',
        'rhinoceros', 'rib_(food)', 'rifle', 'ring', 'river_boat', 'road_map',
        'robe', 'rocking_chair', 'rodent', 'roller_skate', 'Rollerblade',
        'rolling_pin', 'root_beer', 'router_(computer_equipment)',
        'rubber_band', 'runner_(carpet)', 'plastic_bag',
        'saddle_(on_an_animal)', 'saddle_blanket', 'saddlebag', 'safety_pin',
        'sail', 'salad', 'salad_plate', 'salami', 'salmon_(fish)',
        'salmon_(food)', 'salsa', 'saltshaker', 'sandal_(type_of_shoe)',
        'sandwich', 'satchel', 'saucepan', 'saucer', 'sausage', 'sawhorse',
        'saxophone', 'scale_(measuring_instrument)', 'scarecrow', 'scarf',
        'school_bus', 'scissors', 'scoreboard', 'scraper', 'screwdriver',
        'scrubbing_brush', 'sculpture', 'seabird', 'seahorse', 'seaplane',
        'seashell', 'sewing_machine', 'shaker', 'shampoo', 'shark',
        'sharpener', 'Sharpie', 'shaver_(electric)', 'shaving_cream', 'shawl',
        'shears', 'sheep', 'shepherd_dog', 'sherbert', 'shield', 'shirt',
        'shoe', 'shopping_bag', 'shopping_cart', 'short_pants', 'shot_glass',
        'shoulder_bag', 'shovel', 'shower_head', 'shower_cap',
        'shower_curtain', 'shredder_(for_paper)', 'signboard', 'silo', 'sink',
        'skateboard', 'skewer', 'ski', 'ski_boot', 'ski_parka', 'ski_pole',
        'skirt', 'skullcap', 'sled', 'sleeping_bag', 'sling_(bandage)',
        'slipper_(footwear)', 'smoothie', 'snake', 'snowboard', 'snowman',
        'snowmobile', 'soap', 'soccer_ball', 'sock', 'sofa', 'softball',
        'solar_array', 'sombrero', 'soup', 'soup_bowl', 'soupspoon',
        'sour_cream', 'soya_milk', 'space_shuttle', 'sparkler_(fireworks)',
        'spatula', 'spear', 'spectacles', 'spice_rack', 'spider', 'crawfish',
        'sponge', 'spoon', 'sportswear', 'spotlight', 'squid_(food)',
        'squirrel', 'stagecoach', 'stapler_(stapling_machine)', 'starfish',
        'statue_(sculpture)', 'steak_(food)', 'steak_knife', 'steering_wheel',
        'stepladder', 'step_stool', 'stereo_(sound_system)', 'stew', 'stirrer',
        'stirrup', 'stool', 'stop_sign', 'brake_light', 'stove', 'strainer',
        'strap', 'straw_(for_drinking)', 'strawberry', 'street_sign',
        'streetlight', 'string_cheese', 'stylus', 'subwoofer', 'sugar_bowl',
        'sugarcane_(plant)', 'suit_(clothing)', 'sunflower', 'sunglasses',
        'sunhat', 'surfboard', 'sushi', 'mop', 'sweat_pants', 'sweatband',
        'sweater', 'sweatshirt', 'sweet_potato', 'swimsuit', 'sword',
        'syringe', 'Tabasco_sauce', 'table-tennis_table', 'table',
        'table_lamp', 'tablecloth', 'tachometer', 'taco', 'tag', 'taillight',
        'tambourine', 'army_tank', 'tank_(storage_vessel)',
        'tank_top_(clothing)', 'tape_(sticky_cloth_or_paper)', 'tape_measure',
        'tapestry', 'tarp', 'tartan', 'tassel', 'tea_bag', 'teacup',
        'teakettle', 'teapot', 'teddy_bear', 'telephone', 'telephone_booth',
        'telephone_pole', 'telephoto_lens', 'television_camera',
        'television_set', 'tennis_ball', 'tennis_racket', 'tequila',
        'thermometer', 'thermos_bottle', 'thermostat', 'thimble', 'thread',
        'thumbtack', 'tiara', 'tiger', 'tights_(clothing)', 'timer', 'tinfoil',
        'tinsel', 'tissue_paper', 'toast_(food)', 'toaster', 'toaster_oven',
        'toilet', 'toilet_tissue', 'tomato', 'tongs', 'toolbox', 'toothbrush',
        'toothpaste', 'toothpick', 'cover', 'tortilla', 'tow_truck', 'towel',
        'towel_rack', 'toy', 'tractor_(farm_equipment)', 'traffic_light',
        'dirt_bike', 'trailer_truck', 'train_(railroad_vehicle)', 'trampoline',
        'tray', 'trench_coat', 'triangle_(musical_instrument)', 'tricycle',
        'tripod', 'trousers', 'truck', 'truffle_(chocolate)', 'trunk', 'vat',
        'turban', 'turkey_(food)', 'turnip', 'turtle', 'turtleneck_(clothing)',
        'typewriter', 'umbrella', 'underwear', 'unicycle', 'urinal', 'urn',
        'vacuum_cleaner', 'vase', 'vending_machine', 'vent', 'vest',
        'videotape', 'vinegar', 'violin', 'vodka', 'volleyball', 'vulture',
        'waffle', 'waffle_iron', 'wagon', 'wagon_wheel', 'walking_stick',
        'wall_clock', 'wall_socket', 'wallet', 'walrus', 'wardrobe',
        'washbasin', 'automatic_washer', 'watch', 'water_bottle',
        'water_cooler', 'water_faucet', 'water_heater', 'water_jug',
        'water_gun', 'water_scooter', 'water_ski', 'water_tower',
        'watering_can', 'watermelon', 'weathervane', 'webcam', 'wedding_cake',
        'wedding_ring', 'wet_suit', 'wheel', 'wheelchair', 'whipped_cream',
        'whistle', 'wig', 'wind_chime', 'windmill', 'window_box_(for_plants)',
        'windshield_wiper', 'windsock', 'wine_bottle', 'wine_bucket',
        'wineglass', 'blinder_(for_horses)', 'wok', 'wolf', 'wooden_spoon',
        'wreath', 'wrench', 'wristband', 'wristlet', 'yacht', 'yogurt',
        'yoke_(animal_equipment)', 'zebra', 'zucchini'
    ]
def oid_v6_classes():
    return [
        'Tortoise', 'Container', 'Magpie', 'Sea turtle', 'Football',
        'Ambulance', 'Ladder', 'Toothbrush', 'Syringe', 'Sink', 'Toy',
        'Organ (Musical Instrument)', 'Cassette deck', 'Apple', 'Human eye',
        'Cosmetics', 'Paddle', 'Snowman', 'Beer', 'Chopsticks', 'Human beard',
        'Bird', 'Parking meter', 'Traffic light', 'Croissant', 'Cucumber',
        'Radish', 'Towel', 'Doll', 'Skull', 'Washing machine', 'Glove', 'Tick',
        'Belt', 'Sunglasses', 'Banjo', 'Cart', 'Ball', 'Backpack', 'Bicycle',
        'Home appliance', 'Centipede', 'Boat', 'Surfboard', 'Boot',
        'Headphones', 'Hot dog', 'Shorts', 'Fast food', 'Bus', 'Boy',
        'Screwdriver', 'Bicycle wheel', 'Barge', 'Laptop', 'Miniskirt',
        'Drill (Tool)', 'Dress', 'Bear', 'Waffle', 'Pancake', 'Brown bear',
        'Woodpecker', 'Blue jay', 'Pretzel', 'Bagel', 'Tower', 'Teapot',
        'Person', 'Bow and arrow', 'Swimwear', 'Beehive', 'Brassiere', 'Bee',
        'Bat (Animal)', 'Starfish', 'Popcorn', 'Burrito', 'Chainsaw',
        'Balloon', 'Wrench', 'Tent', 'Vehicle registration plate', 'Lantern',
        'Toaster', 'Flashlight', 'Billboard', 'Tiara', 'Limousine', 'Necklace',
        'Carnivore', 'Scissors', 'Stairs', 'Computer keyboard', 'Printer',
        'Traffic sign', 'Chair', 'Shirt', 'Poster', 'Cheese', 'Sock',
        'Fire hydrant', 'Land vehicle', 'Earrings', 'Tie', 'Watercraft',
        'Cabinetry', 'Suitcase', 'Muffin', 'Bidet', 'Snack', 'Snowmobile',
        'Clock', 'Medical equipment', 'Cattle', 'Cello', 'Jet ski', 'Camel',
        'Coat', 'Suit', 'Desk', 'Cat', 'Bronze sculpture', 'Juice', 'Gondola',
        'Beetle', 'Cannon', 'Computer mouse', 'Cookie', 'Office building',
        'Fountain', 'Coin', 'Calculator', 'Cocktail', 'Computer monitor',
        'Box', 'Stapler', 'Christmas tree', 'Cowboy hat', 'Hiking equipment',
        'Studio couch', 'Drum', 'Dessert', 'Wine rack', 'Drink', 'Zucchini',
        'Ladle', 'Human mouth', 'Dairy Product', 'Dice', 'Oven', 'Dinosaur',
        'Ratchet (Device)', 'Couch', 'Cricket ball', 'Winter melon', 'Spatula',
        'Whiteboard', 'Pencil sharpener', 'Door', 'Hat', 'Shower', 'Eraser',
        'Fedora', 'Guacamole', 'Dagger', 'Scarf', 'Dolphin', 'Sombrero',
        'Tin can', 'Mug', 'Tap', 'Harbor seal', 'Stretcher', 'Can opener',
        'Goggles', 'Human body', 'Roller skates', 'Coffee cup',
        'Cutting board', 'Blender', 'Plumbing fixture', 'Stop sign',
        'Office supplies', 'Volleyball (Ball)', 'Vase', 'Slow cooker',
        'Wardrobe', 'Coffee', 'Whisk', 'Paper towel', 'Personal care', 'Food',
        'Sun hat', 'Tree house', 'Flying disc', 'Skirt', 'Gas stove',
        'Salt and pepper shakers', 'Mechanical fan', 'Face powder', 'Fax',
        'Fruit', 'French fries', 'Nightstand', 'Barrel', 'Kite', 'Tart',
        'Treadmill', 'Fox', 'Flag', 'French horn', 'Window blind',
        'Human foot', 'Golf cart', 'Jacket', 'Egg (Food)', 'Street light',
        'Guitar', 'Pillow', 'Human leg', 'Isopod', 'Grape', 'Human ear',
        'Power plugs and sockets', 'Panda', 'Giraffe', 'Woman', 'Door handle',
        'Rhinoceros', 'Bathtub', 'Goldfish', 'Houseplant', 'Goat',
        'Baseball bat', 'Baseball glove', 'Mixing bowl',
        'Marine invertebrates', 'Kitchen utensil', 'Light switch', 'House',
        'Horse', 'Stationary bicycle', 'Hammer', 'Ceiling fan', 'Sofa bed',
        'Adhesive tape', 'Harp', 'Sandal', 'Bicycle helmet', 'Saucer',
        'Harpsichord', 'Human hair', 'Heater', 'Harmonica', 'Hamster',
        'Curtain', 'Bed', 'Kettle', 'Fireplace', 'Scale', 'Drinking straw',
        'Insect', 'Hair dryer', 'Kitchenware', 'Indoor rower', 'Invertebrate',
        'Food processor', 'Bookcase', 'Refrigerator', 'Wood-burning stove',
        'Punching bag', 'Common fig', 'Cocktail shaker', 'Jaguar (Animal)',
        'Golf ball', 'Fashion accessory', 'Alarm clock', 'Filing cabinet',
        'Artichoke', 'Table', 'Tableware', 'Kangaroo', 'Koala', 'Knife',
        'Bottle', 'Bottle opener', 'Lynx', 'Lavender (Plant)', 'Lighthouse',
        'Dumbbell', 'Human head', 'Bowl', 'Humidifier', 'Porch', 'Lizard',
        'Billiard table', 'Mammal', 'Mouse', 'Motorcycle',
        'Musical instrument', 'Swim cap', 'Frying pan', 'Snowplow',
        'Bathroom cabinet', 'Missile', 'Bust', 'Man', 'Waffle iron', 'Milk',
        'Ring binder', 'Plate', 'Mobile phone', 'Baked goods', 'Mushroom',
        'Crutch', 'Pitcher (Container)', 'Mirror', 'Personal flotation device',
        'Table tennis racket', 'Pencil case', 'Musical keyboard', 'Scoreboard',
        'Briefcase', 'Kitchen knife', 'Nail (Construction)', 'Tennis ball',
        'Plastic bag', 'Oboe', 'Chest of drawers', 'Ostrich', 'Piano', 'Girl',
        'Plant', 'Potato', 'Hair spray', 'Sports equipment', 'Pasta',
        'Penguin', 'Pumpkin', 'Pear', 'Infant bed', 'Polar bear', 'Mixer',
        'Cupboard', 'Jacuzzi', 'Pizza', 'Digital clock', 'Pig', 'Reptile',
        'Rifle', 'Lipstick', 'Skateboard', 'Raven', 'High heels', 'Red panda',
        'Rose', 'Rabbit', 'Sculpture', 'Saxophone', 'Shotgun', 'Seafood',
        'Submarine sandwich', 'Snowboard', 'Sword', 'Picture frame', 'Sushi',
        'Loveseat', 'Ski', 'Squirrel', 'Tripod', 'Stethoscope', 'Submarine',
        'Scorpion', 'Segway', 'Training bench', 'Snake', 'Coffee table',
        'Skyscraper', 'Sheep', 'Television', 'Trombone', 'Tea', 'Tank', 'Taco',
        'Telephone', 'Torch', 'Tiger', 'Strawberry', 'Trumpet', 'Tree',
        'Tomato', 'Train', 'Tool', 'Picnic basket', 'Cooking spray',
        'Trousers', 'Bowling equipment', 'Football helmet', 'Truck',
        'Measuring cup', 'Coffeemaker', 'Violin', 'Vehicle', 'Handbag',
        'Paper cutter', 'Wine', 'Weapon', 'Wheel', 'Worm', 'Wok', 'Whale',
        'Zebra', 'Auto part', 'Jug', 'Pizza cutter', 'Cream', 'Monkey', 'Lion',
        'Bread', 'Platter', 'Chicken', 'Eagle', 'Helicopter', 'Owl', 'Duck',
        'Turtle', 'Hippopotamus', 'Crocodile', 'Toilet', 'Toilet paper',
        'Squid', 'Clothing', 'Footwear', 'Lemon', 'Spider', 'Deer', 'Frog',
        'Banana', 'Rocket', 'Wine glass', 'Countertop', 'Tablet computer',
        'Waste container', 'Swimming pool', 'Dog', 'Book', 'Elephant', 'Shark',
        'Candle', 'Leopard', 'Axe', 'Hand dryer', 'Soap dispenser',
        'Porcupine', 'Flower', 'Canary', 'Cheetah', 'Palm tree', 'Hamburger',
        'Maple', 'Building', 'Fish', 'Lobster', 'Garden Asparagus',
        'Furniture', 'Hedgehog', 'Airplane', 'Spoon', 'Otter', 'Bull',
        'Oyster', 'Horizontal bar', 'Convenience store', 'Bomb', 'Bench',
        'Ice cream', 'Caterpillar', 'Butterfly', 'Parachute', 'Orange',
        'Antelope', 'Beaker', 'Moths and butterflies', 'Window', 'Closet',
        'Castle', 'Jellyfish', 'Goose', 'Mule', 'Swan', 'Peach', 'Coconut',
        'Seat belt', 'Raccoon', 'Chisel', 'Fork', 'Lamp', 'Camera',
        'Squash (Plant)', 'Racket', 'Human face', 'Human arm', 'Vegetable',
        'Diaper', 'Unicycle', 'Falcon', 'Chime', 'Snail', 'Shellfish',
        'Cabbage', 'Carrot', 'Mango', 'Jeans', 'Flowerpot', 'Pineapple',
        'Drawer', 'Stool', 'Envelope', 'Cake', 'Dragonfly', 'Common sunflower',
        'Microwave oven', 'Honeycomb', 'Marine mammal', 'Sea lion', 'Ladybug',
        'Shelf', 'Watch', 'Candy', 'Salad', 'Parrot', 'Handgun', 'Sparrow',
        'Van', 'Grinder', 'Spice rack', 'Light bulb', 'Corded phone',
        'Sports uniform', 'Tennis racket', 'Wall clock', 'Serving tray',
        'Kitchen & dining room table', 'Dog bed', 'Cake stand',
        'Cat furniture', 'Bathroom accessory', 'Facial tissue holder',
        'Pressure cooker', 'Kitchen appliance', 'Tire', 'Ruler',
        'Luggage and bags', 'Microphone', 'Broccoli', 'Umbrella', 'Pastry',
        'Grapefruit', 'Band-aid', 'Animal', 'Bell pepper', 'Turkey', 'Lily',
        'Pomegranate', 'Doughnut', 'Glasses', 'Human nose', 'Pen', 'Ant',
        'Car', 'Aircraft', 'Human hand', 'Skunk', 'Teddy bear', 'Watermelon',
        'Cantaloupe', 'Dishwasher', 'Flute', 'Balance beam', 'Sandwich',
        'Shrimp', 'Sewing machine', 'Binoculars', 'Rays and skates', 'Ipod',
        'Accordion', 'Willow', 'Crab', 'Crown', 'Seahorse', 'Perfume',
        'Alpaca', 'Taxi', 'Canoe', 'Remote control', 'Wheelchair',
        'Rugby ball', 'Armadillo', 'Maracas', 'Helmet'
    ]


dataset_aliases = {
    DatasetEnum.VOC: ['voc', 'pascal_voc', 'voc07', 'voc12'],
    DatasetEnum.IMAGENET_DET: ['det', 'imagenet_det', 'ilsvrc_det'],
    DatasetEnum.IMAGENET_VID: ['vid', 'imagenet_vid', 'ilsvrc_vid'],
    DatasetEnum.COCO: ['coco', 'mscoco', 'ms_coco'],
    DatasetEnum.SUN: ['sun'],
    DatasetEnum.LVIS: ['lvis'],
    DatasetEnum.WIDER_FACE: ['WIDERFaceDataset', 'wider_face', 'WIDERFace'],
    DatasetEnum.CITYSCAPES: ['cityscapes'],
    DatasetEnum.OID_CHALLENGE: ['oid_challenge', 'openimages_challenge'],
    DatasetEnum.OID_V6: ['oid_v6', 'openimages_v6']
}

# def get_classes(dataset):
#     """Get class names of a dataset."""
#     alias2name = {}
#     for name, aliases in dataset_aliases.items():
#         for alias in aliases:
#             alias2name[alias] = name

#     if mmcv.is_str(dataset):
#         if dataset in alias2name:
#             labels = eval(alias2name[dataset] + '_classes()')
#         else:
#             raise ValueError(f'Unrecognized dataset: {dataset}')
#     else:
#         raise TypeError(f'dataset must a str, but got {type(dataset)}')
#     return labels

def get_classes(dataset):
    """Get class names of a dataset."""
    dataset=DatasetEnum.SUN ## 修改的地方
    if isinstance(dataset, DatasetEnum):
        if dataset in dataset_aliases:
            labels = eval(dataset_aliases[dataset][0] + '_classes()')
        else:
            raise ValueError(f'Unrecognized dataset: {dataset}')
    else:
        raise TypeError(f'dataset must be a DatasetEnum member, but got {type(dataset)}')
    return labels