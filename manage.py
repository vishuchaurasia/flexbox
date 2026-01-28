#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Management script for FlexBox - CLI commands."""

import click
import os
import sys
from flaskshop.app import create_app
from flaskshop.extensions import db

# Create Flask app
app = create_app()

@click.group()
def cli():
    """FlexBox management commands."""
    pass

@cli.command()
def seed():
    """Seed the database with sample data and users."""
    with app.app_context():
        # Import all seed generators
        from flaskshop.random_data import (
            create_product_type,
            create_categories,
            create_products,
            create_roles,
            create_admin,
            create_pages,
            create_navbar_menu,
            create_shipping_methods,
            create_dashboard_menu,
            create_collections,
            create_sales,
            create_vouchers
        )
        
        # List of generators to run in order
        generators = [
            ('Product Type', create_product_type()),
            ('Categories', create_categories()),
            ('Products', create_products()),
            ('Roles', create_roles()),
            ('Admin Users', create_admin()),
            ('Pages', create_pages()),
            ('Navbar Menu', create_navbar_menu()),
            ('Shipping Methods', create_shipping_methods()),
            ('Dashboard Menu', create_dashboard_menu()),
            ('Collections', create_collections()),
            ('Sales', create_sales()),
            ('Vouchers', create_vouchers()),
        ]
        
        # Execute all generators
        for title, gen in generators:
            click.echo(f'\n📦 Creating {title}...')
            try:
                for msg in gen:
                    click.echo(f'  ✓ {msg}')
            except Exception as e:
                click.echo(f'  ✗ Error: {str(e)}', err=True)
        
        click.echo('\n✅ Database seeded successfully!')
        click.echo('\n👤 Default Admin User:')
        click.echo('   Email: admin@163.com')
        click.echo('   Password: admin')
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
    """Initialize the database (create tables)."""
    with app.app_context():
        click.echo('🗄️  Initializing database...')
        db.create_all()
        click.echo('✅ Database initialized!')

@cli.command()
def dropdb():
    """Drop all database tables (WARNING: destructive)."""
    if click.confirm('⚠️  This will DELETE all data. Are you sure?'):
        with app.app_context():
            click.echo('🗑️  Dropping all tables...')
            db.drop_all()
            click.echo('✅ All tables dropped!')
    else:
        click.echo('Cancelled.')

@cli.command()
def reset():
    """Reset database and re-seed with sample data."""
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
        code.interact(local=namespace, banner='FlexBox Shell')

if __name__ == '__main__':
    cli()
