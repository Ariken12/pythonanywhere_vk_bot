import classcom
import vkapi
import params


def cat(message, attachment, user_id):
   attachment = None
   message = 'Вот тебе котик, но вк все равно гады :<'
   attachment = vkapi.get_random_wall_picture(-32015300, 'wall')
   return message, attachment


cat_command = classcom.Command()

cat_command.keys = ['котик', 'кошка', 'кот', 'котенок', 'котяра', 'cat']
cat_command.description = 'Пришлю картинку с котиком'
cat_command.process = cat
