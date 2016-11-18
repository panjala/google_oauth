

from apiclient import errors
from datetime import datetime
import sys, os
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

token_file = sys.path[0] + '/auth_token.txt'

print token_file

# Copy your credentials from the APIs Console
CLIENT_ID = '326086268283-vm05aajmkf237il0t3qcgd5ekvq0q2cb.apps.googleusercontent.com'
CLIENT_SECRET = 'gbAOo6X92ciuR1SZvQa5IGzz'
# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive.file'
# Redirect URI for installed apps, can be left as is
REDIRECT_URI = 'http://localhost:8080/'
import pdb


def file_ops(file_path):
    mime_type = guess_type(file_path)[0]
    mime_type = mime_type if mime_type else 'text/plain'
    file_name = file_path.split('/')[-1]
    return file_name, mime_type


def create_token_file(token_file):
# Run through the OAuth flow and retrieve credentials
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
    print "&&&&&&&&&&&&&",storage
    return storage
def authorize(token_file, storage):
# Get credentials
    if storage is None:
        storage = Storage(token_file)
    credentials = storage.get()
# Create an httplib2.Http object and authorize it with our credentials
    http = httplib2.Http()
    #credentials.refresh(http)
    http = credentials.authorize(http)
    return http

def insert_file(file_path, file_name, mime_type):
    pdb.set_trace()
    drive_service = build('drive', 'v3', http=http)
    media_body = MediaFileUpload(file_path,
                                 mimetype=mime_type,
                                 resumable=True)
    unicode_type = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    # unicode format 2014-08-10T11:33:16.844Z
    body = {
        'title':  file_name,
        'description': 'Random description',
        'mimeType':mime_type,
        #'parents': [{'id': 'google drive shared folder id']}],
        'modifiedDate': unicode_type
    }

    try:
        file = drive_service.files().insert(
            body=body,
            media_body=media_body).execute()
        print file
        return file
    except errors.HttpError, error:
        print 'An error occured: %s' % error
        return None

if __name__ == '__main__':
# Check if file provied as argument and exists
    if len(sys.argv) != 2:
        print("One file should be provided as argument")
        sys.exit(1)
    else:
# Path to the file to upload
        file_path = sys.argv[1]
    try:
        with open(file_path) as f: pass
    except IOError as e:
        print(e)
        sys.exit(1)
# Check if token file exists, if not create it by requesting authorization code
    try:
        with open(token_file) as f: pass
    except IOError:
       
        http = authorize(token_file, create_token_file(token_file))
# Authorize, get file parameters, upload file and print out result URL for download
    http = authorize(token_file, None)
    file_name, mime_type = file_ops(file_path)
# Sometimes API fails to retrieve starting URI, we wrap it.
    try:
        print(insert_file(file_path, file_name, mime_type))
    except ResumableUploadError as e:
        print("Error occured while first upload try:", e)
        print("Trying one more time.")
        print(upload_file(file_path, file_name, mime_type))
