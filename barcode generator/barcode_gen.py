import barcode
from barcode.writer import ImageWriter

def generate_barcode(data, filename):
    # Use Code128 barcode format (good general-purpose barcode)
    CODE128 = barcode.get_barcode_class('code128')
    code = CODE128(data, writer=ImageWriter())
    code.save(filename)
    print(f"Barcode saved as {filename}.png")

# Example usage:
generate_barcode("123456789012", "my_barcode")
