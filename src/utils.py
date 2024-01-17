import re
import csv
from itertools import islice


regex = r"(?i)(?:episode|ep)\s*(?P<episode_number>\d{1,4})(?:\s+of\s+\d+\s*)?.*"


def get_episode_number(title):
    match = re.search(regex, title)
    if match:
        return int(match.group("episode_number"))
    else:
        return None  # Or handle cases where no episode number is found


def remove_non_episode_video(videos):

    for index, video in enumerate(videos):
        if video["episode_number"] is None:
            videos.pop(index)

    return videos


def get_sorted_videos(videos):
        sort_videos(remove_non_episode_video(videos))

        print(f"Videos Retrieved: {len(videos)}")

        return videos


def sort_videos(videos):
    videos.sort(key=lambda vid:vid["episode_number"])


def get_video_id_from_csv(videos_csv):
    try:
        with open(videos_csv, 'r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)  # Skip the header row
            column_index = header.index("video_id")
            column_items = [row[column_index] for row in reader]
        return column_items

    except FileNotFoundError:
        print(f"Error: File '{videos_csv}' not found.")
        return None

    except ValueError:
        print("Error: Column video id not found in the CSV file.")
        return None


def get_videos_from_csv(videos_csv):
    with open(videos_csv) as csvfile:
        reader = csv.DictReader(csvfile)
        videos = list(reader)
    return videos


def remove_duplicate_videos(videos):
    seen = set()
    new_videos = []

    for video in videos:
        item = tuple(video.items())
        if item not in seen:
            seen.add(item)
            new_videos.append(video)
    return new_videos


def save_to_csv(videos):
    field_names = list(videos[0].keys())

    with open('videos.csv', 'w') as csvfile: 
        writer = csv.DictWriter(csvfile, fieldnames = field_names) 
        writer.writeheader() 
        writer.writerows(videos)


def check_missing_videos(videos):
    missing_episodes = []

    count = 0   
    episode = 0
    expected_episode_number = 1

    while (count < len(videos)):
        count += 1
        episode_number = int(videos[episode]["episode_number"])

        if episode_number != expected_episode_number:
            print(f"episode: {episode_number}\texpected: {expected_episode_number}")
            missing_episodes.append(expected_episode_number)
            expected_episode_number += 1
        else:
            episode += 1
            expected_episode_number += 1
    return missing_episodes


def get_remaining_videos(videos_csv, last_video):
    last_video = offset_missing_episodes(last_video)

    with open(videos_csv) as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)  
        headers = rows[0]  
        data = rows[last_video:]  
        videos = [dict(zip(headers, row)) for row in data[1:]]  # Convert remaining rows to dictionaries

    print(videos[0]["episode_number"])
    return videos


def offset_missing_episodes(last_video):
    missing_episodes = [136, 305, 306, 307, 308, 449]
    
    for index, episode in enumerate(missing_episodes):
        if last_video < episode:
            return last_video - (index +  1)

    return last_video


if __name__ == "__main__":
    videos = get_videos_from_csv("./videos.csv")
    missing_episodes = check_missing_videos(videos)

    vidoes = get_remaining_videos("./videos.csv", 350)
    print(f"Missing episodes: {missing_episodes}")


