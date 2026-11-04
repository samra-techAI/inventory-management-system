# Inventory Management System

A simple command-line inventory management system written in Python. Product data is stored locally in a JSON file, so inventory changes persist between runs.

## Features

- Add products with an ID, name, price, and starting quantity
- View all products or search for a product by ID
- Update a product's stock quantity
- Record a sale and automatically deduct sold units from stock
- Show products with five or fewer units in stock
- Save inventory data to `inventory.json`

## Requirements

- Python 3
- No third-party packages required

## Run

Clone this repository, open a terminal in the project directory, and run:

```bash
python inventory.py
```

On some systems, use `python3 inventory.py` instead.

Follow the numbered menu in the terminal to select an action. Choose **7** to exit.

## Inventory Data

The application reads and writes `inventory.json` in its current working directory. If the file does not exist when the application starts, it begins with an empty inventory. Each product is stored by its ID:

```json
{
  "P001": {
    "name": "Wireless Mouse",
    "price": 1200.0,
    "quantity": 15
  }
}
```

Prices are stored as numbers; the application does not assign a currency. Product IDs must be unique. Prices and stock quantities cannot be negative, and a sale cannot exceed the available stock.

## Project Files

- `inventory.py` - application code
- `inventory.json` - saved inventory data, including the sample products