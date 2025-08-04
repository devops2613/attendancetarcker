from sqlalchemy import text  # Add this import at the top of your file

@app.route('/health')
def health_check():
    try:
        # Simple database check
        db.session.execute(text('SELECT 1'))
        return 'OK', 200
    except Exception as e:
        return str(e), 500check
        db.engine.execute('SELECT 1')
        return 'OK', 200
    except Exception as e:
        return str(e), 500