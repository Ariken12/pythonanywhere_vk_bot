import classcom


def info(message, attachment, user_id):
    global classcom
    message = 'Список команд:\n'
    for c in classcom.command_list:
        message += c.keys[0] + ' - ' + c.description + '\n'
    return message, ''


info_command = classcom.Command()

info_command.keys = ['помощь', 'помоги', 'help']
info_command.description = 'Покажу список команд'
info_command.process = info
