from algoliasearch_django import AlgoliaIndex

class ContentIndex(AlgoliaIndex):
    fields = ('title', 'body', 'author', 'created_at')
    settings = {'searchableAttributes': ['title', 'body']}
    index_name = 'content'