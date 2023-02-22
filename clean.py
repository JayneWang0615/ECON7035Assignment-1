import pandas as pd

def clean(contact_info_file,other_info_file):
    contact = pd.read_csv(contact_info_file)
    other = pd.read_csv(other_info_file)
    cleaned = pd.merge(contact,other,
                       left_on = 'respondent_id', right_on = 'id',
                       how = 'outer').drop('id',axis=1)
    cleaned = cleaned.dropna()
    cleaned = cleaned[~cleaned['job'].str.contains('insurance')]
    cleaned = cleaned[~cleaned['job'].str.contains('Insurance')]
    return cleaned

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('contact_info_file', help='Respondent contact file (CSV)')
    parser.add_argument('other_info_file', help='Respondent other file (CSV)')
    parser.add_argument('output_file', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.contact_info_file,args.other_info_file)
    cleaned.to_csv(args.output_file, index=False)

    output = pd.read_csv(args.output_file)
    print(output.shape)