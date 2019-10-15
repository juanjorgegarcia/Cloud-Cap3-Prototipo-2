import openstack
import credentials
# Initialize and turn on debug logging
openstack.enable_logging(debug=True)

# Initialize connection
# Cloud configs are read with openstack.config

conn = openstack.connection.Connection(**credentials.auth_args)
conn.authorize()

#conn = openstack.connect(cloud='rubinho')

# Upload an image to the cloud
image = conn.get_image(
    'bionic')

# Find a flavor with at least 512M of RAM
flavor = conn.get_flavor_by_ram(512)

network = conn.get_network('8be72a47-ece1-4730-aa9d-86c941f80035')

# Boot a server, wait for it to boot, and then do whatever is needed
# to get a public ip for it.
conn.create_server(
    'ta-funfs', image=image, flavor=flavor, wait=True, auto_ip=True, network=network,key_name='maas')
is_deleted=conn.delete_server('ta-funfs',wait=True,timeout=90)
if is_deleted:
	print("Server deleted")
else:
	print("Server not found")
