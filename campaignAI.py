import callchimp
from callchimp.rest import ApiException
from pprint import pprint
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the Callchimp API key from environment variables
api_key = os.getenv("CALLCHIMP_API_KEY")

if not api_key:
    raise ValueError("CALLCHIMP_API_KEY environment variable is not set. Please check your .env file.")

# Configure API key authorization
configuration = callchimp.Configuration()
configuration.api_key['x-api-key'] = api_key

def get_api_client():
    try:
        api_client = callchimp.ApiClient(configuration)
        return api_client
    except ApiException as e:
        print("Exception when setting up the API client: %s\n" % e)
        return None

def list_scripts(api_client):
    try:
        scripts_api = callchimp.ScriptsApi(api_client)
        scripts_list_response = scripts_api.scripts_list()
        print("Scripts listed:\n")
        pprint(scripts_list_response)
        return scripts_list_response.scripts
    except ApiException as e:
        print("Exception when calling ScriptsApi->scripts_list: %s\n" % e)
        return []

def get_script_by_id(scripts, script_id):
    return next((script for script in scripts if script.id == script_id), None)

def create_and_start_campaign(api_client, script_id, campaign_name):
    scripts = list_scripts(api_client)
    script = get_script_by_id(scripts, script_id)
    
    if script:
        campaign_request = callchimp.CampaignRequest(
            name=campaign_name,
            script_id=script_id
        )
        try:
            campaigns_api = callchimp.CampaignsApi(api_client)
            campaign_response = campaigns_api.campaigns_post(campaign_request)
            print(f"Campaign '{campaign_name}' created:\n")
            pprint(campaign_response)
            # Start the campaign
            campaign_id = campaign_response.id
            campaigns_api.campaigns_campaign_id_start_post(campaign_id)
            print(f"Campaign '{campaign_name}' started.\n")
        except ApiException as e:
            print(f"Exception when calling CampaignsApi->campaigns_post: %s\n" % e)
    else:
        print(f"Script with ID {script_id} not found")

def sustainable_development_campaign():
    api_client = get_api_client()
    if api_client:
        create_and_start_campaign(api_client, 271, "Sustainable Development Campaign")

def waste_management_campaign():
    api_client = get_api_client()
    if api_client:
        create_and_start_campaign(api_client, 258, "Waste Management Campaign")

def water_conservation_campaign():
    api_client = get_api_client()
    if api_client:
        create_and_start_campaign(api_client, 269, "Water Conservation Campaign")

def public_healthcare_campaign():
    api_client = get_api_client()
    if api_client:
        create_and_start_campaign(api_client, 270, "Public Healthcare Campaign")
