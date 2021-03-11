# E-commerce
A simple E-commerce api

To access the site on your machine after cloning it you need to set up a virtual enviroment and installing django and django rest frame work and then you're good to go

If you accessed the site on your local host you'll find that the api is browesable so you'll be able to understand the functionality of the api. But any way here is a documentation of the entire api 

## Product List and Create

accessing localhost/products will give you a list of all the products currently registered on the site the list will look like 

```json
   [
      {
         "url": "local/host/products/1",
          "id": 1,
         "title": "any title",
         "description": "some description",
         "image": "url for the image",
         "price": 300,
         "quantity": 150,
         "seller": "some-user",
         "date": "2021-03-08T01:19:02.148399Z"
      },
    ]
```
    
you can also submit a post request to the same url given that you are logged in. instead of sending the username and password you can send a token that is generated automatically for you once you've registered
    
 You can Register at this url localhost/account/register you will need to send a post request containing the user name and password. Note that you will send the password 1 time so make sure that you validate the password on the client side
    
after registration you will request your token via this endpoint localhost/api-token-auth/ you'll need to send a post request with username and password and you'll recieve a json response like this 
    
 ```json
    {
      "token" : "dcasdvckjnojqnen3jn34no4o3ne3jkon43jon"
    }
 ```
    
 ## Product Retrieve Update and DELETE
    
 after acquiring your token you can also send a GET request to this url localhost/products/<int:productID> you will get a detailed page of the product with JSON like this
 
 
  ```json  
   {
      "url": "localhost/products/1/",
      "id": 1,
      "title": "some title",
      "description": "some description",
      "image": "some image url",
      "price": 34,
      "quantity": 3,
      "seller": "some-user",
      "date": "2021-03-08T01:19:02.148399Z"
   }
 ```

if the you're not authenticated you'll be able to view the details via a GET request only, but if you're authenticated and you're the one who created the product you'lle be able to send a PUT request or a DELETE request


## Order List and create

you can send a GET request to this url localhost/orders/ only if you're authenticated and it will return to you a JSON response of all the orders this user had orderd like this
```json
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
```


You can also send a POST request to the same url to make a new Order given that you're authenticated


## Order Detail 

You can send a a GET request to this url localhost/orders/<int:pk> and it will return to you a JSON response of the details of the order only if you're authenticated and you're the one who created the order the JSON response will look like this

```json
   {
       "url": "localhost/orders/6/",
       "user": "mohamed",
       "quantity": 3,
       "payment_options": 1,
       "Delivery": "sccsc",
       "item": "localhost/products/1/"
   }
```
   
You can also send a PUT and DELETE requests to the same url 


## Cart list and create

you can send a GET request to this url localhost/cart and it will return to you a JSON response of all the products that user has in his cart, like this

```json
   [
       {
           "url": "localhost/cart/1",
           "user": "mohamed",
           "items": [
               "localhost/products/1/",
               "localhost/products/3/"
           ]
       }
   ]
```

You can also send a POST request to the same url to create a new cart


## Cart update and delete

Going to this url  "localhost/cart/1" will allow you to make a PUT or DELETE requets on the cart given that you're the one who crated the cart


## Order State buyer List:


making a GET request to this url localhost/states/buyer wiil give you a list of the the states of all the orders that this user is buying, the JSON will look like this
```json
   [
       {
           "url": "localhost/states/1/",
           "order": "7aga",
           "owner": "mohamed",
           "buyer": "moh",
           "state": "(anywhere between 1: being packaged , 2:on the way , 3:delivered)"
       }
   ]
```
   
you can't make a POST request to this url, the order state is made for you automatically when you make a new order 


## Order state owner list 

making a GET request to this url localhost/state/owner will give you a list of the states of all the orders this user is selling. The JSON will look like this
```json
   [
       {
           "url": "localhost/states/1/",
           "order": "7aga",
           "owner": "mohamed",
           "buyer": "mohamed",
           "state": 2
       },
   ]
```

## updating or deleting the state of an order

Making a PUT request to this url localhost/states/<int:pk> will make you alter the state and only the state of the order if you're the seller of this item
you can also send a DELETE request and a GET request to the same url which will return to you a JSON response like this

```json
   {
       "url": "url/states/1/",
       "order": "7aga",
       "owner": "mohamed",
       "buyer": "moh",
       "state": 2
   }
```



