# https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/
# https://youtu.be/pTB30aXS77U
"""Here is an example of class to make an order and pay it.
"""
class Order:
    def __init__(self):
        self.items = []
        self.price = []
        self.quantity = []
        self.status = "open"
    
    def add_item(self, name, price, quantity):
        self.items.append(name)
        self.price.append(price)
        self.quantity.append(quantity)
    
    def total_price(self):
        if len(self.items)==0:
            return 0
        total = 0
        for i in range(len(self.price)):
            total += self.price[i]*self.quantity[i]
        return total
    
    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())
order.pay("debit", "0372846")

"""
The SOLID Principles are five principles of Object-Oriented class design. 
They are a set of rules and best practices to follow while designing a class structure.

    - S: The Single Responsibility Principle
    - O: The Open-Closed Principle
    - L: The Liskov Substitution Principle
    - I: The Interface Segregation Principle
    - D: The Dependency Inversion Principle
"""
####################################################################################################
"""
S: The Single Responsibility Principle: The Single Responsibility Principle states that a 
class should do one thing and therefore it should have only a single reason to change.
In the example above, the order class three methods: add_item, total_price, and pay.
But to handle the payment, we don't need to add the pay method to the order class.
We can create a new class called PaymentProcessor to handle the payment.
Follow the code example below.
"""
class Order:
    def __init__(self):
        self.items = []
        self.price = []
        self.quantity = []
        self.status = "open"
    
    def add_item(self, name, price, quantity):
        self.items.append(name)
        self.price.append(price)
        self.quantity.append(quantity)
    
    def total_price(self):
        if len(self.items)==0:
            return 0
        total = 0
        for i in range(len(self.price)):
            total += self.price[i]*self.quantity[i]
        return total

class PaymentProcessor:
    def paywithdebit(self, order ,security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
    
    def paywithcredit(self, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
       
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())
paid = PaymentProcessor()
paid.paywithdebit(order,"0372846")

####################################################################################################
"""
O: The Open-Closed Principle: The Open-Closed Principle states that a class should be open for
extension but closed for modification. In the example above, the order class has three methods:
add_item, total_price, and pay. If we want to add a new payment method, we need to modify the
PaymentProcessor class. To avoid this, we can create a new class called PaymentProcessor to handle the payment. 
"""
from abc import ABC, abstractmethod # https://youtu.be/UDmJGvM-OUw
class Order:
    def __init__(self):
        self.items = []
        self.price = []
        self.quantity = []
        self.status = "open"
    
    def add_item(self, name, price, quantity):
        self.items.append(name)
        self.price.append(price)
        self.quantity.append(quantity)
    
    def total_price(self):
        if len(self.items)==0:
            return 0
        total = 0
        for i in range(len(self.price)):
            total += self.price[i]*self.quantity[i]
        return total

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order, security_code):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order ,security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):   
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):   
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())
paid = DebitPaymentProcessor()
paid.pay(order,"0372846")

####################################################################################################
"""
L: The Liskov Substitution Principle: The Liskov Substitution Principle states that a subclass
should be able to substitute its parent class without the consumer knowing it. In the example above,
the DebitPaymentProcessor, CreditPaymentProcessor, and PaypalPaymentProcessor classes are all
subclasses of the PaymentProcessor class. The consumer of the PaymentProcessor class can use any of
the subclasses without knowing it. For example, the PaymentProcessor class can be used to pay with email 
address not a security code. But we are passing a security code to the paypalpaymentprocessor class. So,
we are violating the Liskov Substitution Principle. To fix this, we can remove the security_code parameter and 
use it as initilizer. Follow the code example below.
"""
class Order:
    def __init__(self):
        self.items = []
        self.price = []
        self.quantity = []
        self.status = "open"
    
    def add_item(self, name, price, quantity):
        self.items.append(name)
        self.price.append(price)
        self.quantity.append(quantity)
    
    def total_price(self):
        if len(self.items)==0:
            return 0
        total = 0
        for i in range(len(self.price)):
            total += self.price[i]*self.quantity[i]
        return total

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):   
    def __init__(self, security_code):
        self.security_code = security_code
    
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):   
    def __init__(self, email_address):
        self.email_address = email_address
    
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.email_address}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())
paid = DebitPaymentProcessor("0372846")
paid.pay(order)

####################################################################################################
"""
I: The Interface Segregation Principle: The Interface Segregation Principle states that a client
should not be forced to implement an interface that it doesn't use. For example, lets say we have a 
sms_authenticator method in the PaymentProcessor class. But we don't want to use it in the DebitPaymentProcessor
class. So, we are violating the Interface Segregation Principle. To fix this, we can create a new class called
Authenticator and inherit it in the PaymentProcessor class. Follow the code example below.
"""
class Order:
    def __init__(self):
        self.items = []
        self.price = []
        self.quantity = []
        self.status = "open"
    
    def add_item(self, name, price, quantity):
        self.items.append(name)
        self.price.append(price)
        self.quantity.append(quantity)
    
    def total_price(self):
        if len(self.items)==0:
            return 0
        total = 0
        for i in range(len(self.price)):
            total += self.price[i]*self.quantity[i]
        return total

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass
class PaymentProcessorSMS(PaymentProcessor):
    
    @abstractmethod
    def sms_authenticator(self):
        pass

class DebitPaymentProcessor(PaymentProcessorSMS):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def sms_authenticator(self):
        print(f"Verifying security code via SMS{code}")
        self.verified = True

    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"
    
class CreditPaymentProcessor(PaymentProcessor):   
    def __init__(self, security_code):
        self.security_code = security_code
    
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessorSMS):   
    def __init__(self, email_address):
        self.email_address = email_address
    
    def sms_authenticator(self):
        print(f"Verifying security code via SMS{code}")
        self.verified = True

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.email_address}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())
paid = CreditPaymentProcessor("0372846")
paid.pay(order)

##### COMPOSITION #####
class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class SMSAuthorizer:

    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f"Verifying SMS code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code, authorizer: SMSAuthorizer):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address, authorizer: SMSAuthorizer):
        self.email_address = email_address
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
authorizer = SMSAuthorizer()
processor = PaypalPaymentProcessor("hi@arjancodes.com", authorizer)


####################################################################################################
"""
D: The Dependency Inversion Principle: The Dependency Inversion Principle states that high level modules
should not depend on low level modules. Both should depend on abstractions. Abstractions should not depend
on details. Details should depend on abstractions.
"""
class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

class Authorizer(ABC):
    
    @abstractmethod
    def is_authorized(self) -> bool:
        pass

class SMSAuthorizer(Authorizer):

    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f"Verifying SMS code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class NotARobot(Authorizer):
    def __init__(self):
        self.authorized = False

    def not_a_robot(self):
        print("I am not a robot")
        self.authorized = True
    
    def is_authorized(self) -> bool:
        return self.authorized

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code, authorizer: Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address, authorizer: Authorizer):
        self.email_address = email_address
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
authorizer = NotARobot()
authorizer.not_a_robot()
processor = PaypalPaymentProcessor("hi@arjancodes.com", authorizer)
processor.pay(order)

####################################################################################################
