import json
import re

def convert_to_valid_json(input_str):
    # Function to add quotes around the DataTypes and keys
    def wrap_data_type(match):
        value = match.group(0)
        if value not in ["true", "false", "null"]:
            return f'"{value}"'
        return value

    # Use a regular expression to match keys (id, username, etc.) and wrap them with quotes
    input_str = re.sub(r'(\b\w+\b)(?=:)', r'"\1"', input_str)

    # Use a regular expression to match DataTypes and wrap them with quotes
    input_str = re.sub(r'\b(DataTypes\.\w+)\b', wrap_data_type, input_str)

    # Remove any trailing commas
    input_str = re.sub(r',\s*}', '}', input_str)
    input_str = re.sub(r',\s*\]', ']', input_str)

    # Replace single quotes with double quotes for JSON compatibility
    input_str = input_str.replace("'", '"')

    return input_str

def get_data_from_files(initDB_path, model_paths):
    
    db_connections = []
    with open(initDB_path, "r", encoding="utf-8") as file:
        content = file.read()
        pattern = re.compile(r"(\w+)\.(\w+)\((\w+),\s*\{([^}]*)\}\);")

        matches = pattern.findall(content)

        for match in matches:
            model, association, related_model, options = match
            db_connections.append({
                "model": model,
                "association": association,
                "related_model": related_model,
                "options": options.strip()
            })

    models = []
    for path in model_paths:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()

        pattern = re.search(r"sequelize\.define\(\s*['\"]([^'\"]+)['\"]\s*,\s*({[\s\S]*?})\s*,\s*({[\s\S]*?})?\s*\);", content)

        if not pattern:
            print(f"Error file: {path}")
            print("No match found\n")
            continue  # No match found
        table_name = pattern.group(1)  # Extract table name
        attributes_str = pattern.group(2)  # Extract attributes object
        valid_json = convert_to_valid_json(attributes_str)
        
        try:
            jsonA = json.loads(valid_json)  # Convert attributes object to JSON
            models.append({
                "table_name": table_name,
                "attributes": jsonA
            })
        except json.JSONDecodeError as e:
            print(f"Error file: {path}")
            print(f"Error JSON: {valid_json}")
            print(f"Error decoding JSON: {e}")
        
    return db_connections, models

