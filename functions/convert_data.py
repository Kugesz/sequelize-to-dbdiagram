def get_attributes_string(attributes):

  string = ""

  for key, value in attributes.items():
    match(key):
      case "primaryKey":
        if value:
          string += "primary key, "
      case "autoIncrement":
        if value:
          string += "increment, "
      case "allowNull":
        string += "" if value else "not null, "
      case "defaultValue":
        string += f'default: {value}, '
      case "unique":
        if value:
              string += "unique, "

  return f'[{string[:-2]}]' if len(string) != 0 else ""

def convert_data(connection, table_data):
  string = []
  for table in table_data:
    table_string = f'Table {table['table_name']} ' + "{"

    for key, value in table['attributes'].items():
      attributes = get_attributes_string(value)

      row = f'\n\t {key} {value['type'].replace("DataTypes.", "")} {attributes}'
      table_string += row
    string.append(table_string + "\n}\n\n")
  return string