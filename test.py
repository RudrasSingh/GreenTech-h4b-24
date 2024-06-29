
import callchimp
from callchimp.models.subscribers_post_request import SubscribersPostRequest
from callchimp.models.calls_post_request import CallsPostRequest
from callchimp.rest import ApiException
from pprint import pprint
import os
import dotenv

# Load environment variables from a .env file
dotenv.load_dotenv()

# Configure the API key authorization
configuration = callchimp.Configuration(
    host="https://api.callchimp.ai/v1"
)
configuration.api_key['x-api-key'] = os.getenv("CALLCHIMP_API_KEY")

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with callchimp.ApiClient(configuration) as api_client:
    # Create an instance of the Subscribers API class
    subscribers_api_instance = callchimp.SubscribersApi(api_client)

    # Create a new subscriber request
    subscribers_post_request = SubscribersPostRequest(
        first_name="Rishav",
        last_name="Doe",
        leadlist=142,
        phone_code="91",
        phone_number="7667689413"
    )
    
    try:
        # Check the request object before making the API call
        print("subscribers_post_request:\n")
        pprint(subscribers_post_request)
        
        # Create one or more Subscriber(s)
        api_response = subscribers_api_instance.subscribers_post(subscribers_post_request)
        print("The response of SubscribersApi->subscribers_post:\n")
        pprint(api_response)
        
        # Extract the subscriber ID from the response
        if api_response and hasattr(api_response, 'id'):
            subscriber_id = api_response.id

            # Create a call request
            calls_api_instance = callchimp.CallsApi(api_client)
            calls_post_request = CallsPostRequest(lead=subscriber_id)
            
            # Check the request object before making the API call
            print("calls_post_request:\n")
            pprint(calls_post_request)
            
            # Create a Call
            api_response = calls_api_instance.calls_post(calls_post_request)
            print("The response of CallsApi->calls_post:\n")
            pprint(api_response)
        else:
            print("Error: Subscriber creation failed. No ID returned in response.")
    except ApiException as e:
        print("Exception when calling SubscribersApi or CallsApi: %s\n" % e)
    except Exception as e:
        print("An unexpected error occurred:\n", e)