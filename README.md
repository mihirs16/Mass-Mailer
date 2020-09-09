# Mass Mailer 
This is a utility script that can be used to send mails by importing contacts from given spreadsheets and also allow to embed data to accomodate for stylised content and/or attach PDFs.

## Instructions

* Clone the repository.
```
git clone https://github.com/mihirs16/mass-mailer
```
* Install the required dependencies as follows.
```
pip install pandas python-dotenv
```
* Now create a file with the name `.env`. Add all API Keys inside this file as text. Click [here](https://pypi.org/project/python-dotenv/) to know more about hidden API Keys as Environment Variables.
```
EMAIL_ADDRESS=exampleSenderAddress@gmail.com
EMAIL_PASSWORD=ExamplePassword#123
EMAIL_PORT=465
EMAIL_SMTP=smtp.gmail.com
```
* Create a folder `mail_data` in the *root directory* to save the spreadsheets.
* Create a folder `attachments` to store attachments correlating to the *contacts* data.
* To disable extra prompts set `DEBUG_MODE = False`. You can find it [here](https://github.com/mihirs16/mass-mailer/blob/52441e89a30fb4f239249289db30fba0eb1cbbd3/data.py#L3).

## Built With
| Software | Version |
|----------|---------|
| Python 3 | 3.8.5 |

* Development Libraries

| Name | Last Version Tested With |
|----------|--------------------------|
| Python | 3.8.5 |
| Pandas | 0.25.1 |
| Python-Dotenv | 0.13.0 |

## Disclaimer
Instances of the aforementioned project fit for specific use cases can be spawned and developed for your own use.<br>
If you find this useful :star: this repo. And if you want to use the code go ahead and *fork* it.:fork_and_knife:
