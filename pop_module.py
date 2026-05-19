class Phone:
    def __init__(self, name, model, price, for_sale):
        self.name = name
        self.model = model
        self.price = price
        self.for_sale = for_sale

    def sell(self):
        print(f"You sold the phone: {self.name} {self.model} for ${self.price} ")
    def buy(self):
        print(f"You bought the phone: {self.name} {self.model} for ${self.price} ")
    def describe(self):
        print(f"{self.name} {self.model} is sold for ${self.price} ")