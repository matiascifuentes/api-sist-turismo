class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/SISTEMA_TURISTICO'
    SQLALCHEMY_BINDS = {
	    'db_turismo': SQLALCHEMY_DATABASE_URI,
	    'dm_turismo': 'postgresql://postgres:postgres@localhost:5432/DM_SISTEMA_TURISTICO'
	}
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
}
