import dropbox
import os

class TransferData(object):
    def __init__(self,access_token):
        self.access_token = access_token
      
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for file_name in files:
                local_path = os.path.join(root,file_name)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to,relative_path)   
            with open(local_path, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path,mode = WriteMode('overwrite'))   

def main():
    access_token = 'sl.AsVWlh4IK-bjh1ymMl9PJNacn_Eqfz0F2cLoRKwI3qj899CshouLFusaf9C5vLCPruz-15vP7lHmH0PWUKYYKh4DRLdzxDBRRCPTgBjKVgbLbg8roLcMgVsMHi_d6iQbK7TCTZc'
    tranferData  = TransferData(access_token)
    file_from    = input("Enter the file to be uploaded: ")
    file_to      = input("Enter the file you want to upload it to: ")

    tranferData.upload_file(file_from,file_to)
    print("Your file has been moved!")

main()    