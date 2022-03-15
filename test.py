import requests
import json
import getopt, sys

base_url = "https://jsonplaceholder.typicode.com/"


def get_resource(resource_name="users"):  #gave a default value
    response = requests.get(base_url + resource_name)
    data = json.loads(response.text)
    with open(f'{resource_name}.txt', 'a') as f:
        f.write("        Business Sensitive\n\n")
        if resource_name == "users":
            for item in data:
                line = "name " + "- " + item.get("name") + "\n"
                f.write(line)
                line = "Phone " + "- " + item.get("phone") + "\n"
                f.write(line)
                line = "Address " + "- " + str(item.get("address")) + "\n\n"
                f.write(line)

        if resource_name == "comments":
            for item in data:
                line = "Name " + "- " + item.get("name") + "\n"
                f.write(line)
                line = "Email " + "- " + item.get("email") + "\n"
                f.write(line)
                word = str(item.get("body"))
                word = word.replace("\n","\\n")
                line = "Body " + "- " + word + "\n\n"
                f.write(line)
        if resource_name in ["albums", "todos"]:
            for item in data:
                line = "Title " + "- " + item.get("title") + "\n"
                f.write(line)

        if resource_name == "photos":
            for item in data:
                line = "Title " + "- " + item.get("title") + "\n"
                f.write(line)
                line = "Url " + "- " + item.get("url") + "\n\n"
                f.write(line)
    print(f"{resource_name}.txt file has been created.")


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) <= 0:
        print("Arguments not passed. Exiting ....")
        sys.exit()
    elif args[0] not in ["users", "albums", "todos", "photos", "comments"]:
        print("incorrect argument. Exiting ....")
        sys.exit()
    else:
        get_resource(args[0])
