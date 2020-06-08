from redis import Redis
from pymongo import MongoClient
from http.client import HTTPSConnection
from flask import Flask, request, Response
import urllib.parse

EUTILS_KEY = 'eutils_keys'


class NcbiCache:
    def __init__(self, memory_cache_client: Redis, mongo_client: MongoClient):
        self.memory_cache_client = memory_cache_client
        self.mongo = mongo_client
        self.http_conn = HTTPSConnection('eutils.ncbi.nlm.nih.gov')
        self.http_conn.connect()

    def get_eutils_url(self, eutils_service_url) -> str:
        m_data = self.memory_cache_client.hget(EUTILS_KEY, eutils_service_url)
        if m_data:
            body = m_data.decode('utf-8')
        else:
            try:
                response = self.get_http_response(eutils_service_url)
            except ConnectionResetError:
                self.http_conn.connect()
                response = self.get_http_response(eutils_service_url)
            body = response.read()
            self.memory_cache_client.hset(EUTILS_KEY, eutils_service_url, body)
        response = Response(body)
        response.headers['Content-Type'] = 'text/xml; charset=UTF-8'
        return response

    def get_http_response(self, eutils_service_url):
        self.http_conn.request('GET', '/entrez/eutils/' + eutils_service_url)
        return self.http_conn.getresponse()


rclient = Redis(host='localhost', port=6379, db=0)
mongo_client = MongoClient("mongodb://localhost:27017/")
ncbi_cache = NcbiCache(rclient, mongo_client)
app = Flask(__name__)


@app.route('/eutils', methods=['GET'])
def eutils():
    raw_query = request.args.get('query')
    print(raw_query)
    return ncbi_cache.get_eutils_url(raw_query)
    # query = urllib.parse.quote(raw_query) if (' ' in raw_query) else raw_query


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=False)
