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

try:
    # Create an instance of the API class
    with callchimp.ApiClient(configuration) as api_client:
        scripts_api = callchimp.ScriptsApi(api_client)
        campaigns_api = callchimp.CampaignsApi(api_client)

        # Create a script
        script_request = callchimp.ScriptRequest(
            name="Sustainable Development Campaign Script",
            text="Hello! This is a call to inform you about sustainable development practices. Together, we can make a difference!"
        )
        try:
            script_response = scripts_api.scripts_post(script_request)
            print("Script created:\n")
            pprint(script_response)
        except ApiException as e:
            print("Exception when calling ScriptsApi->scripts_post: %s\n" % e)
            script_response = None

        # Create a campaign using the created script ID
        if script_response:
            campaign_request = callchimp.CampaignRequest(
                name="Sustainable Development Campaign",
                script_id=script_response.id,  # Use the script ID from the created script
                call_time="09:00"
            )
            try:
                campaign_response = campaigns_api.campaigns_post(campaign_request)
                print("Campaign created:\n")
                pprint(campaign_response)
            except ApiException as e:
                print("Exception when calling CampaignsApi->campaigns_post: %s\n" % e)
        
        # List all campaigns
        try:
            campaigns_list_response = campaigns_api.campaigns_list()
            print("Campaigns listed:\n")
            pprint(campaigns_list_response)
        except ApiException as e:
            print("Exception when calling CampaignsApi->campaigns_list: %s\n" % e)

except ApiException as e:
    print("Exception when setting up the API client: %s\n" % e)
