import xml.etree.ElementTree as ET
import requests
from django.db import transaction
from .models import Channel,Episode


def parse_rss_feed(rss_url):
    try:
        response = requests.get(rss_url)
        response.raise_for_status()
        xml_data = response.text

        podcast_metadata = {
            "title": "",
            "description": "",
            "language": "",
            "copyright": "",
            "subtitle": "",
            "author": "",
            "summary": "",
            "image": "",
            "keywords": "",
            "ownerName": "",
            "ownerEmail": "",
            "isExplicit": "",
            "xml": "",
            "follow": "",
            "genres": [],
        }

        episodes = []

        root = ET.fromstring(xml_data)

        for item in root.findall(".//item"):
            episode = {
                "title": item.findtext("title"),
                "duration": item.findtext(
                    "itunes:duration",
                    namespaces={"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"},
                ),
                "enclosure": item.find("enclosure").get("url"),
                "pubdate": item.findtext("pubDate"),
                "isExplicit": item.findtext(
                    "itunes:explicit",
                    namespaces={"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"},
                ),
                "image": item.findtext(
                    "itunes:image",
                    namespaces={"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"},
                ),
                "summary": item.findtext(
                    "itunes:summary",
                    namespaces={"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"},
                ),
                "description": item.findtext(
                    ".//content:encoded",
                    namespaces={"content": "http://purl.org/rss/1.0/modules/content/"},
                ),
            }

            explicit_element = item.find(
                "itunes:explicit",
                namespaces={"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"},
            )
            if explicit_element is not None:
                episode["isExplicit"] = explicit_element.text
            else:
                episode["isExplicit"] = ""

            subtitle_element = item.find(
                "itunes:subtitle",
                namespaces={"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"},
            )
            if subtitle_element is not None:
                episode["subtitle"] = subtitle_element.text
            else:
                episode["subtitle"] = ""

            episodes.append(episode)

        podcast_metadata["title"] = root.findtext("channel/title")
        podcast_metadata["description"] = root.findtext("channel/description")
        podcast_metadata["subtitle"] = root.findtext(
            "channel/itunes:subtitle",
            namespaces={"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"},
        )
        podcast_metadata["author"] = root.findtext(
            "channel/itunes:author",
            namespaces={"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"},
        )
        podcast_metadata["image"] = root.findtext("channel/image/url")
        podcast_metadata["ownerName"] = root.findtext(
            "channel/itunes:owner/itunes:name",
            namespaces={"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"},
        )
        podcast_metadata["ownerEmail"] = root.findtext(
            "channel/itunes:owner/itunes:email",
            namespaces={"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"},
        )
        podcast_metadata["websiteUrl"] = root.findtext("channel/link")
        podcast_metadata["isExplicit"] = root.findtext(
            "channel/itunes:explicit",
            namespaces={"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"},
        )
        podcast_metadata["copyright"] = root.findtext("channel/copyright")
        podcast_metadata["language"] = root.findtext("channel/language")
        podcast_metadata["contentType"] = root.findtext(
            "channel/itunes:type",
            namespaces={"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"},
        )
        podcast_metadata["genres"] = [
            category.text
            for category in root.findall(
                "channel/itunes:category/itunes:category",
                namespaces={"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"},
            )
        ]

        return {"podcast_metadata": podcast_metadata, "episodes": episodes}

    except requests.exceptions.RequestException as e:
        print(f"Error fetching RSS feed: {e}")
        return None


def save_podcast_data_to_db(data):
    podcast_metadata = data.get("podcast_metadata")
    episodes = data.get("episodes")

    with transaction.atomic():
        channel, created = Channel.objects.get_or_create(
            title=podcast_metadata["title"]
        )

        channel.summary = podcast_metadata["summary"]
        channel.subtitle = podcast_metadata["subtitle"]
        channel.author = podcast_metadata["author"]
        channel.image = podcast_metadata["image"]
        channel.ownerName = podcast_metadata["ownerName"]
        channel.ownerEmail = podcast_metadata["ownerEmail"]
        channel.websiteUrl = podcast_metadata["websiteUrl"]
        channel.isExplicit = podcast_metadata["isExplicit"]
        channel.copyright = podcast_metadata["copyright"]
        channel.language = podcast_metadata["language"]
        channel.contentType = podcast_metadata["contentType"]
        channel.genres = podcast_metadata["genres"]

        channel.save()

        for episode_data in episodes:
            if not Episode.objects.filter(
                podcast=channel, enclosure=episode_data["enclosure"]
            ).exists():
                episode = Episode(
                    podcast=channel,
                    title=episode_data["title"],
                    duration=episode_data["duration"],
                    enclosure=episode_data["enclosure"],
                    pubdate=episode_data["pubdate"],
                    isExplicit=episode_data["isExplicit"] == "yes",
                    image=episode_data.get("image", ""),
                    summary=episode_data["summary"],
                    description=episode_data["description"],
                )
                episode.save()