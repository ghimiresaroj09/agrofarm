from product.models import Product
from user.models import Profile

class Cart():
    def __init__(self, request):
        self.session = request.session
        #Get request
        self.request = request
        # Get the cart from the session, if it exists
        cart = request.session.get('cart')
        # If the cart does not exist, create an empty cart
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

   
    
    def db_add(self, product, quantity):
        product_id = str(product)
        # Check if product already exists in the cart
        if product_id in self.cart:
            self.cart[product_id] += quantity  # Increase quantity
        else:
            self.cart[product_id] = quantity  # Add new product
        self.session.modified = True

		# Deal with logged in user
        if self.request.user.is_authenticated:
			# Get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
            current_user.update(old_cart=str(carty))




    def add(self, product, quantity):
        product_id = str(product.id)
        # Check if product already exists in the cart
        if product_id in self.cart:
            self.cart[product_id] += quantity  # Increase quantity
        else:
            self.cart[product_id] = quantity  # Add new product
        self.session.modified = True

        #Deal with loged in user
        if self.request.user.is_authenticated:
            #Get the current user profile
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            # Convert {'3':1, '2':4} to {"3":1, "2":4}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
            current_user.update(old_cart=str(carty))



    def __len__(self):
        return sum(self.cart.values())  # Sum up all quantities



    def get_product(self):
        # Get product IDs from the cart
        product_ids = self.cart.keys()
        # Lookup products in the database
        products = Product.objects.filter(id__in=product_ids)
        return products



    def get_quantity(self):
        # Return quantities of products in the cart
        return self.cart



    def update(self, product_id, quantity):
        product_id = str(product_id)  # Convert product_id to string
        product_qty = int(quantity)  # Ensure quantity is an integer

        # Update product quantity in the cart
        if product_qty > 0:
            self.cart[product_id] = product_qty
        else:
            # Remove product if quantity is zero or less
            self.delete(product_id)
        self.session.modified = True

        # Deal with logged in user
        if self.request.user.is_authenticated:
			# Get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
            current_user.update(old_cart=str(carty))



    def delete(self, product_id):
        product_id = str(product_id)
        # Remove product from the cart
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True

        # Deal with logged in user
        if self.request.user.is_authenticated:
			# Get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
            current_user.update(old_cart=str(carty))



    def cart_total(self):
        # Get product IDs
        product_ids = self.cart.keys()
        # Lookup products in the database
        products = Product.objects.filter(id__in=product_ids)
        # Calculate the total cost
        total = 0
        for product in products:
            product_id = str(product.id)
            if product_id in self.cart:
                quantity = self.cart[product_id]
                if product.is_sale:
                    total += product.sale_price * quantity
                else:
                    total += product.price * quantity
        return total
