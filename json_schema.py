
import os

print("***********************************************************")
print("***    DECT-IP MQTT based API fro AML schema checking  ****")
print("***    Prerequisite: jsonschema                        ****")
print("***                                                    ****")
print("***********************************************************")
print("")
print("********************")
print("***    general  ****")
print("********************")
print("* status request")
print("* Check json_msgs\msg_api_status_request.json against json_schema\schema_general_api_status_req.json")
os.system('jsonschema -i .\json_msgs\msg_api_status_request.json .\json_schema\schema_general_api_status_req.json')

print("* status response")
print("* Check json_msgs\msg_api_status_response.json against json_schema\schema_general_api_status_res.json")
os.system('jsonschema -i .\json_msgs\msg_api_status_response.json .\json_schema\schema_general_api_status_res.json')

print("")
print("********************")
print("***   location  ****")
print("********************")
print("* locate dps req")
print("* Check json_msgs\msg_location_dps_request.json against json_schema\shema_location_request.json")
os.system('jsonschema -i .\json_msgs\msg_location_dps_request.json .\json_schema\schema_location_request.json')

print("* locate dps res")
print("* Check json_msgs\msg_location_dps_response.json against json_schema\schema_location_dps_response.json")
os.system('jsonschema -i .\json_msgs\msg_location_dps_response.json .\json_schema\schema_location_dps_response.json')

print("* locate dps rej")
print("* Check json_msgs\msg_location_dps_reject.json against json_schema\schema_location_dps_reject.json")
os.system('jsonschema -i .\json_msgs\msg_location_dps_reject.json .\json_schema\schema_location_dps_reject.json')

print("* locate ble req")
print("* Check json_msgs\msg_location_ble_request.json against json_schema\schema_location_request.json")
os.system('jsonschema -i .\json_msgs\msg_location_ble_request.json .\json_schema\schema_location_request.json')

print("* locate ble res")
print("* Check json_msgs\msg_location_ble_response.json against json_schema\schema_location_ble_response.json")
os.system('jsonschema -i .\json_msgs\msg_location_ble_response.json .\json_schema\schema_location_ble_response.json')

print("* locate ble rej")
print("* Check json_msgs\msg_location_ble_reject.json against json_schema\schema_location_ble_reject.json")
os.system('jsonschema -i .\json_msgs\msg_location_ble_reject.json .\json_schema\schema_location_ble_reject.json')

print("* locate dps+ble req")
print("* Check json_msgs\msg_location_ble_dps_request.json against json_schema\schema_location_request.json")
os.system('jsonschema -i .\json_msgs\msg_location_ble_dps_request.json .\json_schema\schema_location_request.json')

print("* locate dps+ble res")
print("* Check json_msgs\msg_location_dps_ble_response.json against json_schema\schema_location_dps_ble_response.json")
os.system('jsonschema -i .\json_msgs\msg_location_dps_ble_response.json .\json_schema\schema_location_dps_ble_response.json')

print("")
print("********************")
print("***  messaging  ****")
print("********************")
print("* set msg req")
print("* Check json_msgs\msg_messaging_set_msg_request.json against json_schema\schema_messaging_api_msg_set_req.json")
os.system('jsonschema -i .\json_msgs\msg_messaging_set_msg_request.json .\json_schema\schema_messaging_api_msg_set_req.json')
print("* set msg req with make call elements")
print("* Check json_msgs\msg_messaging_set_msg_request.json against json_schema\schema_messaging_api_msg_set_req.json")
os.system('jsonschema -i .\json_msgs\msg_messaging_set_msg_request_make_call.json .\json_schema\schema_messaging_api_msg_set_req.json')

print("* set msg res")
print("* Check json_msgs\msg_messaging_set_msg_response.json against json_schema\schema_messaging_api_msg_set_respone.json")
os.system('jsonschema -i .\json_msgs\msg_messaging_set_msg_response.json .\json_schema\schema_messaging_api_msg_set_respone.json')

print("* set msg rej")
print("* Check json_msgs\msg_messaging_set_msg_reject.json against json_schema\schema_messaging_api_msg_set_respone.json")
os.system('jsonschema -i .\json_msgs\msg_messaging_set_msg_reject.json .\json_schema\schema_messaging_api_msg_set_respone.json')

print("* del msg req")
print("* Check json_msgs\msg_messaging_del_msg_request.json against json_schema\schema_messaging_api_msg_del_req.json")
os.system('jsonschema -i .\json_msgs\msg_messaging_del_msg_request.json .\json_schema\schema_messaging_api_msg_del_req.json')

print("* del msg res")
print("* Check json_msgs\msg_messaging_del_msg_response.json against json_schema\schema_messaging_api_msg_set_respone.json")
os.system('jsonschema -i .\json_msgs\msg_messaging_del_msg_response.json .\json_schema\schema_messaging_api_msg_del_req.json')

print("* del msg rej")
print("* Check json_msgs\msg_messaging_del_msg_reject.json against json_schema\schema_messaging_api_msg_set_respone.json")
os.system('jsonschema -i .\json_msgs\msg_messaging_del_msg_reject.json .\json_schema\schema_messaging_api_msg_set_respone.json')

print("* msg notify")
print("* Check json_msgs\msg_messaging_notify.json against json_schema\schema_messaging_notify.json")
os.system('jsonschema -i .\json_msgs\msg_messaging_notify.json .\json_schema\schema_messaging_notify.json')

print("* msg notify with reply option")
print("* Check json_msgs\msg_messaging_notify.json against json_schema\schema_messaging_notify.json")
os.system('jsonschema -i .\json_msgs\msg_messaging_notify_with_reply.json .\json_schema\schema_messaging_notify.json')

print("")
print("***********************************************************")
print("***    END END END END END END END END END END END     ****")
print("***********************************************************")




