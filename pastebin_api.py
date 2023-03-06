from urllib import response
import requests 

api_url = 'https://pastebin.com/doc_api'
def main():

    new_paste('Kunj is Great', 'You are the best', expiration='10M',listed=True)
    """
    This will help create a paste using PasteBin 
    All the Parameteres that could be used are listed below:
    Title : Heading of the paste 
    Body : The content of the paste 
    Expiration : The expiry date of the paste 
    Public: The paste should be visible to all or not

"""

def new_paste(title, text, expiry_date, is_public_or_not):
    
#All the parameters that are used are listed below with their description
    Parame = { 
        'api_dev_key': 'g4nR4B1wn3qawcHEy0K_xRHcfxAz0k_G',
        'api_option': 'Paste',
        'api_paste_code': text,
        'api_paste_name':title,
        'api_paste_expire_date':expiry_date,
        'api_paste_private': '0' if is_public_or_not else '1',
        'api_paste_code': text
    }
    
    # Create a request (post) to the API 

    print("There was an addition to the PasteBin ", end='')
    response= requests.post(api_url, data=Parame)

# Performing if the test was successful or not 
 
if  response.status_code == requests.codes.ok:
   Paste_URL= response.text


    
print (f"Creation of new Pastebin was succesfull with URL: {Paste_URL}") 
return Paste_URL

else:
print(f"There was an unexpected error while creating a pastebin: {response.status_code}")
return None
if __name__ == "__main__":
    main()