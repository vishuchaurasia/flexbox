#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Management script for FlexBox - CLI commands."""

import click
import os
import sys
from pathlib import Path
from itertools import chain

# Set SQLite as default database BEFORE importing Flask app
if "DB_TYPE" not in os.environ:
    os.environ["DB_TYPE"] = "sqlite"
if "DB_URI" not in os.environ:
    os.environ["DB_URI"] = "sqlite:///flaskshop.db"

from flaskshop.app import create_app
from flaskshop.extensions import db
from flaskshop.random_data import (
    create_admin,
    create_collections_by_schema,
    create_dashboard_menus,
    create_menus,
    create_orders,
    create_page,
    create_product_sales,
    create_products_by_schema,
    create_roles,
    create_shipping_methods,
    create_users,
    create_vouchers,
    FLEXBOX_SCHEMA,
    FLEXBOX_COLLECTIONS_SCHEMA,
)

# Create Flask app
app = create_app()

@click.group()
def cli():
    """FlexBox management commands."""
    pass

@cli.command()
@click.option('--type', default='flexbox', help='Type of seed: default or flexbox')
def seed(type):
    """Seed the database with sample data and users."""
    with app.app_context():
        click.echo('\n🌱 Seeding database...\n')
        
        if type == 'flexbox':
            # Creates a FlexBox-like demo dataset with categories, products, and menus
            place_holder = Path("placeholders/flexbox")
            # Create products first (this is not a generator)
            create_products_by_schema(
                placeholder_dir=place_holder,
                how_many=5,
                create_images=True,
                schema=FLEXBOX_SCHEMA,
            )
            # Then chain the generator functions
            create_generator = chain(
                create_collections_by_schema(place_holder, schema=FLEXBOX_COLLECTIONS_SCHEMA),
                create_users(),
                create_roles(),
                create_admin(),
                create_page(),
                create_menus(),
                create_shipping_methods(),
                create_dashboard_menus(),
                create_orders(),
                create_product_sales(),
                create_vouchers(),
            )
            
            for msg in create_generator:
                click.echo(f'  ✓ {msg}')
        
        else:  # default
            place_holder = Path("placeholders")
            # Create products first (this is not a generator)
            create_products_by_schema(
                placeholder_dir=place_holder, 
                how_many=10, 
                create_images=True
            )
            # Then chain the generator functions
            create_generator = chain(
                create_collections_by_schema(place_holder),
                create_users(),
                create_roles(),
                create_admin(),
                create_page(),
                create_menus(),
                create_shipping_methods(),
                create_dashboard_menus(),
                create_orders(),
                create_product_sales(),
                create_vouchers(),
            )
            
            for msg in create_generator:
                click.echo(f'  ✓ {msg}')
        
        click.echo('\n✅ Database seeded successfully!')
        click.echo('\n👤 Default Users:')
        click.echo('   Admin: admin@163.com / admin')
        click.echo('   Admin: visaladmin121@test.com / vishal@123')
        click.echo('   User: visal121@test.com / vishal@123')
        click.echo('\n📊 Access admin dashboard at: /dashboard')

@cli.command()
@click.option('--url', default='http://localhost:5000/static', help='Base URL for images')
def update_images(url):
    """Update all product images from Unsplash."""
    with app.app_context():
        from update_product_images import update_images
        click.echo('📸 Updating product images...')
        try:
            update_images()
            click.echo('✅ Product images updated successfully!')
        except Exception as e:
            click.echo(f'✗ Error updating images: {str(e)}', err=True)
            sys.exit(1)

@cli.command()
def initdb():
    """Initialize the database (create tables only)."""
    with app.app_context():
        click.echo('🗄️  Initializing database...')
        db.create_all()
        click.echo('✅ Database tables created!')

@cli.command()
def reset():
    """Reset database - drop all tables and reseed with sample data."""
    if click.confirm('⚠️  This will DELETE all data and create new sample data. Continue?'):
        with app.app_context():
            click.echo('🗑️  Dropping all tables...')
            db.drop_all()
            click.echo('🗄️  Creating tables...')
            db.create_all()
            click.echo('✅ Database reset!')
        
        # Run seed
        ctx = click.get_current_context()
        ctx.invoke(seed)
    else:
        click.echo('Cancelled.')

@cli.command()
def shell():
    """Open interactive shell with app context."""
    with app.app_context():
        import code
        import readline
        
        # Import common modules into shell namespace
        namespace = {
            'app': app,
            'db': db,
        }
        
        # Try to import models
        try:
            from flaskshop.product.models import Product, Category, ProductType
            from flaskshop.account.models import User, Role
            from flaskshop.order.models import Order
            namespace.update({
                'Product': Product,
                'Category': Category,
                'ProductType': ProductType,
                'User': User,
                'Role': Role,
                'Order': Order,
            })
        except ImportError:
            pass
        
        code.interact(
            banner='\n📝 FlexBox Python Shell\nAvailable: app, db, Product, User, Order, etc.\n',
            local=namespace
        )

@cli.command()
def update_images():
    """Update all product images from Unsplash."""
    with app.app_context():
        try:
            from update_product_images import update_images as update_func
            click.echo('📸 Updating product images from Unsplash...')
            update_func()
            click.echo('✅ Product images updated successfully!')
        except ImportError:
            click.echo('⚠️  update_product_images.py not found', err=True)
            sys.exit(1)
        except Exception as e:
            click.echo(f'✗ Error updating images: {str(e)}', err=True)
            sys.exit(1)

if __name__ == '__main__':
    cli()
