"""Setup fixtures."""

from rssreader.interfaces import EntryClass, FeedClass
import pytest


@pytest.fixture
def get_feed_list():

    entry1_1 = EntryClass(title="title_Entry1_1",
                          link="link_Entry1_1",
                          description="description_Entry1_1",
                          description_parsed="description_parsed_Entry1_1",
                          published="published_Entry1_1",
                          guid="guid_Entry1_1",
                          enclosure="enclosure_Entry1_1",
                          content="content_Entry1_1",
                          id=None)

    entry1_2 = EntryClass(title="title_Entry1_2",
                          link="link_Entry1_2",
                          description="description_Entry1_2",
                          description_parsed="description_parsed_Entry1_2",
                          published="published_Entry1_2",
                          guid="guid_Entry1_2",
                          enclosure="enclosure_Entry1_2",
                          content="content_Entry1_2",
                          id=None)

    entry2_1 = EntryClass(title="title_Entry2_1",
                          link="link_Entry2_1",
                          description="description_Entry2_1",
                          description_parsed="description_parsed_Entry2_1",
                          published="published_Entry2_1",
                          guid="guid_Entry2_1",
                          enclosure="enclosure_Entry2_1",
                          content="content_Entry2_1",
                          id=None)

    entry2_2 = EntryClass(title="title_Entry2_2",
                          link="link_Entry2_2",
                          description="description_Entry2_2",
                          description_parsed="description_parsed_Entry2_2",
                          published="published_Entry2_2",
                          guid="guid_Entry2_2",
                          enclosure="enclosure_Entry2_2",
                          content="content_Entry2_2",
                          id=None)

    feed1 = FeedClass(source="source_Feed1",
                      title="title_Feed1",
                      link="link_Feed1",
                      description="description_Feed1",
                      entries=[entry1_1, entry1_2],
                      id=None)

    feed2 = FeedClass(source="source_Feed2",
                      title="title_Feed2",
                      link="link_Feed2",
                      description="description_Feed2",
                      entries=[entry2_1, entry2_2],
                      id=None)

    return [feed1, feed2]
