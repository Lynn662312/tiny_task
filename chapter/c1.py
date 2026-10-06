def add_role(roles: list[str], role: str) -> None:
    """
    Add a role to the list of roles if it doesn't already exist.

    Args:
        roles (List[str]): The current list of roles.
        role (str): The role to be added.
    """
    roles.append(role)

roles = ["user"]
add_role(roles, "admin")
print(roles)

def replace(roles: list[str], new_role: str, role: str) -> None:
    """
    Replace the first role in the list with a new role.

    Args:
        roles (List[str]): The current list of roles.
        new_role (str): The new role to replace with.
        role (str): The role to be replaced.
    """
    if role in roles:
        index = roles.index(role)
        roles[index] = new_role
    else:
        return "Role not found in the list."

replace(roles, "superuser", "admin")
print(roles)
add_role(roles, "guest")
print(roles)

role1 = input("Enter the new role: ")
add_role(roles, role1)
print(roles)
print("\n")
replace1 = input("enter the roles to be replaced: ")
replace2 = input("enter the new role: ")
replace(roles, replace2, replace1)
print(roles)
