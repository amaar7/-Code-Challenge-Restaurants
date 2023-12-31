from customer import Customer
from restaurant import Restaurant
from review import Review


# Create an  instances
customer1 = Customer("John", "Doe")
customer2 = Customer("Alice", "Smith")

restaurant1 = Restaurant("Tasty Treats")
restaurant2 = Restaurant("Burger Palace")

review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant2, 5)

# Test methods
print(customer1.full_name())  # Output should be: John Doe
print(restaurant2.average_star_rating())  # Output should be: 5.0
print(customer2.num_reviews())  # Output should be: 1

