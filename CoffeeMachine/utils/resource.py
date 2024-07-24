def resource_suff(choice_ingre:dict, resources:dict) -> bool:
    for key, item in choice_ingre.items():
        if item > resources[key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True

def modify_resource(machine_resources:dict, choice_ingre:dict) -> dict:
    for key in choice_ingre:
        machine_resources[key] -= choice_ingre[key]
    return machine_resources
    