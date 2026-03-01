import re
import json

def parse_receipt(text):
    data = {"items": [], "total_amount": 0.0, "date_time": "", "payment_method": ""}

    # Main regex: captures Index, Name, Qty, Unit Price, and Subtotal
    # [cite: 1, 2, 3]
    item_pattern = re.compile(r"(\d+)\.\n(.*?)\n(\d+,\d+)\s*x\s*([\d\s,]+)\n([\d\s,]+)")
    
    for match in item_pattern.findall(text):
        # Convert numeric strings (1 200,00 -> 1200.0) for math operations
        qty = float(match[2].replace(',', '.'))
        price = float(match[3].replace(' ', '').replace(',', '.'))
        subtotal = float(match[4].replace(' ', '').replace(',', '.'))
        
        data["items"].append({
            "name": match[1].strip(),
            "quantity": qty,
            "price_per_unit": price,
            "total_item_price": subtotal
        })

    # Extract global receipt data: Total, Date/Time, and Payment type
    # [cite: 1, 7]
    total_val = re.search(r"ИТОГО:\s*([\d\s,]+)", text)
    data["total_amount"] = float(total_val.group(1).replace(' ', '').replace(',', '.'))if total_val else 0.0
    
    date_val = re.search(r"Время:\s*([\d\.:\s]+)", text)
    data["date_time"] = date_val.group(1).strip() if date_val else ""

    data["payment_method"] = "Bank Card" if "Банковская карта" in text else "Cash"

    return data

# Load and execute
with open('raw.txt', 'r', encoding='utf-8') as f:
    print(json.dumps(parse_receipt(f.read()), indent=4, ensure_ascii=False))