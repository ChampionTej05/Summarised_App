# Summarised App with StreamLit & ONE-AI  API 

This is the small attempt on using Streamlit and One-AI API to make the summarised APP in python using libs.


## Dependencies 

1. Please create account on ONE-AI API and obtain the secret key for the API at :  https://studio.oneai.com/ 
2. Install the following dependencies for the project to run smoothly or use requirements.txt 
     1.  `pip3 install streamlit`
     2.   `pip3 install ansible-vault` : optional if you want to use vault to save the key and password


## How to run 
App can be run using ansible-vault secrets (recommended) or hard coding the secrets 
### Use ansible vault to store the API key and vault password 
1. Create the ansible-vault secret yaml file using following command `ansible-vault encrypt vault-secrets.yml`
2. Enter the password for the vault (Store it somewhere in local for later use)
3. Add the contents of the file as below. Replace XXXX with your API KEY obtained from one AI
   ```
    api_key : XXXXXXX
   ```
4. Create one more file for ansible vault secret and **DO NOT PUSH THIS FILE TO LOCAL** 
5. Create the file and add the vault password used in step 2. Ensure to add only password in the txt file and nothing else. 
   ```
    vi vault-password.txt 
    > thisIsTheVaultPassword
   ```
6. Verify your ansible-secrets once using `ansible-vault view vault-secrets.yml` 
7. Update the file paths in the code for **ANSIBLE_VAULT_FILE_PATH** and **ANSIBLE_VAULT_PASSWORD_FILE_PATH**


### Without storing the password in vault 
1. Replace the Variable `API_KEY` with your one-ai API key to run it without vault in `main.py` file


### Run the streamlit app 
1. Run the UI : `streamlit run main.py` 
2. This will open the browser on default port 8501
3. Enter the text to summarise in the box 
4. Click on "Summarise" and wait for the response 



## Credits

#### Made for practice by Rakshit Kathawate  :sunglasses: :ok_hand:

#### :wink: Enjoy !!! 