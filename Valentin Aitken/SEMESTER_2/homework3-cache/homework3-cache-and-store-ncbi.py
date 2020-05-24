import redis
import web

urls = (
    '/', 'Index'
)


class Index:
    def GET(self):
        return "Hello, world!"

class NcbiQuery:
    def __index__(self, query):
        self.parse(query)

    def parse(self, query):
        pass


class NcbiCache:
    def __init__(self, memory_cache_client, mongo_client):
        self.memory_cache_client = memory_cache_client
        self.mongo = mongo_client

    def get_url(self, url):
        m_data = self.get_memory(url)
        if m_data:
            return m_data.decode('utf-8')

        db_data = self.get_db()

    def get_memory(self, url):
        return self.memory_cache_client.get(url)


def main():
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set('foo', 'bar')
    print(r.get('foo'))
    app = web.application(urls, globals())
    app.run()


if __name__ == "__main__":
    main()
