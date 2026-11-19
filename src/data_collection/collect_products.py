import pandas as pd
from pathlib import Path

#locate the folder
Project_root = Path(__file__).resolve().parents[2] 

#define raw file
Data_path = Project_root / "data" / "raw" / "beautyscope_makeup_products.csv"

#define columns
columns = ["product id","brand","product_name","category","product_type",
           "official_price","retailer_price","retailer_name",
           "discount_percentage","rating","review_count",
           "official_product_url","retailer_product_url",
           "data source","price_collection_date"]

#initialize dataset
def initialize_dataset():
    if not Data_path.exists():
        df = pd.DataFrame(columns=columns) 
        df.to_csv(Data_path, index = False) 
        print("BeautyScope dataset created successfully!") 
    else:
        print("Dataset already existed!") 

if __name__ == "__main__": 
    initialize_dataset()  