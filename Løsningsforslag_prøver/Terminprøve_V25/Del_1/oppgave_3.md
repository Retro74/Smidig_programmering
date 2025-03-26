:::mermaid
classDiagram
    class Character {
        -name: str
        -level: int
        -inventory: Inventory
        -weaponInventory: WeaponInventory
        +attack(): None
        +defend(): None
    }

    class Inventory {
        -items: list
        +addItem(item: str): None
        +removeItem(item: str): None
    }

    class WeaponInventory {
        -weapons: list
        +addWeapon(weapon: str): None
        +removeWeapon(weapon: str): None
        +getWeaponList(): list
    }

    Character *-- Inventory : har
    Character *-- WeaponInventory : har
