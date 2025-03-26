:::mermaid
classDiagram
    class Person {
        +string name
        -int age
        +greet() string
    }
    class Employee {
        +int employee_id
        +string position
        +work() void
    }
    Person <|-- Employee
