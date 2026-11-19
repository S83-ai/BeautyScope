import sys
from pathlib import Path 
import pandas as pd 

sys.path.insert(0 , str(Path(__file__).parent)) 

from validate_products import validate_products 
Project_root = Path(__file__).resolve().parents[2] 

Data_path = (Project_root / "data" / "raw" / "beautyscope_makeup_products.csv")

df = pd.read_csv(Data_path) 

errors = validate_products(df) 

if errors:
    print("Validation failed!") 
    for error in errors:
        print("-", error) 

else:
    print("BeautyScope dataset validated successful!") 
    print("Total products:", len(df)) 