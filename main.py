from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response, FileResponse
from starlette.routing import Route
import time
from datetime import date
import os

def checkImage(id: str): 
    images = []
    files = []
    for i in os.listdir('{}/images'.format(os.getcwd())):
        files.append(i)
        images.append(i[:-4])
    if id in images:
        name = files[images.index(id)]
        return name
    else:
        return None

async def image(request):
    ipAddress = request.client.host
    imageID = request.path_params['image']
    if checkImage(imageID) is None:
        return Exception('Image does not exist')
    timedate = '{} at {}'.format(date.today().strftime("%B %d, %Y"), time.strftime("%H:%M:%S", time.localtime()))
    try:
        with open('{}/logs/{}.txt'.format(os.getcwd(), imageID), 'a') as file: 
            file.write('IP Address: {}; Image Id: {}, Time: {}\n'.format(ipAddress, imageID, timedate))
    except:
        os.mkdir('logs')
    return FileResponse('{}/images/{}.png'.format(os.getcwd(), imageID))


routes = [Route('/images/{image:str}', endpoint=image, methods = ["GET"])]


app = Starlette(routes=routes)

