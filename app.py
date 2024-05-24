from flask import Flask, jsonify
from random import randint


app = Flask(__name__)


@app.route("/")
def index():
    return "OK"


@app.route("/about")
def about():
    return "about"


@app.route("/datos")
def datos():
    datos = [
              {
                "_id": "665104884efb1bc60d57aba9",
                "index": 0,
                "guid": "db34fd54-ad95-4c4a-b2fa-f2edbf44c696",
                "isActive": False,
                "balance": "$2,763.78",
                "picture": "http://placehold.it/32x32",
                "age": 36,
                "eyeColor": "green",
                "name": "Lucille Crane",
                "gender": "female",
                "company": "POLARIUM",
                "email": "lucillecrane@polarium.com",
                "phone": "+1 (926) 468-3891",
                "address": "287 Christopher Avenue, Hayden, Florida, 1379",
                "about": "Reprehenderit adipisicing culpa consectetur ea sit laboris minim. Ullamco tempor proident occaecat sit amet voluptate minim. Dolore ipsum irure ea ea adipisicing incididunt ex tempor ipsum consectetur laborum laborum. Ipsum laboris eu proident occaecat elit qui. Ullamco elit pariatur enim consequat qui adipisicing officia laborum ipsum ad.\r\n",
                "registered": "2020-10-14T10:25:49 +05:00",
                "latitude": -33.434874,
                "longitude": 120.174385,
                "tags": [
                  "velit",
                  "officia",
                  "id",
                  "id",
                  "sit",
                  "dolore",
                  "non"
                ],
                "friends": [
                  {
                    "id": 0,
                    "name": "Alberta Stephens"
                  },
                  {
                    "id": 1,
                    "name": "Cherry Hutchinson"
                  },
                  {
                    "id": 2,
                    "name": "Gwendolyn Horton"
                  }
                ],
                "greeting": "Hello, Lucille Crane! You have 9 unread messages.",
                "favoriteFruit": "banana"
              },
              {
                "_id": "6651048881003c8be1651686",
                "index": 1,
                "guid": "a98b5e68-6fa7-4ac3-b06a-180bccc407c5",
                "isActive": True,
                "balance": "$1,260.29",
                "picture": "http://placehold.it/32x32",
                "age": 40,
                "eyeColor": "green",
                "name": "Whitehead West",
                "gender": "male",
                "company": "ULTRIMAX",
                "email": "whiteheadwest@ultrimax.com",
                "phone": "+1 (947) 419-3395",
                "address": "932 Crawford Avenue, Newkirk, South Dakota, 2912",
                "about": "Ullamco non esse elit do nisi ea irure quis aliqua commodo. Pariatur enim fugiat labore aliquip quis enim duis. Incididunt esse do voluptate proident velit consequat labore proident minim et aliqua. Reprehenderit aute anim ut quis nulla anim aliqua adipisicing est. Ut est aute dolore nulla adipisicing eiusmod et sunt ut aute. Occaecat consectetur sit consectetur cillum enim eu nulla do.\r\n",
                "registered": "2016-12-07T09:10:09 +05:00",
                "latitude": 26.116751,
                "longitude": 59.020883,
                "tags": [
                  "fugiat",
                  "commodo",
                  "qui",
                  "cillum",
                  "consequat",
                  "culpa",
                  "duis"
                ],
                "friends": [
                  {
                    "id": 0,
                    "name": "Cooley Hartman"
                  },
                  {
                    "id": 1,
                    "name": "Steele Torres"
                  },
                  {
                    "id": 2,
                    "name": "Dudley Finch"
                  }
                ],
                "greeting": "Hello, Whitehead West! You have 7 unread messages.",
                "favoriteFruit": "apple"
              },
              {
                "_id": "665104883ced65e08a75c0fc",
                "index": 2,
                "guid": "325ed16d-24dc-41d0-9c3a-14c130e80cba",
                "isActive": False,
                "balance": "$3,566.70",
                "picture": "http://placehold.it/32x32",
                "age": 22,
                "eyeColor": "brown",
                "name": "Michele Farmer",
                "gender": "female",
                "company": "CANOPOLY",
                "email": "michelefarmer@canopoly.com",
                "phone": "+1 (881) 584-2201",
                "address": "392 Rapelye Street, Brandywine, Nevada, 5437",
                "about": "Consectetur ex et commodo velit irure dolore cupidatat. Esse sunt minim sint aute exercitation aliqua exercitation veniam officia. Duis laboris ut consequat incididunt dolor adipisicing ea amet aliqua do. Labore nostrud consectetur non esse consectetur duis occaecat mollit cillum aliquip enim ipsum fugiat.\r\n",
                "registered": "2014-10-02T11:35:35 +05:00",
                "latitude": -38.622821,
                "longitude": 139.252255,
                "tags": [
                  "qui",
                  "sint",
                  "nisi",
                  "minim",
                  "mollit",
                  "est",
                  "et"
                ],
                "friends": [
                  {
                    "id": 0,
                    "name": "Holland Ramos"
                  },
                  {
                    "id": 1,
                    "name": "Pauline Cash"
                  },
                  {
                    "id": 2,
                    "name": "Rasmussen Butler"
                  }
                ],
                "greeting": "Hello, Michele Farmer! You have 5 unread messages.",
                "favoriteFruit": "apple"
              },
              {
                "_id": "665104887aa9583924a33dce",
                "index": 3,
                "guid": "a869b03b-3737-4357-8dcd-e206c3651fb0",
                "isActive": True,
                "balance": "$1,677.86",
                "picture": "http://placehold.it/32x32",
                "age": 37,
                "eyeColor": "blue",
                "name": "Jewel Lara",
                "gender": "female",
                "company": "PROSELY",
                "email": "jewellara@prosely.com",
                "phone": "+1 (814) 547-3432",
                "address": "882 Nostrand Avenue, Munjor, Iowa, 8514",
                "about": "Aliquip non ad non culpa eiusmod commodo qui Lorem et. Sunt sunt irure laborum enim nulla pariatur officia ea. Labore veniam minim irure incididunt eu cupidatat proident officia tempor elit minim ea. Lorem exercitation sit minim excepteur nostrud adipisicing mollit id ea quis eu est. Ipsum consequat fugiat deserunt qui culpa. Elit consectetur enim adipisicing exercitation reprehenderit laborum laboris. Eu ad laboris labore nostrud ea consequat laborum do velit qui id sit labore.\r\n",
                "registered": "2020-04-02T06:57:21 +05:00",
                "latitude": 54.00754,
                "longitude": 3.026297,
                "tags": [
                  "magna",
                  "voluptate",
                  "cupidatat",
                  "pariatur",
                  "culpa",
                  "aute",
                  "proident"
                ],
                "friends": [
                  {
                    "id": 0,
                    "name": "Alvarado Benson"
                  },
                  {
                    "id": 1,
                    "name": "Earnestine Alexander"
                  },
                  {
                    "id": 2,
                    "name": "Guerra Watts"
                  }
                ],
                "greeting": "Hello, Jewel Lara! You have 7 unread messages.",
                "favoriteFruit": "banana"
              },
              {
                "_id": "6651048836dd414e7066b397",
                "index": 4,
                "guid": "d68d1a12-e650-4bc1-8d1e-0dd2718a6a3f",
                "isActive": False,
                "balance": "$3,032.12",
                "picture": "http://placehold.it/32x32",
                "age": 39,
                "eyeColor": "brown",
                "name": "Charlene Love",
                "gender": "female",
                "company": "PYRAMI",
                "email": "charlenelove@pyrami.com",
                "phone": "+1 (959) 440-3459",
                "address": "441 Utica Avenue, Biddle, Wyoming, 4982",
                "about": "Sit dolor exercitation irure ut aute occaecat ex incididunt cupidatat dolore esse. Velit ex consequat adipisicing amet in proident sit proident adipisicing. Fugiat anim occaecat aliqua ea incididunt voluptate.\r\n",
                "registered": "2024-03-15T12:19:22 +05:00",
                "latitude": 31.96686,
                "longitude": -96.266996,
                "tags": [
                  "aliqua",
                  "et",
                  "exercitation",
                  "irure",
                  "excepteur",
                  "nostrud",
                  "veniam"
                ],
                "friends": [
                  {
                    "id": 0,
                    "name": "Tamra Huber"
                  },
                  {
                    "id": 1,
                    "name": "Imogene Walsh"
                  },
                  {
                    "id": 2,
                    "name": "Sellers Hart"
                  }
                ],
                "greeting": "Hello, Charlene Love! You have 6 unread messages.",
                "favoriteFruit": "apple"
              }
            ]

    return jsonify(datos, 200, 4)


if __name__ == "__main__":
    app.run()
