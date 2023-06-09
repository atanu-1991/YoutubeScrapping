import logging

logging.basicConfig(filename='scrapper.log', filemode='w', level=logging.INFO, format='[ %(asctime)s ] %(lineno)d %(filename)s - %(levelname)s - %(message)s')

def get_comments(youtube, video_details):

    for id in video_details:

        request = youtube.commentThreads().list(part="snippet", videoId=id['video_id'])
        response = request.execute()

        comment_table = []
        comment = []

        for item in response['items']:
            comments = dict(
                Comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay'],
                author_name = item['snippet']['topLevelComment']['snippet']['authorDisplayName'])

            comment.append(comments)


        comm = dict(video_id=id['video_id'], comments=comment)
        comment_table.append(comm)

    logging.info(comment_table)
    return comment_table


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

    channel_summary = get_channel_status(youtube,channel_id)
    video_ids = get_video_ids(youtube,channel_summary)
    video_details = get_video_details(youtube,video_ids)

    get_comments(youtube,video_details)