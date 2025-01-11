from db import db

from models.collections import Collections

collections_list = [
    {
        "name": "Super Mario Bros.",
        "description": "A classic platformer where Mario embarks on a quest to rescue Princess Peach from Bowser.",
        "image_url": "https://i.ebayimg.com/images/g/eV8AAOSweOhh5i-k/s-l1200.jpg"
    },
    {
        "name": "Super Mario Bros. 3",
        "description": "An iconic platformer that introduces new power-ups and an overworld map.",
        "image_url": "https://preview.redd.it/title-screen-from-super-mario-bros-3-id-0mdjyp7t-v0-619xejuerjka1.png?width=512&format=png&auto=webp&s=b4c082e51250c2739671f7fd4333f79b8b8c214f"
    },
    {
        "name": "Super Mario World",
        "description": "A groundbreaking platformer with expansive levels and the debut of Yoshi.",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/3/32/Super_Mario_World_Coverart.png"
    },
    {
        "name": "Super Mario 64",
        "description": "A revolutionary 3D platformer where Mario explores vast, open-world environments in 3D.",
        "image_url": "https://www.nintendo.com/eu/media/images/10_share_images/games_15/nintendo_7/SI_N64_SuperMario64.jpg"
    },
    {
        "name": "Super Mario Odyssey",
        "description": "A 3D platformer with innovative mechanics, including Mario's new friend Cappy, and vast, diverse worlds.",
        "image_url": "https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/software/switch/70010000001130/c42553b4fd0312c31e70ec7468c6c9bccd739f340152925b9600631f2d29f8b5"
    },
    {
        "name": "Mega Man",
        "description": "The original Mega Man game, introducing the series' signature gameplay and six Robot Masters.",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/9/9b/Rockman_1987.jpg"
    },
    {
        "name": "Mega Man 2",
        "description": "The second game in the series, widely regarded as one of the best, featuring eight Robot Masters and refined gameplay.",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/Rockman_2_1988.jpg/220px-Rockman_2_1988.jpg"
    },
    {
        "name": "Mega Man 3",
        "description": "The third entry in the series, introducing the slide mechanic and Proto Man.",
        "image_url": "https://preview.redd.it/qqep1bbbf8f81.jpg?width=640&crop=smart&auto=webp&s=339b9726731d920de81967f970f475290a0550d7"
    },
    {
        "name": "Mega Man 4",
        "description": "Mega Man's fourth adventure, which introduces the charge shot ability.",
        "image_url": "https://e.snmc.io/lk/fv/x/8098e505aeb6ce3c2e10953ae78d2423/11877607"
    },
    {
        "name": "Mega Man 5",
        "description": "The fifth installment, with new gameplay tweaks and eight new Robot Masters.",
        "image_url": "https://www.sprites-inc.co.uk/files/Classic/MMLC/Artwork/BoxArt/04-MM5.png"
    },
    {
        "name": "Mega Man 6",
        "description": "The sixth entry, which was the last Mega Man game for the NES, featuring Rush Adaptors for more versatile gameplay.",
        "image_url": "https://e.snmc.io/lk/lv/x/889b818c5be6f3ce308bc85b7c9625d5/11877333"
    },
    {
        "name": "Mega Man 7",
        "description": "The first Mega Man game for the Super NES, featuring more detailed sprites and a storyline involving Bass and Treble.",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/2/27/Mega_Man_7_Coverart.jpg"
    },
    {
        "name": "Mega Man 8",
        "description": "The first and only Mega Man game on the original PlayStation, featuring 2.5D graphics and eight Robot Masters.",
        "image_url": "https://e.snmc.io/lk/lv/x/fbfb242394c60fd6ce3d9953884bd837/5277365"
    },
    {
        "name": "Mega Man 9",
        "description": "The ninth entry returns to 8-bit graphics and mechanics, bringing back the classic NES-style gameplay.",
        "image_url": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtRH7KEmJxp6rfE8bla5LYrhJ7HF_Okl99QWemCbHENvh5xlMpSlY-TCeuq_Wy5VkXGXGFBIV4frIBKrAaLGgYhuUpLodnyV7CwJwyTumaUc1ANe_r5qT4uWpQ27XM8AlNbHax6fi7ORZx/s1600/mega+man+9+title+screen.jpg"
    },
    {
        "name": "Mega Man 10",
        "description": "The tenth game, also in 8-bit style, featuring a harder difficulty mode and extra playable characters.",
        "image_url": "https://i.ytimg.com/vi/0c701F1t950/hqdefault.jpg"
    },
    {
        "name": "Mega Man 11",
        "description": "The latest entry in the series, featuring a 2.5D style, the Double Gear system, and vibrant graphics.",
        "image_url": "https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/software/switch/70010000003964/50637ae3b8fe8d88c7617d9fa10f8a13ddad1c3e3066d4342f286771c6403c5f"
    },
    {
        "name": "Mega Man & Bass",
        "description": "A spin-off game that allows players to choose between Mega Man and Bass, with different abilities for each character.",
        "image_url": "https://www.nintendo.com/eu/media/images/10_share_images/games_15/virtual_console_wii_u_7/SI_WiiUVC_MegamanAndBass_image1600w.jpg"
    }
    
]

def add_collections():
    for index, collection in enumerate(collections_list):
        if not db.session.query(Collections).filter(Collections.name == collection["name"]).first():

            name = collection["name"]
            description = collection["description"]
            image_url = collection["image_url"]
            new_collection = Collections(name, description, image_url, False)

            db.session.add(new_collection)
            
    db.session.commit()

