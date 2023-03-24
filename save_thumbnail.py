import base64
import requests
import logging

logging.basicConfig(filename='scrapper.log', filemode='w', level=logging.INFO, format='[ %(asctime)s ] %(lineno)d %(filename)s - %(levelname)s - %(message)s')

def save_image(video_details):
    '''
    It is used to fetch the image and convert it into the base64
    :param video_details:<list> of <dict>, It contains all the info about videos of a specific channel
    :return:<list> of <dict> ,  with image in base64
    '''
    try:
        img_b64s = []
        for i in video_details:
            r = requests.get(i['thumbnail']).content
            image = dict(
                img_b64 = base64.b64encode(r),
                video_id = i['video_id']
            )
            img_b64s.append(image)

        logging.info(img_b64s)
        return  img_b64s

    except Exception as e:
        logging.error(f'An error occured {e}')


if __name__ == '__main__':
    from googleapiclient.discovery import build
    from channel_summary import get_channel_status
    from video_id import get_video_ids
    from video_details import get_video_details
    from dotenv import load_dotenv
    import os

    load_dotenv()
    api_service_name = "youtube"
    api_version = "v3"
    api = os.getenv('inr')
    api_key = f'{api}'
    channel_id = 'UCNU_lfiiWBdtULKOw6X0Dig'
    youtube = build(api_service_name, api_version, developerKey=api_key)

    channel_summary = get_channel_status(youtube, channel_id)
    video_ids = get_video_ids(youtube, channel_summary)
    video_details = get_video_details(youtube, video_ids)
    save_image(video_details)