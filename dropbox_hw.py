import dropbox
import os

class TransferData:
    
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):

        for root, dirs, files in os.walk(file_from) 

        relative_path = os.path.relpath(local_path, file_from)
        dropbox_path = os.path.join(file_to, relative_path)
        dbx = dropbox.Dropbox(self.access_token)

        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BdpVo9xOUYU3HK5xboj-xAwgZacd6VLd8ZImCQ4rZOxGOzCBQKg4GyFjdQkm9rE2lE6zte-Ss_1MVeXZGwFwqwR7pTOsOY7bLbvu6WElwamGz0KhZQkXZsEaQ-ezD9Gl_Y_Noco'
    objectTF = TransferData(access_token)

    file_from = input('Enter the path of file to be uploaded:')
    file_to = input('Enter the path to upload the file to:')  
    objectTF.upload_file(file_from, file_to)
main()
