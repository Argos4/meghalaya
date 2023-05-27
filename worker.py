from git import Repo
import json
import os
import subprocess
def pull_repository():
    # GitHub repository information
    repo_url = 'https://github.com/Argos4/terraform.git'  # URL of the repository
    clone_path = '/Users/aniketharkare/Documents/GitHub/meghalaya-module-repo/'  # Path where you want to clone the repository

    # Clone the repository
    Repo.clone_from(repo_url, clone_path)

    print("Repository cloned successfully.")

def dump_resource_json_file(resource):
    file_path = '/Users/aniketharkare/Documents/GitHub/meghalaya-module-repo/cosmos_db_module/input.auto.tfvars.json'

    # Write Python object to JSON file
    with open(file_path, 'w') as json_file:
        json.dump(resource, json_file, indent=4)

    print(f"JSON file created: {file_path}")


def provision_resource_using_terraform():
    new_dir = "/Users/aniketharkare/Documents/GitHub/meghalaya-module-repo/cosmos_db_module/"
    os.chdir(new_dir)
    terraform_cmd = ['terraform', 'init']

    # Execute the Terraform command
    process = subprocess.Popen(terraform_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for the Terraform command to finish and capture the output
    output, error = process.communicate()

    # Check the return code to determine if the command was successful
    return_code = process.returncode
    if return_code == 0:
        print("Terraform init executed successfully.")
    else:
        print(f"Terraform command failed with return code {return_code}.")
        print("Error:", error.decode())

    terraform_cmd = ['terraform', 'apply', '-auto-approve']

    # Execute the Terraform command
    process = subprocess.Popen(terraform_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for the Terraform command to finish and capture the output
    output, error = process.communicate()

    # Check the return code to determine if the command was successful
    return_code = process.returncode
    if return_code == 0:
        print("Terraform apply executed successfully.")
        print("Error:", output.decode())
    else:
        print(f"Terraform command failed with return code {return_code}.")
        print("Error:", error.decode())