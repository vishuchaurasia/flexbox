# PythonAnywhere Quick Start - FlexBox Setup

## After Git Pull - Step by Step

### 1. SSH into PythonAnywhere Console
```bash
# In PythonAnywhere Bash console
cd ~/proj/flexbox
```

### 2. Activate Virtual Environment
```bash
source venv/bin/activate
```

### 3. Update Dependencies (if requirements.txt changed)
```bash
pip install -r requirements.txt --upgrade
```

### 4. Initialize/Reset Database
```bash
# Option A: Fresh setup (recommended first time)
python manage.py initdb
python manage.py seed

# Option B: Reset everything (if database corrupted)
python manage.py reset

# Option C: Just update seed data (keeps existing data)
python manage.py seed
```

### 5. Update Product Images
```bash
python update_product_images.py
```

### 6. Reload Web App
- Go to PythonAnywhere Dashboard → Web → Reload

## Common Commands

```bash
# Check if virtual env is activated
which python  # Should show: /home/yourusername/proj/flexbox/venv/bin/python

# Seed database
python manage.py seed

# Update product images
python update_product_images.py

# Open Python shell with app context
python manage.py shell

# Reset database completely
python manage.py reset

# Check Flask version
python -c "import flask; print(flask.__version__)"

# Deactivate virtual environment
deactivate
```

## Troubleshooting

### Database Not Creating
```bash
# Make sure directory is writable
ls -la ~/proj/flexbox/
# Should show current directory writable

# If database doesn't create, check:
python -c "
from flaskshop.app import create_app
app = create_app()
with app.app_context():
    from flaskshop.extensions import db
    db.create_all()
    print('Database created!')
"
```

### Import Errors
```bash
# Make sure virtual env is activated
source venv/bin/activate

# Check Python path
python -c "import sys; print(sys.path)"

# Reinstall requirements
pip install -r requirements.txt
```

### Static Files Not Working
- In PythonAnywhere Web tab, check static files mapping:
  - URL: `/static/`
  - Directory: `/home/yourusername/proj/flexbox/flaskshop/static/`
- Click "Reload" button after checking

### App Not Starting
- Check error logs in PythonAnywhere Dashboard
- In Web tab, check error log file path
- Reload web app

## WSGI Configuration

If using custom WSGI, make sure it looks like:

```python
import os
import sys

path = '/home/yourusername/proj/flexbox'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DB_TYPE'] = 'sqlite'
os.environ['DB_URI'] = 'sqlite:////home/yourusername/proj/flexbox/flaskshop.db'

from app import app as application
```

## Admin Login

After seeding:
- **URL**: `https://yourdomain.pythonanywhere.com/login`
- **Email**: `admin@163.com`
- **Password**: `admin`

## Database Location

SQLite database is stored at:
```
/home/yourusername/proj/flexbox/flaskshop.db
```

## File Permissions

If you get permission errors:
```bash
# Make directory accessible
chmod 755 ~/proj/flexbox

# Make database writable (if it exists)
chmod 666 ~/proj/flexbox/flaskshop.db
```

## Updating After Pull

```bash
# 1. Pull latest code
git pull origin main

# 2. Activate virtual env
source venv/bin/activate

# 3. Update dependencies
pip install -r requirements.txt

# 4. No need to reseed unless data structure changed
# (existing data will be preserved)

# 5. Reload web app in PythonAnywhere Dashboard
```

## Environment Variables

Set in PythonAnywhere Web tab → Environment variables, or in WSGI file:

```
DB_TYPE=sqlite
DB_URI=sqlite:////home/yourusername/proj/flexbox/flaskshop.db
FLASK_ENV=production
FLASK_DEBUG=0
```

## Monitoring

Check logs in PythonAnywhere:
- Server error log: `/var/log/...`
- Application log: Check in Web tab
- Slow queries: Check `slow_queries.log` in project directory

## Support

- Documentation: See [PYTHONANYWHERE_SETUP.md](PYTHONANYWHERE_SETUP.md)
- GitHub: https://github.com/vishuchaurasia/flexbox
- Issues: https://github.com/vishuchaurasia/flexbox/issues
