from app.models.product import Product


sample_product = Product(
    name="Gaming Laptop",
    sku="LAPTOP001",
    price=75000
)

print(sample_product.name)
print(sample_product.sku)
print(sample_product.price)