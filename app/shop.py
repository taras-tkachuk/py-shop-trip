import datetime

from app.customer import Customer


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_product_price(self, customer: Customer) -> float:
        full_price = 0
        for product, amount in customer.product_cart.items():
            full_price += self.products[product] * amount
        return full_price

    def print_receipt(self, customer: Customer) -> None:
        now = datetime.datetime.now()
        print(f"Date: {now.strftime("%d/%m/%Y %H:%M:%S")}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product, amount in customer.product_cart.items():
            price = self.products[product] * amount
            print(
                f"{amount} {product}s for "
                f"{int(price) if price == int(price) else price} dollars"
            )
        print(f"Total cost is "
              f"{self.calculate_product_price(customer)} dollars\n"
              f"See you again!\n")
