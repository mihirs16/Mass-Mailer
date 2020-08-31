import pandas as pd 

DEBUG_MODE = True

# Load contacts with name, email and their corresponding attachment filename
def load_contacts(filename = 'mail_data/contacts.csv', name = 'contact_name', emails = 'contact_email', attachments = 'attachments'):
    df = pd.read_csv(filename)
    contacts = []
    for i in range(df.shape[0]):
        contacts.append({
            'name': df.iloc[i][name],
            'email': df.iloc[i][emails],
            'attachment': "attachments/" + df.iloc[i][attachments] + ".pdf"
        })
    
    if DEBUG_MODE:
        print(contacts)
    return contacts

# Load all coupon codes w/o Status = Given
def load_coupons(filename = 'mail_data/coupons.csv'):
    df = pd.read_csv(filename)
    df = df[df['Status'] != 'Given']
    coupons = list(df[df.columns[0]].values)

    if DEBUG_MODE:
        print(coupons)
    return coupons

# Update Status for all sent Coupon Codes
def update_coupons(coupon_code, filename = 'mail_data/coupons.csv'):
    df = pd.read_csv(filename, index_col=0)
    for coupon in coupon_code:
        if DEBUG_MODE:
            print('Updating Coupon: {}'.format(coupon))
        df['Status'][df.index == coupon] = 'Given'
    df.to_csv(filename)

# Test Functions    
# load_contacts(attachments='certificates')
# load_coupons()
# update_coupons(['BMWMERC2013'])
# load_coupons()