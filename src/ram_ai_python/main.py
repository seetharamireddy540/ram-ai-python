"""Main module."""
from ram_ai_python.module1.util import say_module_name as say_module_name1
from ram_ai_python.module2.util import say_module_name as say_module_name2


def main():
    """Entry point."""
    print("Hello, World!")
    say_module_name2()
    say_module_name1()


if __name__ == "__main__":
    main()