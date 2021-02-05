from dotenv import load_dotenv, find_dotenv, set_key, unset_key, dotenv_values

env_path = find_dotenv()
load_dotenv(env_path)

def set_variable(env_name, value):
    set_key(env_path, f"export {env_name.upper()}", str(value))
    print(f"Environment Variable set\n{env_name.upper()}={str(value)}\n at {env_path}")


while True:
    option = input("\n[1] Change environment config (Prod, Dev) or \n[2] Add custom environment varibale\n")
    if option == str(1):
        while True:
            value = input(f"\nWhat config to select?\n[1] Development\n[2] Production\n")
            print(dotenv_values())
            if value == str(1):
                unset_key(env_path, f"APP_SETTINGS")
                set_variable("APP_SETTINGS", "config.DevelopmentConfig")
                break
            elif value == str(2):
                unset_key(env_path, f"APP_SETTINGS")
                set_variable("APP_SETTINGS", "config.ProductionConfig")
                break
            else:
                print("Invalid choice, try 1 or 2")
        break
    elif option == str(2):
        env_name = input("What is the name of your environment variable?\n")
        value = input(f"\nWhat is the value to set for {env_name}\n")
        unset_key(env_path, env_name)
        set_variable(env_name, value)
        break
    else:
        print("Invalid choice, try 1 or 2")
