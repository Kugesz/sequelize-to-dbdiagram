def get_attributes_string(attributes):
  print(f'Attributes: {attributes}')
  atributes = ""
  for key, value in attributes.items():
    match(key):
     case "primaryKey":
       atributes += "primary key, "
     case "autoIncrement":
       atributes += "increment, "
     case "allowNull":
       atributes += "" if value else "not null, "
       break
     case "deafultValue":
       atributes += f'default: {value}, '

    return atributes[:-2] if len(atributes) == 0 else ""

def convert_data(connection, table_data):
  string = []
  for table in table_data:
    table_string = f'Table {table['table_name']} ' + "{"

    for key, value in table['attributes'].items():
      print(f'Key: {key} Value: {value}')
      row = f'\n\t {key} {get_attributes_string(value)}'
      table_string += row

    print(table_string + "}")

  return string

  #   atributes = ""
  #   for key, value in table['attributes'].items():
  #     match(key):
  #       case "type":
  #         table_string += f'\n\t {key} {value['type'].replace("DataTypes.", "")} '
  #       case "primaryKey":
  #         atributes += "primary key, "
  #       case "autoIncrement":
  #         atributes += "increment, "
  #       case "allowNull":
  #         atributes += "" if value else "not null, "
  #         break
  #       case "deafultValue":
  #         atributes += f'default: {value}, '
  #     print(atributes)
  # if(len(atributes) == 0):
  #   string.append(table_string + "}")
      
  # table_string += f'[{atributes[:-2]}]'

  # string.append(table_string +"}")