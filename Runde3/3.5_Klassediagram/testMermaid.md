classDiagram
    class CoffeeShop {
        <<fa:fa-coffee>>
        +string name
        +sellCoffee() void
    }

    class Customer {
        <<fa:fa-user>>
        +string name
        +buyCoffee(CoffeeShop shop) void
    }

    Customer --> CoffeeShop : buys from
