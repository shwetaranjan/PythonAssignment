import pandas as pd
chunk_size = 500000
batch_no = 1
for chunk in pd.read_csv('New_file.csv',chunksize=chunk_size):
    chunk.to_csv('New_file' + str(batch_no) + '.csv', index=False)
    batch_no +=1
print("Split Completed!")