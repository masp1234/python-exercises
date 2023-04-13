file_name = 'techcrunch.csv'
lines = (line for line in open(file_name))
print(lines)


# rstrip() to make sure there are no trailing newline characters, which can be present in CSV files.
list_line = (s.rstrip().split(',') for s in lines)

cols = next(list_line)

# returns a dictionary with key-value pairs from cols (a list with the column values) and the data yielded from the "list_line" generator
company_dicts = (dict(zip(cols, data)) for data in list_line)

# a generator (created with a generator expression) that yields an int with the raised amount if the yielded company_dict's (from the above generator) key "round" has the value "a". Iterating through the generator "funding" will yield all the raised amounts of the companies with founding round 'a' 
funding = (
    int(company_dict['raisedAmt'])
    for company_dict in company_dicts
    if company_dict['round'] == 'a'
)

total_series_a = sum(funding)
print(f'Total series A fundraising: ${total_series_a}')


#companies_with_a = [company for company in funding]
#print(len(companies_with_a))
#for company in companies_with_a:
 #   print(company)