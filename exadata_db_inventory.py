import collections
import sys

node1_inventory_file = 'R:\\pmpl_inventory\\pmpl_db_inventory_node1.lst'
node2_inventory_file = 'R:\\pmpl_inventory\\pmpl_db_inventory_node2.lst'
node3_inventory_file = 'R:\\ajax_inv\\ajax_db_inventory_node3.lst'
node4_inventory_file = 'R:\\ajax_inv\\ajax_db_inventory_node4.lst'
exadata_inventory_csv = 'R:\\pmpl_inventory\\pmpl_db_inventory.csv'

node1 = 'pmpllexd1001-m'
node2 = 'pmpllexd1002-m'
node3 = 'pmpllexd1003-m'
node4 = 'pmpllexd1004-m'


inventory = {}
inventory[node1] = []
with open(node1_inventory_file, 'r') as node1_inventory:
    for inst in node1_inventory:
        inventory[node1].append(inst.strip())
inventory[node2] = []
with open(node2_inventory_file, 'r') as node2_inventory:
    for inst in node2_inventory:
        inventory[node2].append(inst.strip())
# inventory[node3] = []
# with open(node3_inventory_file, 'r') as node3_inventory:
#     for inst in node3_inventory:
#         inventory[node3].append(inst.strip())
# inventory[node4] = []
# with open(node4_inventory_file, 'r') as node4_inventory:
#     for inst in node4_inventory:
#         inventory[node4].append(inst.strip())

database_names = []
for value in inventory.values():
    for dbname in value:
        database_names.append(dbname[:-1])
database_names_set = set(database_names)

ordered_inventory = collections.OrderedDict(sorted(inventory.items()))


single_instance_databases = {}
single_instance_node = None

sys.stdout = open(exadata_inventory_csv, 'w+')
print("Database name;" + node1 + ";" + node2 + ";")
for dbname in database_names_set:
    single_instance_counter = 0
    if dbname == '+ASM':
        print(dbname[1:], end=';')
    elif dbname == '-MGMTD':
        continue
    else:
        print(dbname, end=';')
    for key, values in ordered_inventory.items():
        for db_instance in values:
            if dbname == db_instance[:-1]:
                if db_instance in ['+ASM1', '+ASM2', '+ASM3', '+ASM4']:
                    print(db_instance[1:], end='')
                else:
                    print(db_instance, end='')
                single_instance_counter += 1
                single_instance_node = key
        print(end=';')
    if single_instance_counter == 1:
        single_instance_databases[dbname] = single_instance_node
    print()


print()
print('There are ' + str(len(single_instance_databases)) + ' databases running with only one instance')
for database, nodename in single_instance_databases.items():
    print('Database ' + database + ' has only one instance running on ' + nodename)
sys.stdout = sys.__stdout__



