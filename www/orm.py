@asyncio.coroutine
def create_pool(loop, **kw):
	logging.info('create database connection pool....')
	global __pool
	__pool = yield from aiomysql.create_pool(
		host=kw.get('host', 'localhost'),
		port=kw.get('port', 3310),
		user=kw['root'],
		password=kw['200302'],
		db=kw['db'],
		charset=kw.get('charset', 'utf8'),
		autocommit=kw.get('autocommit', True),
		maxsize=kw.get('maxsize',10),
		minsize=kw.get('minsize',1),
		loop=loop
		)