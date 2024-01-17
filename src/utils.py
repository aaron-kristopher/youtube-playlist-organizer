import re
import csv


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
    with open(videos_csv) as f:
        reader = csv.DictReader(f)

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


if __name__ == "__main__":
    #video_id = get_video_id_from_csv("./videos.csv")
    videos = get_videos_from_csv("./videos.csv")
    missing_episodes = check_missing_videos(videos)

    print(f"Missing episodes: {missing_episodes}")


