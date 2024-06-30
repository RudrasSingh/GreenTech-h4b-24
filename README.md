# GreenTech-h4b-24

GreenTech-h4b-24 is an innovative project focused on tracking and reducing the carbon footprint of individuals. It includes features like Green-o-gram community for user posts, an AI suggestion chatbot, live temperature and pollution indicators, and automated campaigns using Callchimp API.

## Features

- **Carbon Footprint Tracker**: Calculate and track your carbon footprint based on various parameters like electricity consumption, fuel usage, waste production, and flight hours.
- **Green-o-gram Community**: A platform for users to post and share their eco-friendly activities and tips.

- **AI Suggestion Chatbot**: An intelligent bot providing suggestions and tips on sustainable living.

- **Live Temperature and Pollution Indicators**: Real-time display of temperature and pollution levels in your area.

- **Automated Campaigns**: Use Callchimp API to automate calls and share important messages on water conservation, waste management, public healthcare, and sustainable development.

## Setup

### Prerequisites

- Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Setup

````bash
# Clone the repository
git clone https://github.com/RudrasSingh/GreenTech-h4b-24.git
cd GreenTech-h4b-24

# Setup the Virtual Environment
pip install virtualenv
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Dependencies
pip install -r requirements.txt

# Create a .env file in the root directory and add your environment variables
# Example .env file:
# CALLCHIMP_API_KEY=your_callchimp_api_key

# Initialize the Database
python initialize_db.py
````

Usage
Carbon Footprint Tracker
Navigate to the carbon footprint tracking page.
Enter the required details like electricity consumption, fuel usage, waste production, and flight hours.
Submit the form to calculate and track your carbon footprint.
Green-o-gram Community
Navigate to the Green-o-gram community page.
Post and share your eco-friendly activities and tips with the community.
AI Suggestion Chatbot
Interact with the AI chatbot available on the website.
Receive intelligent suggestions and tips on sustainable living.
Live Temperature and Pollution Indicators
View the real-time temperature and pollution levels displayed on the homepage.
Automated Campaigns
Automated campaigns are managed through Callchimp API. The following functions are available to start different campaigns:


````
import callchimp_campaigns

# Start Sustainable Development Campaign
callchimp_campaigns.sustainable_development_campaign()

# Start Waste Management Campaign
callchimp_campaigns.waste_management_campaign()

# Start Water Conservation Campaign
callchimp_campaigns.water_conservation_campaign()

# Start Public Healthcare Campaign
callchimp_campaigns.public_healthcare_campaign()
````

##Contributing
We welcome contributions to enhance the features and functionalities of this project. Please feel free to raise issues or submit pull requests
