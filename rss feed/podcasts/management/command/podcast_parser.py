from django.core.management.base import BaseCommand
from podcasts.parser import parse_rss_feed, save_podcast_data_to_db
from podcasts.models import XML


class Command(BaseCommand):
    help = "Parse and update podcast data"

    def handle(self, *args, **options):
        xml = XML.objects.all()

        for link in xml:
            rss_feed_url = link.url
            podcast_data = parse_rss_feed(rss_feed_url)

            if podcast_data:
                podcast_title = link.title

                save_podcast_data_to_db(podcast_data)

                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully parsed and updated podcast data for '{podcast_title}' ({rss_feed_url})"
                    )
                )
            else:
                self.stderr.write(
                    self.style.ERROR(
                        f"Error parsing the podcast data for {rss_feed_url}"
                    )
                )