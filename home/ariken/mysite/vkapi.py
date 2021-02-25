import vk
import random
from params import token, confirmation_token, service_token

session = vk.Session()
api = vk.API(session, v=5.107)
token = token
confirmation_token = confirmation_token
service_token = service_token


def send_message(user_id, message, attach):
    randomid = random.randint(10 ** 6, 2 * 10 ** 6)
    try:
        api.messages.send(
            access_token=token,
            peer_id=str(user_id),
            message=message,
            attachment=attach,
            random_id=randomid
                         )
    except vk.exceptions.VkAPIError as error:
        api.messages.send(
            access_token=token,
            peer_id=str(user_id),
            message=error,
            attachment=attach,
            random_id=randomid
                         )


def get_random_wall_picture(group_id, albumid):
    max_num = api.photos.get(
            owner_id=group_id,
            album_id=str(albumid),
            count=0,
            access_token=service_token,
            expires_in=0
                            )['count']
    num = random.randint(1, max_num)
    photo = api.photos.get(
        owner_id=str(group_id),
        album_id=str(albumid),
        count=1, offset=num,
        access_token=service_token
                            )['items'][0]['id']
    attachment = 'photo' + str(group_id) + '_' + str(photo)
    return attachment


def searcher_of_likes(id):
    output = ''
    user_id = api.users.get(user_ids=id, access_token=service_token)
    if user_id:
        user_id = user_id[0]['id']
    groups = api.users.getSubscriptions(user_id=user_id, access_token=service_token)
    groups = groups['groups']['items']
    for i in groups:
        group = -i
        try:
            output += 'https://vk.com/public' + str(i) + '\n'
        except:
            output += 'Сообщество ' + 'group' + 'закрытое' + '\n'
    return output
