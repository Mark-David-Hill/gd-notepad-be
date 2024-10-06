from db import db

from models.game_elements import GameElements
from models.games import Games
from models.types import Types


enemies_list = [
    {
        "description": "A Mario enemy",
        "image_url": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/568b364a-1f61-4a93-b875-eeb2069ddf57/dfpro2l-28600397-d28c-42e2-9321-105a48d8fd3e.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzU2OGIzNjRhLTFmNjEtNGE5My1iODc1LWVlYjIwNjlkZGY1N1wvZGZwcm8ybC0yODYwMDM5Ny1kMjhjLTQyZTItOTMyMS0xMDVhNDhkOGZkM2UucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.H-ZbJl8b9IHg_Q3OfH208p-tXPcYZ6ciuPE2Qfdd2Ow",
        "name": "Goomba"
    },
    {
        "description": "A turtle-like enemy that can be kicked",
        "image_url": "https://s2.aminoapps.com/image/4ppllvib5f6h47b5fcjjdcv6b2fvpmh5_hq.jpg",
        "name": "Green Shell Koopa Troopa"
    },
    {
        "description": "A turtle-like enemy that can be kicked. Unlike Green Shell Koopas, will not walk off edges",
        "image_url": "https://cdn3.iconfinder.com/data/icons/pixel-nes-mario-characters/105/Super_Mario_Bros_Page_28-512.png",
        "name": "Red Shell Koopa Troopa"
    },
    {
        "description": "A faster, winged version of Koopa Troopa",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRv_eZNRtLD7Z5u0ce2vEr73VfNmjOB80bMgA&s",
        "name": "Koopa Paratroopa"
    },
    {
        "description": "A spiked enemy that cannot be jumped on",
        "image_url": "https://pm1.aminoapps.com/6546/e6dfb2ddcd70444b5c9588d002435b01ccfe761d_hq.jpg",
        "name": "Spiny"
    },
    {
        "description": "A flying, beetle-like enemy",
        "image_url": "https://cdn.thingiverse.com/renders/ac/24/68/29/70/cc916d24355bfba4acbb766f1ce1c0a9_preview_featured.JPG",
        "name": "Buzzy Beetle"
    },
    {
        "description": "A squid-like underwater enemy",
        "image_url": "https://i.etsystatic.com/9680903/r/il/26312a/620419040/il_570xN.620419040_rwuo.jpg",
        "name": "Blooper"
    },
    {
        "description": "A fish that swims in underwater levels",
        "image_url": "https://live.staticflickr.com/76/194963886_f6818b589d.jpg",
        "name": "Red Cheep Cheep"
    },
    {
        "description": "A fish that swims in underwater levels",
        "image_url": "https://cdn3.iconfinder.com/data/icons/pixel-nes-mario-characters/105/Super_Mario_Bros_Page_31-512.png",
        "name": "Green Cheep Cheep"
    },
    {
        "description": "A rotating bar of fireballs, often found in castles",
        "image_url": "https://44.media.tumblr.com/8671968088cb6b7a7b445eadd4a4d731/tumblr_mhti0bb55b1rrftcdo1_250.gif",
        "name": "Firebar"
    },
    {
        "description": "A hammer-throwing enemy",
        "image_url": "https://cdn3.iconfinder.com/data/icons/pixel-nes-mario-characters/105/Super_Mario_Bros_Page_21-512.png",
        "name": "Hammer Bro"
    },
    {
        "description": "A green dragon-like enemy that shoots fireballs",
        "image_url": "https://pbs.twimg.com/media/F7wlqexXEAANuAk.jpg",
        "name": "Bowser"
    },
    {
        "description": "A plant that emerges from pipes",
        "image_url": "https://i.pinimg.com/236x/89/64/09/896409c127c740a8cecd586c3e0df118.jpg",
        "name": "Piranha Plant"
    },
    {
        "description": "A cannonball-like projectile shot from Bill Blasters",
        "image_url": "https://preview.redd.it/oqyi2xxu6lb31.jpg?width=640&crop=smart&auto=webp&s=017a61eb5f99226ff86d3bec85042a4435201d98",
        "name": "Bullet Bill"
    },
    {
        "description": "A cloud-riding enemy that throws Spinies",
        "image_url": "https://nintendoeverything.com/wp-content/uploads/lakitu.jpg",
        "name": "Lakitu"
    }
]


def add_enemies():
    game_query = db.session.query(Games).filter(Games.name == "Super Mario Bros.").first()
    type_query = db.session.query(Types).filter(Types.name == "Enemy Element").first()
    for index, game_element in enumerate(enemies_list):
        if not db.session.query(GameElements).filter(GameElements.name == game_element["name"]).first():

            name = game_element["name"]
            description = game_element["description"]
            image_url = game_element["image_url"]
            new_game_element = GameElements(name, description, None, None, image_url)
            new_game_element.game_id = game_query.game_id
            new_game_element.type_id = type_query.type_id

            db.session.add(new_game_element)
            
    db.session.commit()

