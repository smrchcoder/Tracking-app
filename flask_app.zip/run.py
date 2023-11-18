from app import app
from app.repo.create_tables import create_tables_if_not_exist,encoprate_dbChanges



if __name__ == '__main__':
    create_tables_if_not_exist()
    app.run(debug=True)