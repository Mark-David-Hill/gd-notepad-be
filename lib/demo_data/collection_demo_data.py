from db import db

from models.collections import Collections
from models.users import Users

collections_list = [
    {
        "name": "Super Mario Bros.",
        "description": "A classic platformer where Mario embarks on a quest to rescue Princess Peach from Bowser.",
        "image_url": "https://i.ebayimg.com/images/g/eV8AAOSweOhh5i-k/s-l1200.jpg"
    },
    {
        "name": "Watership Down",
        "description": "A book by Richard Adams published in 1972",
        "image_url": "https://cdn.penguin.co.uk/dam-assets/books/9780241953235/9780241953235-jacket-large.jpg"
    },
    {
        "name": "Chinese Characters",
        "description": "Component parts of the Chinese writing system, also used to a lesser extent in Japanese and Korean",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Hanzi.svg/800px-Hanzi.svg.png"
    },
    {
        "name": "Programming Technologies",
        "description": "Languages and other technologies used in programming",
        "image_url": "https://dnycf48t040dh.cloudfront.net/top-10-programming-languages-in-2023.jpg"
    },
    {
        "name": "Mega Man Classic Series",
        "description": "A series of action platformers",
        "image_url": "https://i.ytimg.com/vi/9P2fVmh-hV4/maxresdefault.jpg"
    },
    
    
]

def add_collections():
    user_query = db.session.query(Users).filter(Users.email == "super@test.com").first()

    for index, collection in enumerate(collections_list):
        if not db.session.query(Collections).filter(Collections.name == collection["name"]).first():

            name = collection["name"]
            description = collection["description"]
            image_url = collection["image_url"]
            new_collection = Collections(name, description, image_url, False)

            new_collection.owner_id = user_query.user_id

            db.session.add(new_collection)
            
    db.session.commit()

