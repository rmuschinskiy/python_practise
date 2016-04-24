__author__ = 'Sindbad the Sailor'


def create_namespace(cmd_namespace, cmd_namespc_parent):
    namespaces[cmd_namespace] = cmd_namespc_parent
    if cmd_namespace not in variables:
        variables[cmd_namespace] = []
    #print(namespaces)


def add_var(cmd_namespace, cmd_variable):
    variables[cmd_namespace].append(cmd_variable)
    #print(variables)


def get_namespace(cmd_namespace, cmd_variable):
    for variable in variables[cmd_namespace]:
        if variable == cmd_variable:
            print(cmd_namespace)
            return
    if cmd_namespace == 'global':
        print('None')
        return
    get_namespace(namespaces[cmd_namespace], cmd_variable)


def parse(cmd):
    cmd_words = cmd.split()
    cmd_action = cmd_words[0]
    cmd_namespace = cmd_words[1]
    cmd_variable = cmd_words[2]
    if cmd_action == "add":
        add_var(cmd_namespace, cmd_variable)
    elif cmd_action == "create":
        cmd_namespc_parent = cmd_words[2]
        create_namespace(cmd_namespace, cmd_namespc_parent)
    elif cmd_action == "get":
        get_namespace(cmd_namespace, cmd_variable)


def main():
    global namespaces
    namespaces = {}
    global variables
    variables = {'global': []}
    cmd_n = int(input())
    counter = 0
    commands = []
    while counter < cmd_n:
        commands.append(str(input()))
        counter += 1
    for cmd in commands:
        parse(cmd)

if __name__ == '__main__':
    main()
