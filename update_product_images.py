#!/usr/bin/env python
"""Update product images with high-quality photos from Unsplash."""

import os
import sys

# Use SQLite for development - no MySQL server needed
os.environ['DB_TYPE'] = 'sqlite'
os.environ['DB_URI'] = 'sqlite:///flaskshop.db'

sys.path.insert(0, '.')

from flaskshop.app import create_app
from flaskshop.extensions import db
from flaskshop.product.models import Product

PRODUCT_IMAGES = {
    'Electronics': [
        'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&q=80',
        'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800&q=80',
        'https://images.unsplash.com/photo-1516714435716-81dcd9b52f6d?w=800&q=80',
        'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&q=80',
        'https://images.unsplash.com/photo-1587829191301-4b53d0a4f851?w=800&q=80',
        'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=800&q=80',
        'https://images.unsplash.com/photo-1527814050087-3793815479db?w=800&q=80',
        'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80',
        'https://images.unsplash.com/photo-1569163139394-de4798aa62b1?w=800&q=80',
        'https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=800&q=80',
    ],
    'Fashion': [
        'https://images.unsplash.com/photo-1542272604-787c62d465d1?w=800&q=80',
        'https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=800&q=80',
        'https://images.unsplash.com/photo-1506629082632-2d0d5b0c0f11?w=800&q=80',
        'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=800&q=80',
        'https://images.unsplash.com/photo-1551145362-01fbf7ca8167?w=800&q=80',
        'https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=800&q=80',
        'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800&q=80',
        'https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=800&q=80',
        'https://images.unsplash.com/photo-1544923408-75c7e0ad6e5e?w=800&q=80',
        'https://images.unsplash.com/photo-1460353581641-37baddab0fa2?w=800&q=80',
    ],
    'Home': [
        'https://images.unsplash.com/photo-1550439062-b57b3f27c62c?w=800&q=80',
        'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=800&q=80',
        'https://images.unsplash.com/photo-1565193566173-7cde230f17f8?w=800&q=80',
        'https://images.unsplash.com/photo-1523580494863-6f3031224c94?w=800&q=80',
        'https://images.unsplash.com/photo-1506439773649-6e0eb8cfb237?w=800&q=80',
        'https://images.unsplash.com/photo-1578500494198-246f612d03b3?w=800&q=80',
        'https://images.unsplash.com/photo-1533043464125-16e3b20636a3?w=800&q=80',
        'https://images.unsplash.com/photo-1540932239986-310128078ceb?w=800&q=80',
        'https://images.unsplash.com/photo-1566279549557-5e442c6c7d8d?w=800&q=80',
        'https://images.unsplash.com/photo-1595524677302-3ed4146d1e73?w=800&q=80',
    ],
    'Books': [
        'https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=800&q=80',
        'https://images.unsplash.com/photo-1507842217343-583f7270bfba?w=800&q=80',
        'https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?w=800&q=80',
        'https://images.unsplash.com/photo-1543002588-d83cee259f1d?w=800&q=80',
        'https://images.unsplash.com/photo-1516979187457-637abb4f9353?w=800&q=80',
        'https://images.unsplash.com/photo-1491841573634-28fb1df537d1?w=800&q=80',
        'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=800&q=80',
        'https://images.unsplash.com/photo-1512820790803-83ca734da794?w=800&q=80',
    ],
}

def update_images():
    app = create_app()
    with app.app_context():
        products = Product.query.all()
        if not products:
            print("No products found. Run: python -m flask --app app seed")
            return
        
        for idx, product in enumerate(products):
            category = product.category.title if product.category else 'Electronics'
            images = PRODUCT_IMAGES.get(category, PRODUCT_IMAGES['Electronics'])
            product.image = images[idx % len(images)]
            print(f"✓ Updated: {product.title[:40]}")
        
        db.session.commit()
        print(f"\n✅ Successfully updated {len(products)} product images!")

if __name__ == '__main__':
    update_images()
