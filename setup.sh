#!/bin/bash

# Assuming your app has Python dependencies
# It's common to use a virtual environment to isolate dependencies
python3 -m venv venv
source venv/bin/activate

# Install required Python packages
pip install -r requirements.txt

# Set environment variables
echo "export SERVER=my_server_address" >> venv/bin/activate
echo "export DATABASE=my_database_name" >> venv/bin/activate
echo "export USER=my_database_user" >> venv/bin/activate
echo "export PASSWORD=my_database_password" >> venv/bin/activate
echo "export AZURE_KEY=my_azure_key" >> venv/bin/activate

# Activate the virtual environment to make the environment variables available
source venv/bin/activate

# Optional: If you have additional setup steps, like database migrations or data downloads
# python manage.py migrate
# python manage.py download_data

# Print a message indicating that the setup is complete
echo "Setup completed successfully. You can now run your Streamlit app."
