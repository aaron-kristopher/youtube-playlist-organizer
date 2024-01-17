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

def save_to_csv(videos):
    field_names = list(videos[0].keys())

    with open('videos.csv', 'w') as csvfile: 
        writer = csv.DictWriter(csvfile, fieldnames = field_names) 
        writer.writeheader() 
        writer.writerows(videos)


if __name__ == "__main__":
    video_id = get_video_id_from_csv("./videos.csv")
    print(video_id)
