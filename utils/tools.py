from langchain_core.tools import tool

@tool
def addition(a: int, b: int) -> int:
    """
    This tool adds two numbers.
    :param a:
    :param b:
    :return: the sum of the two numbers
    """
    print("In tool")
    return a + b

tools = [addition]