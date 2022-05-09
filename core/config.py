import os

# from core.libs import log

# root_dir = os.path.split(os.getcwd())[1]
# logger = log.get_logger(__name__)


class Config:

    # SQLAlchemy and DB configurations
    DB_DATABASE_URI = '{0}://{1}:{2}@{3}:{4}/{5}'.format(
        'postgresql',
        os.environ.get('PGUSER'),
        os.environ.get('PGPASSWORD'),
        os.environ.get('PGHOST'),
        os.environ.get('PGPORT', 5432),
        os.environ.get('PGDATABASE')
    )

    # DB_RANDOM_PAGE_COST = float(os.environ.get('DB_RANDOM_PAGE_COST', '1.1'))
    # DB_SEQ_PAGE_COST = int(os.environ.get('DB_SEQ_PAGE_COST', '1'))
    # DB_STATEMENT_TIMEOUT = int(os.environ.get('DB_STATEMENT_TIMEOUT', '500'))

    # HOSTNAME = os.environ.get('HOSTNAME', root_dir)

    # DB_APPLICATION_NAME = HOSTNAME

    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # DB_ECHO = (os.environ.get('SQLALCHEMY_ECHO', 'F') == 'T')
    # DB_ECHO_POOL = (os.environ.get('SQLALCHEMY_ECHO_POOL', 'F') == 'T')

    # SCHEMA_NAME = 'platform_schema'

    # # AWS Configs
    # AWS_S3_PUT_URL_EXPIRATION = int(os.environ.get('AWS_S3_PUT_URL_EXPIRATION', 3600))
    # AWS_S3_GET_URL_EXPIRATION = int(os.environ.get('AWS_S3_GET_URL_EXPIRATION', 3600))
    # AWS_S3_PRIMARY_BUCKET = os.environ['AWS_S3_PRIMARY_BUCKET']
    # AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    # AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    # AWS_REGION = os.environ['AWS_REGION']

    # # Currency API KEYS
    # CURRENCYLAYER_KEY = os.environ['CURRENCYLAYER_KEY']
    # CURRENCYLAYER_HOST = 'https://api.currencylayer.com'
    # CURRENCYLAYER_GET_EXCHANGE_RATE_API = CURRENCYLAYER_HOST + '/convert'

    # # Google Places key
    # GOOGLE_MAPS_HOST = 'https://maps.googleapis.com'
    # GOOGLE_PLACE_API_KEY = os.environ['GOOGLE_PLACE_API_KEY']

    # # Service Endpoints
    # POLICY_SERVICE_URL = os.environ['POLICY_SERVICE_URL']
    # POLICY_TEST_API = POLICY_SERVICE_URL + '/internal/policy/test'

    # DATA_EXTRACTOR_SERVICE_URL = os.environ['DATA_EXTRACTOR_SERVICE_URL']
    # NOTIF_SERVICE_URL = os.environ['NOTIF_SERVICE_URL']
    # APP_PUBLIC_URL = os.environ['APP_PUBLIC_URL']
    # DEFAULT_LIMIT = 100

    # ENVIRONMENT = os.environ['ENVIRONMENT']

    # SUPPORT_EMAIL = 'support@fylehq.com'

    # # Twilio keys
    # TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
    # TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
    # TWILIO_MESSAGING_SERVICE_SID = os.environ['TWILIO_MESSAGING_SERVICE_SID']
    # TWILIO_SMS_DEMO_NUMBER = os.environ.get('TWILIO_SMS_DEMO_NUMBER')

    # # Visa Enrollment
    # VISA_ENROLLMENT_HOST = os.environ['VISA_ENROLLMENT_HOST']
    # VISA_COMMUNITY_CODE = os.environ['VISA_COMMUNITY_CODE']
    # VISA_ENROLLMENT_URL = '%s/ExpressApi/%s/api/Enrollees' % (VISA_ENROLLMENT_HOST, VISA_COMMUNITY_CODE)

    # VISA_MLE_RSA_CERT = os.environ['VISA_MLE_RSA_CERT']


config_dict = {key: value for key, value in Config.__dict__.items() if not key.startswith('__') and not callable(key)}
