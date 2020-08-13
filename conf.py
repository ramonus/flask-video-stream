from pathlib import Path

p = Path("logs")
if not p.exists():
	p.mkdir()

dictConfig = {
	'version': 1,
	'disable_existing_loggers': True,
	'formatters': {
		'standard': {
			'format': '%(asctime)s [%(levelname)s] %(name)s:: %(message)s',
		},
	},
	'handlers': {
		'default': {
			'level': 'INFO',
			'formatter': 'standard',
			'class': 'logging.StreamHandler',
			'stream': 'ext://sys.stdout',
		},
		'file': {
			'class': 'logging.handlers.RotatingFileHandler',
			'level': 'DEBUG',
			'formatter': 'standard',
			'filename': 'logs/logfile.log',
			'mode': 'a',
			'maxBytes': 5_242_880,
			'backupCount': 3,
			'encoding': 'utf-8',
		},
	},
	'loggers': {
		'__main__': {
			'handlers': ['default','file'],
			'level': 'DEBUG',
			'propagate': False,
		},
		'camera': {
			'handlers': ['default', 'file'],
			'level': 'DEBUG',
			'propagate': False,
		},
	}
}