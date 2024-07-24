deco = {'water':'ml', 'milk':'ml','coffee':'g', 'money':'$'}


def make_report(resource:dict, profit:int) -> None:
    print("The remaining resources are as follows.")
    for key, item in resource.items():
        print(f"{key.title()}: {item}{deco[key]}")
    print(f"Money: ${profit}")