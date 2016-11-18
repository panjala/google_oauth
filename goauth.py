from apiclient import errors

import sys
import logging
import httplib2
from mimetypes import guess_type

# Following libraries can be installed by executing:
# sudo pip install --upgrade google-api-python-client
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from apiclient.errors import ResumableUploadError
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage

import pdb
# Log only oauth2client errors
logging.basicConfig(level="ERROR")

token_file = sys.path[0] + '/auth_token.txt'

CLIENT_ID = '326086268283-vm05aajmkf237il0t3qcgd5ekvq0q2cb.apps.googleusercontent.com'
CLIENT_SECRET = 'gbAOo6X92ciuR1SZvQa5IGzz'
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive.file'
REDIRECT_URI = 'http://localhost:8080/'


# Get mime type and name of given file
'''def file_ops(file_path):
    mime_type = guess_type(file_path)[0]
    mime_type = mime_type if mime_type else 'text/plain'
    file_name = file_path.split('/')[-1]
    return file_name, mime_type'''


def create_token_file(token_file):
    flow = OAuth2WebServerFlow(
        CLIENT_ID,
        CLIENT_SECRET,
        OAUTH_SCOPE,
        redirect_uri=REDIRECT_URI
        )
    authorize_url = flow.step1_get_authorize_url()
    print('Go to the following link in your browser: ' + authorize_url)
    code = raw_input('Enter verification code: ').strip()
    credentials = flow.step2_exchange(code)
    storage = Storage(token_file)
    storage.put(credentials)
    return storage


def authorize(token_file, storage):
# Get credentials
    if storage is None:
        storage = Storage(token_file)
    credentials = storage.get()
    http1 = httplib2.Http()
    return credentials.authorize(http1)

def crteate_folder():
    drive_service = build('drive', 'v3', http=http)
    file_metadata = {
    'name' : 'sachin',
    'mimeType' : 'application/vnd.google-apps.folder'
    }
    file = drive_service.files().create(body=file_metadata,
                                    fields='id').execute()
    print 'Foldier ID: %s' % file.get('id')
    origin_file_id=file.get('id')
    print "*********************",origin_file_id
    return origin_file_id

pdb.set_trace()
def copy_file():
  """Copy an existing file.

  Args:
    service: Drive API service instance.
    origin_file_id: ID of the origin file to copy.
    copy_title: Title of the copy.

  Returns:
    The copied file if successful, None otherwise.
  """
  drive_service = build('drive', 'v3', http=http)
  origin_file_id=crteate_folder()
  copy_title="sai.txt"
  copied_file = {'title': copy_title}
  try:
    return drive_service.files().copy(
        fileId=origin_file_id, body=copied_file).execute()
  except errors.HttpError, error:
    print 'An error occurred: %s' %error

if __name__ == '__main__':
    try:
        with open(token_file) as f: pass
    except IOError:
        http = authorize(token_file, create_token_file(token_file))
    http = authorize(token_file, create_token_file(token_file))

    http = authorize(token_file, None)
    try:
        crteate_folder()
        copy_file()
    except ResumableUploadError as e:
        print("Error occured while first upload try:", e)
        print("Trying one more time.")
