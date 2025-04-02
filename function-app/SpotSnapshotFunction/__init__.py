import datetime
import logging
import os
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

def main(mytimer: func.TimerRequest) -> None:
    logging.info("🔁 Snapshot automation function triggered")

    subscription_id = os.environ["SUBSCRIPTION_ID"]
    resource_group = os.environ["RESOURCE_GROUP_NAME"]

    credential = DefaultAzureCredential()
    compute_client = ComputeManagementClient(credential, subscription_id)

    vms = compute_client.virtual_machines.list(resource_group)

    for vm in vms:
        if vm.priority != "Spot":
            continue

        vm_name = vm.name
        location = vm.location
        timestamp = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")

        os_disk = vm.storage_profile.os_disk
        snapshot_name = f"{vm_name}-snapshot-{timestamp}"

        snapshot_params = {
            "location": location,
            "creation_data": {
                "create_option": "Copy",
                "source_resource_id": os_disk.managed_disk.id
            },
            "tags": {
                "sourceVM": vm_name,
                "type": "auto-backup"
            }
        }

        logging.info(f"📸 Creating snapshot for {vm_name}")
        compute_client.snapshots.begin_create_or_update(
            resource_group,
            snapshot_name,
            snapshot_params
        )

    logging.info("✅ Snapshot job complete.")
