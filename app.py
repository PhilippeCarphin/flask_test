#!/usr/bin/env python
from app import app
import os

if __name__ == '__main__':
        import os  
        from app.model import db
        db.create_all()
        port = int(os.environ.get('PORT', 33507)) 
        app.run(host='0.0.0.0', port=port, use_reloader=True)
