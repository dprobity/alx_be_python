user_response = input("What's the weather like today? (sunny/rainy/cold):")

if user_response.lower() == "sunny":
    print(" Wear a t-shirt and sunglasses")
elif user_response.lower() == "rainy":
    print("Dont forget your umbrella and a raincoat ")
elif user_response.lower() == "cold":
    print("Make sure to wear a warm coat and a scarf ")
else:
    print("Sorry, I dont have recommendations for")