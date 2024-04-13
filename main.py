class SymbolTable:
    def __init__(self):
        self.table = {}

    def add_variable(self, name, value, type):
        if name in self.table:
            raise Exception(f"Variable '{name}' already declared.")
        self.table[name] = {"value": value, "type": type}

    def get_variable(self, name):
        variable = self.table.get(name)
        if variable is None:
            raise Exception(f"Variable '{name}' is not defined.")
        return variable

    def set_variable(self, name, value):
        if name not in self.table:
            raise Exception(f"Variable '{name}' is not defined.")
        # Allow type reassignment
        self.table[name]["value"] = value
        self.table[name]["type"] = type(value).__name__  # Update the type information

    def print_state(self):
        for name, details in self.table.items():
            print(f"{name}: ({details['type']}): {details['value']}")

def proc_statements(statements, symbol_table):
    for statement in statements:
        if "=" in statement:
            var_name, _, value_part = statement.partition("=")
            var_name = var_name.strip()
            try:
                value = eval(value_part.strip())  # Evaluate the expression
            except NameError as e:
                print(f"Error evaluating value: {e}")
                continue
            if var_name in symbol_table.table:
                symbol_table.set_variable(var_name, value)
            else:
                symbol_table.add_variable(var_name, value, type(value).__name__)
        else:
            print(f"Invalid statement '{statement}'")

def main():
    symbol_table = SymbolTable()
    statements = [
        "x = 23",
        "y = 'Hello Prof.Nelson'",
        "z = 'Hello World'",
        "x = 22"
    ]
    print("Initial State: ")
    proc_statements(statements, symbol_table)
    symbol_table.print_state()

    print("\nFinal State: ")
    update_statements = [
        "x = 15",
        "z = 22.04"
    ]
    proc_statements(update_statements, symbol_table)
    symbol_table.print_state()

if __name__ == "__main__":
    main()









