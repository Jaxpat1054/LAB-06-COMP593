import requests
import hashlib
import os
def main():

    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):

        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)

        # Delete the VLC installer from disk
       # delete_installer(installer_path)
#DONE
def get_expected_sha256():
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.18/win64/vlc-3.0.18-win64.exe.sha256'
    resp_msg = requests.get(file_url)
    # Check whether the download was successful
    if resp_msg.status_code == requests.codes.ok:
    # Extract text file content from response message body
        file_content = resp_msg.text
        after_editing = file_content[:64]
    return  after_editing
#DONE
def download_installer():
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.18/win64/vlc-3.0.18-win64.exe'
    resp_msg = requests.get(file_url)
    # Check whether the download was successful
    if resp_msg.status_code == requests.codes.ok:
    # Extract text file content from response message
        file_content = resp_msg.content
        # Save the text file to disk
        return file_content
    
#work on this function
def installer_ok(installer_data, expected_sha256):
    expected_sha256 = hashlib.sha256(installer_data).hexdigest()
    if expected_sha256 == expected_sha256:
        return True
    
def save_installer(installer_data):
    file_path = os.getenv('TEMP')
    location_path = os.path.join(file_path, "vlc_installer.exe")
    with open(location_path, "wb") as p:
        p.write(installer_data)
    return location_path

def run_installer(installer_path):
    run_script = f'{installer_path} /S'
    os.system(run_script)
    
def delete_installer(installer_path):
    installer_path = r'C:\temp\vlc_installer.exe'
    os.remove(installer_path)
    return
    

if __name__ == '__main__':
    main()