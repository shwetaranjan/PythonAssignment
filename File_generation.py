import csv  
from faker import Faker

def datagenerate(records, headers):
    fake = Faker('en_US')
    fake1 = Faker('en_GB')   
    with open("New_file.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            writer.writerow({
                    "Prefix" : fake.prefix(), 
                    "Name": fake.name(),
                    "Phone Number" : fake1.phone_number(),
                    "Address" : fake.address(),
                    "Zip Code" : fake.zipcode(),
                    "City" : fake.city(),
                    "State" : fake.state(),
                    "Country" : fake.country(),
                    })
    
if __name__ == '__main__':
    records = 1000000
    headers = ["Prefix", "Name", "Phone Number","Address", "Zip Code", "City","State", "Country"]
    datagenerate(records, headers)  
    print("CSV File Generated!") 