# E-commerce
A simple E-commerce api

To access the site on your machine after cloning it you need to set up a virtual enviroment and installing django and django rest frame work and then you're good to go

If you accessed the site on your local host you'll find that the api is browesable so you'll be able to understand the functionality of the api. But any way here is a documentation of the entire api 

-Product List and Create
accessing localhost/products will give you a list of all the products currently registered on the site the list will look like [
   [
   {
        "url": "http://127.0.0.1:8000/products/1/",
        "id": 1,
        "title": "any title",
        "description": "some description",
        "image": url for the image,
        "price": 300,
        "quantity": 150,
        "seller": "some-user",
        "date": "2021-03-08T01:19:02.148399Z"
    },
    ]
    
    you can also submit a post request to the same url given that you are logged in. instead of sending the username and password you can send a token that is generated automatically for you once you've registered
    
    You can Register at this url localhost/account/register you will need to send a post request containing the user name and password. Note that you will send the password 1 time so make sure that you validate the password on the client side
    
    after registration you will request your token via this endpoint localhost/api-token-auth/ you'll need to send a post request with username and password and you'll recieve a json response like this 
    {
      "token" : "dcasdvckjnojqnen3jn34no4o3ne3jkon43jon"
    }
    
 - Product Retrieve Update and DELETE
    
    after acquiring your token you can also send a GET request to this url localhost/products/<int:productID> you will get a detailed page of the product with JSON like this
    
{
    "url": "localhost/products/1/",
    "id": 1,
    "title": "some title",
    "description": "some description",
    "image": some image url,
    "price": 34,
    "quantity": 3,
    "seller": "some-user",
    "date": "2021-03-08T01:19:02.148399Z"
}

if the you're not authenticated you'll be able to view the details via a GET request only, but if you're authenticated and you're the one who created the product you'lle be able to send a PUT request or a DELETE request


-Order List and create

you can send a GET request to this url localhost/orders/ only if you're authenticated and it will return to you a JSON response of all the orders this user had orderd like this
[
    {
        "url": "the url to take you to the details of the order",
        "user": "name of the user who made the order",
        "quantity": 3,
        "payment_options": "one of three options 1: credit card 2:cash 3: paypal",
        "Delivery": " Where to be delivered",
        "item": "the url for the product detail"
    },
]

You can also send a POST request to the same url to make a new Order




