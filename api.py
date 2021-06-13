import requests

def fox():
    response = requests.get('http://randomfox.ca/floof')
    status = response.status_code

    if (status == 200):
        # print(response.text)
        json = response.json()
        image = json['image']
        print(image)

    else:
        print('Error: ' + str(status))


def translation(sentence, language):
    payload = {
        'text':sentence,
    }
    response = requests.get(f'https://api.funtranslations.com/translate/{language}', payload)
    json = response.json()
    print(json)
    






if __name__ == '__main__':
    # fox()
    sentence = 'translate this sentence'
    language = 'klingon'
    translation(sentence, language)

    