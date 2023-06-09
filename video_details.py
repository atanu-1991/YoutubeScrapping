import logging

logging.basicConfig(filename='scrapper.log', filemode='w', level=logging.INFO, format='[ %(asctime)s ] %(lineno)d %(filename)s - %(levelname)s - %(message)s')

def get_video_details(youtube, video_id):
    '''
    This function will return the information about each video the channel such as video_title, views, likes and comments
    :param youtube:<googleapiclient.discovery.Resource at 0x1601bd94b50>
    :param video_id:<dict> of <list> it contains all the video Id from a channel
    :return:information about each video of specific video_id
    '''
    try:

        video_data = []
        request = youtube.videos().list(part='snippet,statistics', id=','.join(video_id['video_ids']))

        response = request.execute()

        for i in range(len(response['items'])):
            video_info = dict(
                channel_id = video_id['channel_id'],
                video_title = response['items'][i]['snippet']['title'],
                thumbnail = response['items'][i]['snippet']['thumbnails']['high']['url'],
                viewcount = int(response['items'][i]['statistics']['viewCount']),
                likecount = int(response['items'][i]['statistics']['likeCount']),
                commentcount = int(response['items'][i]['statistics']['commentCount']),
                video_link = 'https://www.youtube.com/watch?v=' + response['items'][i]['id'],
                video_id = response['items'][i]['id']
            )

            video_data.append(video_info)

        logging.info(video_data)
        return video_data

    except Exception as e:
        logging.error('An error has occured',e)


def get_vid_details(youtube, video_id):
    '''
    This function will return the information about each video the channel such as video_title, views, likes and comments etc.
    :param youtube:<googleapiclient.discovery.Resource at 0x1601bd94b50>
    :param video_id:<dict> of <list> it contains all the video Id from a channel
    :return: information about each video of specific video_id
    '''
    try:
        video_data = []
        request = youtube.videos().list(part='snippet,statistics', id=video_id)

        response = request.execute()

        for i in range(len(response['items'])):
            video_info = dict(
                video_title = response['items'][i]['snippet']['title'],
                thumbnail = response['items'][i]['snippet']['thumbnails']['high']['url'],
                viewcount = int(response['items'][i]['statistics']['viewCount']),
                likecount = int(response['items'][i]['statistics']['likeCount']),
                commentcount = int(response['items'][i]['statistics']['commentCount']),
                video_link = 'https://www.youtube.com/watch?v=' + response['items'][i]['id'],
                video_id = response['items'][i]['id'])

            video_data.append(video_info)

        logging.info(video_data)
        return video_data

    except Exception as e:
        logging.error('An error has occured',e)


if __name__ == '__main__':
    from googleapiclient.discovery import build
    from channel_summary import get_channel_status
    from video_id import get_video_ids
    from dotenv import load_dotenv
    import os

    load_dotenv()
    api_service_name = "youtube"
    api_version = "v3"
    api = os.getenv('inr')
    api_key = f'{api}'
    channel_id = 'UCNU_lfiiWBdtULKOw6X0Dig'
    youtube = build(api_service_name, api_version, developerKey=api_key)
    channel_summary = get_channel_status(youtube,channel_id)
    video_id = get_video_ids(youtube,channel_summary)

    get_vid_details(youtube,'bDJkMOvhAmc')
