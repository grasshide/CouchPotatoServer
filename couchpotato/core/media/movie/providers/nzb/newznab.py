from couchpotato.core.helpers.encoding import tryUrlencode
from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.nzb.newznab import Base
from couchpotato.core.media.movie.providers.base import MovieProvider

log = CPLog(__name__)

autoload = 'Newznab'


class Newznab(MovieProvider, Base):

    def buildUrl(self, media, api_key):
        query = tryUrlencode({
            't': 'movie',
            'imdbid': media['identifier'].replace('tt', ''),
            'apikey': api_key,
            'extended': 1
        })
        return query